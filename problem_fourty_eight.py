i = 1
total = 0
while (i < 1001):
	p = 0
	cur = 1
	while (p < i):
		cur *= i
		p += 1
	total += cur
	i += 1
print(total)