from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home_pg():
    return render_template('index.html')


@app.route('/blog')
def blog_pg():
    return render_template('blog.html')


@app.route('/contact')
def contact_pg():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)