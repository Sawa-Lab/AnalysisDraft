できること：
転職ドラフトの一覧から情報を抽出し、そこからタグクラウドを作成する。

手順：
1.CreateTableを実行して、DBとテーブルを作成する（初回のみ）
2.AnalysisDraftを実行して、転職ドラフトの一覧からデータを抽出、DBに保存する
3.OutputWordCloudを実行して、タグクラウドを作成する

-------------------------------------------
・ポートフォリオとして
使用技術の選定：
python2.7.15 ライブラリが充実している為、勉強の為。2.7.15なのは今後GAEでの使用を想定している為。
mecab 学生の頃から使っており、慣れている為（pythonが初めてなので、他は慣れているものにした）。
SQLite 今後もっと分析するときに、DBに保存していた方が使い勝手がいい為。またDBサーバが不要な為。

工数：
環境構築含めて1.5人日（12h）程度

その他：
Windows環境、さらにユーザ名が平仮名だったため、python/GAEの環境構築、及び文字コード周りに時間がかかった。
次は仮想環境にCentOSを入れて、そこで開発しようと考えている（あるいはMacを買うか…）。

次のアクションとして、
・企業側の属性情報の取得
・ユーザの詳細ページの情報の取得
・野望全文、使用技術、キャラクター、やりたいこと、基本プロフィールなどによるクラスタリング
・企業のクラスタリング（規模、WEB/SIer、0to1/1to100…）
・クラスタと指名数/金額の相関分析
など。

