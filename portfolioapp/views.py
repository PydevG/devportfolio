from django.shortcuts import render
from .models import SoftwareProject, GraphicDesign


# Create your views here.
def home(request):
    # Get featured projects first, then others
    featured_software = SoftwareProject.objects.filter(is_featured=True).order_by('-completion_date')
    other_software = SoftwareProject.objects.filter(is_featured=False).order_by('-completion_date')
    software_projects = list(featured_software) + list(other_software)
    
    featured_designs = GraphicDesign.objects.filter(is_featured=True).order_by('-project_date')
    other_designs = GraphicDesign.objects.filter(is_featured=False).order_by('-project_date')
    graphic_designs = list(featured_designs) + list(other_designs)
    
    # Limit to 12 projects total for better performance
    software_projects = software_projects[:6]
    graphic_designs = graphic_designs[:6]
    
    context = {
        'software_projects': software_projects,
        'graphic_designs': graphic_designs,
    }
    
    return render(request, 'portfolioapp/index.html', context)