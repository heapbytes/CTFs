from Crypto.Util.number import long_to_bytes

n = 112982701372174135714541042310119603841026379112918124295881022614737112371220762441907782664659731337882611618073932602250654493138913463938845301253189700405866110321629159954074959013313377755909094741063956063693566385004932946379171399803086360345144176502740660343813066761541114575303369296657820791163
e = 65537
c = 88141540951737078954711359053703593325078389546811543323485621484335479181438565486859296481048233669690960889452061331519730183047651396823229616235927347293019123019960473648346632385013116149218399356862585923576702106272464521515411861334123999555184256317150974435399215722800702933617092969151016036160

phi = n -1

d = pow(e,-1,phi)

flag = pow(c,d,n)
print(long_to_bytes(flag).decode())

# Flag : Gisec{prime?big_mistake}

