from django.db import models

class Candidate(models.Model):
    candidate_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    qualification = models.CharField(max_length=255)
    skills = models.CharField(max_length=500)
    experience = models.IntegerField(default=0)
    password = models.CharField(max_length=255)

    def to_dict(self):
        return {
            "candidate_id": self.candidate_id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "qualification": self.qualification,
            "skills": self.skills,
            "experience": self.experience,
            "password": self.password,
        }


class Employer(models.Model):
    employer_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=255)
    hr_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

    def to_dict(self):
        return {
            "employer_id": self.employer_id,
            "company_name": self.company_name,
            "hr_name": self.hr_name,
            "email": self.email,
            "phone": self.phone,
            "location": self.location,
            "industry": self.industry,
        }


class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50)
    experience_required = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    last_date = models.CharField(max_length=50)  # String/Date format YYYY-MM-DD

    def to_dict(self):
        return {
            "job_id": self.job_id,
            "job_title": self.job_title,
            "company_name": self.company_name,
            "location": self.location,
            "job_type": self.job_type,
            "experience_required": self.experience_required,
            "salary": self.salary,
            "last_date": str(self.last_date),
        }


class JobApplication(models.Model):
    application_id = models.IntegerField(primary_key=True)
    candidate_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    applied_date = models.CharField(max_length=50)  # String/Date format YYYY-MM-DD
    resume = models.CharField(max_length=255)
    application_status = models.CharField(max_length=100, default="Applied")

    def to_dict(self):
        return {
            "application_id": self.application_id,
            "candidate_name": self.candidate_name,
            "company_name": self.company_name,
            "job_title": self.job_title,
            "applied_date": str(self.applied_date),
            "resume": self.resume,
            "application_status": self.application_status,
        }


class Interview(models.Model):
    interview_id = models.IntegerField(primary_key=True)
    candidate_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    interview_date = models.CharField(max_length=50)  # String/Date format YYYY-MM-DD
    interview_time = models.CharField(max_length=50)  # String/Time format HH:MM
    interview_mode = models.CharField(max_length=50)
    interview_status = models.CharField(max_length=100, default="Scheduled")

    def to_dict(self):
        return {
            "interview_id": self.interview_id,
            "candidate_name": self.candidate_name,
            "company_name": self.company_name,
            "interview_date": str(self.interview_date),
            "interview_time": str(self.interview_time),
            "interview_mode": self.interview_mode,
            "interview_status": self.interview_status,
        }
