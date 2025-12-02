from django.urls import path

from mce_filebrowser import views


urlpatterns = [
    path('image/',
        views.filebrowser,
        {'file_type': 'img'},
        name='mce-filebrowser-images'
    ),
    path('media/',
        views.filebrowser,
        {'file_type': 'img'},
        name='mce-filebrowser-images'
    ),
    path('file/',
        views.filebrowser,
        {'file_type': 'doc'},
        name='mce-filebrowser-documents'
    ),
    path('image/remove/<int:item_id>/',
        views.filebrowser_remove_file,
        {'file_type': 'img'},
        name='mce-filebrowser-remove-image'
    ),
    path('media/remove/<int:item_id>/',
        views.filebrowser_remove_file,
        {'file_type': 'img'},
        name='mce-filebrowser-remove-media'
    ),
    path('file/remove/<int:item_id>/',
        views.filebrowser_remove_file,
        {'file_type': 'doc'},
        name='mce-filebrowser-remove-document'
    )
]
