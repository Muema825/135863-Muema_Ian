from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import CustomUser

from .models import MentalHealthAssessment




admin.site.register(MentalHealthAssessment)


'''
class UserAdminConfig(UserAdmin):
    search_fields =('email', 'username', 'firstName','lastName')
    list_filter =('email','username', 'firstName', 'is_active','is_staff')
    ordering = ('firstName',)
    list_display =('email','username','firstName','lastName',
                   'is_active', 'is_staff')

admin.site.register(CustomUser,UserAdminConfig)
'''