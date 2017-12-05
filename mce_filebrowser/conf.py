from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


LOCAL_MCE_FILEBROWSER_JQUERY = getattr(settings, 'MCE_FILEBROWSER_JQUERY', None)
LOCAL_MCE_FILEBROWSER_THEMECSS = getattr(settings, 'MCE_FILEBROWSER_THEMECSS', None)

if LOCAL_MCE_FILEBROWSER_JQUERY is None:
    raise ImproperlyConfigured("MCE_FILEBROWSER_JQUERY must be set (path relative to your static files root)")

if LOCAL_MCE_FILEBROWSER_THEMECSS is None:
    raise ImproperlyConfigured("MCE_FILEBROWSER_THEMECSS must be set (path relative to your static files root). This should be the path to the TinyMCE theme css file.")
