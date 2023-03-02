import time
import random

from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)


endpoints = ('books', 'authors', 'admin',)


@app.route('/books')
def first_route():
    time.sleep(random.random())
    return jsonify([
        'Приключения Гекльберри Финна',
        'Приключения Тома Сойера',
        'Принц и нищий',
        ])


@app.route("/authors")
def the_second():
    time.sleep(random.random())
    return jsonify(name='Марк Твен')


@app.route("/admin")
def oops():
    return ":(", 500


if __name__ == "__main__":
    app.run("0.0.0.0", 8080, threaded=True)
