import flask
import backend.gameplay as gp
app=flask.Flask(__name__)

@app.route('/',methods=['POST'])
def start():
    rq=flask.request.get_json()
    return flask.jsonify(gp.start(rq.get('startplayer'),rq.get('numberofplayers')))
@app.route('/', methods=['PUT'])
def put():
    rq=flask.request.args.get('toput')
    gp.resolve_put(rq)
    return flask.jsonify(True)
@app.route('/',methods=['GET'])
def get():
    rq=flask.request.args.get('action')
    return flask.jsonify(gp.resolve_get(rq))
if __name__ == '__main__':
    app.run()