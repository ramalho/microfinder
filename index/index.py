
import sys, unicodedata
from quart import Quart, jsonify, abort


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
app = Quart(__name__)


@app.route("/")
async def root():
    return "This is the microfinder index API server"


@app.route("/<query>")
async def query(query):
    try:
        res = word_index[query.upper()]
    except KeyError:
        abort(404)
    else:
        return jsonify(res)


if __name__ == "__main__":
    app.run()
