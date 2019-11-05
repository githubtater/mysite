from django.shortcuts import render
from blogging.models import Poll
# Create your views here.


def list_view(request):
    context = {'poll': Poll.objects.all()}
    return render(request, 'blogging/list.html', context)
