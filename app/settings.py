import os

REDIS_URL = os.environ.get('REDIS_URL',
                           default='redis://redis')

QUEUES = ['default']
TASK_TIMEOUT = os.environ.get('TASK_TIMEOUT', default=600)

# job result lifetime
RESULT_TTL = os.environ.get('RESULT_TTL', default=500)
