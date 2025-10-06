# qa_python

---

##  Что делает приложение

Класс `BooksCollector` позволяет:
- Добавлять книги и указывать им жанры.
- Сохранять книги в список избранных.
- Получать книги по жанрам и возрастным ограничениям.

---

##  Реализованные тесты

Все тесты написаны с использованием **pytest**.  
В каждом тесте создаётся новый экземпляр `BooksCollector`, чтобы тесты были независимыми.  
Некоторые тесты используют **параметризацию** для сокращения повторяющегося кода.

###  Список тестов:

| № | Метод класса | Название теста | Что проверяет |
|---|---------------|----------------|----------------|
| 1 | `add_new_book` | `test_add_new_book_valid` | Добавление новых книг с корректными названиями (параметризация) |
| 2 | `add_new_book` | `test_add_new_book_too_long_name` | Проверка, что книга с названием длиннее 40 символов не добавляется |
| 3 | `set_book_genre` | `test_set_book_genre_success` | Успешная установка жанра книге |
| 4 | `set_book_genre` | `test_set_book_genre_invalid_genre` | Проверка, что жанр не устанавливается, если его нет в списке допустимых |
| 5 | `get_books_with_specific_genre` | `test_get_books_with_specific_genre` | Возвращаются только книги с заданным жанром |
| 6 | `get_books_for_children` | `test_get_books_for_children` | Проверка фильтрации книг без возрастных ограничений |
| 7 | `add_book_in_favorites` | `test_add_book_in_favorites` | Добавление книги в избранное |
| 8 | `add_book_in_favorites` | `test_add_book_in_favorites_twice` | Невозможно добавить книгу в избранное дважды |
| 9 | `delete_book_from_favorites` | `test_delete_book_from_favorites` | Удаление книги из избранного |
| 10 | `get_list_of_favorites_books` | `test_get_list_of_favorites_books` | Проверка корректного вывода списка избранных книг |