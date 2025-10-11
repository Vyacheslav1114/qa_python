import pytest
from main import BooksCollector


class TestBooksCollector:

    # 1️⃣ add_new_book — добавление новой книги
    @pytest.mark.parametrize('book_name', [
        'Властелин колец',
        'Пикник на обочине',
        'Короткое название'
    ])
    def test_add_new_book_valid(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()
        assert collector.books_genre[book_name] == ''

    # 2️⃣ add_new_book — книга не добавляется, если длиннее 40 символов
    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        long_name = 'А' * 41
        collector.add_new_book(long_name)

        assert long_name not in collector.get_books_genre()

    # 3️⃣ set_book_genre — установка корректного жанра книге
    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.books_genre['Матрица'] = ''
        collector.set_book_genre('Матрица', 'Фантастика')

        assert collector.books_genre['Матрица'] == 'Фантастика'

    # 4️⃣ set_book_genre — жанр не устанавливается, если жанра нет в списке genre
    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.books_genre['Книга'] = ''
        collector.set_book_genre('Книга', 'Драма')

        assert collector.books_genre['Книга'] == ''

    # 5️⃣ get_book_genre — возвращает правильный жанр
    def test_get_book_genre_returns_correct_value(self):
        collector = BooksCollector()
        collector.books_genre['Матрица'] = 'Фантастика'

        assert collector.get_book_genre('Матрица') == 'Фантастика'

    # 6️⃣ get_books_with_specific_genre — возвращает только книги нужного жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Книга 1': 'Комедии', 'Книга 2': 'Ужасы'}

        result = collector.get_books_with_specific_genre('Комедии')

        assert result == ['Книга 1']

    # 7️⃣ get_books_genre — возвращает весь словарь книг и жанров
    def test_get_books_genre_returns_correct_dict(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Матрица': 'Фантастика',
            'Оно': 'Ужасы'
        }

        result = collector.get_books_genre()

        assert result == {'Матрица': 'Фантастика', 'Оно': 'Ужасы'}

    # 8️⃣ get_books_for_children — возвращает только книги без возрастного рейтинга
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Смешарики': 'Мультфильмы',
            'Оно': 'Ужасы',
            'Матрица': 'Фантастика'
        }

        result = collector.get_books_for_children()

        assert 'Смешарики' in result
        assert 'Матрица' in result
        assert 'Оно' not in result

    # 9️⃣ add_book_in_favorites — добавление книги в избранное
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()
        collector.books_genre['Гарри Поттер'] = 'Фантастика'
        collector.add_book_in_favorites('Гарри Поттер')

        assert 'Гарри Поттер' in collector.favorites

    # 🔟 delete_book_from_favorites — удаление книги из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.favorites = ['Том и Джерри']
        collector.delete_book_from_favorites('Том и Джерри')

        assert 'Том и Джерри' not in collector.favorites

    # 1️⃣1️⃣ get_list_of_favorites_books — возвращает корректный список избранного
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.favorites = ['Шрек', 'Матрица']

        result = collector.get_list_of_favorites_books()

        assert result == ['Шрек', 'Матрица']