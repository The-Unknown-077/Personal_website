from django.contrib import admin
from app.models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name', 'description')
    list_filter = ('full_name',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'procentage')
    search_fields = ('title', 'procentage')
    list_filter = ('title',)

    
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('clients_count', 'projects_count')
    search_fields = ('clients_count', 'project_count')
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title',)
    


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title',)


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)