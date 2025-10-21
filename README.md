a = 1
while a == 1:
    starts = input("найти книгу по названию - найти"
                   "удалить книгу - удалить"
                   "добавить книгу - добавить"
                   "удалить все - удалить все   ")
    if starts == "добавить":
        tittle_book = input('Введите название книги и год:')
        myfile = open('books.txt', 'a')
        myfile.write(tittle_book + '\n')
        myfile.close()
    elif starts == "найти":
        myfile = open('books.txt', 'r')
        content = myfile.read()
        myfile.close()
        print(content)
    elif starts == "удалить":
        title = input('Введите название книги которую хотите удалить')
        myfile = open('books.txt', 'r')
        books = myfile.readlines()
        myfile.close()
    elif starts == "удалить все":
        myfile = open('books.txt', 'r').close()
    else:
        print("ошибка")
