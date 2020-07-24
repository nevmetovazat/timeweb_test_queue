import os

REDIS_URL = os.environ.get('REDIS_URL',
                           default='redis://:JWt6p0rBDOV31cl5bdwokEZNq1XCuHVB@redis-19207.c135.eu-central-1-1.ec2.cloud.redislabs.com:19207')

QUEUES = ['default']
TASK_TIMEOUT = os.environ.get('TASK_TIMEOUT', default=600)

# job result lifetime
RESULT_TTL = os.environ.get('RESULT_TTL', default=500)
