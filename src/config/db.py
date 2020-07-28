import MySQLdb

class Db(object):
    host = "localhost"
    user = "levi"
    password = "123"
    def __init__(self):
        try:
            self.db = MySQLdb.connect(self.host, self.user, self.password)
        except:
            print("Erro ao conectar ao banco")
    def getDb(self):
        return self.db