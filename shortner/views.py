from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create(request):
    if request.method == 'POST':
        link = request.POST.get('link')

        if link:
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link, uuid=uid)
            new_url.save()
            return HttpResponse(uid)
        else:
            return HttpResponse("Missing 'link' parameter", status=400)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)