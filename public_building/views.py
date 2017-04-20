# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from public_building.models import Building, Gallery_building
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
#funcion render project (project_list)
#second list----------------------------------------------------
def building ( request ):
    items = Building.objects.filter( name_rozdela_id = 3 )
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

#second list-----------------------------------------------------


#3rd list------------------------------------------------------------------------------------------
def detail_gallery ( request , building_id ):
    photos = Building.objects.get( id = building_id )
    photo_list = Gallery_building.objects.filter( project_id = building_id )
    return render(request, 'photo_detail.html', locals())

#end 3rd list----------------------------------------------------------------------------------------