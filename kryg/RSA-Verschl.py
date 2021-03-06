#!/usr/bin/python

# Das RSA-Verfahren - Verschluesselung (Beispiel vom RSA Skript, Seite 9)

frase = 'ICH-TREFFE-HEUTE-ABEND-EIN'

n = 2773

e = 17


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
	   'Z': '26',
	   '00': '-',
	   '01': 'A',
	   '02': 'B',
	   '03': 'C', 
	   '04': 'D', 
	   '05': 'E', 
	   '06': 'F', 
	   '07': 'G', 
	   '08': 'H', 
	   '09': 'I', 
	   '10': 'J', 
	   '11': 'K', 
	   '12': 'L', 
	   '13': 'M', 
	   '14': 'N',
	   '15': 'O', 
	   '16': 'P', 
	   '17': 'Q', 
	   '18': 'R', 
	   '19': 'S', 
	   '20': 'T', 
	   '21': 'U', 
	   '22': 'V', 
	   '23': 'W', 
	   '24': 'X', 
	   '25': 'Y', 
	   '26': 'Z' }
	     
   
	   
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

size = len(frase)

codiert = []

codsize = 0

for i in range(size):
	#print i
	if(i%2==1):
		codiert[codsize-1] = codiert[codsize-1] + dic[frase[i]]
		#print codsize
	else:
		codiert.append(dic[frase[i]])
		codsize = codsize +1
		
codsize = codsize -1
		
#print codiert

if(not (len(codiert[codsize]) == 4)):
	codiert[codsize] = codiert[codsize] + '17'
	
print codiert


finalstring = ''

LM = []

for i in range(codsize+1):
	next = largemod(int(codiert[i]), e, n)
	finalstring = finalstring + next
	#print largemod(int(codiert[i]), e, n)
	LM.append(next)
	
print LM

print finalstring





	


