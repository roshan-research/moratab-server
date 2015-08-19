
import time
import moratab
import pdfkit
from flask import Flask, request, render_template, make_response
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


new_pdf_filename = lambda: 'static/{}.pdf'.format(int(time.time()*100))

options = {
	'margin-top': '0.75in',
	'margin-right': '0.75in',
	'margin-left': '0.75in',
	'margin-bottom': '0.75in',
	'print-media-type': None,
	# 'user-style-sheet': 'static/main.css',
	'load-error-handling': 'ignore'
}


@app.route('/')
def main():
	return 'Moratab Server!'


@app.route('/html', methods=['POST'])
def html():
	content = moratab.render(request.form['moratab'])
	return render_template('main.html', content=content)


@app.route('/test')
def test():
	pdf_file = new_pdf_filename()
	pdfkit.from_url('http://google.com', pdf_file)
	response = make_response(open(pdf_file).read())
	response.content_type = 'application/pdf'
	return response


@app.route('/pdf', methods=['POST'])
def pdf():
	content = moratab.render(request.form['moratab'])
	html = render_template('main.html', content=content)
	pdf_file = new_pdf_filename()
	pdfkit.from_string(html, pdf_file, options=options)
	response = make_response(open(pdf_file).read())
	response.content_type = 'application/pdf'
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Content-Disposition'] = 'attachment; filename="moratab.pdf"'
	return response


if __name__ == '__main__':
	app.run(debug=True)
