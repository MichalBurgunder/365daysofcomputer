# TEXT HASHER

import hashlib

# place the text you wish to hash in between the apostrophies
text = """Though random number generation itself has plenty of uses, sometimes you need a (seemingly) random set of data that is dependent on a given string of data. You can imagine this as a “short code” identifier; In the same way that we label physical parts of a machine with different IDs, we will need a way to label the data that we have in a file system, a database, etc. automatically, without human intervention. To make it clear that a given labelling is a label in the first place, we must standardize the length of the short code to specific length.

IMAGE: A PART, E.G. ARDUINO WITH THE PRODUCT NUMBER, OR OTHER PARTS OF A COMPUTER WITH THEIR ID CODE

A function that transforms some data, a file, an entire software, etc. into such a short code, is known as a hash function. That is, it takes any amount of data and transforms it into a fixed-size amount of data. The first obvious use of such a code is, analogously, when we have innumerable different products/files that we need to label uniquely, which is why hash functions have not come into use until early 1960s, when computers began to hold more memory*.

Modern hash functions are significantly complex in terms of what operations are performed, although they don’t have to be that complicated. Given the basic definition above, the trivial hash function can be as simple as returning the same “hash” regardless of the data inputted. It cannot do any distinguishing between any two files (read: data strings), so let’s make a function that actually changes based on the data inputted. The simplest such function is a function based on the XOR bit function.

Take some data, and split it into blocks of 256 blocks of bits. If the data cannot be segmented in such a way, let the remaining bits be 0s, a process known as padding. Then, we take the first block of bits, and XOR it with the next block. And again and again, until we have no more blocks left. This in effect, gives us a function that will, for the most part, convert “big” files, into 256 bits, i.e 32 hexadecimal characters, or 16 characters with an encoding of 32 characters. Hashes however, are typically expressed in hexadecimal form. 

IMAGE: SIMPLEST HASH FUNCTION ILLUSTRATION

Hash functions are typically split into blocks, which means that hash functions are typically expressed in the language of binary operations on a set of bits: XOR, NOT, ADD (add 1, to the number), SHIFT (shifting bits in one direction, having a zero at one end) ROTATE (the same thing, but having data wrap around to the other end), and probably several more. Given the simplicity of these operations, most programming languages support these operations with very similar syntax: | (OR), ~ (NOT), & (AND), << (SHIFT left), >> (SHIFT right). Often times they use all the functions multiple times, to obfuscate the original data. 

The most prominent use of hash functions is not labelling however. Instead, it forms the basis of the data structure known as the hash map/hash table. Recall that ever line of memory can be addressed/called upon using some binary code. If the hash code identifies a place in memory where some data sits, it gives us a good reason to believe that some data associated with some other data, can be found without searching memory for it. This is how: Take some data, known as the key, and hash it. The resulting hash points to a line of memory where we can store more data. 

For example, if we wanted to, say, record how much salary each employee receives per year (or map virtual addresses to physical addresses in the MMU), we might hash their full names, and wherever the hash function points to, we’d place the salary of that person there. This way, if we have 1000 employees, and we would need to find how much they make, we’d hash their name, use the resulting hash as a memory location pointer, and simply call upon that memory location to know their salary. Running in O(1) time, this is the minimum theoretical algorithmic time required to call upon some data in memory, forming the basis of this data structure. 

If the hash function had only a length of, say, 8 bits, then, clearly after at most 2^8=256 data points (but usually way before), there inevitably must come a time where two files hash to the same value, known as a collision. When a collision occurs, then the hash map cannot accommodate the piece of data. To fix this, the hashmap remaps each data point by taking the original keys, and hashing it using a hash function that outputs a hash of longer length, maybe now with 16 bits. Now, when the new key is hashed, it should likely map to a memory location that has not yet been used. An algorithmic complexity that only occasionally performs a heavy operation as is the case here, is known as amortized complexity, of which the hashmap has O(n).

It’s clear then, that hashes need to be relatively random, as otherwise, there might be a large amount of collisions, hence needing more and more memory to accommodate the operation of the data structure. But wait, we know how to test for randomness! It turns out, the diehard tests used for testing pseudo random number generators, can also be used to test hash functions. Other tests that are relatively straightforward, are collision testing, where a large number of hashes are created using different inputs, to see if check how many collisions can be found (ideally minimal), or preimage resistance testing, whereby you try to reverse engineer a hash, i.e. can you figure out the original data, in any way, if you have a hash?

IMAGE: ILLUSTRATION OF COLLISION TESTING, PREIMAGE & SECOND PREIMAGE TESTING

Preimage testing is particularly important when it comes to getting access to accounts protected by a password. Typically, when users register passwords, these passwords are saved as hashes (i.e. when you log in, it hashes your password, sends the hash, and checks if the hash is the same as the one in the database). This means that even if someone has access to the hashes of many passwords, they still don’t know the password.

Note, that because we are mapping any data input of any length, to a fixed length, there are inevitably many/in theory infinite inputs that result in the same hash. This in effect means you don’t really need the password of the user, but instead, you just need to find an input that results in the hash to bypass password security. Second preimage testing ensures/reveals whether one has a hash, one cannot create another input with a given hash function. One can also place additional security mechanisms on hashes by using a key (in the cryptographic sense), where the key can be appended to the file in some way, and then the function then hashes the file with the key. If the key depends on the clock, then every creation of the hash map, would generate unique keys every time. 

As this battery of tests begins stacking more and more requirements on any hash function, we distinguish cryptographic vs non-cryptographic hash functions. Non-cryptographic hash functions have relatively lenient requirements, which also often means that the computational power needed to compute them are relatively little. Such functions typically make up the hash function implemented: SipHash for example, a key-based, non-cryptographic hash is used for Python’s dictionaries. Other languages may use more sophisticated mechanisms for hashing, e.g. choosing a hash function based on properties of the incoming data.

Given the importance of cryptographic hash functions, their testing cannot be underestimated, and must be standardized, for widespread use. The NIST released a series of secure hash functions that should be used for sensitive things like passwords. This series is updated when needed, although the current version of the secure hashing algorithms (SHA), SHA-3, has so far evaded many attempted attacks, and so, stands as one of the best hash functions we have for secure hashing.

With secure hashing, we cannot actually do some pretty funky things. For example, if we wish to find some data in a database, we can save the all the files, 100’000, 1’000’000, based on their hash, which means that if we wish to call upon the file, we can do so in O(1) time.

Another prominent use of hash functions is one that Apple has discovered. In order to counter people owning illegal files (in this case, photographs of child pornography), the company decided to include the hashes of these photographs on the operating systems of iphones and computers. This way, whenever a file arrives onto the device, the OS can hash the file to see if it matches up with any of the hashes saved. This way, it can with a relatively high probability detect whether people own illegal material on their computers, without knowing what images the users actually have. Of course, there are a tremendous number of issues with this initiative (privacy & surveillance concerns, false positive outcomes, law enforcement issues), but more on that later. 

Two final notes: One things that particularly interests me personally, are things known as hash cycles. A hash is said to be on a hash cycle when hashing that hash, and hashing the output ad nauseum, eventually gets you back to the original chosen hash. As hash functions are limited in their size, every hash is on a hash cycle of at most 2x, where x is the number of bits used for a hash. So the question is, what is the smallest hash cycle we can find? Given the cryptography tests, there is, as far as we know, no way to figure out the shortest cycle, except for hashing every single hash, and checking if its been found or not.

Is there a hash of cycle length 1, i.e. does a has has to itself? Impossible to definitively answer with today;s technology. Still fun to see if you can find one. Here, some code to try out for the MD5 hash:

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



Finally, if you wish to try to see how hashes behave, feel free to hash to use this Python code: 

import hashlib


# place the text you wish to hash in between the apostrophies
text = "".encode('utf8')


def md5_hash_it(text):
   result = hashlib.md5(text)
   return result.hexdigest()


def sha256_hash_it(text):
   result = hashlib.sha256(text)
   return result.hexdigest()


# custom hashing
sha256_result = sha256_hash_it()
md5_result = md5_hash_it(text)


print(sha256_result)
print(md5_result)

Do you need something to hash? Use this article. Excluding the hash itself, the hash of this article should result in 
""".encode('utf8')

def md5_hash_it(text):
    result = hashlib.md5(text)
    return result.hexdigest()

def sha256_hash_it(text):
    result = hashlib.sha256(text)
    return result.hexdigest()

# custom hashing
sha256_result = sha256_hash_it(text)
md5_result = md5_hash_it(text)

print(sha256_result)
print(md5_result)