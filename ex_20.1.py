fib_dic={}
def recurve(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		if n not in fib_dic:
			fib_dic[n] = recurve(n-1)+recurve(n-2)
		return fib_dic[n]

print(recurve(300))

def sum(n):
	if n == 1:
		return 1
	else:
		return n + sum(n-1)

print(sum(100))

def power(x,n):
	if n == 0:
		return 1
	else:
		return x*power(x,n-1)

print(power(4,10))

def reverse(lista):
	i = len(lista)
	for k in range(i):
		lista[k-1] = lista[k] 
	return lista

lista = [1,2,3,4]
print(reverse(lista))