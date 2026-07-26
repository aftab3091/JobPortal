from django.urls import path
from . import views

urlpatterns = [
    # Module 1: Candidates
    path('candidates/add/', views.add_candidate, name='add_candidate'),
    path('candidates/', views.get_candidates, name='get_candidates'),
    path('candidates/update/<int:id>/', views.update_candidate, name='update_candidate'),
    path('candidates/delete/<int:id>/', views.delete_candidate, name='delete_candidate'),

    # Module 2: Employers
    path('employers/add/', views.add_employer, name='add_employer'),
    path('employers/', views.get_employers, name='get_employers'),
    path('employers/update/<int:id>/', views.update_employer, name='update_employer'),
    path('employers/delete/<int:id>/', views.delete_employer, name='delete_employer'),

    # Module 3: Jobs
    path('jobs/add/', views.add_job, name='add_job'),
    path('jobs/', views.get_jobs, name='get_jobs'),
    path('jobs/update/<int:id>/', views.update_job, name='update_job'),
    path('jobs/delete/<int:id>/', views.delete_job, name='delete_job'),

    # Module 4: Job Applications
    path('applications/add/', views.add_application, name='add_application'),
    path('applications/', views.get_applications, name='get_applications'),
    path('applications/update/<int:id>/', views.update_application, name='update_application'),
    path('applications/delete/<int:id>/', views.delete_application, name='delete_application'),

    # Module 5: Interviews
    path('interviews/add/', views.add_interview, name='add_interview'),
    path('interviews/', views.get_interviews, name='get_interviews'),
    path('interviews/update/<int:id>/', views.update_interview, name='update_interview'),
    path('interviews/delete/<int:id>/', views.delete_interview, name='delete_interview'),

    # Seed Data Route
    path('seed/', views.seed_data, name='seed_data'),
]
