from flask import Flask, render_template, request
import ipretriever

app = Flask(__name__)

@app.route('/')
def index():
    networkIp = ipretriever.getIp()
    requestIp = request.remote_addr
    return render_template('home.html', networkIp=networkIp, requestIp=requestIp)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')