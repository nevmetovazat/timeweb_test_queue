from flask import g, current_app
from rq import Queue
import redis

def get_redis_connection():
    redis_connection = getattr(g, '_redis_connection', None) # get conn from context
    if redis_connection is None:
        redis_url = current_app.config.get('REDIS_URL')
        redis_connection = g._redis_connection = redis.from_url(redis_url) # set conn to context

    return redis_connection

def create_task(task, *args, **kwargs):
    q = Queue()
    job = q.enqueue(task, args=args, kwargs=kwargs,
                    job_timeout=current_app.config.get("TASK_TIMEOUT"))

    return job.get_id()