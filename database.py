import sqlalchemy as db


class BaseDao:
    # TODO: Move this to BaseDao class and use config file, using the .env file
    __user = "root"
    __password = "root"
    __host = "localhost"
    __port = 33060
    __database = "bookstore"

    def __init__(self):
        self.uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
            user=self.__user,
            password=self.__password,
            host=self.__host,
            port=self.__port,
            database=self.__database,
        )


class BookDao(BaseDao):
    __table_name = "books"

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
