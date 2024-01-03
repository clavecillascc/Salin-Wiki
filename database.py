from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://kryk46fj2ll8x8p7735z:pscale_pw_cLqurIOVHkaqbGI7NQ9z0moXyOC6ie8T0yRhAuil38n@aws.connect.psdb.cloud/salinwiki?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
    return jobs
