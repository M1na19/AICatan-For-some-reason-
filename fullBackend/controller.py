import flask
import backend.gameplay as gp
app=flask.Flask(__name__)


@app.route('/',methods=['POST'])
def post():
    startplayer=flask.request.json.get('params').get('startplayer')
    nrPlayers=flask.request.json.get('params').get('numberofplayers')
    if(startplayer!=None and nrPlayers!=None):
        return flask.jsonify(gp.start(startplayer,nrPlayers))
    return flask.jsonify("Wrong input")


@app.route('/', methods=['PUT'])
def put():
    act=flask.request.json.get('params').get('action')
    player=flask.request.json.get('params').get('player')
    info=flask.request.json.get('params').get('info')
    gp.resolve_put(act,player,info)
    return "yey"


@app.route('/',methods=['GET'])
def get():
    act=flask.request.args.get('action')
    player=flask.request.args.get('player')
    player=int(player)
    if(act!=None and player!=None):
        response=gp.resolve_get(act,player)
        return flask.jsonify(response)
    return flask.jsonify("wrong input")




if __name__ == '__main__':
    app.run(port=8080)