from rest_framework.decorators import api_view

# Create your views here.
def restaurant_view(request, *args, **kwargs):
  return redirect(request.body)
