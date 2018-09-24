# coding:utf-8
import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab as mc
import collections

#functions
def create_tech_list_array(sql_where):
    #settings
    DATABASE = 'DRAFT.db'
    conn = sqlite3.connect(DATABASE)
    conn.text_factory = str 
    db_cursor = conn.cursor()
    tech_result_array = []

    select_sql = 'SELECT tech_List from currentUsers ' + sql_where
    cur = conn.execute(select_sql)
    tech_array = [app for app in cur.fetchall()]
    for item in tech_array:
        tech_result_array.append(item[0])
    conn.close()
    return tech_result_array

def creat_ambition_array(sql_where):
    #settings
    DATABASE = 'DRAFT.db'
    conn = sqlite3.connect(DATABASE)
    conn.text_factory = str 
    db_cursor = conn.cursor()
    ambition_result_array = []
    #We should use mecab-ipadic-neologd for mecab dic, but cannot install it to Windows, and ubuntu. So use default.
    tagger = mc.Tagger('-Ochasen')

    select_sql = 'SELECT ambition from currentUsers ' + sql_where
    result_cursor = conn.execute(select_sql)
    ambition_array = [app for app in result_cursor.fetchall()]
    for item in ambition_array:
        node = tagger.parseToNode(item[0]) 
        while(node):
            if node.surface != "":  # remove header and footer
                word_type = node.feature.split(",")[0]
                if word_type in [u"形容詞", u"名詞", u"動詞", u"副詞"]:
                    ambition_result_array.append(node.surface)
            node = node.next
            if node is None:
                break
    conn.close()
    return ambition_result_array

def create_word_cloud(word_array, output_name):
    FONT_PATH = './meiryo.ttc'
    wordcloud = WordCloud(background_color="white",font_path=FONT_PATH, width=900, height=500).generate(" ".join(word_array).decode('utf-8'))
    wordcloud.to_file("./" + output_name + ".png")
    print("output done ! --- " + output_name + ".png ---")

#main
print('Please choose tech list or ambition.')
print('Please input 1 or 2. (1:tech list, 2:ambition)')
target = raw_input('>>')

print('Please input where condition for sql.')
print('e.g. WHERE under_consideration_count > 3')
sql_where = raw_input('>>')

print('Please input output file name without extension.')
print('e.g. tagCloudOfTech')
output_name = raw_input('>>')
if len(output_name)==0:
    output_name = 'sample'

if target == '1':
    create_word_cloud(create_tech_list_array(sql_where), output_name)
elif target == '2':
    create_word_cloud(creat_ambition_array(sql_where), output_name)
else:
    print('Input is incorrect.')




