from django.shortcuts import render
from blogging.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404

# Create your views here.


def list_view(request):
    context = {'poll': Poll.objects.all()}
    return render(request, 'blogging/list.html', context)


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
