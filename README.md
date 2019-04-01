# howTo
A blog application which uses GitHub as data storage.

## motivation 
Blog applications usually come along either in form of highly elaborated content managment systems (CMS) (e.g. Wordpress) or static blogs (e.g. Jekyll). The first category provides a rich feature list (tagging, commets, feeds, fultext searches, user management, ...) and is in general very easy to install and use. The downside is that those applications can't be customize without digging into the dephts of the application's codebase. 
Static blogs like Jekyll instead are propably easyer to customize, especially when it comes to the questions where the content of the blog is actually stored. But they lack many of the features which CMS based blogs provide easily.
The current project tries to combine the advanteges of both worlds. 

## feature list
* the post's text can be written, modified, edited with any text editor locally **done**
* posts metadata is edited/stored in application's db **done**
* the text of the posts can be fetched by the application from any public GitHub account and imported into the app's database **done**
    * maybe the app can be updated automatically using [GitHub's WebHooks](https://help.github.com/articles/about-webhooks/)
    * from the database one should be enabled to load further versions of the text
* the app renders documents to HTML which were encoded in 
    * markdown **done**
    * XML/TEI **done**
* posts can be grouped together into 'books' **done**
* the application's user management allows to publish posts for **done**
    * everybody (i.e. public)
    * persons related to the hosting institution
    * institution's internal staff. 
* [RSS](https://docs.djangoproject.com/ja/1.10/ref/contrib/syndication/)
* [sitemap](https://docs.djangoproject.com/ja/1.10/ref/contrib/sitemaps/)
* [tags](https://github.com/alex/django-taggit) **done**
* searching/filtering
    * by tags
    * fulltext (https://github.com/acdh-oeaw/howto/issues/4)

## install
The application was build with Python 3.4 and django 1.9.x. It was brought to run on Windows and Centos.

1. clone the repo
2. create a virtual environment and run install the required packages `pip install > requirements`
3. makemigrations and migrate `python manage.py makemigrations`and `python manage.py migrate`
4. start the dev-server `python manage.py runserver --settings=howto.settings.dev`
5. browse to http://127.0.0.1:8000/

### create an index
Since [this commit](https://github.com/acdh-oeaw/howto/commit/a2728a219b7867dda2d365897ff3c5cd018ec2f9) posts can be search by their full texts. Index and search functions are based on [Whoosh](https://pypi.python.org/pypi/Whoosh/) and [Haystack](http://haystacksearch.org/). 
To create an index, the following steps have to be done:

1. create a new directory called `whoosh` in the application's root directory. This directory will hold all index data. You can change the name and the location of this directory as it suits you best. But make sure that you updated the `WHOOSH_INDEX`parameter in `howto/settings/base.py` according to your changes.   
2. run the following `manage.py` command: `python manage.py rebuild_index --settings=howto.settings.dev` and confirm with yes that you want to override any already existing index. Be aware, this command makes of course only sense in case you have alredey written some posts. 
