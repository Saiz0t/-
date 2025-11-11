b = 1
books = []


def save_books_to_file():
    with open('books.txt', 'w') as myfile1:
        myfile1.write(",".join(map(str, books)))


while 1 == b:
    print("добавить книгу — 1\n"
          "Удалить книгу — 2\n"
          "Найти книгу — 3\n"
          "Удалить все книги — 4\n"
          "вывести все — 5\n"
          "заменить — 6")

    task = input()

    if task == "1":
        title_and_year = input("Введите название и год издания книги: ")
        books.append(title_and_year)
        save_books_to_file()
        print(f'Книга "{title_and_year}" успешно добавлена.')

    elif task == "5":
        with open('books.txt', 'r') as myfile:
            content = myfile.read()
            print(content)

    elif task == "2":
        try:
            title_and_year = input("Введите название и год издания книги для удаления: ")
            books.remove(title_and_year)
            save_books_to_file()
        except ValueError:
            print("Ошибка: книга не найдена.")

    elif task == "4":
        books.clear()
        save_books_to_file()

    elif task == "6":
        try:
            old_title_and_year = input("Введите название и год издания книги, которую вы хотите заменить: ")
            new_title_and_year = input("Введите новое название и год издания книги: ")
            index = next((i for i, book in enumerate(books) if old_title_and_year in book), None)
            if index is not None:
                books[index] = new_title_and_year
                save_books_to_file()
            else:
                print("Ошибка: книга не найдена.")
        except Exception as e:
            print("Ошибка:", e)

    elif task == "3":
        search_term = input("Введите название книги, которую вы хотите найти: ")
        found = False
        with open('books.txt', 'r') as myfile:
            lines = myfile.readlines()
            for line in lines:
                if search_term in line:
                    print(line.strip())
                    found = True
        if not found:
            print("Такой книги нет в файле.")