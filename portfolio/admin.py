from django.contrib import admin

# Register your models here.
from .models import Portfolios
admin.site.register(Portfolios)

from .models import Samofund
admin.site.register(Samofund)

