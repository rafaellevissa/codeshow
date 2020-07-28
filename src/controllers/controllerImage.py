from config.db import Db

class ControllerImage(object):

    def setTitulo(self,titulo):
        self.titulo = titulo
    def setDescricao(self,descricao):
        self.descricao = descricao
    def setImage(self, image):
        self.image = image
    def AddImage():
        print("adicionando imagem")