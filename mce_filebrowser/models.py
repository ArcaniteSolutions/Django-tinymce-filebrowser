import datetime
from django.db import models
from django.utils.translation import ugettext as _


def content_file_name(instance, filename):
    return "uploaded/%s/%s/%s".format(datetime.datetime.now().strftime("%Y/%m/%d"), filename)


class FileBrowserFile(models.Model):
    """ Uploaded file model """
    FILE_TYPES = (
        ('img', _('Image')),
        ('doc', _('Document')),
    )

    file_type = models.CharField(max_length=3, choices=FILE_TYPES)

    uploaded_file = models.FileField(
        upload_to=content_file_name,
        verbose_name=_('File / Image'),
        max_length=300,
    )
    create_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Create date')
    )

    user_id = models.IntegerField(null=True, blank=True, verbose_name=_('Who does this file belong to?'))

    def __unicode__(self):
        return u'{0}'.format(self.uploaded_file.name)
