from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'


@app.route('/')
def table():
    db_s = db_session.create_session()
    data = []
    for i in db_s.query(Jobs):
        data.append(
            {
                'id': i.id,
                'name': i.job,
                'team_leader': i.team_leader,
                'duration': f'{i.work_size} hours',
                'collaborators': i.collaborators,
                'is_finished': 'yes' if i.is_finished else 'no'
            }
        )
    return render_template('table.html', data=data)


if __name__ == '__main__':
    db_session.global_init('db/init.db')
    job = Jobs()
    job.job = 'бот для шадрина'
    job.collaborators = 'Андрей'
    job.work_size = '15'
    job.is_finished = False
    job.team_leader = 'Женя'
    sess = db_session.create_session()
    sess.add(job)
    sess.commit()
    sess.close()
    app.run(port=80)
