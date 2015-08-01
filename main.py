
import moratab
import pdfkit
from flask import Flask, request, render_template, make_response
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


css_file = 'static/main.css'
pdf_file = 'static/document.pdf'
options = {
	'margin-top': '0.75in',
	'margin-right': '0.75in',
	'margin-left': '0.75in',
	'margin-bottom': '0.75in',
}


@app.route('/')
def main():
	return 'Moratab Server!'


@app.route('/html', methods=['POST'])
def html():
	content = moratab.render(request.form['moratab'])
	content = '<link type="text/css" rel="stylesheet" href="{0}">'.format(css_file) + content
	return render_template('main.html', content=content)


@app.route('/pdf', methods=['POST'])
def pdf():
	content = moratab.render(request.form['moratab'])
	html = render_template('main.html', content=content)
	pdfkit.from_string(html, pdf_file, options=options, css=css_file)
	response = make_response(open(pdf_file).read())
	response.content_type = 'application/pdf'
	return response


if __name__ == '__main__':
	app.run(debug=True)
