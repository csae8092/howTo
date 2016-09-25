# howTo

A blog application which uses GitHub as data storage.

Building a blog application with django is easy as fishing in barrel given the plethora of tutorials describing in detail how to build such an application. Such projects usually leverage django's ORM, defining something like a *Posts* model, derive a form from the model (model.form) enabling users to create, edit posts, store all in the application's database and presenting the posts to the audience in nicely rendered HTML leveraging django's template system. 

## requirements

This blog application should stores it's data (and metadata) in the application's database but is linked/synced with a GitHub account. This means 
* the post's text can be written, modified, edited with any text editor locally,
* posts metadata is edited/stored in application's db
* the texts will be pushed to GitHub
* from there the text can be fetched by the application and imported into its database
** maybe the app can be updated automatically using "GitHub's WebHooks":https://help.github.com/articles/about-webhooks/
** From the database one should be enabled to load further versions of the text

Such an approach would leverage the whole battery of django features (e.g. "tags":https://github.com/alex/django-taggit, "RSS":https://docs.djangoproject.com/ja/1.10/ref/contrib/syndication/, "sitemap":https://docs.djangoproject.com/ja/1.10/ref/contrib/sitemaps/) as well as the advantages of a static blog like jekyll (version control).
