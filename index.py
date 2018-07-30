
import sys, unicodedata
from quart import Quart


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


app = Quart(__name__)


@app.route("/")
async def hello():
    return "This is the microfinder index API server"


if __name__ == "__main__":
    app.run()
