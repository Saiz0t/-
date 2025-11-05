
b = 1
books = []
def save_books_file():
    with open('books.txt', 'w') as myfile1:
        myfile1.write(",".join(map(str, books)))
while b == 1:
    print("добавить книгу - 1\n"
          "удалить книгу - 2\n"
          "найти книгу - 3\n"
          "удалить все книги - 4\n"
          "вывести все - 5\n"
          "заменить - 6 ")
    task = input()
    if task == "1":
        title_and_year = input("Введите название и год книги: ")
        books.append(title_and_year)
        save_books_file()
        print(f'Книга "{title_and_year}" успешно добавлена.')
    elif task == "5":
        myfile = open('books.txt', 'r')
        concept = myfile.read()
        print(concept)
    elif task == "2":
        try:
            title_and_year = input("Введите название и год книги для удаления: ")
            books.remove(title_and_year)
            save_books_file()
        except:
            print("баг")
    elif task == "4":
        books.clear()
        save_books_file()
    if task == "6":
        try:
            old = input("Введите название и год книги, которую хотите заменить: ")
            new = input("Введите новое название и год книги: ")
            for i, book in enumerate(books, 1):
                if old in book or old == str(i):
                    ntu = books.index(book)
                    books[ntu] = new
            save_books_file()
        except:
            print("Отстань")
    elif task == "3":
        search = input('Введите название книги которую вы хотите найти: ')
        myfile = open('books.txt', 'r')
        books = myfile.readlines()
        myfile.close()
        if search in books:
            print(search)
        else:
            print("Такой книги нету в файле")