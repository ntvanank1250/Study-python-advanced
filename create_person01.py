
import os
import sys
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assignment_app.settings")
django.setup()
from lession01.models import Person


Person.objects.create(name='Hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')
Person.objects.create(name='hieu', age='12',address='ha noi', mobile_number='0947983316')



