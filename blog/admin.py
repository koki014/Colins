from django.contrib import admin


from .models import (
    Blog,
    Slayder,
    Category
)

admin.site.register([Blog, Slayder, Category])