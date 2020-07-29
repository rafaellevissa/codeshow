import MySQLdb

class Db(object):
    host = "database-1.czlhpvhotuj3.us-east-2.rds.amazonaws.com"
    user = "campus"
    password = "Ardu1nohub"
    def __init__(self):
        try:
            self.db = MySQLdb.connect(self.host, self.user, self.password)
        except:
            print("Erro ao conectar ao banco")
    def getDb(self):
        return self.db