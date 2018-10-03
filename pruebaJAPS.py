__author__ = "Jonathan Andres Pardo"

def numerosAletras(numero):
	unidades=('cero uno dos tres cuatro cinco seis siete ocho nueve').split()
	unidadesD=('diez once doce trece catorce quince').split()
	decenas=('diez viente treinta cuarenta cincuenta sesenta setenta ochenta noventa').split()
	numeror=str(numero)
	cuentaCar=len(numeror)
	if cuentaCar==1:
		numeror='00'+numeror
	if cuentaCar==2:
		numeror='0'+numeror
	a=int(numeror[0])
	b=int(numeror[1])
	c=int(numeror[2])

	if a==0:
		if b==0:
			res=unidades[a]
			return res
		elif b==1:
			if c>=0 and c<=5:
				res=unidadesD[c]
				return res
			elif c >= 6 and c <= 9:
				res=decenas[b-1]+' y '+unidades[c]
				return res
		elif b==2:
			if c==0:
				res=decenas[1]
				return res

			elif c>=1 and c<=9:
				res="veinti" + unidades[c]
				return res	

		elif b >=3 and b <= 9:
			if c == 0:
				res = decenas[b]
				return res
			if c>= 1 and c<= 9:
				res = decenas[b-1]+' y '+unidades[c]
                return res
	elif a==1:
		if b==0:
			if c==0:
				res="cien"
				return res
			elif c>=1 and c<=9:
				res="ciento "+unidades[c]
		elif b==1:
			if c>=0 and c<=5:
				res="ciento "+unidadesD[c]
				return res
			elif c>=6 and c<=9:
				res="ciento "+decenas[b-1]+' y '+unidades[c]
				return res	
		elif b==2:
			if c==0:
				res='ciento veinte'
				return res

			elif c>=1 and c<=9:
				res="ciento veinti y" + unidades[c]
				return res
		elif b >=3 and b <= 9:
			if c == 0:
				res = 'ciento '+ decenas[b-1]
				return res
			if c>= 1 and c<= 9:

				res = "ciento "+ decenas[b-1]+' y '+unidades[c]
                return res			
       	elif a>=2 and a<=9:           
       		if a == 5:
       		    prefijo='quinientos '
       		elif a == 7:
       		    prefijo='setecientos '
       		elif a == 9:
       		    prefijo='novecientos '
       		else:
       		    prefijo=unidades[a]+' cientos '
       		if b == 0:
	            if c == 0:
	                res = prefijo
	                return res
	            elif c > 0 and c <= 9:
	                res = prefijo+unidades[c]
	                return res
	        elif b == 1:
	            if c >= 0 and c <= 5:
	                res = prefijo+unidadesD[c]
	                return res
	            elif c >= 6 and c <= 9:
	                res = prefijo+decenas[b-1]+' y '+unidades[c]
	                return res
	        elif b == 2:
	            if c == 0:
	                res = prefijo+' veinte'
	                return res
	            elif c > 0 and c <= 9:
	                res = prefijo+' veinti '+unidades[c]
	                return res
	        elif b >= 3 and b <= 9:
	            if c == 0:
	                res = prefijo+decenas[b]
	                return res
	            elif c > 0 and c <= 9:
	                res = prefijo+decenas[b-1]+' y '+unidades[c]
	                return res	

def run(x):
	numeror=str(x)
	cuentaCar=len(x)
	result=''
	if cuentaCar == 1:
		numeror='00000000'+numeror
	if cuentaCar == 2:
		numeror='0000000'+numeror
	if cuentaCar == 3:
		numeror='000000'+numeror
	if cuentaCar == 4:
		numeror='00000'+numeror
	if cuentaCar == 5:
		numeror='0000'+numeror
	if cuentaCar == 6:
		numeror='000'+numeror
	if cuentaCar == 7:
		numeror='00'+numeror
	if cuentaCar == 8:
		numeror='0'+numeror
	posicion=1
	for i in [0,3,6]:
		var=numeror[i]+numeror[i+1]+numeror[i+2]
		if int(var) != 0:
			res=numerosAletras(var)
			if i == 0:
				result=res+" millones "
			elif i == 3:
				result=result+res+" mil "
			elif i == 6:
				result=result+res
	return result        					

print "Ingrese un numero"
numeroI=raw_input()
print run(numeroI)

			