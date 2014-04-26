#!/usr/bin/python

# Das RSA-Verfahren - Entschluesselung (Beispiel vom RSA Skript, Seite 9)

#frase = '23551505098561251305962706011712481096205082503'
frase = '2355150509850061251305962706011700012481096205082503'

n = 2773

e = 157

frsize = len(frase)

Li = []

for i in range(frsize/4):
	Li.append(frase[(4*i):(4*i+4)])

#print Li

dic = {'-': '00',
	   'A': '01',
	   'B': '02',
	   'C': '03', 
	   'D': '04', 
	   'E': '05', 
	   'F': '06', 
	   'G': '07', 
	   'H': '08', 
	   'I': '09', 
	   'J': '10', 
	   'K': '11', 
	   'L': '12', 
	   'M': '13', 
	   'N': '14',
	   'O': '15', 
	   'P': '16', 
	   'Q': '17', 
	   'R': '18', 
	   'S': '19', 
	   'T': '20', 
	   'U': '21', 
	   'V': '22', 
	   'W': '23', 
	   'X': '24', 
	   'Y': '25', 
	   'Z': '26' }
	   
def largemod(a,b,m):
	binb = bin(b)

	#print binb

	size = len(binb) -3

	#print size

	L = [int(i) for i in str(bin(b))[2:]]

	#print L

	x = a % m

	N = [x]

	for j in range(size):
		pow2 = pow(x,2)
		x = pow2 % m
		N = [x] + N

	#print N

	#print len(N)

	product = 1

	for k in range(size+1):
		if(L[k]==1):
			product = product * N[k]
			
	result = product % m
	#print 'res: ' ,result
	
	strresult = str(result)
	
	if(len(strresult) == 3):
		strresult = '0' + strresult
		
	if(len(strresult) == 2):
		strresult = '00' + strresult
		
	if(len(strresult) == 1):
		strresult = '000' + strresult
		
	return strresult

#size = len(frase)

finalstring = ''

LM = []

for i in range(frsize/4):
	next = largemod(int(Li[i]), e, n)
	finalstring = finalstring + next
	#print largemod(int(codiert[i]), e, n)
	LM.append(next)
	
print LM	
	
print finalstring #this comes with an extra '17' at the end





	


