from flask import Flask, render_template
import ipretriever

app = Flask(__name__)

@app.route('/')
def index():
    ip = ipretriever.getIp()
    return render_template('index.html', ip=ip)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')