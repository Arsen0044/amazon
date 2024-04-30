from src.page_objects.filter_books_page import FilterBooksPage


class TestFilterBooks:
    books = FilterBooksPage()

    def test_filter_books(self):
        self.books.provide_full_flow()
