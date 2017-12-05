This is a fork of https://github.com/aisayko/Django-tinymce-filebrowser, including the changes of https://github.com/FullFact/Django-tinymce-filebrowser

Updated for TinyMCE 4 and added new settings which can be set as follows

MCE_FILEBROWSER_JQUERY = 'js/jquery-1.9.1.min.js'

MCE_FILEBROWSER_THEMECSS = 'js/3rdparty/tinymce4.0.2/skins/lightgray/skin.min.css'

In addition, uploads are linked to users and only available to authenticated ones. The returned url is given in absolute path.

django-tinymce-filebrowser
===

**django-tinymce-filebrowser** is a simple and flexible tool for managing your files and images from TinyMCE editor.

Current version of package support only TinyMCE 3.x versions.

Quickstart:
===

Install django-tinymce-filebrowser:

    $ pip install django-tinymce-filebrowser

Add tinymce and mce_filebrowser to INSTALLED_APPS in settings.py for your project:

    INSTALLED_APPS = (
        ...
        'tinymce',
        'sorl.thumbnail',
        'mce_filebrowser',
    )

Note: sorl.thumbnail is required package for correct filebrowser work.

Migrate django-tinymce-filebrowser models

    $ python manage.py migrate mce_filebrowser

Change tinymce config to work with filebrowser:

    TINYMCE_DEFAULT_CONFIG = {
      'file_browser_callback': 'mce_filebrowser'
    }

Add mce_filebrowser.urls to urls.py for your project:

    urlpatterns = [
        ...
        url(r'^tinymce/', include('tinymce.urls')),
        url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    ]

In your models.py code:

    from django.db import models
    from tinymce.models import HTMLField

    class MyModel(models.Model):
        ...
        content = HTMLField()

In your admin.py:

    from django.contrib import admin
    from myapp.models import MyModel
    from mce_filebrowser.admin import MCEFilebrowserAdmin

    class MyModelAdmin(MCEFilebrowserAdmin):
        pass

    admin.site.register(MyModel, MyModelAdmin)

**django-tinymce-filebrowser** uses django staticfiles.


If You do not use django-tinymce package then add next lines to TinyMCE init:

    tinyMCE.init({
        ...
        file_browser_callback: mce_filebrowser
    })


Additional settings:

    FILEBROWSER_PER_PAGE - files per page in filebrowser
