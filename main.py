#!/usr/bin/env python

__author__ = "student"
__version__ = "1.0"
# June 2017
# Flask Blog App re: LaunchCode lc-101
# Rubric: http://education.launchcode.org/web-fundamentals/assignments/build-a-blog/


from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:helloworld@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(720))
    date = db.Column(db.DateTime)

    def __init__(self, title, body, date=None):
        self.title = title
        self.body = body
        if date is None:
            date = datetime.utcnow()
        self.date = date


def is_blog_valid(user_input):
    if user_input != "":
        return True
    else:
        return False


@app.route('/newpost', methods=['GET', 'POST'])
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
            return render_template('newpost.html', entry_title=entry_title, entry_body=entry_body,
                                   title_error=title_error, body_error=body_error)
    else:
        entries = Blog.query.all()
        return render_template('newpost.html', title="Add a Blog Post!", entries=entries)


@app.route('/blog', methods=['GET','POST'])
def blog():
    # TODO: Added the code for SQLAlchemy to timestamp the blog entries, so if you want, you can add a filter_by date
    # descending option to your query so the posts implement all the extra use cases
    entries = Blog.query.all()
    return render_template('blog.html', title="List of Blog Posts", entries=entries)


@app.route('/individual', methods=['GET', 'POST'])
def individual():
    blog_post_id = request.args.get('id')
    entry = Blog.query.get(blog_post_id)
    return render_template('individual.html', title="Blog", entry=entry)


if __name__ == '__main__':
    app.run()
