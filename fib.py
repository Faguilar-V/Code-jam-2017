import matplotlib.pyplot as plt
from time import time

"""
initial_time = time()

#recursivo
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
"""       
   
#iterativo
def fib(n):
	a, b, c, arr =0, 1, 0, [0, 1]
	
	initial_time = time()
	
	for i in range(n-1):
		c = a + b
		a = b
		b = c
		arr.append(c)
		finaly_time = time()
		finaly_time -= initial_time
		
	return arr

nterms = int(input("Ingresa el n de la serie de fibonacci: "))
array = fib(nterms)
print(array)

y = range(nterms+1)	

plt.plot(array, y)
plt.show()
