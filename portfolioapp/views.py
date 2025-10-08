from django.shortcuts import render
from .models import SoftwareProject, GraphicDesign
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    # Get page numbers from request
    software_page = request.GET.get('software_page', 1)
    design_page = request.GET.get('design_page', 1)
    
    # Software projects pagination
    featured_software = SoftwareProject.objects.filter(is_featured=True).order_by('-completion_date')
    other_software = SoftwareProject.objects.filter(is_featured=False).order_by('-completion_date')
    all_software = list(featured_software) + list(other_software)
    
    software_paginator = Paginator(all_software, 6)  # 6 software projects per page
    try:
        software_projects = software_paginator.page(software_page)
    except (PageNotAnInteger, EmptyPage):
        software_projects = software_paginator.page(1)
    
    # Design projects pagination
    featured_designs = GraphicDesign.objects.filter(is_featured=True).order_by('-project_date')
    other_designs = GraphicDesign.objects.filter(is_featured=False).order_by('-project_date')
    all_designs = list(featured_designs) + list(other_designs)
    
    design_paginator = Paginator(all_designs, 6)  # 6 design projects per page
    try:
        graphic_designs = design_paginator.page(design_page)
    except (PageNotAnInteger, EmptyPage):
        graphic_designs = design_paginator.page(1)
    
    context = {
        'software_projects': software_projects,
        'graphic_designs': graphic_designs,
    }
    
    return render(request, 'portfolioapp/index.html', context)