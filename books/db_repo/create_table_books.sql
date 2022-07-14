CREATE TABLE books (
   id BINARY(16),
   title VARCHAR2(50) NOT NULL,
   published_date Date,
   genre str, 
   isbn VARCHAR2(20)
)
   

CREATE TABLE book_authors (
   id BINARY(16),
   book_id BINARY(16),
   author_id BINARY(16),
   CONSTRAINT book_id_fk FOREIGN KEY books_id REFERENCES books(id)
)

CREATE TABLE book_ratings (
   id BINARY(16),
   book_id BINARY(16),
   user_id BINARY(16),
   rating smallint,
   rating_last_updated_date date,
   is_deleted boolean,
)

CREATE TABLE book_availability (
   id BINARY(16),
   book_id BINARY(16),
   available_copies int,
   last_updated_by BINARY(16),
   last_updated_ts timestamp,
)

CREATE TABLE book_price (
   id BINARY(16),
   book_id BINARY(16),
   cost_in_cents int,
   last_updated_by BINARY(16),
   last_updated_ts timestamp,
)

CREATE TABLE book_discounts (
   ...
)