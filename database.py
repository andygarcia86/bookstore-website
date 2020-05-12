import sqlalchemy as db

class BaseDao:
    def __init__(self):
        pass

class BookDao(BaseDao):

    def save_in_db(self, title, description, language):
        # TODO: Move this to BaseDao class and use config file, using the .env file
        user = "root"
        password = "root"
        host = "localhost"
        port = 33060
        database = "bookstore"

        uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
            user=user, password=password, host=host, port=port, database=database
        )

        engine = db.create_engine(uri)
        connection = engine.connect()
        metadata = db.MetaData()
        books_table = db.Table("books", metadata, autoload=True, autoload_with=engine)

        query = books_table.insert().values(title=title, description=description, language=language)

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
