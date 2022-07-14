class BooksBaseTest:
    # common setup, fixtures, helpers

    def create_book(self):
        pass


class CreateBookTest(BooksBaseTest):
    def test_validates_inputs(self):
        pass

    def test_book_created_successfully(self):
        pass

    def test_raises_book_already_exists_error(self):
        pass

    def test_create_with_no_author_raises_error(self):
        pass

    def test_create_without_ratings_success(self):
        pass


class UpdateBookAvailabilityTest(BooksBaseTest):
    def test_invalid_book_id_raises_error(self):
        pass

    def test_increasing_book_availability(self):
        pass

    def test_decreasing_book_availabilty(self):
        pass

    def test_decreasing_book_availabilty_beyond_available_raises(self):
        pass


class CalculatePriceWithDiscount(BooksBaseTest):
    def test_cost_with_no_discount(self):
        pass

    def test_price_rounded_to_nearest_cent(self):
        pass


class GetAllBooksForAuthor(BooksBaseTest):
    def test_get_books_for_author_within_limit(self):
        pass

    def test_pagination_for_results_with_token(self):
        pass

    def test_author_with_no_books(self):
        pass
