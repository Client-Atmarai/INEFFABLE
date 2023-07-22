from django.urls import path,include
from ineffable_app import views

urlpatterns = [
    path('',views.home,name=""),
    # path('ineffable/',include('django.contrib.auth.urls')), 
    path('about/',views.about,name="about"),
    path('notice/',views.notice,name="notice"),
    path('contact/',views.contact,name="contact"),
    path('enquiry/',views.enquiry,name="enquiry"),
    path('reg/',views.registration,name="reg"),
    path('index/',views.index,name="index"),
    path('hello/',views.hello),
    path('logout_admin/',views.admin_logout,name="admin_logout"),
    #path('sample/',views.sample,name="sample"),
    path('validate/',views.validateuser,name="validateuser"),
    path('enq_form/',views.enq_form,name="enq_form"),
    path('adduser/',views.adduser,name='adduser'),
    path('pdf/',views.pdf_report,name="pdf_report"),
    path('generatePdf/?P<int:c_id>/',views.pdf_creation,name="pdf_creation"),
    path('centre_registration/',views.centre_registration,name="centre_registration"),
    path('StudentregisterForm/',views.StudentRegisterForm,name="StudentRegisterForm"),
    path('centre_login/',views.centre_login,name="centre_login"),
    path('register_student/',views.create_centre_form,name="create_centre_form"),
    path('centre_logout/',views.centre_logout,name="centre_logout"),
    path('',views.stu_logout,name="stu_logout"),
    path('',views.stu_log,name="stu_log"),
    path('error/',views.error,name="error"),
    path('add_student/',views.add_student,name="add_student"),
    path('student_status/',views.status_check,name="status_check"),
    path('admin_check_status/',views.admin_check_status,name="admin_check_status"),
    path('form_update/',views.form_update,name="form_update"),
    path('stu_form/',views.stu_form,name="stu_form"),
    path('courses/',views.courses,name="courses"),
    path('logout_student/',views.logout_student,name="logout_student"),
    path('search/',views.search,name="search"),
    path('searchcentre/',views.searchcentre,name="searchcentre")

]

