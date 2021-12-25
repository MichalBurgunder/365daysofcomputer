import math
import hashlib

# the text that eventually gets hashed
text = "".encode('utf8')

def md5_hash_it(text):
    result = hashlib.md5(text)
    return result.hexdigest()

def sha256_hash_it(text):
    result = hashlib.sha256(text)
    return result.hexdigest()

def birthday_attack(probability, number_bits):
    return math.sqrt(2*number_bits*math.log(1/(1-probability)))


p = 0.5

res = birthday_attack(p, 2**128)
res2 =  birthday_attack(p, 2**160)

print(res)
print(res2)

# custom hashing
sha256_result = sha256_hash_it()
md5_result = md5_hash_it()

print(sha256_result)
print(md5_result)