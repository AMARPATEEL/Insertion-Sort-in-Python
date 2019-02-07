def inserctionSort(lista):
	for i in range(1,len(lista)):
		valor=lista[i]
		j = i
		while j>0 and lista[j-1]>valor:
			lista[j]=lista[j-1]
			j=j-1
		lista[j]=valor
lista=[55,44,33,22]
inserctionSort(lista)
print(lista)
