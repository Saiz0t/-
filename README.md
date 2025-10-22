a = 1
while a == 1:
    starts = input("найти книгу по названию - 1  \n"
                   "удалить книгу - 2  \n"
                   "добавить книгу - 3  \n"
                   "удалить все - 4   \n"
                   "вывести весь файл - 5 \n")
    if starts == "3":
        try:
            tittle_book = input('Введите название книги и год через двоеточие: ')
            myfile = open('books.txt', 'a')
            myfile.write(tittle_book + '\n')
            myfile.close()
        except:
            print('Ошибка,')

    elif starts == "1":
        try:
            myfile = open('books.txt', 'r')
            content = input("название: ")
            print(content.get)
            myfile.close()
            print(content)
        except:
            print("Ошибка, такой книги нет")

    elif starts == "2":
        try:
            title = input('Введите название книги которую хотите удалить')
            myfile = open('books.txt', 'w')
            books = myfile.readlines(title)
            del books [title]
            myfile.close()
        except:
            print("Ошибка, такой книги нет")

    elif starts == "4":
        try:
            myfile = open('books.txt', 'r').close()
        except:
            print("Ошибка")

    elif starts == "5":
        myfile = open('books.txt', 'r')
        concept = myfile.read()
        print(concept)
    else:
        print("ошибка")
