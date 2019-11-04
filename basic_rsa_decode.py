def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print('--------------------------------------------------------')
print("Please use any of following to factorize N")
print("sudo pip install factordb-pycli")
print("Usage: factordb integer_you_want_to_factorize")
print("Or use https://github.com/p4r4xor/integer-factorization :) ")
print("--------------------------------------------------------")
print("----------------------")
print"INPUT"
print"-----------------------"
p = input("prime_1: ")
q = input("prime_2: ")
e = input("e: ")
c = input("cipher_text (integer): ")
d = modinv(e, (p - 1) * (q - 1))
print"-----------------------"
print"OUTPUT"
print"-----------------------"
print "d:",d
plain_text = pow(c, d, p * q)
print"plain_text:",plain_text
