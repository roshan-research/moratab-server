import time
import moratab
import pdfkit

from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True


def new_pdf_filename():
    return '{}.pdf'.format(int(time.time()*100))

options = {
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-left': '0.75in',
    'margin-bottom': '0.75in',
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
    pdfkit.from_url('http://google.com', 'static/%s' % pdf_file)
    return send_from_directory('static', pdf_file)


@app.route('/pdf', methods=['POST'])
def pdf():
    content = moratab.render(request.form['moratab'])
    html = render_template('main.html', content=content)
    pdf_file = new_pdf_filename()
    pdfkit.from_string(html, 'static/%s' % pdf_file,
                       options=options, css='static/main.css')
    return send_from_directory('static', pdf_file)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1373)
