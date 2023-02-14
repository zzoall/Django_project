"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
# django_project/urls.py에 추가
# 이미지 업로드 필드를 위한 추가
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include('blog.urls')), # 일단 /blog/ 접속 귀찮으니까 추가
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),  # blog 폴더(앱)의 urls.py에 포함된 내용을 참조해줘 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)