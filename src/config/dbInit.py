from config.db import Db

class DbInit(object):
    database  = Db() 
    def iniciar(self):
        db = self.database.getDb()
        print(db)
        MAIN_DB = db.cursor()                         
        try:           
            MAIN_DB.execute("drop database if exists account")
            MAIN_DB.execute("create database account")
            MAIN_DB.execute("use account")
            MAIN_DB.execute('CREATE TABLE `users`(`id` int AUTO_INCREMENT PRIMARY KEY, `nome` varchar(20), `email` varchar(250), `cidade` varchar(100),`uf` varchar(3))')            
            db.commit()
            return "[{ \"message\":\"Database create new account table done\"}]"
        except:
            return "[{ \"message\":\"Erro ao iniciar o banco\"}]"    

        
