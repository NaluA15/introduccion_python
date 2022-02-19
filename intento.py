 
conjugacion = {
	'ar': ('o', 'as', 'a', 'amos', 'ais', 'an'),

	'er': ('o', 'es', 'e', 'emos', 'is', 'en'),

	'ir': ('o', 'es', 'e', 'imos', 'is', 'en')

}


verbo = input("Ingrese verbo: ")


prefijo = verbo[:-2]

sufijo = verbo[-2:]
 

for i in range(len(['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos'])):
    print (['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos'])[i] + " " + prefijo + conjugacion[sufijo][i]