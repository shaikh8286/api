from django.contrib import admin
from django.urls import path, include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

#from companyapi.api.views import EmployeeViewSet

router =routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees',EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls))
      
]