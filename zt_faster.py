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

def zfermat(n, verbose=True):
    a = isqrt(n)
    #if a % 2 == 0:
    #    a += 1
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
    sq2 = sq * 2
    sq3 = sq * 3
    #sq3 = ((n * n) % (sq * 2))
    #n2 = int(n // 2)
    a = isqrt(n)
    sqs = isqrt(a)
    l = int(gmpy2.log(n))
    ll = int(gmpy2.log(l))
    n2 = int(n // 2)
    sql = sq // (l * l)
    #sqm = (sq + (sqs))
    sqh = sq // 2
    sqm = (sq - (l * l))
    ls = l * l
    x = (n2 - sq2) * 2
    #a = ((n2 - sq) * 1) + sqs
    y = ((n2 - sq) * 2) + (sqs * 2)
    a = (sq + (sqs * l * ll) + sql)
    if a % 2 == 0:
        a += 1
    #a = ((n2 - sq) * 2)
    #x = sq2
    #a = sq
    v = sq * l
    print(a, l, ll, sqs, sq, sq2, sq3, n2, x, y)
    b2 = a*a - n
    b = isqrt(n)
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

psize = 32
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
ap, aq = ztx(n, pk, ctxt)
e = time.time()
print(e - s)
print(ap, aq)
#print(T, n % T)
#Osk = number.inverse(pk, T)
#ptxt = decrypt(ctxt, Osk, n)
#print(ptxt)
#ctxt = encrypt(123, pk, n)
#ptxt = decrypt(ctxt, Osk, n)
#print(ptxt)
