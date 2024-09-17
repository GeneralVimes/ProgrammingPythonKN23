"""
n = 5
m=n/2
print(m)
p=n//2
print(p)
d=n%3
# print(d)

n  += 3
print(n)
"""
# n=17
# if n>10:
# 	print("big")
# else:
# 	print("small")

# n=17
# if n>20:
# 	print("big")
# elif n>10:
# 	print("average")
# else:
# 	print("small")

# for n in range(5,10,2):
	# print(n)

"""
#програма для моделювання сіракузської послідовності (задача "3n+1")
n = 777
x=0 #кількість кроків
while n!=1:
	if n%2==0:
		n=n//2
	else:
		n=3*n+1
	x+=1
	print(n)
print(x,"кроків")
"""
"""
def count_steps(n):
	x=0 #кількість кроків
	while n!=1:
		if n%2==0:
			n=n//2
		else:
			n=3*n+1
		x+=1
		# print(n)
	return x;

#пробіжимося по n від 1 до 1000 та визначимо для них кількість кроків
for n in range(1, 1000):
	print(n, count_steps(n))
"""

"""
ar = [1,5,3,8,0]
print(ar[2])
ar[4] = 12
print(ar)
ar.append(4)
ar.append(7)
ar.append(2)
ar.append(1)
print(ar)
"""
"""
string = "Hello, World!"
res=""
for n in range(len(string)):#n - це номер символа у рядку string
	ch = string[n] #ch - це символ рядку string під номером n
	
	res = ch + res
	print(n, ch, res)
"""

string = "Hello, World!"
print(string[1:8])
print(string[1:8:2])#перший:останній(не включ):крок
print(string[8:1:-1])
print(string[::-1])