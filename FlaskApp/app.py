from flask import Flask, render_template, request, json, jsonify
from fortnite_api import Fortnite, InvalidUsage
import yaml

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/_stats")
def stats():
    print("gametag: " + request.args.get('username'))
    print("platform: " + request.args.get('platform'))

    fortnite = Fortnite(request.args.get('username'), request.args.get('platform'))
    stats = fortnite.get_stats()

    return json.dumps(stats)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    with open("conf/server_conf.yaml", 'r') as stream:
        try:
            conf = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    app.run(host=conf["host"], port=conf["port"], debug=conf["debug"])