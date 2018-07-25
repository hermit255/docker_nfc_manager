import nfc
import binascii
from datetime import datetime

import db

clf = nfc.ContactlessFrontend('usb')

def get_uid(tag):
  result = binascii.hexlify(tag.identifier).upper()
  return result

def get_data(tag):
  uid = get_uid(tag)
  stamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
  result = {'uid': uid, 'stamp': stamp}
  return result

def show_info(data):
  print(data['uid'])
  print(data['stamp'] + '\n')

def save_to_database(tag):
  data = get_data(tag)
  show_info(data)
  db.save_stamp(data)
  print('----------------------')

def save_to_text(tag):
  filename = 'output.txt'

  data = get_data(tag)
  show_info(data)
  with open(filename, mode='a') as f:
      f.write('uid: ' + data['uid'] + ' / ' + 'stamp: ' + data['stamp'] + '\n')
  print('wrote to ' + filename)
  print('----------------------')

def ready():
  print('----------------------')
  print('ready to read...')
  print('----------------------')
  clf.connect(rdwr={'on-release':save_to_database})
  # clf.connect(rdwr={'on-release':save_to_text})
