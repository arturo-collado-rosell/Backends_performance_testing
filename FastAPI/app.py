from fastapi import FastAPI
import uvicorn
#import multiprocessing

app = FastAPI()

@app.get("/")
def test():
    return {"result":"Hello world!"*10000}

@app.get("/healthcheck")
def healthcheck():
    return 'OK'

if __name__ == "__main__":
    #num_cores = multiprocessing.cpu_count()
    uvicorn.run("app:app", host="0.0.0.0", port=5002, workers = 4)