b = 1
books = []
def save_books_file():
    with open('books.txt', 'w') as file:
        file.write(",".join(map(str, books)))
while b == 1:
    print("добавить книгу - 1\n"
          "удалить книгу - 2\n"
          "найти книгу - 3\n"
          "удалить все книги - 4\n"
          "вывести все - 5\n"
          "заменить - 6 ")
    a = input()
    if a == "1":
        title_and_year = input("Введите название и год книги: ")
        books.append(title_and_year)
        save_books_file()
        print(f'Книга "{title_and_year}" успешно добавлена.')
    elif a == "5":
        myfile = open('books.txt', 'r')
        concept = myfile.read()
        print(concept)
    elif a == "2":
        title_and_year = input("Введите название и год книги для удаления: ")
        books.remove(title_and_year)
        save_books_file()
    elif a == "4":
        books.clear()
        save_books_file()
    if a == "6":
        old = input("Введите название и год книги, которую хотите заменить: ")
        new = input("Введите новое название и год книги: ")
        index = books.index(old)
        books[index] = new
        save_books_file()
    elif a == "3":
        myfile = open('books.txt', 'r', encoding='utf-8')
        content = myfile.read()
        myfile.close()
        print(content)
    else:
        print("баг")
