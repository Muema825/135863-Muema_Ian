from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from .models import CustomUser
from .models import MentalHealthDiagnosis
from .models import MentalHealthAssessment
#from .models import DepressionQuestionnaire


admin.site.register(MentalHealthDiagnosis)
admin.site.register(MentalHealthAssessment)
#admin.site.register(DepressionQuestionnaire)

'''
class UserAdminConfig(UserAdmin):
    search_fields =('email', 'username', 'firstName','lastName')
    list_filter =('email','username', 'firstName', 'is_active','is_staff')
    ordering = ('firstName',)
    list_display =('email','username','firstName','lastName',
                   'is_active', 'is_staff')

admin.site.register(CustomUser,UserAdminConfig)
'''