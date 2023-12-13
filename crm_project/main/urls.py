# urls.py

from django.urls import path
from . import views  
from .views import *


urlpatterns = [
    
    path('',views.homefun,name='home'),
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', change_password_view, name='change_password'),
    path('custom_password_reset/', custom_forgot_password, name='custom_password_reset'),
    path('password_reset_done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', YourPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Create functions

    path('create_trainer/', views.create_trainer, name='create_trainer'),
    path('create_course/', views.create_course, name='create_course'),
    path('create_batch/', views.create_batch, name='create_batch'),
    path('create_student/', views.create_student, name='create_student'),
    path('upload_student_data/', views.upload_student_data, name='upload_student_data'),
    path('student_upload_success/', views.student_upload_success, name='student_upload_success'),

    # Get functions
    path('get_all_trainers/', views.get_all_trainers, name='get_all_trainers'),
    path('get_all_courses/', views.get_all_courses, name='get_all_courses'),
    path('get_all_batches/', views.get_all_batches, name='get_all_batches'),
    path('get_trainer/<int:trainer_id>/', views.get_trainer_by_id, name='get_trainer_by_id'),
    path('get_course/<int:course_id>/', views.get_course_by_id, name='get_course_by_id'),
    path('batches/<str:batch_id>/', views.batch_detail, name='batch_detail'),
    path('get_student/<int:student_id>/',views.get_student_by_id, name='get_student_by_id'),
    path('get_trainers/', views.get_trainers, name='get_trainers'),
    path('courses/', studentCourseListView.as_view(), name='student_course_list'),
    path('student/batch/<int:course_id>/', studentBatchListView.as_view(), name='student-batch-list'),
    path('students/<str:batch_number>/', StudentListView.as_view(), name='get_all_students'),
    path('search-students/', views.search_students, name='search_students'),



    # Update functions
    path('update_trainer/<int:trainer_id>/', views.update_trainer, name='update_trainer'),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    path('update_batch/<str:batch_id>/', views.update_batch, name='update_batch'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),

    # Delete functions
    path('delete_trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('delete_batch/<str:batch_id>/', views.delete_batch, name='delete_batch'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    #adduser
    path('add_user/',views. add_user, name='add_user'),

    #show
    path('course_student', CourseListView.as_view(), name='course_student'),
    path('course_batch/<int:course_id>/', BatchListView.as_view(), name='batch-list'),
    path('course_student/<str:batch_number>/', StudentuserListView.as_view(), name='student-list'),
    path('studentss/<int:student_id>/', staff_student_details, name='student_detailss'),
    path('edit_student_user/<int:student_id>/', edit_student_user, name='edit_student_user'),

    #student_user
    path('student/', student_home, name='student_home_url'),
    path('update_profile/', update_profile, name='update_profile'),


    #upload
    path('upload/test/', upload_test_data, name='upload_test_data'),
    path('upload/attendance/', upload_attendance_data, name='upload_attendance_data'),
    path('upload/lab/', upload_lab_data, name='upload_lab_data'),
    path('upload/softskills/', upload_softskills_data, name='upload_softskills_data'),
    path('upload/interview/', upload_interview_data, name='upload_interview_data'),
]
