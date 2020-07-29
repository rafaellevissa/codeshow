import mysql.connector

class Db(object):
    host = "database-1.czlhpvhotuj3.us-east-2.rds.amazonaws.com"
    user = "campus"
    password = "Ardu1nohub"
    def __init__(self):
        try:
            self.db = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        except:
            print("Erro ao conectar ao banco")
    def getDb(self):
        return self.db