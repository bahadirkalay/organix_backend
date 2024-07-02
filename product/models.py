from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from pip._internal.cli.cmdoptions import editable


# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    image = models.ImageField(upload_to='media/product/')
    pay = models.FloatField(default=0, )

    def get_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        uniqe = slug
        number = 1

        while Product.objects.filter(slug=uniqe).exists():
            uniqe = '{}-{}'.format(slug, number)
            number += 1
        return uniqe

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        self.slug = self.get_slug()
        return super(Product, self).save(*args, **kwargs)
