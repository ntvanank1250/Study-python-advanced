import os
import django
from django.utils import timezone
from pygame import DROPCOMPLETE
os.environ.setdefault("DJANGO_SETTING_MODULE", "django_proj.setting")
django.setup()

from lession05.models import Product

for i in range(1000):
    Product.objects.create(name='Alfreds Futterkiste', description='Germany', price=101, date_create=timezone.now(), date_modified=timezone.now())