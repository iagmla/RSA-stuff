from Crypto.Util import number
import gmpy2
import math
from rsa import keygen, encrypt, decrypt
import time

def isqrt_mod(n):
  l = int(gmpy2.log(n))
  ll = int(gmpy2.log(l))
  x = n
  y = (x + n // x) // ll
  while y < x:
    x = y
    y = (x + n // x) // ll
  return x

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
    while b*b != b2:
        a += 1
        b2 = a*a - n
        b = isqrt(b2)
        steps += 1
    print("fermat steps", steps)
    p=a+b
    q=a-b
    return p, q

def ztx(n, pk, ctxt):
    sq = isqrt(n)
    sq_mod = isqrt_mod(n)
    sq2 = sq * 2
    sq3 = ((n * n) % (sq * 2))
    n2 = int(n // 2)
    a = isqrt(n)
    l = int(gmpy2.log(n))
    ll = int(gmpy2.log(l))
    ls = l * l
    x = (n2 - sq2) * 2
    a = sq_mod * 2
    a = ((n2 - sq) * ll)
    #if a % 2 == 0:
    #    a += 1
    #x = sq2
    #a = sq
    v = sq * l
    print(a, l, sq, sq2, sq3, n2, x)
    b2 = a*a - n
    b = isqrt(n)
    steps = 0
    ptxt = 2
    while ptxt != 65:
    #while ((n % a) != 0):
    #while ((n % a) != x):
    #while b*b != b2:
        #a = ((a * n) % n2)
        a -= ll
        #b2 = a*a - n
        #b = isqrt(b2)
        try:
            Osk = number.inverse(pk, a)
        except ValueError:
            continue
        ptxt = decrypt(ctxt, Osk, n)
        #print(ptxt)
        #steps += 1
    #print("ztx steps", steps)
    print("result", a)
    p=a+b
    q=a-b
    return a

psize = 24
sk, pk, n, t, p, q = keygen(psize)
print(t, p, q)
print(n % t)
message = b"A"
msg = number.bytes_to_long(message)
ctxt = encrypt(msg, pk, n)
PTXT = decrypt(ctxt, sk, n)
print(PTXT)
#p, q = fermat(n)
#print(p, q)
#p, q = ztx(n)
#print(p, q)
s = time.time()
T = ztx(n, pk, ctxt)
e = time.time() - s
print(e)
print(T, n % T)
Osk = number.inverse(pk, T)
ptxt = decrypt(ctxt, Osk, n)
print(ptxt)
ctxt = encrypt(123, pk, n)
ptxt = decrypt(ctxt, Osk, n)
print(ptxt)
