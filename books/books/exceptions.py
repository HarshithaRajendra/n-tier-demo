# File for internal exceptions


class BookNotFound(Exception):
    pass


class BookAlreadyExists(Exception):
    pass


class NoMoreBooksToSell(Exception):
    # TODO add additional info like book id and currently available books number
    pass
