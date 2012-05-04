from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from meals.models import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', ListView.as_view(
        model=MealDay,
    )),
    # url(r'^mealplanner/', include('mealplanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
