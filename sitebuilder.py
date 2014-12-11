import sys
import os

from flask import Flask, render_template, redirect
from flask_flatpages import FlatPages
from flaskext.markdown import Markdown
from flask.ext.assets import Environment as AssetManager
from flask_frozen import Freezer



# configuration
REPO_NAME = "gleeguesite"
APP_DIR = os.path.dirname(os.path.abspath(__file__))

#def parent_dir(path):
#    '''Return the parent of a directory.'''
#    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = APP_DIR
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# print PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer

DEBUG = True
TESTING = True
ASSETS_DEBUG = DEBUG
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
#FLATPAGES_ROOT = 'pages'
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
#FREEZER_RELATIVE_URLS = True
# App configuration
#SECTION_MAX_LINKS = 12
#BASE_URL = "https://neotheicebird.github.io/gleegue.com"

#FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)


app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)
asset_manager = AssetManager(app)

###############################################################################
# Context processors

#@app.context_processor
#def inject_ga():
    #return dict(BASE_URL=BASE_URL)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

#@app.route('/sublocator/')
#def sublocator():
#    return redirect("https://docs.google.com/spreadsheets/d/1-TsLhg2NbzardgX6KckQM_p5O5VMesYYabcnwR09fZ0", code=302)

@app.route('/photos/')
def photos():
    return render_template("photos/photos.html")

#@app.route('/wiki/')
#def wiki():
#    return redirect("http://gleegue.wikidot.com/", code=302)

@app.route('/blog/')
def blog():
    return render_template("blog/blogs.html")

@app.route('/track/')
def track():
    return render_template("track/tracking-sheets.html")

@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        app.debug = False
        asset_manager.config['ASSETS_DEBUG'] = False
        freezer.freeze()
    elif len(sys.argv) > 1 and sys.argv[1] == "serve":
        freezer.serve()
    else:
        app.run(port=8000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            