import os, random

from sqlalchemy import create_engine, text

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret,
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

def featured_word_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM words ORDER BY RAND() LIMIT 1"))
      fw = []
      for row in result.all():
        fw.append(row._asdict())
      return fw
