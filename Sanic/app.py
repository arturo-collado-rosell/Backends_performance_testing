import sanic
import multiprocessing

app = sanic.Sanic(__name__)


@app.route('/', methods = ['GET'])
async def test(request):
    return sanic.response.json({"result":"Hello world!"*10000})

@app.route('/healtcheck')
async def healtcheck(request):
    return sanic.response.json({"status": "ok"})

if __name__ =='__main__':
    num_cores = multiprocessing.cpu_count()
    app.run(host = '0.0.0.0', port=5001, debug = True, workers= num_cores)