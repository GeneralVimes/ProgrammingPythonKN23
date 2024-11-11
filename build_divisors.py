# Задача: дано розклад числа на прості множники
# Цей розклад має вигляд 2х масивів однакової довжини: самі дільники та їхні степені
# Приклад: для числа 1800 = 1800 = 2^3×3^2×5^2
# дільники: [2, 3, 5]
# степені:  [3, 2, 2]

# Треба згенерувати всі дільничи числа 1800

# Ми можемо генерувати дільники числа 1800, беручи добутки чисел [2, 3, 5] такі, щоб 
# степень двійки була від 0 до 3, степень трійки від 0 до 2 і степень 5ки від 0 до 2

# Якщо дільників рівно 3, можна було б написати 3 вкладених for-цикли та пробігати їхні значення від 0 до3, від 0 до 2 та від 0 до 2 і отримати всі дільники числа 1800
prime_divisors = [2, 3, 5]
prime_powers = [3, 2, 2]

for a0 in range(0, prime_powers[0]+1):
	for a1 in range(0, prime_powers[1]+1):
		for a2 in range(0, prime_powers[2]+1):
			d = prime_divisors[0]**a0 * prime_divisors[1]**a1 * prime_divisors[2]**a2
			print(d)

# Такий підхід буде працювати для числа 1800 і за аналогією, з усіма числами, що діляться лине на 2, 3 та 5
# Якщо ж у числа будуть інші прості дільники (7, 11, 13 і т.д.), то при такому підході треба переписувати програмний код та додавати нові вкладені цикли
# Треба написати універсальну функцію, яка б пробігала по циклу з довільним числом параметрів