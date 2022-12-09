from django.shortcuts import render

from django.utils import hashable


def index(request):
  template_name = 'restaurant/index.html'
  data = hashable.make_hashable('Hello World')

  return render(request, template_name, context={'data':data})
