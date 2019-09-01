from django.urls import path
from django.urls import include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('students',views.StudentView)
router.register('teachers',views.TeacherView)

urlpatterns = [
   path('', include(router.urls))

]
