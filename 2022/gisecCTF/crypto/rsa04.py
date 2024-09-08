from Crypto.Util.number import *
from sympy import * 


def getPrimes():
	while True:
		p=getPrime(1024)
		q=nextprime(p)
		return p,q


def encrypt(data,modulus,exponent):
	m = bytes_to_long(data)
	return pow(m,exponent,modulus)

p,q=getPrimes()
n=p*q
e=65537

flag=b'REDACTED'
encrypted = encrypt(flag,n,e)

print(f"modulus N : {n}")
print(f"encrypted message : {encrypted}")

## output
# N : 32219919510426152586745238462649846338856481501819261146488316825965855721457811962585612767322123075029014657633852192407854077747563039617613911265405809733465026568360333424003409099686474913664136521459660017839882803821030404889448337865632805211648367923951305187383572695647101337464402291662464996445236498940229779310623780344162769846221850742109201215053773533136088807007609854117395555230462172074537197893160531285779716438101477700106712937070212574440180234268471977381509645029287186503047434243990221804033394490658118899601265880531489306947634567090005521121362945120861257418372602804954782336679
# C : 17552096424859510977092930360732323539522176558134679498735487491739875408448150133984590260023653976535459076334255165071668209148920842455301832130700694570152799695358683522181484886942897675200804761021836530194116282951027361683594371713428899936834229050124797356404498440751104779827345304245900904255976048865039997051799407805943793352553654942723277966262545196330073401305053126409633919451477054182835431218032209414333276441659480900964864691220770851928431232233794315904644700838299181746804466682417732732091259452631598499303529324015892457416611728775391883219742918980974137422081765639502244594915
