# rsa-tool
rsa-tool implemented in Python. An all-in-one tool to solve most of the problems at CTFs.

### Attacks Include
  
 - Prime N detection
 - Weak public key factorization
 - Wiener's attack
 - Hastad's attack (Small public exponent attack)
 - Small q (q < 100,000)
 - Common factor between ciphertext and modulus attack
 - Fermat's factorisation for close p and q
 - Gimmicky Primes method
 - Past CTF Primes method
 - Self-Initializing Quadratic Sieve (SIQS) using Yafu
 - Common factor attacks across multiple keys
 - Small fractions method when p/q is close to a small fraction
 - Boneh Durfee Method when the private exponent d is too small compared to the modulus (i.e d < n^0.292)
 - Elliptic Curve Method
 - Pollards p-1 for relatively smooth numbers


### Usage
```
git clone https://github.com/p4r4xor/rsa-tool.git  
cd integer-factorization/  

```
Feel Free to explore each of the following tools.
```
 Main files to run are the following
 real_rsa ------ python RsaCtfTool.py
 rsatool ------- python rsatool.py
```
