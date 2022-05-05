from flask import Flask, request
from flask_cors import CORS
import functions.criador as cri
import functions.log_reader as log_reader
import json

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/criar')
def criar():
    ret = cri.criacao(print)
    return str(ret)

@app.route('/logs')
def logs():
    lastLogNumber = 0
    # query parameter last log number
    try:
        lastLogNumber = int(request.args.get('last_log_number'))
    except:
        pass
    # get logs
    logs = log_reader.reader(lastLogNumber)
    # return logs
    return json.dumps({
        'logs': logs,
        'last_log_number': 1
    })


@app.route('/limparlogs')
def limparlogs():
    ret = cri.criacao(print)
    return str(ret)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5250)
