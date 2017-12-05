from django.contrib import admin

from .models import FileBrowserFile


class MCEFilebrowserAdmin(admin.ModelAdmin):
    class Media:
        js = ('mce_filebrowser/js/filebrowser_init.js',)


@admin.register(FileBrowserFile)
class FileBrowserFileAdmin(admin.ModelAdmin):
    pass
