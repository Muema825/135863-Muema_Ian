from django.contrib import admin
from .models import CustomUser
from .models import MentalHealthDiagnosis
from .models import MentalHealthAssessment

admin.site.register(CustomUser)
admin.site.register(MentalHealthDiagnosis)
admin.site.register(MentalHealthAssessment)


