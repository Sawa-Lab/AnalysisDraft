# coding:utf-8
import urllib
from bs4 import BeautifulSoup
import sqlite3
from time import sleep

#functions
def extcact_data_into_db(url):
    #settings
    DATABASE = 'DRAFT.db'
    conn = sqlite3.connect(DATABASE)
    conn.text_factory = str 
    db_cursor = conn.cursor()

    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    detail_array = soup.find_all('div',class_='p-users-listview__item')
    if len(detail_array) == 0:
        return False

    for detail in detail_array:
        #get user id and the user's url
        user_id = detail.find('a',class_='u-font-sl f-w-bold').get('href').replace('/users/','')

        #get age
        age = detail.find('span',class_='u-font-sl').text

        #get under_consideration_count,rank,past_amount
        rank_array = detail.find_all('span',class_='f-w-bold u-font-ml')
        under_consideration_count = rank_array[0].text
        rank = rank_array[1].text
        past_amount = 0 if rank_array[2].text.replace('万円','') == '--' else rank_array[2].text.replace('万円','')

        #get ambition
        ambition = detail.find('span',class_='f-w-bold u-font-mm').text

        #get tech list
        tech_block_array = detail.find('ul',class_='p-aside-taglist u-m-t-5')
        tech_array = tech_block_array.find_all('li',class_='c-tag c-tag--s c-tag--border-gray3 c-tag--s-rounded')
        tech_csv = ''
        for tech_name in tech_array:
            tech_csv += tech_name.text if len(tech_csv) == 0 else ',' + tech_name.text
        
        #insert data to DB
        insert_user_data_sql = 'INSERT INTO currentUsers (user_id, age, under_consideration_count, rank, past_amount, ambition, tech_list) values (?,?,?,?,?,?,?)' 
        user_data = (user_id, age, under_consideration_count, rank, past_amount, ambition, tech_csv)
        db_cursor.execute(insert_user_data_sql,user_data)
    conn.commit()
    conn.close()
    return True

#main
url_pre = 'https://job-draft.jp/festivals/14/users?page='
url_suf = '&user_search%5Bage_about%5D=&user_search%5Bfreeword%5D=&user_search%5Bsort%5D=favorited'
page_number = 1
is_page_exist = True

print('start !')
while is_page_exist == True:
    print('extracting page ' + str(page_number))
    sleep(2)
    url = url_pre + str(page_number) + url_suf
    page_number += 1
    is_page_exist = extcact_data_into_db(url)
    
print('done !')
