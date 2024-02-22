import datetime

from flask import Flask

from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'


@app.route('/')
def index():
    return 'Доступ закрыт', 403


if __name__ == '__main__':
    db_session.global_init("./db/init.db")
    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    job.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    app.run(port=80)
