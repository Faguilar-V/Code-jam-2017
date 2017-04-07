def sheep(n):
	array = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
	j = 0

	if n == 0:
		return ("INSOMNIA")
	
	else:
		while len(array) != 0:
			j += 1
			c = n * j
			temp = str(c)
			for i in range(len(temp)):
				if temp[i] in array:
					array.remove(temp[i])
		return c


casos,aux = int(input()), 0
for i in range(1, casos + 1):
	aux = int(input())
	print "Case #%d: " % (i) + str(sheep(aux))
