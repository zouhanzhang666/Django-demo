
# url声明
"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from message_board import views
# django2.0一般不用正则
urlpatterns = [
    url(r'^$',views.homePage),
    url(r'^school/', include('testapp1.urls')),  # 转到app1的urls.py
    url(r'^message/', include('message_board.urls')),  # 转到message_board的urls.py
    url(r'^admin/', admin.site.urls),  # 管理员
]
