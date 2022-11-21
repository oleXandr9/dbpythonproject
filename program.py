import sqlite3

db = sqlite3.connect('notatky.db')
dbcur = db.cursor()

db.execute('CREATE TABLE IF NOT EXISTS {}(Name PRIMARY KEY, Data, Priority)'.format('notatky'))
db.commit()

def insert(nam, dat, pri):
	dbcur.execute('INSERT INTO notatky VALUES(?, ?, ?)', (nam, dat, pri))
	db.commit()

def select():
	r = dbcur.execute('SELECT * FROM notatky').fetchall()
	db.commit()
	return r

def update(nam1, dat, pri, nam2):
	dbcur.execute('UPDATE notatky SET Name=?, Data=?, Priority=? WHERE Name = ?', (nam1, dat, pri, nam2))
	db.commit()

def delete(nam):
	dbcur.execute('DELETE FROM notatky WHERE Name = ?', ('nam',))
	db.commit()


def main():
	print("Виберіть операцію:")
	print("	1)Вставка рядка")
	print("	2)Зчитування рядка")
	print("	3)Зміна рядка")
	print("	4)Видалення рядка")

	x = input("Ваш вибір: ")


	match x:
		case "1":
			nam = input("Введіть назву: ")
			dat = input("Введіть дату: ")
			pri = input("Введіть пріорітет: ")
			insert(nam, dat, pri)
			print("Вставка завершена")
			main()

		case "2":
			r = select()
			print(r) 
			print(" ")
			main()
		case "3": 
			nam1 = input("Введіть назву(для вставки): ")
			dat = input("Введіть дату: ")
			pri = input("Введіть пріорітет: ")
			nam2 = input("Введіть назву(для пошуку): ")
			update(nam1, dat, pri, nam2)
			print(" ")
			main()
		case "4": 
			nam = input("Введіть назву: ")
			delete(nam)
			print(" ")
			main() 
		case _:
			print("Error")


main()