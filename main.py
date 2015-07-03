
import pdfkit
from flask import Flask, make_response
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.route('/')
def main(url=None):
	pdf_file = 'static/document.pdf'
	pdfkit.from_url('http://google.com', pdf_file)
	response = make_response(open(pdf_file).read())
	response.content_type = 'application/pdf'
	return response


if __name__ == '__main__':
	app.run(debug=True)
