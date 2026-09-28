import json
import sqlite3
x = input("Json dosyasını giriniz: ")
arsivjson = f"{x}.json"
arsivdb = f"{x}.db"
def json_to_sql(json_dosya, db_dosya):
	with open(json_dosya, 'r', encoding='utf-8') as f:
		data = json.load(f)
	conn = sqlite3.connect(db_dosya)
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS mesajlar (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			yazan TEXT, 
			tarih TEXT, 
			mesaj TEXT
		)
	''')
	veriler = [(item['Yazan: '], item['Tarih: '], item['Mesaj: ']) for item in data]
	cursor.executemany('INSERT INTO mesajlar (yazan, tarih, mesaj) VALUES (?,?, ?)', veriler)
	conn.commit()
	conn.close()
	print(f"İşlem tamamdır! {len(veriler)} mesaj veritabanına gömüldü.")
json_to_sql(arsivjson, arsivdb)
