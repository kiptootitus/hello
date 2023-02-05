from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import myapp

def members(request):
  myapps = myapp.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'myapp': myapps,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = myapp.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myapp': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  member = myapp.objects.all().values()
  template = loader.get_template('template.html')
  context = {
      'myapp' : member,
  }
  return HttpResponse(template.render(context, request))