from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://ccfs3wxctgjs7lftkian:pscale_pw_bXvR0fDEVyYhT82aUVfcS9BpLJPAOXYLfIlqVloCKbp@aws.connect.psdb.cloud/salinwiki?charset=utf8mb4",
    connect_args={"ssl": {
        "ssl_cert": "/etc/ssl/cert.pem"
    }})

def load_words_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from words"))
    words = []
    for row in result.all():
      words.append(row._asdict())
    return words
