import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Candidate, Employer, Job, JobApplication, Interview

def parse_json(request):
    try:
        return json.loads(request.body.decode('utf-8'))
    except Exception:
        return {}

# ==========================================
# MODULE 1 - CANDIDATE MANAGEMENT APIs
# ==========================================

@csrf_exempt
@require_http_methods(["POST"])
def add_candidate(request):
    data = parse_json(request)
    cid = data.get("candidate_id")
    if not cid:
        last = Candidate.objects.order_by("-candidate_id").first()
        cid = (last.candidate_id + 1) if last else 101

    candidate, created = Candidate.objects.update_or_create(
        candidate_id=cid,
        defaults={
            "full_name": data.get("full_name", ""),
            "email": data.get("email", ""),
            "phone": data.get("phone", ""),
            "qualification": data.get("qualification", ""),
            "skills": data.get("skills", ""),
            "experience": int(data.get("experience", 0)),
            "password": data.get("password", ""),
        }
    )
    return JsonResponse({"status": "success", "message": "Candidate created successfully", "candidate": candidate.to_dict()}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_candidates(request):
    candidates = Candidate.objects.all().order_by("candidate_id")
    return JsonResponse([c.to_dict() for c in candidates], safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_candidate(request, id):
    try:
        candidate = Candidate.objects.get(candidate_id=id)
    except Candidate.DoesNotExist:
        return JsonResponse({"error": "Candidate not found"}, status=404)
    
    data = parse_json(request)
    if "full_name" in data: candidate.full_name = data["full_name"]
    if "email" in data: candidate.email = data["email"]
    if "phone" in data: candidate.phone = data["phone"]
    if "qualification" in data: candidate.qualification = data["qualification"]
    if "skills" in data: candidate.skills = data["skills"]
    if "experience" in data: candidate.experience = int(data["experience"])
    if "password" in data: candidate.password = data["password"]
    candidate.save()
    return JsonResponse({"status": "success", "message": "Candidate updated successfully", "candidate": candidate.to_dict()})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_candidate(request, id):
    try:
        candidate = Candidate.objects.get(candidate_id=id)
        candidate.delete()
        return JsonResponse({"status": "success", "message": f"Candidate {id} deleted successfully"})
    except Candidate.DoesNotExist:
        return JsonResponse({"error": "Candidate not found"}, status=404)


# ==========================================
# MODULE 2 - EMPLOYER MANAGEMENT APIs
# ==========================================

@csrf_exempt
@require_http_methods(["POST"])
def add_employer(request):
    data = parse_json(request)
    eid = data.get("employer_id")
    if not eid:
        last = Employer.objects.order_by("-employer_id").first()
        eid = (last.employer_id + 1) if last else 201

    employer, created = Employer.objects.update_or_create(
        employer_id=eid,
        defaults={
            "company_name": data.get("company_name", ""),
            "hr_name": data.get("hr_name", ""),
            "email": data.get("email", ""),
            "phone": data.get("phone", ""),
            "location": data.get("location", ""),
            "industry": data.get("industry", ""),
        }
    )
    return JsonResponse({"status": "success", "message": "Employer created successfully", "employer": employer.to_dict()}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_employers(request):
    employers = Employer.objects.all().order_by("employer_id")
    return JsonResponse([e.to_dict() for e in employers], safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_employer(request, id):
    try:
        employer = Employer.objects.get(employer_id=id)
    except Employer.DoesNotExist:
        return JsonResponse({"error": "Employer not found"}, status=404)
    
    data = parse_json(request)
    if "company_name" in data: employer.company_name = data["company_name"]
    if "hr_name" in data: employer.hr_name = data["hr_name"]
    if "email" in data: employer.email = data["email"]
    if "phone" in data: employer.phone = data["phone"]
    if "location" in data: employer.location = data["location"]
    if "industry" in data: employer.industry = data["industry"]
    employer.save()
    return JsonResponse({"status": "success", "message": "Employer updated successfully", "employer": employer.to_dict()})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_employer(request, id):
    try:
        employer = Employer.objects.get(employer_id=id)
        employer.delete()
        return JsonResponse({"status": "success", "message": f"Employer {id} deleted successfully"})
    except Employer.DoesNotExist:
        return JsonResponse({"error": "Employer not found"}, status=404)


# ==========================================
# MODULE 3 - JOB MANAGEMENT APIs
# ==========================================

@csrf_exempt
@require_http_methods(["POST"])
def add_job(request):
    data = parse_json(request)
    jid = data.get("job_id")
    if not jid:
        last = Job.objects.order_by("-job_id").first()
        jid = (last.job_id + 1) if last else 301

    job = Job.objects.create(
        job_id=jid,
        job_title=data.get("job_title", ""),
        company_name=data.get("company_name", ""),
        location=data.get("location", ""),
        job_type=data.get("job_type", "Full Time"),
        experience_required=int(data.get("experience_required", 0)),
        salary=int(data.get("salary", 0)),
        last_date=str(data.get("last_date", "2026-12-31"))
    )
    return JsonResponse({"status": "success", "message": "Job posted successfully", "job": job.to_dict()}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_jobs(request):
    jobs = Job.objects.all().order_by("-job_id")
    return JsonResponse([j.to_dict() for j in jobs], safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_job(request, id):
    try:
        job = Job.objects.get(job_id=id)
    except Job.DoesNotExist:
        return JsonResponse({"error": "Job not found"}, status=404)
    
    data = parse_json(request)
    if "job_title" in data: job.job_title = data["job_title"]
    if "company_name" in data: job.company_name = data["company_name"]
    if "location" in data: job.location = data["location"]
    if "job_type" in data: job.job_type = data["job_type"]
    if "experience_required" in data: job.experience_required = int(data["experience_required"])
    if "salary" in data: job.salary = int(data["salary"])
    if "last_date" in data: job.last_date = str(data["last_date"])
    job.save()
    return JsonResponse({"status": "success", "message": "Job updated successfully", "job": job.to_dict()})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_job(request, id):
    try:
        job = Job.objects.get(job_id=id)
        job.delete()
        return JsonResponse({"status": "success", "message": f"Job {id} deleted successfully"})
    except Job.DoesNotExist:
        return JsonResponse({"error": "Job not found"}, status=404)


# ==========================================
# MODULE 4 - JOB APPLICATION APIs
# ==========================================

@csrf_exempt
@require_http_methods(["POST"])
def add_application(request):
    data = parse_json(request)
    aid = data.get("application_id")
    if not aid:
        last = JobApplication.objects.order_by("-application_id").first()
        aid = (last.application_id + 1) if last else 401

    app = JobApplication.objects.create(
        application_id=aid,
        candidate_name=data.get("candidate_name", ""),
        company_name=data.get("company_name", ""),
        job_title=data.get("job_title", ""),
        applied_date=str(data.get("applied_date", "2026-07-15")),
        resume=data.get("resume", "resume.pdf"),
        application_status=data.get("application_status", "Applied")
    )
    return JsonResponse({"status": "success", "message": "Application submitted successfully", "application": app.to_dict()}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_applications(request):
    apps = JobApplication.objects.all().order_by("-application_id")
    return JsonResponse([a.to_dict() for a in apps], safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_application(request, id):
    try:
        app = JobApplication.objects.get(application_id=id)
    except JobApplication.DoesNotExist:
        return JsonResponse({"error": "Application not found"}, status=404)
    
    data = parse_json(request)
    if "candidate_name" in data: app.candidate_name = data["candidate_name"]
    if "company_name" in data: app.company_name = data["company_name"]
    if "job_title" in data: app.job_title = data["job_title"]
    if "applied_date" in data: app.applied_date = str(data["applied_date"])
    if "resume" in data: app.resume = data["resume"]
    if "application_status" in data: app.application_status = data["application_status"]
    app.save()
    return JsonResponse({"status": "success", "message": "Application updated successfully", "application": app.to_dict()})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_application(request, id):
    try:
        app = JobApplication.objects.get(application_id=id)
        app.delete()
        return JsonResponse({"status": "success", "message": f"Application {id} deleted successfully"})
    except JobApplication.DoesNotExist:
        return JsonResponse({"error": "Application not found"}, status=404)


# ==========================================
# MODULE 5 - INTERVIEW MANAGEMENT APIs
# ==========================================

@csrf_exempt
@require_http_methods(["POST"])
def add_interview(request):
    data = parse_json(request)
    iid = data.get("interview_id")
    if not iid:
        last = Interview.objects.order_by("-interview_id").first()
        iid = (last.interview_id + 1) if last else 501

    interview = Interview.objects.create(
        interview_id=iid,
        candidate_name=data.get("candidate_name", ""),
        company_name=data.get("company_name", ""),
        interview_date=str(data.get("interview_date", "2026-07-25")),
        interview_time=str(data.get("interview_time", "10:30")),
        interview_mode=data.get("interview_mode", "Online"),
        interview_status=data.get("interview_status", "Scheduled")
    )
    return JsonResponse({"status": "success", "message": "Interview scheduled successfully", "interview": interview.to_dict()}, status=201)

@csrf_exempt
@require_http_methods(["GET"])
def get_interviews(request):
    interviews = Interview.objects.all().order_by("-interview_id")
    return JsonResponse([i.to_dict() for i in interviews], safe=False)

@csrf_exempt
@require_http_methods(["PUT"])
def update_interview(request, id):
    try:
        interview = Interview.objects.get(interview_id=id)
    except Interview.DoesNotExist:
        return JsonResponse({"error": "Interview not found"}, status=404)
    
    data = parse_json(request)
    if "candidate_name" in data: interview.candidate_name = data["candidate_name"]
    if "company_name" in data: interview.company_name = data["company_name"]
    if "interview_date" in data: interview.interview_date = str(data["interview_date"])
    if "interview_time" in data: interview.interview_time = str(data["interview_time"])
    if "interview_mode" in data: interview.interview_mode = data["interview_mode"]
    if "interview_status" in data: interview.interview_status = data["interview_status"]
    interview.save()
    return JsonResponse({"status": "success", "message": "Interview updated successfully", "interview": interview.to_dict()})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_interview(request, id):
    try:
        interview = Interview.objects.get(interview_id=id)
        interview.delete()
        return JsonResponse({"status": "success", "message": f"Interview {id} deleted successfully"})
    except Interview.DoesNotExist:
        return JsonResponse({"error": "Interview not found"}, status=404)


# ==========================================
# SEED DATA API
# ==========================================

@csrf_exempt
@require_http_methods(["GET", "POST"])
def seed_data(request):
    # Candidate Seed
    c1, _ = Candidate.objects.update_or_create(
        candidate_id=101,
        defaults={
            "full_name": "Rahul Sharma",
            "email": "rahul@gmail.com",
            "phone": "9876543210",
            "qualification": "B.Tech CSE",
            "skills": "Python, Django, JavaScript",
            "experience": 2,
            "password": "rahul123"
        }
    )
    c2, _ = Candidate.objects.update_or_create(
        candidate_id=102,
        defaults={
            "full_name": "Ananya Roy",
            "email": "ananya@gmail.com",
            "phone": "9812345678",
            "qualification": "M.Tech Software Engineering",
            "skills": "React, Node.js, Python, SQL",
            "experience": 4,
            "password": "ananya123"
        }
    )

    # Employer Seed
    e1, _ = Employer.objects.update_or_create(
        employer_id=201,
        defaults={
            "company_name": "Infosys",
            "hr_name": "Priya Reddy",
            "email": "hr@infosys.com",
            "phone": "9988776655",
            "location": "Bangalore",
            "industry": "Information Technology"
        }
    )
    e2, _ = Employer.objects.update_or_create(
        employer_id=202,
        defaults={
            "company_name": "TCS",
            "hr_name": "Amit Shah",
            "email": "hr@tcs.com",
            "phone": "9876123450",
            "location": "Hyderabad",
            "industry": "IT Services & Consulting"
        }
    )

    # Job Seed
    j1, _ = Job.objects.update_or_create(
        job_id=301,
        defaults={
            "job_title": "Python Full Stack Developer",
            "company_name": "Infosys",
            "location": "Bangalore",
            "job_type": "Full Time",
            "experience_required": 2,
            "salary": 800000,
            "last_date": "2026-08-15"
        }
    )
    j2, _ = Job.objects.update_or_create(
        job_id=302,
        defaults={
            "job_title": "Senior Frontend Developer",
            "company_name": "TCS",
            "location": "Remote",
            "job_type": "Remote",
            "experience_required": 3,
            "salary": 1200000,
            "last_date": "2026-09-01"
        }
    )
    j3, _ = Job.objects.update_or_create(
        job_id=303,
        defaults={
            "job_title": "Backend Engineering Intern",
            "company_name": "Infosys",
            "location": "Bangalore",
            "job_type": "Internship",
            "experience_required": 0,
            "salary": 300000,
            "last_date": "2026-08-30"
        }
    )

    # Job Application Seed
    a1, _ = JobApplication.objects.update_or_create(
        application_id=401,
        defaults={
            "candidate_name": "Rahul Sharma",
            "company_name": "Infosys",
            "job_title": "Python Full Stack Developer",
            "applied_date": "2026-07-15",
            "resume": "rahul_resume.pdf",
            "application_status": "Applied"
        }
    )

    # Interview Seed
    i1, _ = Interview.objects.update_or_create(
        interview_id=501,
        defaults={
            "candidate_name": "Rahul Sharma",
            "company_name": "Infosys",
            "interview_date": "2026-07-25",
            "interview_time": "10:30",
            "interview_mode": "Online",
            "interview_status": "Scheduled"
        }
    )

    return JsonResponse({
        "status": "success",
        "message": "Sample testing data seeded successfully!",
        "seeded_counts": {
            "candidates": Candidate.objects.count(),
            "employers": Employer.objects.count(),
            "jobs": Job.objects.count(),
            "applications": JobApplication.objects.count(),
            "interviews": Interview.objects.count()
        }
    })
