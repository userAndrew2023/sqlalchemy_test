import flask
from flask import jsonify, request

from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)


@blueprint.route('/jobs')
def get_jobs():
    sess = db_session.create_session()
    jobs = sess.query(Jobs).all()
    return jsonify(
        {
            'data': [i.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished')) for i in jobs]
        }
    )


@blueprint.route('/jobs/<id>')
def get_job(id: int):
    try:
        id = int(id)
    except ValueError:
        return jsonify({
            'msg': 'wrong data, integer required'
        }), 400
    sess = db_session.create_session()
    job = sess.query(Jobs).get(id)
    if not job:
        return jsonify({
            'msg': 'not found'
        }), 404

    return jsonify(
        {
            'data': job.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'is_finished'))
        }
    ), 200


@blueprint.route('/jobs', methods=['POST'])
def add_job():
    sess = db_session.create_session()
    data = request.json
    try:
        job = Jobs(**data)
        sess.add(job)
        sess.commit()
    except Exception as e:
        print(e)

    return jsonify({
        'msg': 'ok'
    }), 200
