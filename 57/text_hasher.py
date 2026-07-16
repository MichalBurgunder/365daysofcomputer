# TEXT HASHER

import hashlib

# place the text you wish to hash in between the apostrophies
text = """Though random number generation itself has plenty of uses, sometimes you need a (seemingly) random set of data that is dependent on a given string of data. You can imagine this as a “short code” identifier, a type of checksum; In the same way that we label physical parts of a machine with different IDs, we will need a way to label the data that we have in a file system, a database, etc. automatically, without human intervention. To make it clear that a given labelling is a label in the first place, we must standardize the length of the short code to specific length.

A function that transforms some data, a file, an entire software, etc. into such a short code, is known as a hash function. That is, it takes any amount of data and transforms it into a fixed-size amount of data. The first obvious use of such a code is to label innumerable different products/files uniquely, in order to identify them without much hassle. Hash functions then, are useful whenever we have a lot of data, which is why hash functions have not come into use until early 1960s, when computers began to hold more memory*.





A serial number. Although it has the structure of a hash (same length, same characters), it is not in fact a hash. Hashes result in the same code given the same data, every time. Serial numbers however, only give unique names to each copy of a product, regardless of some underlying data.

Given the basic definition above, the trivial hash function can be as simple as returning the same “hash” regardless of the data inputted. It always returns the same length data, the same data even. It’s useless, but strictly speaking, still a hash function… a very bad one at that. Using this function, it cannot distinguish between any two files (read: data strings). Let’s design a better hash function that actually changes based on the data inputted. The simplest such function is a function based on the XOR bit function performed on blocks data of a predefined length.

In other words, take the data you wish to hash, and split it into 128 blocks of bits. If the data cannot be segmented in such a way, let the remaining bits be 0s (adding extra data to a file for data processing is known as padding). Then we take the first block of bits, and XOR it with the next block. We take the result of this operation, and use it as our first block, and XOR it with the third block. And again and again, until we have no more blocks left. This in effect, gives us a function that will, for the most part, convert any size files, into 128 bits, i.e 32 hexadecimal characters. Hashes are typically expressed in hexadecimal form, because each character is a visible character. It also makes it easier to see the difference in values between two hashes, if there are only 16 characters vs, say, 128 characters.





The XOR hash function is probably the simplest effective hash function, which performs the XOR operation on all bits with a predefined block-size. As the XOR function is associative (meaning that the function can run in any order), the most efficient implementation is the one above.

More complex hash functions are easily created, although because they operate on individual bits, hash functions are typically expressed in the language of binary operations. XOR, NOT, ADD (add 1, to the number), SHIFT (shifting bits in one direction, having a zero at one end) , ROTATE (the same thing, but having data wrap around to the other end), and probably several more. Given the simplicity of these operations, most programming languages support these operations with very similar syntax: | (OR), ~ (NOT), & (AND), << (SHIFT left), >> (SHIFT right). Oftentimes hash functions use all the functions multiple times, to obfuscate the original data, and give a stronger case for the uniqueness of each hash. Modern hash functions have grown to be significantly complex in terms of what operations are performed, and continue to probe more and more complex methods.

The most prominent use of hash functions within computers is, however, not labelling files; such an operation is used when copying files to verify that the copy process has been performed successfully (i.e. take the hash of the origin file and the hash of the copied file, and they must be the same), or identifying unique files in the context of forensics. Instead, it forms the basis of the a hash map (or just map), a ubiquitous data structure present in nearly every commercial program.

Recall that every line of memory can be addressed/called upon using some binary code. If the hash code identifies a place in memory where some data sits in, say, an address with 32 bits, then short keys of only a few bytes can be hashed, and instantly, without searching where the data resides in memory, be found. This short data is typically known as a key inside of a hashmap, which can be associated with some other data, e.g. a number.

For example, if we wanted to map virtual addresses to physical addresses in the MMU (inside of the CPU), then it is enough to hash the virtual address, the hash of which acts as a key for access to the physical address.

A more practical example would be if we wanted to record the salaries of thousands of employees. We might take their full names & date of birth, hash the concatenated version thereof, and whatever address the hash function points to, we’d place all of that data of the person in that memory location, including salary information. This way, we would use their name and date of birth, hash them, then use the resulting hash as a memory location pointer, which  tells us what memory we need to call upon to get the relevant data. Running in O(log(n)) time for querying, where n is the length of the memory address in question, means that it is the minimum theoretical algorithmic time required to call upon some data in memory, hence that it is optimal.

Clearly, you don’t have infinite memory though. If the hash function outputted hashes of length 8 bits, then after at most 2^8=256 data points, the next unique data point would inevitably hash to a previously used value. Such an operation is known as a collision. When a collision occurs, then the hash map cannot accommodate the piece of data, making it full.

To make it bigger, all one needs to do is apply a hash function on the present hashes, and this time, retain more bits to act as the address. In other words, you hash the hashes, and copy the contents of those hashes to another hashmap. Then you hash the incoming new key twice (apply the hash function on the hash of the key), and you have a bigger hashmap. You just need to apply the hash function twice instead of once, to generate a new entry. In other words, the worst running time for insertion into a hashmap is O(n), mainly because of the recomputation. Because it is a rare/uncommon occurrence, an algorithm that only occasionally performs a heavy operation as is the case here, can be understood through amortized complexity. This complexity only takes the vast majority of operations, and classifies an algorithm based on that. Thus, hashmap insertions have O(1) amortized complexity, and O(n) algorithmic complexity.

An interesting use of hash functions is one that Apple has discovered. In order to counter people owning illegal files (in this case, photographs of child pornography), the company decided to include the hashes of these photographs on the operating systems of iPhones and computers. This way, whenever a file arrives onto the device, the OS can hash the file to see if it matches up with any of the hashes saved. This way, it can with a relatively high probability detect whether people own illegal material on their computers, without knowing what images the users actually have. Of course, there are a tremendous number of issues with this initiative (privacy & surveillance concerns, false positive outcomes, law enforcement issues), but more on that later.

It’s clear then, that hashes need to be relatively random, as otherwise, there might be a large amount of collisions, needing more and more memory to accommodate the operation of the data structure, or in Apple case, a large number of false positives, where innocent people might be labeled as pedophiles. We already know how to test for the randomness of numbers, namely by using the diehard tests used for testing pseudo random number generators. Because binary data can be interpreted as numbers, it means that the same methodology that is used for testing pseudo-random number generators can also be used to test hash functions.





If a hash function has too many collisions, it is not a good hash function.

Another basic way of testing hash functions are through collision testing where a large number of hashes are created using different inputs, to see if check how many collisions can be found (ideally minimal). Preimage resistance testing is another method, whereby you try to reverse engineer a hash, i.e. can you figure out the original data, in any way, if you have just the hash?

Preimage resistance testing is particularly important when it comes to getting access to accounts protected by a password. Typically, when users register passwords, these passwords are saved as hashes (i.e. when you log in, it hashes your password, sends the hash to the server, which checks if the hash is the same as the one in the database). This means that even if someone has access to the hashes of my password, they still don’t know what it is. A hash function that passes preimage resistance testing would ensure security in such a case.





Given a hash, if you can find the original data by somehow reverse engineering the hash function, it is not a good hash function.

Because we are mapping any data of any length to a fixed length, there are inevitably many inputs that result in the same hash, i.e. in collisions. This in effect means you don’t really need the password of the user to bypass password security, but just an input that results in the saved hash. Second preimage testing ensures/reveals whether if one has a hash, one cannot create another input with a given hash function, making sure that if someone has access to your hashed passwords, they can find another input that bypasses password security. One can also place additional security mechanisms on hashes by using salt (a key, in the cryptographic sense), where extra data can be appended to the file in some way, before the actual hash function runs†. Even better would be to first encrypt the data, before hashing it.





Given the original data and the hash, if you can use these to reverse any hash with reasonable room for error, then it is not a good hash function.

As this battery of tests begins stacking more and more requirements on any hash function, we can distinguish between cryptographic vs non-cryptographic hash functions. Non-cryptographic hash functions have relatively lenient characteristics, which often also means that the computational power needed to compute them is relatively little. Such functions typically make up the hash function implemented for hashmaps: SipHash for example, a key-based, non-cryptographic hash is used for Python’s dictionaries. Other languages may use more sophisticated mechanisms for hashing, e.g. choosing a hash function based on properties of the incoming data Cryptographic hash functions on the other hand, are resistant to the previously mentioned tinkering.

Given the importance of cryptographic hash functions, their security cannot be understated, and must be standardized to make sure that every hash function is scrutinized in the same, rigorous way. The National Institute of Standards and Technology (NIST, a US based Standards organization) released a competition for hash functions, the wnneres of which would be used as a series of standard secure hash functions that should be used for sensitive things like passwords. This series is updated when needed, although the current version of the secure hashing algorithms (SHA), SHA-3, has so far evaded many attempted attacks, and so, stands as one of the best hash functions we have for secure hashing.

With both types of hash functions accounted for with appropriate tests, unless someone finds weaknesses in the currently-used hash functions, there is no need create better hashes. For the most part, hash function engineering is a rare, but undoubtedly a necessary occurrence, which, given the many difficulties in information security, should be kept at the back of our heads.

Two final notes: One thing that particularly interests me personally, are things known as hash cycles. A hash is said to be on a hash cycle when hashing that hash, and hashing the output of that hash, ad nauseum, eventually gets you back to the original chosen hash. As hash functions are limited in their size, every hash is on a hash cycle of at most 2n, where n is the number of bits used to express a hash. So the question is, what is the smallest hash cycle we can find? As far as we know, there is no way to find or determine the length of the shortest cycle, except for hashing every single hash, mapping them onto a cycle, and taking the shortest one.





Although this is not a genuine hash cycle because these hashes do not actually hash to themselves, this is an example of a hash cycle of length two. These are very hard to find, if at all even possible.



Is there a hash of cycle length 1, i.e. does a hash hash to itself? Impossible to definitively answer with today’s technology, for any practical hash. Even mathematical approaches fail to produce an answer. Thus, if you want to gamble a little, even if it’s just losing some computing time, here is some code to try out for the MD5 hash. If you can find a hash that does the job, I guarantee, the hash you found would be world-famous:

import hashlib

import random

import math

import os

def generate_random_md5():

   arr = “0123456789abcdef”

   first_hash = “”

   for i in range(32):

       pos = math.floor(random.random()*16)

       first_hash += arr[pos]

   return first_hash

divider = 1000000

theHash = generate_random_md5()

startingHash = theHash

print(f“Starting hash: {startingHash}”)

i = 0

hamming_res = {theHash: True}

while True:

   prev_hash = theHash

   theHash = hashlib.md5(theHash.encode()).hexdigest()

   i += 1

   if theHash in hamming_res:

       print(f“n-Cycle found! Hash: {theHash}, step: {str(i)}”)

       exit()

   if i%divider == 0:

       print(f“Step {int(i/divider)}e{len(str(divider))}. Current hash: {theHash}”)

       hamming_res[theHash] = True

Finally, if you wish to try to see how hashes behave, feel free to hash to use this Python code:

import hashlib

# place the text you wish to hash in between the apostrophies

text = “”.encode(’utf8’)

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

Do you need something to hash? Use this article. Excluding the hash itself below, the below that & the images (so just the text). the SHA hash of this article, from the first to the final word before the hash, should result in """.encode('utf8')

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