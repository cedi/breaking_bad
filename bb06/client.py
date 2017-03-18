#!/usr/bin/python3

import requests
import binascii
import math
from gmpy2 import mpz
from gmpy2 import iroot
import hashlib
import re


# send the request
def send_req(name, sig):

    sig = binascii.hexlify(sig)

    url = "http://127.0.0.1:4242/api"
    data = {
        'sig': sig,
        'name': name
    }

    print("Get-Request to send")
    print("{}?sig={}&name={}".format(url, str(sig)[2:-1], name))

    return requests.get(url, params=data)

def to_bytes(n):
    """ Return a bytes representation of a int """
    return n.to_bytes((n.bit_length() // 8) + 1, byteorder='big')

def from_bytes(b):
    """ Makes a int from a bytestring """
    return int.from_bytes(b, byteorder='big')

def get_bit(n, b):
    """ Returns the b-th rightmost bit of n """
    return ((1 << b) & n) >> b

def set_bit(n, b, x):
    """ Returns n with the b-th rightmost bit set to x """
    if x == 0: return ~(1 << b) & n
    if x == 1: return (1 << b) | n

def cube_root(n):
    return int(iroot(mpz(n), 3)[0])


# Main
if __name__ == "__main__":
    request = ""

    # send request to server
    answer = send_req('admin', request)

    # get the answer from the server
    print("Server Answer: ", answer)

