#Шифр Цезаря - є ключ - число n і кожна літера замінюється на іншу через n позицій в алфавіті
# для дешифрування потрібно виконати обернений зсув
def ceasar_encode(text, n):
	# примає текст для шифрування та ключ, а повертає зашифрований текст
	# потрібен весь алфавіт
	alphabet="абвгґдеєдзиіїйколмнопрстуфхцчшщьюя"
	# одразу створюємо пусту строкову змінну для результату
	res=""

	# пробігаємося по символах вхідного тексту
	for x in text:#x буде пробігати всі значення літер у вхідному тексті
		# чи є х у алфавіті
		id = alphabet.find(x)#якщо вона є, то id буде рівним позиції літери х у alphabet
		# якщо нема, то id буде -1
		if id!=-1:
			id1 = id+n#знаходимо позицію тієї літери, якою будемо зашифровувати дану
			# можливий підводний камінь: якщо id+n вийде ща межі алфавіту
			# тоді треба починати алфвіт з початку
			# це можна вирішити через if
			# if id1>=len(alphabet):
			#	id1-=len(alphabet)
			# але так зациклення буде оброблятися лише для невеликих n
			# а якщо, наприклад, n==100, то id1 буде все одно виходити за алфавіт
			# можна зробити через while, віднімати довжину доти, доки id1 виходить за межі алфавіту
			while id1>=len(alphabet):
				id1-=len(alphabet)
			# подумати, як можна швидше, не циклом, скинути величину id1, що виходить за межі довжини алфавіту

			# тепер id1 гарантовано між 0 та 32 (включаючи)
			# знаходимо літеру у позиції id1
			y = alphabet[id1]
			# тепер в результат допишемо літеру y
			res+=y
		else:#якщо ж символа не було в алфавіті, залишаємо його у шифрованому тексті як є
			res+=x

	return res

message = "привіт, як справи в тебе?"
key = 3
encoded_message = ceasar_encode(message,key)
print("оригінал:",message)
print("зашифроване:",encoded_message)
# щоб декодувати треба викликатифункцію кодування, лише з від'ємним ключем
# decoded_message = ceasar_encode(encoded_message,-key)
# print("розшифроване:",decoded_message)

# якщо ми не знаємо ключ, можемо просто перебрати 32 варіанти для ключа і подивитися, що вийде
#for possible_key in range(1, 33):
#	print(possible_key, ceasar_encode(encoded_message,-possible_key))

# Зараз функція шифрування шифрує лише маленькі літери
# можна весь текст перед шифруванням перевести в нижній регістр
# але що можна зробити, якщо ми все-таки хочемо, щоб і великі літери також шифрувалися, але залишалися великими?


# Квадрат Полібія для кирилиці - це квадрат 6х6, в якому спочатку буде писатися слово ключ, а потім - вся решта алфавіта
# Для латини це квадрат 5х5, де i та j займають одну клітинку

def build_polybius_square(key):
	#готуємо пустий масив 6х6
	res=[]
	for i in range(6):
		res.append("")
	
	alphabet="абвгґдеєдзиіїйколмнопрстуфхцчшщьюя"
	# пробігаємося по літерах ключа та унікальні літери заносимо в комірки масиву res
	# індекс початкової комірки
	idx=0;
	idy=0;
	used_letters=""
	for x in key:
		if not x in used_letters:
			used_letters+=x
			res[idx]+=x
			idx+=1
			if idx>=6:
				idx=0
				idy+=1
	# після цього додаємо решту алфавіту
	for x in alphabet:
		if not x in used_letters:
			used_letters+=x
			res[idx]+=x
			idx+=1
			if idx>=6:
				idx=0
				idy+=1
	return res

# print()


def polybius_encode(text, square):
	res=""
	for x in text:
		# шукаємо літеру шифрованого тексту у квадраті
		# шукаємо потрібнку колонку
		idx=-1;#координати клітники літери у квадраті
		idy=-1;
		for id_col in range(0, len(square)):
			id_row = square[id_col].find(x)
			if id_row!=-1:
				idx=id_col
				idy = id_row
				break;

		if idx!=-1:
			idy+=1
			if idy>=len(square[idx]):
				idy=0
			res+=square[idx][idy]
		else:
			res+=x
	return res

text_key = "секрет"
square = build_polybius_square("секрет")
print(square)

message1="""
Титан — найбільший супутник Сатурна, другий за розміром у Сонячній системі. Другий за віддаленістю серед семи гравітаційно округлих супутників Сатурна. Єдиний супутник у Сонячній системі, який має щільну атмосферу, що складається переважно з азоту й метану, а також єдине місце, окрім Землі, де знайдено рідини у формі морів, озер та річок.

Титан відкритий в 1655 році астрономом Християном Гюйгенсом, який досліджував кільця Сатурна за допомогою телескопа. В 1944 році встановили, що супутник має щільну атмосферу. Впродовж наступних десятиліть він досліджувався за допомогою космічного телескопа «Габбл» та космічних апаратів «Піонер-11», «Вояджер-1» та «Кассіні». У 2005 році на поверхню Титану сів зонд «Гюйгенс», що зробило його другим природним супутником Сонячної системи, на які відбувалася посадка космічних апаратів.

Титан складається переважно з водяного льоду та кам'янистих порід. Припускають, що він має велике кам'янисте ядро та кілька шарів; можливе існування підповерхневого океану рідкої води. Поверхня рівнинна, з невеликою кількістю ударних кратерів, гір та дюн; наявні озера з рідкого метану.

"""
print(polybius_encode(message1.lower(),square))