class BooksBaseTest:
    # Some helper method
    # Some base level fixtures setup
    pass


class BooksTest(BooksBaseTest):
    """Tests for CRUD for books table"""

    def test_create_invalid():
        pass

    def test_create_success():
        pass

    def test_get_no_present():
        pass

    def test_get_success():
        pass

    def test_get_with_filters():
        pass

    def test_update_field_1():
        pass

    def test_update_field_2():
        pass

    def test_update_multiple_fields():
        pass

    def test_delete():
        pass


class BookAuthorsTest(BooksBaseTest):
    """Tests for CRUD for books authors table"""

    def test_create_invalid():
        pass

    def test_create_success_one_author():
        pass

    def test_create_success_multiple_authors():
        pass

    def test_get_no_present():
        pass

    def test_get_success():
        pass

    def test_get_with_filters():
        pass

    def test_update_field_1():
        pass

    def test_update_field_2():
        pass

    def test_update_multiple_fields():
        pass

    def test_delete():
        pass


class BookRatingsTest(BooksBaseTest):
    """Tests for CRUD for books ratings table"""

    ...
    pass
