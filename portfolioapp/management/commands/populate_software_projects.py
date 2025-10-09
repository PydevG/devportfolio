from django.core.management.base import BaseCommand
from portfolioapp.models import SoftwareProject
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with software projects'

    def handle(self, *args, **options):
        projects = [
            {
                'title': 'Church Management System',
                'description': 'A comprehensive church management system that handles member registration, attendance tracking, event management, and financial contributions. The system provides real-time analytics and reporting for church administration.',
                'technologies': 'Django, PostgreSQL, React, Bootstrap, Chart.js',
                'category': 'web',
                'project_url': '',
                'github_url': 'https://github.com/yourusername/church-management',
                'completion_date': date(2023, 8, 15),
                'is_featured': True
            },
            {
                'title': 'E-Library',
                'description': 'A digital library platform that allows users to browse, borrow, and read books online. Features include user authentication, book categorization, search functionality, and reading progress tracking.',
                'technologies': 'Python, Django, SQLite, HTML/CSS, JavaScript',
                'category': 'web',
                'project_url': '',
                'github_url': 'https://github.com/yourusername/e-library',
                'completion_date': date(2023, 5, 20),
                'is_featured': False
            },
            {
                'title': 'Blog Platform (Stalog)',
                'description': 'A modern blogging platform with rich text editing, user comments, social sharing, and SEO optimization. Includes admin panel for content management and user role-based access control.',
                'technologies': 'Django, PostgreSQL, Summernote, Django-Allauth, Redis',
                'category': 'web',
                'project_url': '',
                'github_url': 'https://github.com/yourusername/stalog-blog',
                'completion_date': date(2023, 11, 10),
                'is_featured': True
            },
            {
                'title': 'Tanolope Consulting Firm',
                'description': 'A professional website for Tanolope Consulting Firm featuring service pages, team profiles, case studies, and client testimonials. Includes contact forms and appointment scheduling functionality.',
                'technologies': 'HTML5, CSS3, JavaScript, Bootstrap, Django',
                'category': 'web',
                'project_url': 'https://tanolopeconsulting.com',
                'github_url': 'https://github.com/yourusername/tanolope-consulting',
                'completion_date': date(2024, 1, 5),
                'is_featured': True
            },
            {
                'title': 'Bondeni Childrens Home Website',
                'description': 'A responsive website for Bondeni Childrens Home showcasing their mission, programs, and donation opportunities. Features photo galleries, event calendars, and secure donation processing.',
                'technologies': 'Django, Bootstrap, Stripe API, PostgreSQL, Cloudinary',
                'category': 'web',
                'project_url': 'https://bondeni-children.org',
                'github_url': 'https://github.com/yourusername/bondeni-children',
                'completion_date': date(2023, 9, 30),
                'is_featured': False
            },
            {
                'title': 'Mercy Safe Haven Academy Website',
                'description': 'An educational institution website with student portal, course catalog, faculty information, and news updates. Includes parent communication system and academic calendar.',
                'technologies': 'Django, HTML/CSS, JavaScript, SQLite, Django REST Framework',
                'category': 'web',
                'project_url': 'https://mercysafehaven.edu',
                'github_url': 'https://github.com/yourusername/mercy-academy',
                'completion_date': date(2023, 12, 15),
                'is_featured': True
            },
            {
                'title': 'Content Management System',
                'description': 'A custom content management system built from scratch with dynamic page creation, media management, user roles, and template system. Provides intuitive interface for non-technical users.',
                'technologies': 'Django, PostgreSQL, Django REST Framework, React, Tailwind CSS',
                'category': 'web',
                'project_url': '',
                'github_url': 'https://github.com/yourusername/custom-cms',
                'completion_date': date(2024, 2, 1),
                'is_featured': True
            }
        ]

        created_count = 0
        updated_count = 0

        for project_data in projects:
            # Use the default image name
            project_data['image'] = 'software/softwaredefault.jpg'
            
            project, created = SoftwareProject.objects.update_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created: {project.title}')
                )
            else:
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Updated: {project.title}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully processed {created_count + updated_count} projects '
                f'({created_count} created, {updated_count} updated)'
            )
        )