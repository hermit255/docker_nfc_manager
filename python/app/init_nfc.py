import nfc
import binascii
import logging

import json
import urllib.request

def init():
  clf = nfc.ContactlessFrontend('usb')
  logging.basicConfig(level=logging.INFO)
  logging.info('ready to read...')
  # `action` method run on nfc-card release
  clf.connect(rdwr={'on-release':action})

def action(tag):
  try:
    uid = binascii.hexlify(tag.identifier).upper()
    send(uid)
    logging.info('Successfully sent' )
  except Exception as e:
    logging.info('Failed to send')

def send(uid):

  url = '/api'
  data = {
      'uid': uid,
  }
  headers = {
      'Content-Type': 'application/json',
  }
  req = urllib.request.Request(url, json.dumps(data).encode(), headers)
  with urllib.request.urlopen(req) as res:
      body = res.read()
