drop table author;
create table author (
ID Integer PRIMARY KEY,
Name Text NOT NULL
);
drop table book;
create table book (
ID Integer PRIMARY KEY,
Title Text NOT NULL
);
drop table book_author;
create table book_author (
bookID Integer NOT NULL REFERENCES book(ID),
authorID Integer NOT NULL REFERENCES author(ID)
);