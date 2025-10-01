
from django.contrib import admin
from .models import GraphicDesign, SoftwareProject


@admin.register(GraphicDesign)
class GraphicDesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'project_date', 'is_featured')
    list_filter = ('category', 'project_date', 'is_featured')
    search_fields = ('title', 'description', 'client')
    list_editable = ('is_featured',)
    
@admin.register(SoftwareProject)
class SoftwareProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'technologies', 'completion_date', 'is_featured')
    list_filter = ('category', 'completion_date', 'is_featured')
    search_fields = ('title', 'description', 'technologies')
    list_editable = ('is_featured',)