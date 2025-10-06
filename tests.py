import pytest
from main import BooksCollector


class TestBooksCollector:

    #  Тест add_new_book — добавление новой книги
    @pytest.mark.parametrize('book_name', [
        'Властелин колец',
        'Пикник на обочине',
        'Короткое название'
    ])
    def test_add_new_book_valid(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()
        assert collector.get_book_genre(book_name) == ''

    #  Тест add_new_book — книга не добавляется, если длиннее 40 символов
    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)

        assert long_name not in collector.get_books_genre()

    #  Тест set_book_genre — установка жанра книге
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')

        assert collector.get_book_genre('Матрица') == 'Фантастика'

    #  Тест set_book_genre — жанр не устанавливается, если его нет в списке genre
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Драма')

        assert collector.get_book_genre('Книга') == ''

    #  Тест get_books_with_specific_genre — возвращает только книги нужного жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Комедии')
        collector.set_book_genre('Книга 2', 'Ужасы')

        result = collector.get_books_with_specific_genre('Комедии')

        assert result == ['Книга 1']

    #  Тест get_books_for_children — возвращает книги без возрастного рейтинга
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Смешарики')
        collector.add_new_book('Оно')
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')

        books_for_children = collector.get_books_for_children()

        assert 'Смешарики' in books_for_children
        assert 'Оно' not in books_for_children

    #  Тест add_book_in_favorites — добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    #  Тест add_book_in_favorites — нельзя добавить книгу дважды
    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.add_book_in_favorites('Шрек')
        collector.add_book_in_favorites('Шрек')

        assert collector.get_list_of_favorites_books().count('Шрек') == 1

    #  Тест delete_book_from_favorites — удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Том и Джерри')
        collector.add_book_in_favorites('Том и Джерри')
        collector.delete_book_from_favorites('Том и Джерри')

        assert 'Том и Джерри' not in collector.get_list_of_favorites_books()

    #  Тест get_list_of_favorites_books — возвращает корректный список
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')

        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Книга 1', 'Книга 2']

