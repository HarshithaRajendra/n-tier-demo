from ..books.books_business_logic_layer import Books
from . import rpc_coverters


class BooksRPC:
    def __init__(self, books_logic):
        self._books = Books(books_db_repo)

    def increase_book_availbility(self, request):
        # Maybe only some roles in the back office can do this.
        user_service.check_user_has_permissions_for_actions(requesting_user)
        try:
            new_number_of_books = self._books.update_book_availbility(
                book_id=request.book_id, number_of_books=request.number_of_books
            )
        except BookNotFound:
            log.error(
                "Trying to update availabilty for a book that is not in the system."
            )
            return Response(error_code=book_not_found)

        return Response(success=new_number_of_books)

    def decrease_book_availbility(self, request):
        """This can be called in two cases
        1. User buys one or more books so we want to update this in our system.
        2. Admin user want to correct mistakes.
        """
        # checks user is a account holder or an admin
        check_valid_user_in_our_system(requesting_user)
        try:
            new_number_of_books = self._books.update_book_availbility(
                book_id=request.book_id, number_of_books=request.number_of_books
            )
        except BookNotFound:
            log.error(
                "Trying to update availabilty for a book that is not in the system."
            )
            return Response(error_code=book_not_found)

        return Response(success=new_number_of_books)

    def get_book_details_for_user(self):
        book_details = self._books.get_book_details(request.book_id)
        rpc_book_details = (
            rpc_coverters.convert_internal_book_details_to_customer_book_details_rpc(
                book_details
            )
        )

        return Response(success=rpc_book_details)

    def get_book_details_for_admin(self):
        book_details = self._books.get_book_details(request.book_id)
        rpc_book_details = (
            rpc_coverters.convert_internal_book_details_to_admin_book_details_rpc(
                book_details
            )
        )

        return Response(success=rpc_book_details)
