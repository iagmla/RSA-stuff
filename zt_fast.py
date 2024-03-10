from Crypto.Util import number
import gmpy2
import math
from rsa import keygen, encrypt, decrypt
import time

def isqrt(n):
  l = int(gmpy2.log(n))
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=True):
    a = isqrt(n)
    b2 = a*a - n
    b = isqrt(n)
    steps = 0
    while (n % a) != 0:
        a += 1
        steps += 1
    print("fermat steps", steps)
    p = a
    q = n // a
    return p, q

def ztx(n, pk, ctxt):
    sq = isqrt(n)
    sqs = isqrt(sq)
    l = int(gmpy2.log(n))
    ll = int(gmpy2.log(l))
    sqh = sq // 2
    sqm = (sq - (l * l))
    ls = l * l
    a = sq + (sqs * l * ll)
    if a % 2 == 0:
        a += 1
    steps = 0
    while ((n % a) != 0):
        a += 2
        steps += 1
    print("ztx steps", steps)
    print("result", a, a % sq)
    p = a
    q = n // p
    return p, q

psize = 24
sk, pk, n, t, p, q = keygen(psize)
print(t, p, q)
print(n % t)
message = b"A"
msg = number.bytes_to_long(message)
ctxt = encrypt(msg, pk, n)
PTXT = decrypt(ctxt, sk, n)
print(PTXT)
s = time.time()
p, q = fermat(n)
e = time.time()
print(e - s)
print(p, q)
#p, q = ztx(n)
#print(p, q)
s = time.time()
ap, aq = ztx(n, pk, ctxt)
e = time.time()
print(e - s)
print(ap, aq)
