
verbo= input("Ingrese verbo: ")

letrafinal = verbo[len(verbo)-1]
letraantepenultima = verbo[len(verbo)-2]
terminacion = letraantepenultima + letrafinal
verbofinal = verbo.replace(terminacion, "")
print(verbofinal)
print()