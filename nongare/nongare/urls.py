"""
URL configuration for nongare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns ([
    path('admin/', admin.site.urls),
    # path('snippets/', views.SnippetList.as_view(), name='snippet_list'),
    path('contact/', views.SnippetList.as_view(), name='contact-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet_detail'),
    path('', views.api_root),
])
