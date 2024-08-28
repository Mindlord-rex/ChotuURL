from django.db import models

# Create your models here.

class ShortURL(models.Model):
    created = models.DateTimeField(auto_not_add=True)
    
    times_followed = models.PositiveIntegerField(default=0)
    
    org_url = models.URLField()
    
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    
    class Meta:
        ordering = ["-created"]
        
    def __str__(self):
        return f'{self.org_url} to {self.short_url}'