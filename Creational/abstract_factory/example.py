# -----------------------------------------------------------------------------------------------------------------
# Abstract Factory example:  Web and App are two different applications. Both use Sql And No SQL databases,
# Web uses mongodb and SQL but App uses Oracle and OrientDB. Both have different implementations.
# -----------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class db_factory(ABC):
    @abstractmethod
    def create_no_sql_db(self):
        pass

    @abstractmethod
    def create_sql_db(self):
        pass


class web_factory(db_factory):
    def create_no_sql_db(self):
        return mongodb()

    def create_sql_db(self):
        return SQL()    


class app_factory(db_factory):
    def create_no_sql_db(self):
        return orientDb()

    def create_sql_db(self):
        return Oracle()


class sql_database(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def select(self):
        pass


class SQL(sql_database):
    def save(self):
        print("SQL save called.")

    def select(self):
        print("SQL select called.")


class Oracle(sql_database):
    def save(self):
        print("Oracle save called.")

    def select(self):
        print("Oracle select called")


class no_sql_database(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def get_object(self):
        pass


class mongodb(no_sql_database):
    def insert(self):
        print("mongodb insert called.")

    def get_object(self):
        print("mongodb get_object called.")


class orientDb(no_sql_database):
    def insert(self):
        print("orientdb insert called.")

    def get_object(self):
        print("orientdb get_object called.")


class client:
    @staticmethod
    def get_database():
        web_sql_factory = web_factory().create_sql_db()
        web_sql_factory.save()
        web_sql_factory.select()

        # -------------------------------------------
        web_nos_factory = web_factory().create_no_sql_db()
        web_nos_factory.insert()
        web_nos_factory.get_object()

        # -------------------------------------------
        app_sql_factory = app_factory().create_sql_db()
        app_sql_factory.save()
        app_sql_factory.select()

        # -------------------------------------------
        app_nos_factory = app_factory().create_no_sql_db()
        app_nos_factory.insert()
        app_nos_factory.get_object()


client = client()
client.get_database()
