"""Todo URL Configuration

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
from django.urls import include, path
from Plan.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("students-view", StudentViewSet)
router.register('plans-view', PlanViewSet)
router.register('accounts-view', AccountViewSet)
router.register('todos-view', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('admin/', admin.site.urls),
    path('students/', students),
    path('student_edit/<int:num>/', student_edit),
    path('plans/', plans),
    path('plans_delete/<int:num>/', plans_delete),
    path('plan_edit/<int:num>/', plan_edit),
    path('donefalse/', donefalse),
    path('seniors/', seniors),
    path('todo/', todo),
    path('', loginView),
    path('logout/', logoutView),
    path('todo/todo_delete/<int:num>', todo_delete),
    path('signup/', signup),
]
