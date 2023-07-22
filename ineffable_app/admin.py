from django.contrib import admin
from .models import AdminLogin,ResgisterStudent,CentreRegisterStudent,Status_create,Studentform,CentreStatus,Student_form_creation
# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(ResgisterStudent)
admin.site.register(CentreRegisterStudent)
admin.site.register(Studentform)
admin.site.register(Status_create)
admin.site.register(CentreStatus)
admin.site.register(Student_form_creation)
 