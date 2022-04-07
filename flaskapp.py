from flask import Flask
from celery import Celery
import time

app = Flask(__name__)

celery = Celery(app.name)
celery.config_from_object('celeryconfig')

@app.route('/')
def index():
    task1 = my_background_task.apply_async(args=[10, 20], countdown=1)
    task2 = my_background_task.apply_async(args=[20, 20], countdown=5)
    task3 = my_background_task.apply_async(args=[30, 20], countdown=10)
    return f'ello mate'

@celery.task(bind=True)
def my_background_task(self, arg1, arg2):
    self.update_state(state="PROGRESS")
    result = arg1+arg2
    time.sleep(20)
    return result

@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
