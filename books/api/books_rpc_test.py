from ..books.books_business_logic_test import BooksBaseTest


class BooksRPCBaseTest(BooksBaseTest):
    # add some RPC helpers
    # mock other services.
    pass


class IncreaseBookAvailabilityTest(BooksRPCBaseTest):
    def test_successful_response(self):
        pass

    def test_error_response(self):
        pass


class DecreaseBookAvailabilityTest(BooksRPCBaseTest):
    def test_successful_response(self):
        pass

    def test_error_response(self):
        pass
