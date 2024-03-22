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

def zfermat(n, verbose=True):
    a = isqrt(n)
    #if a % 2 == 0:
    #    a += 1
    steps = 0
    while (n % a) != 0:
        a += 1
        #steps += 1
    #print("fermat steps", steps)
    p = a
    q = n // a
    return p, q

def ztx(n, psize):
    sq = isqrt_mod(n)
    sq_mod = isqrt(n)
    sq2 = sq * 2
    sq3 = sq * 3
    sqm2 = sq_mod * 2
    a = sq_mod
    #sq3 = ((n * n) % (sq * 2))
    #n2 = int(n // 2)
    sqs = isqrt_mod(a)
    sqp = isqrt_mod(psize)
    l = int(gmpy2.log(n))
    ll = int(gmpy2.log(l))
    n2 = int(n // 2)
    sql = sq // l
    #sqm = (sq + (sqs))
    sqh = sq // 2
    sqm = (sq - (l * l))
    ls = l * l
    x = (n2 - sq2) * 2
    #a = ((n2 - sq) * 1) + sqs
    y = ((n2 - sq) * 2) + (sqs * 2)
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) - (ll ** ll * l * ll * ll * l))
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) + (ll ** ll * l))
    #a = sq + (psize * psize * psize * psize * psize)
    a = sq_mod + (sqs * psize * ll) + (sqs * 2)
    if a % 2 == 0:
        a += 1
        print("help")
    #a = ((n2 - sq) * 2)
    #x = sq2
    #a = sq
    v = sq * l
    print(a, l, ll, sqs, sq, sq2, sq3, n2, x, y)
    print(sq, sq_mod)
    steps = 0
    ptxt = 2
    #while ptxt != 65:
    while ((n % a) != 0):
    #while ((n % a) != x):
    #while b*b != b2:
        #a = ((a - 2) % y)
        a += 2
        #b2 = a*a - n
        #b = isqrt(b2)
        #try:
        #    Osk = number.inverse(pk, a)
        #except ValueError:
        #    continue
        #ptxt = decrypt(ctxt, Osk, n)
        #print(ptxt)
        #steps += 1
    #print("ztx steps", steps)
    print("result", a, a % sq)
    #p=a+b
    #q=a-b
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
p, q = zfermat(n)
e = time.time()
print(e - s)
print(p, q)
#p, q = ztx(n)
#print(p, q)
s = time.time()
ap, aq = ztx(n, psize)
e = time.time()
print(e - s)
print(ap, aq)
#print(T, n % T)
#Osk = number.inverse(pk, aq)
#ptxt = decrypt(ctxt, Osk, n)
#print(ptxt)
#ctxt = encrypt(123, pk, n)
#ptxt = decrypt(ctxt, Osk, n)
#print(ptxt)
