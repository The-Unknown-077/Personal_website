from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')
    url = models.URLField()

    def __str__(self):
        return self.full_name

class Skill(models.Model):
    title = models.CharField(max_length=255)
    procentage = models.IntegerField()
    order = models.IntegerField()

    def __str__(self):
        return self.title

class AboutMe(models.Model):
    body = models.CharField(max_length=255)
    clients_count = models.IntegerField()
    projects_count = models.IntegerField()
    total_users = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id)

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')
    duration = models.DurationField()
    users_count = models.IntegerField()
    demo_link = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project/', null=True)
    created_at = models.DateField()
    description = models.TextField(null=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')
    link = models.URLField()
    used_tools = models.ManyToManyField(Skill)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    completed_at = models.DateField()