import flask
import backend.gameplay as gp
app=flask.Flask(__name__)


@app.route('/',methods=['POST'])
def start():
    rq=flask.request.get_json()
    return flask.jsonify(gp.start(rq.get('startplayer'),rq.get('numberofplayers')))


@app.route('/', methods=['PUT'])
def put():
    act=flask.request.args.get('action')
    player=flask.request.args.get('player')
    info=flask.request.args.get('info')
    gp.resolve_put(act,player,info)


@app.route('/',methods=['GET'])
def get():
    act=flask.request.args.get('action')
    player=flask.request.args.get('player')
    info=flask.request.args.get('info')
    return flask.jsonify(gp.resolve_get(act,player,info))




if __name__ == '__main__':
    app.run()