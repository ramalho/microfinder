
import unicodedata
from quart import Quart, jsonify, abort


app = Quart(__name__)


@app.route("/")
async def root():
    return "This is the microfinder names API server"


@app.route("/<character>")
async def name(character):
    try:
        res = unicodedata.name(character)
    except ValueError:
        abort(404)
    else:
        return jsonify(res)


if __name__ == "__main__":
    app.run()
