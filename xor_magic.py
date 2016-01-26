#!/usr/bin/env python2
'''
tries to brute force single byte xor by xoring a blob then
check if libmagic recognizes it.
'''
#Standard Imports
import collections, os, sys, itertools, operator, hexdump

#Non Standard Imports
try:
    import magic
except ImportError:
    print "[!] Couldn't Import magic 'sudo pip install filemagic'"

#Functions
def xor(data, key):
    returnVal = ''
    for c in data:
        returnVal += chr(ord(c) ^ ord(key))
    return returnVal

def findType(data):
    with magic.Magic() as m:
        return m.id_buffer(data)

def mostFreq(data, num):
    counter = collections.Counter(data)
    return sorted(counter.items(), key=operator.itemgetter(1), reverse=True)[:num] # returns a list of tuples...

def dumpSlice(data, numBytes):
    slice = data[:numBytes]
    print hexdump.hexdump(slice)

#Main
with open(sys.argv[1], 'r') as f:
    data = f.read()

#mostFreq(data, 10)
#print findType(data)

for i in range(0,255):
    if findType(xor(data, chr(i))) != 'data':
        #import pdb; pdb.set_trace()

        print 'key: ' + hex(i)
        print findType(xor(data, chr(i)))
        dumpSlice(xor(data, chr(i)),32)
