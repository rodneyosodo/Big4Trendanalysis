from flask import Flask, jsonify
from Scripts import Sentiment as s

api = Flask(__name__)


@api.route("/")
def index():
	return jsonify({
		"message": "Success"
		})

@api.route("/data/<message>", methods=["GET", "PUT"])
def data(message):
	a = s.sentiment(str(message))
	if a[0] == 1:
		return jsonify({
			"message" : message,
			"response": "The message is positive with a confidence of {}".format(a[1] * 100)
			})
	elif a[0] == 0:
		return jsonify({
			"message" : message,
			"response": "The message is negative with a confidence of {}".format(a[1] * 100)
			})


if __name__ == '__main__':
	api.run("0.0.0.0", port=80, debug=True)
