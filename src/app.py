from flask import Flask, request, Response
import time 
import json

from config.db import Db
from config.dbInit import DbInit
from controllers.controllerUser import ControllerUser
from controllers.controllerImage import ControllerImage

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    #curl -i http://$Server_IP:$Server_Port/
    resposta="[{\"message\":\"API Rest - Galeria de fotos - Checkpoint Date/Time"+time.strftime("%c")+"\"}]"
    return Response(resposta, status=200, mimetype='application/json')

@app.route("/init")
def init():
    #curl -i http://$Server_IP:$Server_Port/init            
    dbinit = DbInit()
    return dbinit.iniciar()

@app.route("/users", methods=['POST'])
def insertuser():
    #curl -i -H "Content-Type: application/json" -X POST -d '{"uid": "3", "user": "jimmy", "description": "security"}' $Server_IP:$Server_Port/users/insertuser
    req_json = request.get_json()
    controllerUser = ControllerUser()
    controllerUser.setNome(req_json["name"])    
    controllerUser.setEmail(req_json["email"])
    controllerUser.setCidade(req_json["city"])
    controllerUser.setUf(req_json["uf"])    
    try:
        controllerUser.AddUser()
        return Response("[{ \"message\":\"user added, \"id\": \"0\"", status=200, mimetype='application/json')
    except:
        return Response("[{ \"message\":\"user wasn't added\"}]", status=400, mimetype='application/json')    
    
@app.route("/users/<id>", methods=['GET'])
def getuser(id):
    #curl -i http://$Server_IP:$Server_Port/users/2
    controllerUser = ControllerUser()
    data = controllerUser.GetUserById(id)
    if data:
        return Response("[{ \"usuario: \""+str(data[0])+"\"", status=200, mimetype='application/json')
    else:
        return Response("[{ \"message\":\"User not found\"}]", status=400, mimetype='application/json') 

@app.route("/users/removeuser/<id>")
def deluser(id):
    #curl -i http://$Server_IP:$Server_Port/users/removeuser/4
    controllerUser = ControllerUser()
    try:
        controllerUser.DeleteUser(id)
        return Response("[{ \"message\":\"User was deleted\"}]", status=200, mimetype="application/json")
    except:
        return Response("[{ \"message\":\"User wasn't deleted\"}]", status=400, mimetype="application/json")

@app.route("/image", methods=['POST'])
def insertImage():
    req_json = request.get_json()
    controllerImage = ControllerImage()
    controllerImage.setTitulo(req_json["titulo"])    
    controllerImage.setDescricao(req_json["descricap"])
    controllerImage.setImagem(req_json["imagem"])
       
    try:
        controllerImage.AddImage()
        return Response("[{ \"message\":\"Image was added\"}]", status=200, mimetype='application/json')        
    except:
        return Response("[{ \"message\":\"Image wasn't added\"}]", status=400, mimetype='application/json')    


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)