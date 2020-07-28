from config.db import Db

class ControllerUser(object):
        
    def setNome(self, nome):
        self.nome = nome
    def setEmail(self, email):
        self.email = email
    def setCidade(self,cidade):
        self.cidade = cidade
    def setUf(self, uf):
        self.uf = uf
    def AddUser(self):
        database  = Db()        
        db = database.getDb()
        MAIN_DB = db.cursor()
        MAIN_DB.execute("""INSERT INTO account.users(nome, email, cidade, uf) values (%s, %s, %s, %s)""",(self.nome,self.email,self.cidade, self.uf))
        db.commit()                 
    def GetIdByEmail(self):
        database  = Db()        
        db = database.getDb()
        MAIN_DB = db.cursor()
        MAIN_DB.execute("select id from account.users where email="+str(self.email))
        data = MAIN_DB.fetchone()
        return data         
    def GetUserById(self,id):
        db = self.database.getDb()
        MAIN_DB = db.cursor()
        MAIN_DB.execute("select nome from account.users where id="+ str(id))
        data = MAIN_DB.fetchone()
        return data                
    def DeleteUser(self, id):
        db = self.database.getDb()
        MAIN_DB = db.cursor()
        MAIN_DB.execute("delete from account.users where id="+ str(id))
        db.commit()