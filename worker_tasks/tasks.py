import time
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

# redis-server
# celery -A tasks worker --loglevel=INFO

# app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
# app.conf.broker_url = 'redis://redis:6379/0'

app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')
app.conf.broker_url = 'redis://localhost:6379/0'

@app.task()
def longtime_add(x, y):
    logger.info('Got Request - Starting work ')
    time.sleep(10)
    logger.info('Work Finished ')
    return x + y