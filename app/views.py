import redis
from flask import Blueprint, request, jsonify, current_app, g, url_for
from rq import push_connection, pop_connection, Queue
from . import tasks
from .utils import get_redis_connection, create_task

bp = Blueprint('main', __name__)

@bp.before_request
def push_rq_connection(*args, **kwargs):
    push_connection(get_redis_connection())

@bp.teardown_request
def push_rq_connection(*args, **kwargs):
    pop_connection()

@bp.route('/scrape', methods=['POST'], )
def run_scrape_task():
    data = request.json
    scraping_url = data.get('url')
    job_id = create_task(tasks.scrape, scraping_url)

    return jsonify({'job_id': job_id}), 202,\
           {'Location': url_for('.status', job_id=job_id)}

@bp.route('/status/<job_id>')
def status(job_id):
    q = Queue()
    job = q.fetch_job(job_id)

    if job is None:
        response = {'status': 'unknown'}

    else:
        response = {
            'status': job.get_status(),
            'result': job.result,
        }
        if job.is_failed:
            response['message'] = job.exc_info.strip().split('\n')[-1]

    return jsonify(response)