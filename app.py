from flask import Flask, jsonify, render_template

from database import load_jobs_from_db

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Job 1',
    'description': 'Job 1 description',
    'company': 'Company 1',
    'location': 'Location 1',
    'salary': 'Salary 1'
}, {
    'id': 2,
    'title': 'Job 2',
    'description': 'Job 2 description',
    'company': 'Company 2',
    'location': 'Location 2',
    'salary': 'Salary 2'
}, {
    'id': 3,
    'title': 'Job 3',
    'description': 'Job 3 description',
    'company': 'Company 3',
    'location': 'Location 3',
    'salary': 'Salary 3'
}]


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
