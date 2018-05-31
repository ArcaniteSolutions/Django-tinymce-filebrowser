from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from mce_filebrowser.models import FileBrowserFile
from mce_filebrowser.forms import FileUploadForm
from mce_filebrowser.utils import render_paginate

from mce_filebrowser.conf import LOCAL_MCE_FILEBROWSER_JQUERY, LOCAL_MCE_FILEBROWSER_THEMECSS


@login_required
def filebrowser(request, file_type):
    """ Trigger view for filebrowser """
    template = 'filebrowser.html'
    upload_form = FileUploadForm()
    uploaded_file = None
    upload_tab_active = False
    is_images_dialog = (file_type == 'img')
    is_documents_dialog = (file_type == 'doc')

    files = FileBrowserFile.objects.filter(file_type=file_type).filter(user_id=request.user.id).order_by('pk')

    if request.POST:
        upload_form = FileUploadForm(request.POST, request.FILES)
        upload_tab_active = True

        if upload_form.is_valid():
            uploaded_file = upload_form.save(commit=False)
            fname = request.FILES['uploaded_file'].name.rpartition(".")
            filename = "{}.{}".format(slugify(fname[0]), fname[2])
            uploaded_file.file_name = filename
            uploaded_file.file_type = file_type
            uploaded_file.user_id = request.user.id
            uploaded_file.save()

    context = {
        'upload_form': upload_form,
        'uploaded_file': uploaded_file,
        'upload_tab_active': upload_tab_active,
        'is_images_dialog': is_images_dialog,
        'is_documents_dialog': is_documents_dialog,
        'LOCAL_MCE_FILEBROWSER_JQUERY': LOCAL_MCE_FILEBROWSER_JQUERY,
        'LOCAL_MCE_FILEBROWSER_THEMECSS': LOCAL_MCE_FILEBROWSER_THEMECSS,
        'absolute_domain': request.build_absolute_uri('/')[:-1],
    }

    per_page = getattr(settings, 'FILEBROWSER_PER_PAGE', 20)
    return render_paginate(request, template, files, per_page, context)


@login_required
def filebrowser_remove_file(request, item_id, file_type):
    """ Remove file """
    fobj = get_object_or_404(FileBrowserFile, file_type=file_type, id=item_id, user_id=request.user.id)
    fobj.delete()

    if file_type == 'doc':
        return HttpResponseRedirect(reverse('mce-filebrowser-documents'))

    return HttpResponseRedirect(reverse('mce-filebrowser-images'))
