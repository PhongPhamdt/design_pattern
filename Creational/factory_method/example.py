# ---------------------------------------------------------------------------------------------------
# Gang of Four definition
# ---------------------------------------------------------------------------------------------------
# Define an interface for creating an object, but let subclasses decide which class to instantiate. 
# The Factory method lets a class defer instantiation it uses to subclasses.
# 
# In example, client code is deciding about object instantiation.
# ---------------------------------------------------------------------------------------------------


class Database(object):
    def connection(self):
        pass


class SqlServer(Database):
    def connection(self):
        return 'Sql database connection'


class Oracle(Database):
    def connection(self):
        return 'Oracle database connection.'


class DbFactory:
    @staticmethod
    def create_connection(database):
        if database == "SqlServer":
            return SqlServer().connection()
        elif database == "Oracle":
            return Oracle().connection()
        else:
            return "WRONG PARAMS"


#  Client Code
# -----------------------------
factory = DbFactory()
first_db = "SqlServer"
second_db = "Oracle"
print(factory.create_connection(first_db))
print(factory.create_connection(second_db))
