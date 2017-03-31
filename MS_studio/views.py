from django.shortcuts import render, render_to_response

def index( request ):
    return render(request,'index.html', locals())

def about_ms_studio ( request ):
    return render(request, 'about-ms-studio.html')

def contacts (request):
    return render(request, 'contacts.html' )