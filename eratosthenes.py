import math
# визначаємо, до якого числа будемо знаходити прості
maxN = 31
maxSqN = math.floor(math.sqrt(maxN))
# готуємо масив чисел
numbers=[True]*(maxN+1) #робимо масив з maxN невикреслених чисел
print("створили масив, де всі числа невикреслені")
print(numbers)
numbers[0]=False#число 0 не просте, викреслюємо його
numbers[1]=False#число 1 не просте, викреслюємо його
print("викреслили 0 та 1")
print(numbers)

id=0
while True:
# знаходимо наступне невикреслене число до кореня з довжини масиву
	hasNewId = False
	for i in range(id+1, maxSqN+1):
		if numbers[i]:
			id=i;
			hasNewId=True
			break
	#якщо такого числа нема, то виходимо взагалі
	if not hasNewId:
		print("нових чисел ми не викреслимо, виходимо")
		break
	print ("Невикреслене число - число", id)
	#тепер нам треба пробігтися по масиву та викреслити всі числа від 4 до кінця з кроком 2
	for i in range(id*id,maxN+1,id):
		numbers[i] = False
	print ("Пробіглися по масиву та викреслили всі числа, що діляться на", id)
	print(numbers)


