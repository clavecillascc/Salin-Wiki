from flask import Flask, render_template, redirect, url_for, request

from database import load_words_from_db

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def salinwiki_home():
  if request.method == "POST":
    searched_word = request.form["search"]
    return redirect(url_for("search",searched_word=searched_word))
  else:
    return render_template('0_home.html')

@app.route("/Search_<searched_word>", methods=["POST", "GET"])
def search(searched_word):
  words = load_words_from_db()
  if request.method == "POST":
    searched_word = request.form["search"]
  searched_word = searched_word
  return render_template('search.html', searched_word=searched_word, words=words)

@app.route("/Dictionary")
def salinwiki_dictionary():
  words = load_words_from_db()
  return render_template('1_dictionary.html', words=words)

@app.route("/FAQs")
def salinwiki_faqs():
  return render_template('2_faqs.html')

@app.route("/About")
def salinwiki_about():
  return render_template('3_about.html')

@app.route("/Bicolano")
def salinwiki_dictionary_bicolano():
  words = load_words_from_db()
  return render_template('1_dictionary_bicolano.html', words=words)

@app.route("/Cebuano")
def salinwiki_dictionary_cebuano():
  words = load_words_from_db()
  return render_template('1_dictionary_cebuano.html', words=words)

@app.route("/Ilocano")
def salinwiki_dictionary_ilocano():
  words = load_words_from_db()
  return render_template('1_dictionary_ilocano.html', words=words)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
