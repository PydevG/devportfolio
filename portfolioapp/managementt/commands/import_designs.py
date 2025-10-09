# graphics/management/commands/import_designs.py
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from graphics.models import GraphicDesign
from django.core.files import File
from datetime import datetime

class Command(BaseCommand):
    help = 'Import Photoshop designs from a folder to the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--folder',
            type=str,
            help='Path to the folder containing design images',
            default='photoshop-designs'
        )
        parser.add_argument(
            '--category',
            type=str,
            help='Category for the designs',
            default='branding',
            choices=['branding', 'ui-ux', 'print', 'digital', 'fullstack']
        )

    def handle(self, *args, **options):
        folder_path = options['folder']
        category = options['category']
        
        # Get absolute path
        if not os.path.isabs(folder_path):
            folder_path = os.path.join(settings.BASE_DIR, folder_path)
        
        self.stdout.write(f"Scanning folder: {folder_path}")
        
        if not os.path.exists(folder_path):
            self.stderr.write(f"Error: Folder '{folder_path}' does not exist")
            return
        
        # Supported image extensions
        valid_extensions = ['.png', '.jpg', '.jpeg', '.webp', '.svg']
        
        designs_imported = 0
        designs_skipped = 0
        
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            
            # Skip directories and non-image files
            if (os.path.isdir(file_path) or 
                not any(filename.lower().endswith(ext) for ext in valid_extensions)):
                continue
            
            # Generate title from filename (remove extension and replace underscores/hyphens)
            title = self.generate_title_from_filename(filename)
            
            # Check if design already exists
            if GraphicDesign.objects.filter(title=title).exists():
                self.stdout.write(f"Skipping '{title}' - already exists")
                designs_skipped += 1
                continue
            
            try:
                # Create new GraphicDesign instance
                with open(file_path, 'rb') as f:
                    design = GraphicDesign(
                        title=title,
                        description=self.generate_description(title, category),
                        category=category,
                        tools_used="Adobe Photoshop, Adobe Creative Suite",
                        client="Personal Project",
                        project_date=datetime.now().date(),
                        is_featured=False  # You can modify this as needed
                    )
                    
                    # Save the image file
                    design.image.save(filename, File(f), save=True)
                    
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Successfully imported: {title}")
                    )
                    designs_imported += 1
                    
            except Exception as e:
                self.stderr.write(f"❌ Error importing {filename}: {str(e)}")
        
        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Import completed: {designs_imported} designs imported, {designs_skipped} skipped"
            )
        )
    
    def generate_title_from_filename(self, filename):
        """Generate a human-readable title from filename"""
        # Remove file extension
        name_without_ext = os.path.splitext(filename)[0]
        
        # Replace underscores and hyphens with spaces
        title = name_without_ext.replace('_', ' ').replace('-', ' ')
        
        # Capitalize first letter of each word
        title = ' '.join(word.capitalize() for word in title.split())
        
        return title
    
    def generate_description(self, title, category):
        """Generate a description based on title and category"""
        category_descriptions = {
            'branding': f"Brand identity design for {title} featuring logo, color palette, and visual elements",
            'ui-ux': f"User interface and experience design for {title} with modern, intuitive layouts",
            'print': f"Print design project for {title} including brochures, business cards, and marketing materials", 
            'digital': f"Digital artwork and graphic design for {title} created using Adobe Creative Suite",
            'fullstack': f"Full stack project design for {title} combining frontend visuals with backend functionality"
        }
        
        return category_descriptions.get(category, f"Graphic design project for {title}")