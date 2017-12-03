
from __future__ import print_function
import os, time, tempfile
import moratab
from flask import Flask, request, render_template, make_response
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


new_pdf_filename = lambda: 'static/{}.pdf'.format(int(time.time()*100))


def to_pdf(html, output):
	address = os.path.abspath(os.path.dirname(__file__))
	with tempfile.NamedTemporaryFile(delete=True, suffix='.html', dir=address) as html_file:
		html_file.write(html.encode('utf-8'))
		html_file.flush()

		filename = os.path.join(address, html_file.name)
		# os.system('chromium-browser --headless --disable-gpu --print-to-pdf={} file://{}'.format(output, filename))
		os.system('chrome-headless-render-pdf --include-background --url file://{} --pdf {}'.format(filename, output))


@app.route('/')
def main():
	return 'Moratab Server!'


@app.route('/form')
def form():
	return render_template('form.html')


@app.route('/html', methods=['POST'])
def html():
	content = moratab.render(request.form['moratab'])
	return render_template('main.html', content=content)


@app.route('/test')
def test():
	pdf_file = new_pdf_filename()
	to_pdf('Salam!', pdf_file)
	response = make_response(open(pdf_file).read())
	response.content_type = 'application/pdf'
	return response


@app.route('/pdf', methods=['POST'])
def pdf():
	content = moratab.render(request.form['moratab'])
	html = render_template('main.html', content=content)
	pdf_file = new_pdf_filename()
	to_pdf(html, pdf_file)
	response = make_response(open(pdf_file).read())
	response.content_type = 'application/pdf'
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Content-Disposition'] = 'attachment; filename="moratab.pdf"'
	return response


if __name__ == '__main__':
	app.run(debug=True)
