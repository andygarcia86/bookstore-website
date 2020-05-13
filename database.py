import sqlalchemy as db


class BaseDao:
    # TODO: Move this to BaseDao class and use config file, using the .env file
    user = "root"
    password = "root"
    host = "localhost"
    port = 33060
    database = "bookstore"

    def __init__(self):
        self.uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )


class BookDao(BaseDao):
    __table_name = "books"

    def put(self, title, description, language):
        """ This function save a new book record in the database

        Args:
            title (str): Title of the book.
            description (str): Small description of the book.
            language (str): Language is written the book.
        """

        engine = db.create_engine(self.uri)
        connection = engine.connect()
        metadata = db.MetaData()
        books_table = db.Table(
            self.__table_name, metadata, autoload=True, autoload_with=engine
        )
        query = books_table.insert().values(
            title=title, description=description, language=language
        )
        connection.execute(query)


class AuthorDao(BaseDao):
    pass


class SubjectDao(BaseDao):
    pass

    """
    query = db.select([books_table])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    print(ResultSet)
    """
