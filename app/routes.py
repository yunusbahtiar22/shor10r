from flask import Blueprint, request, render_template, redirect, url_for
from app.models import Link
from app.extension import db 
from app.auth import requires_auth


short = Blueprint('short', __name__)


@short.route('/')
def index():
    return render_template('index.html')


@short.route('/<short_url>')
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    link.visits = link.visits + 1
    db.session.commit()

    return redirect(link.original_url)


@short.route('/add_url', methods=['POST'])
def add_url():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template('url_added.html', 
        new_link=link.short_url, original_url=link.original_url)


@short.route('/stats')
@requires_auth
def stats():
    links = Link.query.all()

    return render_template('stats.html', links=links)


@short.route('/delete/<int:id>')
def delete_url(id):
    url_to_delete = Link.query.get_or_404(id)
    try:
        db.session.delete(url_to_delete)
        db.session.commit()
    except:
        return "There was a problem deleting that url"
    
    return redirect('/stats')
    
@short.errorhandler(404)
def page_not_found(e):
    return '<h1>Page Not Found !</h1>', 404


