# ⚡ CareerPulse - Full-Stack Job Portal Application

A comprehensive, production-grade **Job Portal Application** designed to connect employers with candidates, enable online job searching and application pipelines, track interviews, and provide full administrative management.

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3 (Modern Glassmorphic Dark Design System), JavaScript (ES6 Modules), Fetch API
- **Backend**: Python, Django, Function-Based Views (FBVs), REST APIs, `@csrf_exempt`, CORS Middleware
- **Database**: SQLite 3 (ORM & Direct Relational Engine)

---

## 📂 Project Folder Structure

```text
JobPortal/
│── manage.py
│── Backend/
│     ├── models.py
│     ├── views.py
│     ├── urls.py
│     ├── db.py
│     ├── settings.py
│     ├── wsgi.py
│     └── db.sqlite3
│
└── Frontend/
      ├── index.html
      ├── login.html
      ├── register.html
      ├── jobs.html
      ├── applications.html
      ├── interviews.html
      ├── candidate_dashboard.html
      ├── employer_dashboard.html
      ├── admin_dashboard.html
      ├── style.css
      └── script.js
```

---

## 📡 REST API Documentation (20 Endpoints)

### Module 1 – Candidate Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/candidates/add/` | Register new candidate profile |
| `GET`  | `/candidates/` | Fetch list of all candidates |
| `PUT`  | `/candidates/update/<id>/` | Update candidate details by ID |
| `DELETE` | `/candidates/delete/<id>/` | Remove candidate by ID |

**Sample Candidate Payload**:
```json
{
    "candidate_id": 101,
    "full_name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "qualification": "B.Tech CSE",
    "skills": "Python, Django, JavaScript",
    "experience": 2,
    "password": "rahul123"
}
```

### Module 2 – Employer Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/employers/add/` | Add/Register employer profile |
| `GET`  | `/employers/` | Retrieve all registered employers |
| `PUT`  | `/employers/update/<id>/` | Edit employer info by ID |
| `DELETE` | `/employers/delete/<id>/` | Remove employer by ID |

**Sample Employer Payload**:
```json
{
    "employer_id": 201,
    "company_name": "Infosys",
    "hr_name": "Priya Reddy",
    "email": "hr@infosys.com",
    "phone": "9988776655",
    "location": "Bangalore",
    "industry": "Information Technology"
}
```

### Module 3 – Job Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/jobs/add/` | Post new job opening |
| `GET`  | `/jobs/` | Get list of available jobs |
| `PUT`  | `/jobs/update/<id>/` | Edit job requirements by ID |
| `DELETE` | `/jobs/delete/<id>/` | Delete job opening |

**Sample Job Payload**:
```json
{
    "job_id": 301,
    "job_title": "Python Full Stack Developer",
    "company_name": "Infosys",
    "location": "Bangalore",
    "job_type": "Full Time",
    "experience_required": 2,
    "salary": 800000,
    "last_date": "2026-08-15"
}
```

### Module 4 – Job Application Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/applications/add/` | Apply for open job vacancy |
| `GET`  | `/applications/` | Fetch submitted applications |
| `PUT`  | `/applications/update/<id>/` | Update pipeline status |
| `DELETE` | `/applications/delete/<id>/` | Delete job application |

**Sample Job Application Payload**:
```json
{
    "application_id": 401,
    "candidate_name": "Rahul Sharma",
    "company_name": "Infosys",
    "job_title": "Python Full Stack Developer",
    "applied_date": "2026-07-15",
    "resume": "rahul_resume.pdf",
    "application_status": "Applied"
}
```

### Module 5 – Interview Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/interviews/add/` | Schedule technical interview |
| `GET`  | `/interviews/` | Get interview schedules |
| `PUT`  | `/interviews/update/<id>/` | Update interview status/time |
| `DELETE` | `/interviews/delete/<id>/` | Cancel & remove interview |

**Sample Interview Payload**:
```json
{
    "interview_id": 501,
    "candidate_name": "Rahul Sharma",
    "company_name": "Infosys",
    "interview_date": "2026-07-25",
    "interview_time": "10:30",
    "interview_mode": "Online",
    "interview_status": "Scheduled"
}
```

---

## 🚀 How to Run the Application

### 1. Start Django Backend Server
```bash
python manage.py runserver 8000
```
*The backend server will launch at `http://127.0.0.1:8000/`.*

### 2. Launch Frontend Application
Open `Frontend/index.html` directly in any web browser, or serve it using Python's http server:
```bash
cd Frontend
python -m http.server 3000
```
Open `http://localhost:3000/` in your browser.

---

## 🔥 Included Bonus Features

1. **Job Search & Advanced Filter Engine**: Search across keywords, locations, job types (Full Time, Part Time, Internship, Remote).
2. **Resume Upload & Interactive Download**: Attach custom resumes and download/preview candidate files in real-time.
3. **Company Profile Cards**: View detailed employer metrics, HR contacts, and active job postings.
4. **Visual Interview Calendar & Timeline**: Highlighting upcoming schedules and candidate interview slots.
5. **AI/Smart Job Recommendation Engine**: Auto-matches candidates with open jobs based on their experience and skills.
