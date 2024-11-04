# Числа Фібоначчі - послідовність, у якій наступне число дорівнює сумі двох попередніх
# Ось початкові числа послідовності
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# Написати функцію, що прийме номер числа у послідовності та поверне саме число
# Приклади:
# 6 -> 13
# 8 -> 34

"""
memory={}

def F(n):
	if n==0:
		return 1
	if n==1:
		return 1
	if n in memory:#перш ніж іти у рекурсію, перевіряємо, чи знаходили ми вже таке значення
		return memory[n] #і якщо знаходили, то беремо з пам'яті
	
	res = F(n-1)+F(n-2)
	memory[n]=res#нові значення вносимо у пам'ять
	return res

for n in range(50):
	print(n, F(n))

"""

# Задача: дано рядок. Згенерувати всі можливі перестановки символів цього рядка
# Приклад: з рядку test можна отримати:
# test
# ttes
# ttse
# estt
# sett
# etst
# stet
# tset
# etts
# tste
# tets
# stte
# Зробивши побудову вручну, помічаємо, що рекурсивна функція має приймати 2 параметри:
# частина рядка, що вже побудована
# літери, які треба доставити
# оголосимо функцію так
def make_all_combinations(ready_string, letters):
	# вихід з рекурсії буде тоді, коли letters - пусте, тобто всі літери ми розставили
	if len(letters)==0:
		print(ready_string)#для тестової функції будемо просто виводити результати на екран
		return
	#якщо в нас є літери, які треба доставити
	#пробігаємося по літерах, доліплюємо їх до побудованої перестановки та знов викликаємо рекурсію з новими параметрами
	# будемо враховувати раніше зустрічені літери
	used_letters=[]
	for i in range(len(letters)):#пробігаємося по всіх літерах
		x = letters[i]
		if not x in used_letters:
			used_letters.append(x)
			#наступний раз будемо викликати рекрусію, коли до побудованого рядка буде доданий ще 1 символ
			new_string = ready_string+x
			#цей же символ треба буде прибрати зі списку нерозставлених символів
			new_letters=letters[0:i]+letters[i+1:]#використовуємо оператор зрізу масиву
			#викликаємо рекурсію
			make_all_combinations(new_string, new_letters)

# make_all_combinations("","test")
# make_all_combinations("","молоко")

# Зненерувати рядки з 0 та 1 довжини n, у яких не буде двох одиниць підряд
# для рекурсії будемо використовувати ready_string - поточний зібраний рядок
# n - цільова довжина рядка
def build_binary_combinations(ready_string, n):
	if len(ready_string)==n:
		print(ready_string)
		return
	if ready_string.endswith("1"):
		build_binary_combinations(ready_string+"0",n)
	else:
		build_binary_combinations(ready_string+"0",n)
		build_binary_combinations(ready_string+"1",n)

# build_binary_combinations("",10)

# Завдання: написати функцію, що знаходитиме кількість бінарних рядків двожини n, у яких 2 одиниці не йдуть підряд





