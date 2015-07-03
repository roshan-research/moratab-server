
import pdfkit
from flask import Flask
app = Flask(__name__)


@app.route('/')
def main(url=None):
	pdfkit.from_url('http://google.com', 'out.pdf')
	return 'Moratab Server!'


if __name__ == '__main__':
	app.run(debug=True)
