from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    CATEGORY_CHOICES = [
        ("Data Analysis", "Data Analysis"), ("Dashboard", "Dashboard"),
        ("Business Intelligence", "Business Intelligence"), ("Data Cleaning", "Data Cleaning"),
        ("Reporting", "Reporting"), ("Other", "Other"),
    ]
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES, default="Data Analysis")
    completion_date = models.DateField()
    tools = models.JSONField(default=list, blank=True)
    summary = models.TextField()
    problem = models.TextField(blank=True)
    approach = models.TextField(blank=True)
    insights = models.JSONField(default=list, blank=True)
    outcome = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="project_images/", blank=True, null=True)
    project_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-featured", "-completion_date", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:180] or "project"
            candidate, counter = base, 1
            while Project.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                counter += 1
                candidate = f"{base}-{counter}"
            self.slug = candidate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
