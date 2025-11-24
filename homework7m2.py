import sqlite3


def create_connection(db_name: str = "library.db"):

    conn = sqlite3.connect(db_name)
    return conn


def create_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    ''')

    conn.commit()
    conn.close()
    print("Таблица 'books' успешно создана.")


def insert_books():

    conn = create_connection()
    cursor = conn.cursor()

    books_data = [
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 5),
        ("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 504, 8),
        ("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 3),
        ("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997, "Фэнтези", 432, 12),
        ("Война и мир", "Лев Толстой", 1869, "Роман-эпопея", 1225, 2),
        ("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 15),
        ("Три товарища", "Эрих Мария Ремарк", 1936, "Роман", 480, 6),
        ("Сто лет одиночества", "Габриэль Гарсиа Маркес", 1967, "Магический реализм", 422, 4),
        ("Атлант расправил плечи", "Айн Рэнд", 1957, "Философия", 1168, 1),
        ("Дюна", "Фрэнк Герберт", 1965, "Научная фантастика", 412, 7),
    ]

    cursor.executemany('''
        INSERT INTO books 
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', books_data)

    conn.commit()
    conn.close()
    print("10 книг успешно добавлено в таблицу 'books'!")


if name == "main":
    create_table()
    insert_books()

    # Проверка: выводим то, что хранится в баз
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, author, number_of_copies FROM books")

    print("\nСодержимое таблицы 'books':")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | {row[1]:35} | Автор: {row[2]:25} | Копий: {row[3]}")

    conn.close()