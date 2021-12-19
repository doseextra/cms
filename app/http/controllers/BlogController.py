from flask import render_template


def index():
    """
    List all blog posts
    """
    return render_template('blog/index.html')


def single(slug):
    """
    Show a single blog post
    """
    title = slug.replace('-', ' ')
    return render_template('blog/single.html', title=title)