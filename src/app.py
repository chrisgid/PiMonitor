from flask import Flask, render_template, request, jsonify
from result import get_results
import speedtest
import ipretriever

app = Flask(__name__)


@app.route('/')
def index():
    networkIp = ipretriever.get_ip()
    requestIp = request.remote_addr
    return render_template('home.html', networkIp=networkIp, requestIp=requestIp)


@app.route('/api/result')
def result():
    results = get_results(test=True)
    return jsonify(results)


@app.route('/api/speedtest')
def run_speedtest():
    '''Run a speedtest and output the result. For testing purposes'''
    return jsonify(speedtest.run_speedtest().speed_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')