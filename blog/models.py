from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='Null')
    image = models.ImageField(upload_to='gfx')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title


