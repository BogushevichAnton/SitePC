from django.db import models
from django.urls import reverse

class PC(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    src = models.CharField(max_length=255, null = True)

    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
        name = models.CharField(max_length=100, db_index=True)
        def __str__(self):
            return self.name
        def get_absolute_url(self):
            return reverse('category', kwargs={'cat_id': self.pk})