from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    if request.method == "POST":
        link = request.form.get('link')
        return redirect(url_for('answer', linku = link))
    else:
        return render_template('home.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/answer', methods=['GET', 'POST'])
def answer():
    if request.method == "POST":
        link = request.form.get('link')
        return render_template('answer.html', linkku=link)



if __name__ == '__main__':
    app.run(debug=True)