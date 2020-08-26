from flask import Flask, render_template, request, jsonify
from result import get_results
import network

app = Flask(__name__)


@app.route('/')
def index():
    networkIp = network.get_ip()
    requestIp = request.remote_addr
    return render_template('home.html', networkIp=networkIp, requestIp=requestIp)


@app.route('/api/result')
def result():
    results = get_results(test=True)
    return jsonify(results)


@app.route('/api/speedtest')
def run_speedtest():
    '''Run a speedtest and output the result. For testing purposes'''
    return jsonify(network.run_speedtest().__dict__)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')