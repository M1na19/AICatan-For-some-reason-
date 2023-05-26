import flask
from flask_cors import CORS
import backend.gameplay as gp
app=flask.Flask(__name__)
CORS(app)

@app.route('/',methods=['POST'])
def post():
    startplayer=flask.request.json.get('params').get('startplayer')
    nrPlayers=flask.request.json.get('params').get('numberofplayers')
    if(startplayer!=None and nrPlayers!=None):
        response=flask.jsonify(gp.start(startplayer,nrPlayers))
        return response
    return flask.jsonify("Wrong input")


@app.route('/', methods=['PUT'])
def put():
    act=flask.request.json.get('params').get('action')
    player=flask.request.json.get('params').get('player')
    info=flask.request.json.get('params').get('info')
    gp.resolve_put(act,player,info)
    return "succes"


@app.route('/',methods=['GET'])
def get():
    act=flask.request.args.get('action')
    player=flask.request.args.get('player')
    info=flask.request.args.getlist('info[]')
    player=int(player)
    if(act!=None and player!=None and info==[]):
        response=gp.resolve_get(act,player)
        response=flask.jsonify(response)
        return response
    elif(info!=[]):
        response=gp.resolve_getInfo(act,player,info)
        response=flask.jsonify(response)
        return response
    return flask.jsonify("wrong input")




if __name__ == '__main__':
    app.run(port=8080)