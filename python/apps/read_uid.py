import nfc
import binascii
import logging
from datetime import datetime

import db

clf = nfc.ContactlessFrontend('usb')
logging.basicConfig(level=logging.INFO)

def read(tag):
  data = get_data(tag)
  show_info(data)

  try:
    save_to_text(data)
    db.save_stamp(data)
    logging.info('saving to database successful / ' + 'uid: ' + data['uid'] + ' / ' + 'stamp: ' + data['stamp'] )
  except Exception as e:
    logging.info('saving to database failed')

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

def save_to_text(data):
  filename = 'output.txt'
  with open(filename, mode='a') as f:
      f.write('uid: ' + data['uid'] + ' / ' + 'stamp: ' + data['stamp'] + '\n')
  print('wrote to ' + filename)
  print('----------------------')

def ready():
  print('----------------------')
  print('ready to read...')
  print('----------------------')
  clf.connect(rdwr={'on-release':read})
