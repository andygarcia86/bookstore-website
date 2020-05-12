import sqlalchemy as db


def save_in_db():
    # TODO: Move this to config file
    user = "root"
    password = ""
    host = "localhost"
    port = 3306
    database = "calibre_books"

    uri = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
        user=user, password=password, host=host, port=port, database=database
    )

    engine = db.create_engine(uri)
    connection = engine.connect()
    metadata = db.MetaData()
    books_table = db.Table("books", metadata, autoload=True, autoload_with=engine)

    query = db.select([books_table])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    print(ResultSet)
