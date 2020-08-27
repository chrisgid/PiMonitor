from flask import Flask, render_template, request, jsonify
from result import get_results
import network
import runner
import json

app = Flask(__name__)


@app.route('/')
def index():
    network_ip = network.get_ip()
    request_ip = request.remote_addr
    return render_template('home.html', network_ip=network_ip, request_ip=request_ip)


@app.route('/api/result')
def result():
    results = get_results(all_results=True)
    return jsonify(results)


@app.route('/api/speedtest')
def run_speedtest():
    """Run a speedtest and output the result. For testing purposes"""
    return jsonify(network.run_speedtest().__dict__)


@app.route('/api/speedtest/save')
def save_speedtest():
    """Run a speedtest and store it in the database. For testing purposes"""
    try:
        runner.run()
        return 'Done', 200
    except Exception as e:
        return e, 500


if __name__ == '__main__':
    with open('config.json') as json_config:
        data = json.load(json_config)
    
    debug = data.get('flask.debug').lower() == 'true'

    app.run(debug=debug, host='0.0.0.0')
