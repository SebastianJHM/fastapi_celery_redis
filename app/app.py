from fastapi import FastAPI
import uvicorn
from celery import Celery

app = FastAPI()
# simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
simple_app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')

@app.get('/')
def init():
    return {"mensaje": "que pasa"}

@app.get('/simple_start_task')
def call_method():
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
    return (
        {
            "id_task": r.id, 
            "status_task": f"http://localhost:8080/simple_task_status/{r.id}",
            "result_task": f"http://localhost:8080/simple_task_result/{r.id}"
        }
    )


@app.get('/simple_task_status/{task_id}')
def get_status(task_id: str):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    print("Invoking Method ")
    return {"Status of the Task": str(status.state)}


@app.get('/simple_task_result/{task_id}')
def task_result(task_id: str):
    result = simple_app.AsyncResult(task_id).result
    return {"Result of the Task": str(result)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)