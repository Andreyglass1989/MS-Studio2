# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from public_building.models import Building, Gallery_building
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
#funcion render project (project_list)
#second list----------------------------------------------------
def building ( request ):
    items = Building.objects.filter( name_rozdela_id = 3 )
    return render( request, 'projects_building.html', locals() )

#second list-----------------------------------------------------


#3rd list------------------------------------------------------------------------------------------
def detail_gallery ( request , building_id ):
    photos = Building.objects.get( id = building_id )
    photo_list = Gallery_building.objects.filter( project_id = building_id )
    paginator = Paginator(photo_list, 1)  # Show 1 contacts per page """" Paginator begin """""
    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        photos = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        photos = paginator.page(paginator.num_pages) # """""" Paginator end """"""
    return render(request, 'photo_detail.html', locals())
                   #                             { 'photo_list':photo_list,
                   #                               'photos':photos,
                   #                               'project_id':project_id } )
#end 3rd list----------------------------------------------------------------------------------------