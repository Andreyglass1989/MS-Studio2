# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from design_interera.models import Interer, Gallery_design_interera
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import pdb; pdb.set_trace()

# Create your views here.
#funcion render project (design_interera_list)
#second list----------------------------------------------------
def design_intr ( request ):
    items = Interer.objects.all()
    paginator = Paginator(items, 9)  # Show 1 contacts per page """" Paginator begin """""
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)  # """""" Paginator end """"""
    return render( request, 'projects.html', locals() )
#end second list----------------------------------------------------




#3rd list------------------------------------------------------------------------------------------
def detail_gallery ( request , interer_id ):
    photos = Interer.objects.get( id = interer_id )
    photo_list = Gallery_design_interera.objects.filter( project_id = interer_id )
    return render(request, 'photo_detail.html', locals())
                   #                             { 'photo_list':photo_list,
                   #                               'photos':photos,
                   #                               'project_id':project_id } )
#end 3rd list----------------------------------------------------------------------------------------