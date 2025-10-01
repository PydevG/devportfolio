from django.db import models

# Create your models here.
class GraphicDesign(models.Model):
    CATEGORY_CHOICES = [
        ('branding', 'Branding & Identity'),
        ('ui-ux', 'UI/UX Design'),
        ('print', 'Print Design'),
        ('digital', 'Digital Art'),
        ('fullstack', 'Full Stack Project'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='graphics/')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='branding')
    tools_used = models.CharField(max_length=200)
    client = models.CharField(max_length=200, blank=True)
    project_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class SoftwareProject(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Application'),
        ('mobile', 'Mobile App'),
        ('api', 'API Development'),
        ('desktop', 'Desktop Software'),
        ('fullstack', 'Full Stack Project'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='software/')
    technologies = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='web')
    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    completion_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title