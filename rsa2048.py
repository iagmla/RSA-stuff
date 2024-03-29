from Crypto.Util import number
import gmpy2
import math
from rsa import keygen, encrypt, decrypt
import time

# Estimated 838 days to factor

n = 25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357
print(len(str(n)))

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

def ztx(n, psize):
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
    sql = sq // l
    #sqm = (sq + (sqs))
    sqh = sq // 2 // 2 // 2
    sqm = (sq - (l * l))
    ls = l * l
    x = (n2 - sq2) * 2
    #a = ((n2 - sq) * 1) + sqs
    y = ((n2 - sq) * 2) + (sqs * 2)
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + sqs)
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) + ((ll ** ll * (psize * psize))))
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) - (ll ** ll * l * ll * ll * l))
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) - (ll ** ll * l * ll * ll * l))
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) - (ll ** ll * l * ll * ll * ll))
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) + (ll ** ll * l)) + sql
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) + (ll ** ll * l)) + (sql + (ll ** ll))
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) + (ll ** ll * l)) - (sql + (ll ** ll) + sql)
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * l) + (ll ** ll * l)) - (sql + (ll ** ll) + sql)
    #a = (sq + (sqs * l * ll) + sql) + (((l * l * l * l) * ll) + (sqs * ll) + (ll ** ll * l))
    #a = sq + (sqs * ll * l * ll)
    a = sq + (psize * psize)
    if a % 2 == 0:
        a += 1
    #a = ((n2 - sq) * 2)
    #x = sq2
    #a = sq
    v = sq * l
    print(a, l, sqs, sq, sq2, sq3, n2, x, y)
    b2 = a*a - n
    b = isqrt(n)
    steps = 0
    ptxt = 2
    #while ptxt != 65:
    while ((n % a) != 0):
    #while ((n % a) != x):
    #while b*b != b2:
        #a = ((a - 2) % y)
        a -= 2
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
#sk, pk, n, t, p, q = keygen(psize)
#print(t, p, q)
#print(n % t)
#message = b"A"
#msg = number.bytes_to_long(message)
#ctxt = encrypt(msg, pk, n)
#PTXT = decrypt(ctxt, sk, n)
#print(PTXT)
#s = time.time()
#p, q = fermat(n)
#e = time.time()
#print(e - s)
#print(p, q)
#p, q = ztx(n)
#print(p, q)
pk = 0
ctxt = 0
s = time.time()
ap, aq = ztx(n, psize)
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
