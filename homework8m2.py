books = []

def add_book(book_id, title):

    books.append({"id": book_id, "title": title})
    print(f"Книга добавлена: {title}")

def delete_book(book_id):

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print(f"Книга с id {book_id} удалена")
            return
    print(f"Книга с id {book_id} не найдена")

def update_book_title(book_id, new_title):

    for book in books:
        if book["id"] == book_id:
            book["title"] = new_title
            print(f"Название книги с id {book_id} обновлено")
            return
    print(f"Книга с id {book_id} не найдена")

def get_all_books():

    return books

if __name__ == "__main__":

    add_book(1, "Harry Potter")
    add_book(2, "Lord of the Rings")

    update_book_title(1, "Harry Potter and the Chamber of Secrets")
    delete_book(2)
    all_books = get_all_books()
    print("\nВсе книги:")
    for book in all_books:
        print(book)