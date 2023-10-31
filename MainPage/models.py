from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
