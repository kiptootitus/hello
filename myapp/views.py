from django.http import HttpResponse
from django.template import loader
from .models import myapp

def members(request):
  myapps = myapp.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'myapp': myapps,
  }
  return HttpResponse(template.render(context, request))
