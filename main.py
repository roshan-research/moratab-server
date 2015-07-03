
import pdfkit
from flask import Flask, make_response
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/')
def main(url=None):
	pdfkit.from_url('http://google.com', '~/static/out.pdf')
	response = make_response(open('~/static/out.pdf').read())
	response.content_type = 'application/pdf'
	return response


if __name__ == '__main__':
	app.run(debug=True)
