from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Http request
def home(request):
    ...
    # return Http response
    return HttpResponse('Home')

# Http request
def sobre(request):
    ...
    # return Http response
    return HttpResponse('Sobre')

# Http request
def contato(request):
    ...
    # return Http response
    return HttpResponse('Contato')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
]
