from flask import Flask,render_template,url_for

app = Flask(__name__)

posts =[
    {
        'author': 'Saravanan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Aug 5, 2020'
    },
    {
        'author': 'Sathish',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Aug 5, 2020'
    },
    {
        'author': 'Sagar',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'Aug 5, 2020'
    }
    
]

@app.route('/')
@app.route('/home')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return render_template('home.html',posts=posts)
    
    
@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__':
    app.run(debug=True)
    
