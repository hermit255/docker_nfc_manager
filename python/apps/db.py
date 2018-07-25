# coding: utf-8
import mysql.connector
import config

def connect():
  # mysql との接続
  result = mysql.connector.connect(
    user = config.db['user'],
    passwd = config.db['passwd'],
    host = config.db['host'],
    database = config.db['database']
  )
  return result

def exec_sql(sql, message = None):
  conn = connect()
  c = conn.cursor()
  try:
    c.execute(sql)
    conn.commit()
  except Exception as e:
    message = 'failed to exec SQL'
  finally:
    print(message)
    c.close()
    conn.close()

def save_stamp(data):
  # SQLの作成と実行
  sql = 'INSERT INTO ' + config.table['main'] + ' (uid, stamp) VALUES ("' + data['uid'] + '", "' + data['stamp'] + '")'
  message = '打刻しました'
  exec_sql(sql, message)
  
def save_to_text(uid = 'no data',stamp = 'no time'):
  filename = 'output.txt'

  try:
    with open(filename, mode='a') as f:
      f.write('uid: ' + uid + ' / ' + 'stamp: ' + stamp + '\n')
  except Exception as e:
    print('failed to write to text-data')

def truncate_table():
  # テーブルの作成
  sql = 'TRUNCATE TABLE ' + config.table['main']
  message = 'stamp テーブルを空にしました'
  exec_sql(sql, message)

def drop_table():
  # テーブルの作成
  sql = 'DROP TABLE ' + config.table['main']
  message = 'stamp テーブルを削除しました'
  exec_sql(sql, message)

def create_table():
  # テーブルの作成
  sql = 'create table ' + config.db['database'] + '.' + config.table['main'] + ' (id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, uid VARCHAR(32), stamp DATETIME, sended TINYINT)'
  message = 'stamp テーブルを作成しました'
  exec_sql(sql, message)
