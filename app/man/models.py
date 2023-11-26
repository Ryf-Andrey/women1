from django.db import models
from django.urls import reverse
# Create your models here.

class Man(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.id}) # формирует маршрут к записи
    
    class Meta:
        verbose_name = 'Известные люди'
        verbose_name_plural = 'Известные люди'
        ordering = ['time_create', 'title']      #ordering = ['-time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk}) # формирует маршрут к записи
    