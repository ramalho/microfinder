
import sys, unicodedata
import quart

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
app = quart.Quart(__name__)


@app.route("/")
async def root():
    return "This is the microfinder index API server"


@app.route("/<query_str>")
async def query(query_str):
    try:
        res = word_index[query_str.upper()]
    except KeyError:
        quart.abort(404)
    else:
        return quart.jsonify(res)


if __name__ == "__main__":
    app.run()
