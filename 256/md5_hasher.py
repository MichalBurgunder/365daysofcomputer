

import hashlib
import random
import math
import os

def generate_random_md5():
    arr = "0123456789abcdef"
    
    first_hash = ""
    for i in range(32):
        pos = math.floor(random.random()*16)
        first_hash += arr[pos]
    return first_hash

divider = 1000000
theHash = generate_random_md5()
startingHash = theHash

print(f"Starting hash: {startingHash}")
i = 0

hamming_res = {theHash: True}

while True:
    prev_hash = theHash
    theHash = hashlib.md5(theHash.encode()).hexdigest()

    i += 1

    if theHash in hamming_res:
        print(f"n-Cycle found! Hash: {theHash}, step: {str(i)}")
        exit()
    if i%divider == 0:
        print(f"Step {int(i/divider)}e{len(str(divider))}. Current hash: {theHash}")
        hamming_res[theHash] = True
