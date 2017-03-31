# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from projects_home.models import Project, Gallery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#import pdb; pdb.set_trace()

# Create your views here.
#funcion render project (project_list)
#second list----------------------------------------------------
def projects_house ( request ):
    items = Project.objects.filter( name_rozdela_id = 1 )
    return render( request, 'projects_house.html', locals() )

#funcion render design-interera (design-interera_list)
# def design_interera ( request, pk ):
#     items = Project.objects.filter( name_rozdela_id = 2)
#     return render( request, 'design_interera.html', locals() )

#funcion render public_building (public_building_list)
# def public_building ( request ):
#     items = Project.objects.filter( name_rozdela_id = 3)
#     return render( request, 'projects_building.html', locals() )
#second list-----------------------------------------------------

#3rd list------------------------------------------------------------------------------------------
def detail_gallery ( request , project_id ):
    photos = Project.objects.get( id = project_id )
    photo_list = Gallery.objects.filter( project_id = project_id )
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

