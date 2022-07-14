from . import exception

class Books:
	""" NOTE: this can be broken down into additional classes """
	def __init__(self, books_db_repo):
		self._books_db_repo = books_db_repo

	def _check_book_exists(self, book_id):
		pass

	def create_book_details(self):
		pass

	def get_book_availability(self, book_id):
		pass

	def get_book_details(self, book_id):
		pass

	def get_books_in_genre(self, genre, limit, token):
		pass

	def get_book_availabilty(self, book_id):
		pass

	def update_book_availbility(self, book_id, number_of_books: int):
		""" This can be updated by the store when they receive 
		more books or when a book or a few copies of books are sold"""
		self._check_book_exists(book_id)
		# TODO: acquire a lock on the book before this action
		if not number_of_books:
			# we can either raise an internal error here or return early since there is nothing to do.
			return 0

		current_avail = db_repo.book_availbility.get(book_id=book_id)
		
		if number_of_books > 0:
			no_of_books = number_of_books + current_avail
		else:
			if current_avail <= 0 or current_avail - number_of_books <=0:
				raise exception.NoMoreBooksToSell()
			no_of_books = current_avail + number_of_books

		db_repo.book_availability.update(book_id=book_id, available_copies=no_of_books)
		return no_of_books
		
	def calculate_price_after_discounts(self, book_id):
		# Get the book object
		# Get the discounts
		# Apply discounts and return value
		pass

	def get_all_books_for_author(self, author_id, limit, token):
		pass
