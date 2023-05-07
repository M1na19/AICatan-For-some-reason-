import flask
import gameplay as gp
app=flask.Flask(__name__)
@app.route('/api/input')
def control():
    request=flask.request.get_json
    return gp.resolve_action(request.action,request.player)