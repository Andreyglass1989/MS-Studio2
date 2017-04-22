from django.shortcuts import render, render_to_response
from partner.models import Gallery

def index( request ):
    return render(request,'index.html')

def about_ms_studio ( request ):
    return render(request, 'about-ms-studio.html')

def contacts (request):
    return render(request, 'contacts.html' )

def price( request ):
    return render(request,'price.html')

def partner( request ):
    items = Gallery.objects.all()
    return render(request,'partner.html', locals())

def menu( request ):
    return render(request,'base.html')