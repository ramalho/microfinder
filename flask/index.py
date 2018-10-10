
import sys, unicodedata
import flask

def add_entry(index, char, name):
    for word in name.split():
        index.setdefault(word, []).append(char)


def index():
    entries = {}
    for code in range(sys.maxunicode):
        char = chr(code)
        try:
            name = unicodedata.name(char)
        except ValueError:
            continue
        add_entry(entries, char, name)

    return entries


word_index = index()
app = flask.Flask(__name__)


@app.route("/")
def root():
    return "This is the microfinder index API server"


@app.route("/<query_str>")
def query(query_str):
    try:
        res = word_index[query_str.upper()]
    except KeyError:
        flask.abort(404)
    else:
        return flask.jsonify(res)


if __name__ == "__main__":
    app.run()
