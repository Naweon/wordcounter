from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import wordcounter.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcounter.views.index, name="index"),
    path('about/', wordcounter.views.about, name="about"),
    path('result/', wordcounter.views.result, name="result"),
]
