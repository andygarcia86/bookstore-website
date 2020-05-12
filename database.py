import sqlalchemy as db

# TODO: Create class book dao, author dao
# class book dao
# class author dao
# class subjects dao


def save_in_db(title, description, language):
    # TODO: Move this to config file, using the .env file
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

    query = books_table.insert().values(title=title, description=description)

    connection.execute(query)

    """
    query = db.select([books_table])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    print(ResultSet)
    """
