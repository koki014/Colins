from django.contrib import admin

from .models import (
    SalesFeatures,
    Slayder,
    Discovery,
    Follow,
    Company,
    Subscriber
    
)

admin.site.register([SalesFeatures, Slayder, Discovery, Follow, Company, Subscriber])

# 