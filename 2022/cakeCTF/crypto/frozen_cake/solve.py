
from Crypto.Util.number import *

n = 101205131618457490641888226172378900782027938652382007193297646066245321085334424928920128567827889452079884571045344711457176257019858157287424646000972526730522884040459357134430948940886663606586037466289300864147185085616790054121654786459639161527509024925015109654917697542322418538800304501255357308131
a = 38686943509950033726712042913718602015746270494794620817845630744834821038141855935687477445507431250618882887343417719366326751444481151632966047740583539454488232216388308299503129892656814962238386222995387787074530151173515835774172341113153924268653274210010830431617266231895651198976989796620254642528
b = 83977895709438322981595417453453058400465353471362634652936475655371158094363869813512319678334779139681172477729044378942906546785697439730712057649619691929500952253818768414839548038664187232924265128952392200845425064991075296143440829148415481807496095010301335416711112897000382336725454278461965303477
c = 21459707600930866066419234194792759634183685313775248277484460333960658047171300820279668556014320938220170794027117386852057041210320434076253459389230704653466300429747719579911728990434338588576613885658479123772761552010662234507298817973164062457755456249314287213795660922615911433075228241429771610549

ig = (c * inverse(a,n) * inverse(b,n)) %n
flag = long_to_bytes(inverse(ig,n)).decode()
print(flag)


