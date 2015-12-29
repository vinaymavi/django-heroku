from django.contrib import admin

# Register your models here.
from .models import Grade,Designation,FunctionArea,Employee,Trigger,TrainingCategory,NeedCategory,ModeOfLearning,ImpactOnWork,LearningPlan,ScoreCardArea,Objective

admin.site.register(Grade)
admin.site.register(Designation)
admin.site.register(FunctionArea)
admin.site.register(Employee)
admin.site.register(Trigger)
admin.site.register(TrainingCategory)
admin.site.register(NeedCategory)
admin.site.register(ModeOfLearning)
admin.site.register(ImpactOnWork)
admin.site.register(LearningPlan)
admin.site.register(ScoreCardArea)
admin.site.register(Objective)