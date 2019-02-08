from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=100)
    watch_grade = models.CharField(max_length=100)
    score = models.FloatField(null=True, blank=True, default=None)
    poster_url = models.TextField()
    description = models.TextField()
        
        
        
# class Comment(models.Model):
    
#     photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
#     title = models.CharField(max_length = 100)
#     content = models.TextField()

    def __str__(self):
        return self.title