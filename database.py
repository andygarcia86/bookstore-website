import sqlalchemy as db
import os


class BaseDao:
    def __init__(self):
        self.uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
            user=os.getenv("DATABASE_USER", "root"),
            password=os.getenv("DATABASE_PASSWORD", "root"),
            host=os.getenv("DATABASE_HOST", "localhost"),
            port=os.getenv("DATABASE_PORT", 33060),
            database=os.getenv("DATABASE_NAME", "bookstore"),
        )


class BookDao(BaseDao):
    __table_name = "books"

    def get(self, title):
        """ This function return a book searched by the title

        Args:
            title (str): Title of the book.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = db.select([table]).where(table.c.title == title)
        ResultProxy = connection.execute(query)
        return ResultProxy.fetchone()

    def put(self, author_id, title, description, language):
        """ This function save a new book record in the database

        Args:
            title (str): Title of the book.
            description (str): Small description of the book.
            language (str): Language is written the book.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = table.insert().values(
            author_id=author_id, title=title, description=description, language=language
        )
        connection.execute(query)


class AuthorDao(BaseDao):
    __table_name = "authors"

    def get(self, name):
        """ This function search for a Author by a given name

        Args:
            name (str): Name of the author.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = db.select([table]).where(table.c.name == name)
        ResultProxy = connection.execute(query)
        return ResultProxy.fetchone()

    def put(self, name):
        """ This function save a new author record in the database

        Args:
            name (str): Name of the author.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = table.insert().values(name=name)
        result = connection.execute(query)
        return result.lastrowid


class SubjectDao(BaseDao):
    __table_name = "subjects"

    def get(self, name):
        """ This function search for a Subject by a given name

        Args:
            name (str): Name of the subject.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = db.select([table]).where(table.c.name == name)
        ResultProxy = connection.execute(query)
        return ResultProxy.fetchone()

    def put(self, name):
        """ This function save a new subject record in the database

        Args:
            name (str): Name of the subject.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = table.insert().values(name=name)
        connection.execute(query)


class BooksSubjectDao(BaseDao):
    __table_name = "books_subjects"

    def get(self, book_id, subject_id):
        """ This function search for a Book Subject relationship by the two keys

        Args:
            book_id (int): Book id.
            subject_id (int): Subject id.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = db.select([table]).where(table.c.book_id == book_id and table.c.subject_id == subject_id)
        ResultProxy = connection.execute(query)
        return ResultProxy.fetchone()

    def put(self, book_id, subject_id):
        """ This function saves a new book subject record in the database, making a relationship between a book and a subject

        Args:
            book_id (int): Book id.
            subject_id (int): Subject id.
        """

        # TODO: Use a session with Singleton instead of
        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = table.insert().values(book_id=book_id, subject_id=subject_id)
        connection.execute(query)
