import time
import math

def sum_digits(n):
	res=0
	while n>0:
		d = n%10
		res+=d
		n = n//10
	return res

def sum_digits_alt(n):
	res=0
	s = str(n)
	for ch in s:
		res+=int(ch)
	return res

"""
#порівняння швидкодії двох функцій
n = 1295234243
k = 1000000
t = time.time()
for i in range(k):
	sum_digits(n)
print("time used:",time.time()-t)

t = time.time()

for i in range(k):
	sum_digits_alt(n)

print("time used alt:",time.time()-t)
"""

#функція перевірки, чи є число n простим
#просто пробігаємо всі числа від 2 до n-1
def is_prime_var1(n):
	if n==1:
		return False
	for d in range(2, n):
		if n%d==0:
			return False
	return True
#перша ідея оптимізація - перевіряти тільки непарні дільники
def is_prime_var2(n):
	if n==1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	for d in range(3, n, 2):
		if n%d==0:
			return False
	return True

#наступна ідея оптимізація - перевіряти тільки непарні дільники, що не діляться на 3
def is_prime_var3(n):
	if n==1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	if n==3:
		return True
	if n%3==0:
		return False
	for d in range(6, n, 6):
		if n%(d-1)==0:
			return False	
		if n%(d+1)==0:
			if d+1==n:
				return True
			else:
				return False
	return True

#наступна ідея оптимізація - перевіряти тільки непарні дільники, що не діляться на 3
#і йти до кореня з n
def is_prime_var4(n):
	if n==1:
		return False
	if n==2:
		return True
	if n%2==0:
		return False
	if n==3:
		return True
	if n%3==0:
		return False
	for d in range(6, n, 6):
		if n%(d-1)==0:
			return False	
		if n%(d+1)==0:
			if d+1==n:
				return True
			else:
				return False
		if (d+1)*(d+1)>=n:
			break;
	return True

# Подальша ідея оптимізації - вести список простих чисел і перевіряти подільність лише на прості
# Доходячи до кореня з n

primes=[]
def is_prime_var5(n):
	if n==1:#перевіряємо виняток
		return False
	maxD = math.floor(math.sqrt(n))#максимальний дільник, до якого треба перевіряти
	# пробігаємося по простих числах, раніше знайдених
	for d in primes:
		if d>maxD:#якщо вийшли за максимум, далі не пробігаємося
			break
		if n%d==0:#якщо число ділиться на якесь з простих, то повертаємо, що воно не просте
			return False
	return True

#виводимо список всіх простих чисел від 1 до 100
t = time.time()
total_primes=0
maxN = 100000000
maxNeededPrime = math.ceil(math.sqrt(maxN))
for n in range(1,maxN+1):
	if is_prime_var5(n):
		# print(n)
		total_primes+=1

		if n<=maxNeededPrime:
			primes.append(n)
print("total_primes=",total_primes)
print(time.time()-t)