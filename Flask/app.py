import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
def test():
    return {"result":"Hello world!"*10000}

@app.route('/healtcheck')
def healtcheck():
    return 'OK', 200

if __name__ =='__main__':
    app.run(host = '0.0.0.0', port=5000)