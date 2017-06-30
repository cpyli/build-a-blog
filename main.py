<<<<<<< HEAD
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:helloworld@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

def is_blog_valid(user_input):
    if user_input != "":
        return True
    else:
        return False

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(720))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/newpost', methods=['GET','POST'])
def newpost():

    if request.method == 'POST':

        entry_title = request.form['title']
        entry_body = request.form['body']

        title_error = ""
        body_error = ""

        if not is_blog_valid(entry_title):
            title_error = "Enter blog title"
    
        if not is_blog_valid(entry_body):
            body_error = "Enter blog body"

        if not title_error and not body_error:
            new_entry = Blog(entry_title, entry_body)
            db.session.add(new_entry)
            db.session.commit()   

            new_entry_id = str(new_entry.id)

            new_entry_URL = '/individual?id=' + new_entry_id

            return redirect(new_entry_URL)
        
        else:
            return render_template('newpost.html', 
            entry_title=entry_title,entry_body=entry_body,
            title_error=title_error,body_error=body_error)

    else:
        entries = Blog.query.all()
        return render_template('newpost.html', title="Add a Blog Post!", entries=entries)

@app.route('/blog', methods=['GET','POST'])
def blog():   

    entries = Blog.query.all()

    return render_template('blog.html', title="List of Blog Posts", entries=entries)

@app.route('/individual', methods=['GET', 'POST'])
def individual(): 

    id = request.args.get('id')
    entry = Blog.query.get(id)

    return render_template('individual.html', title="Blog", entry=entry)

if __name__ == '__main__':
=======
from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:helloworld@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

def is_blog_valid(user_input):
    if user_input != "":
        return True
    else:
        return False

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(720))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/newpost', methods=['GET','POST'])
def newpost():

    if request.method == 'POST':

        entry_title = request.form['title']
        entry_body = request.form['body']

        title_error = ""
        body_error = ""

        if not is_blog_valid(entry_title):
            title_error = "Enter blog title"
    
        if not is_blog_valid(entry_body):
            body_error = "Enter blog body"

        if not title_error and not body_error:
            new_entry = Blog(entry_title, entry_body)
            db.session.add(new_entry)
            db.session.commit()   

            new_entry_id = str(new_entry.id)

            new_entry_URL = '/individual?id=' + new_entry_id

            return redirect(new_entry_URL)
        
        else:
            return render_template('newpost.html', 
            entry_title=entry_title,entry_body=entry_body,
            title_error=title_error,body_error=body_error)

    else:
        entries = Blog.query.all()
        return render_template('newpost.html', title="Add a Blog Post!", entries=entries)

@app.route('/blog', methods=['GET','POST'])
def blog():   

    entries = Blog.query.all()

    return render_template('blog.html', title="List of Blog Posts", entries=entries)

@app.route('/individual', methods=['GET', 'POST'])
def individual(): 

    id = request.args.get('id')
    entry = Blog.query.get(id)

    return render_template('individual.html', title="Blog", entry=entry)

if __name__ == '__main__':
>>>>>>> 36179790ef80907bbd367ddfac39a672a8fc4992
    app.run()