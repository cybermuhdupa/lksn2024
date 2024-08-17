#pip install pycryptodome
from Crypto.Util.number import *
import random
from datetime import datetime

flag = bytes_to_long(b"LKSN{REDACTED}")

def generatepub():
	a, b = 0, 0
	while GCD(a,b) != 1:
		random.seed(int(datetime.now().timestamp()))
		a = random.randint(128, 65536)
		b = random.randint(128, 65536)
	return a, b

p, q = getPrime(1024), getPrime(1024)
pq = p * q

a, b = generatepub()

msg1 = pow(flag, a, pq)
msg2 = pow(flag, b, pq)

print(f"{pq = }")
print(f"{a = }")
print(f"{b = }")
print(f"{msg1 = }")
print(f"{msg2 = }")

"""
pq = 11982142464148814134864150671075176904534148559417853244723822707695481603687379021046034049360104507210192113864132423300699780355828500317773807463435701389832511388542943322856382916032645137238937604382833723434171769405621825132780412079213378151070370563522201385149806626114946712819570640846135563212419789490464480045562307956866356647927988070246216392610399528769002431015999831438204604153541972682767805868108461752048194914375653296537173335460166395656505743502144404992465565550704547724389863637125224487097837966043414503704378488410135776435700021737029503739450135640825156960450569447884702393419
a = 7225
b = 60791
msg1 = 11143593942461757839968611394669696890239723676346538418415666227747882828311719226686744461307505928139278543564173250541813874284290423021214905761086963306355105788943779530437489749268065932352477150255587658027019286960813811574194131863460080584505393708041405829696289961330929602003834707315209877844714397422369378134075494683619061834695642000048814170907985612394143931467004113589230015339538905713331144813895529754983763764812767980506933083410452683829130547403422371908735584251766022684771835026849222278651179936783477567320227628534407254711922406859085858970580349099913701656507022257199694038929
msg2 = 4340530694567439838251218281411978534154446115365844427866900274823417472283890088329179497881941487571461517005953069520640515113146132674680003068150533318235045570615101680933526305754982886030162106309189066219541066924340657593661737752578759931414915485703382800804854645595506405378578261829220945557766907646191309312583106296590505501639203185720089378198117222103423480335385603007566831329615809394449473830878284281784257673008620721337571287752541346915276582576871513568741017136725996877526244322040240159687972916021848795595182944900762056102432818665390686369033358629207903129727788415853231529241
"""