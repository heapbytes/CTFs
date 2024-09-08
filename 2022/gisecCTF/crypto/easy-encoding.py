from Crypto.Util.number import getPrime, long_to_bytes as ltb ,bytes_to_long as btl

def encrypt(data,modulus,exponent):
	m = btl(data)
	assert m<modulus
	return pow(m,exponent,modulus)

# Initilizing parameters
p = getPrime(110)
q = getPrime(110)
e = 65537
N = p*q

# Message
flag = b"Redacted"
enc  = encrypt(flag,N,e)

print(f"Public Modulus: {N} and Public exponent: {e}")
print(f"The encrypted message is: {enc}")

######## output
# N = 1004995496566346075873930707800493321236968239524622949507762127653
# enrypted = 391954716711415946350985916860618751332906967581871181532410342734