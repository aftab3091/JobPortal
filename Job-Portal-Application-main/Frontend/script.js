/* ==========================================
   JOB PORTAL APPLICATION - JAVASCRIPT ES6 & FETCH API
   Connecting 20 REST APIs with Dynamic DOM Rendering
   ========================================== */

const API_BASE = 'http://127.0.0.1:8000';

// Global User Session State (stored in LocalStorage)
const State = {
    userType: localStorage.getItem('userType') || 'guest', // 'candidate', 'employer', 'admin', 'guest'
    currentUser: JSON.parse(localStorage.getItem('currentUser') || 'null'),
};

// Toast notification helper
function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container') || createToastContainer();
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <span style="font-size:1.2rem;">${type === 'success' ? '✓' : type === 'error' ? '✕' : 'ℹ'}</span>
        <div>${message}</div>
    `;
    container.appendChild(toast);
    setTimeout(() => {
        toast.remove();
    }, 4000);
}

function createToastContainer() {
    const cont = document.createElement('div');
    cont.id = 'toast-container';
    document.body.appendChild(cont);
    return cont;
}

// Global API Service Wrapper using Fetch API
const API = {
    // Candidates (Module 1)
    async getCandidates() {
        const res = await fetch(`${API_BASE}/candidates/`);
        return await res.json();
    },
    async addCandidate(data) {
        const res = await fetch(`${API_BASE}/candidates/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async updateCandidate(id, data) {
        const res = await fetch(`${API_BASE}/candidates/update/${id}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async deleteCandidate(id) {
        const res = await fetch(`${API_BASE}/candidates/delete/${id}/`, { method: 'DELETE' });
        return await res.json();
    },

    // Employers (Module 2)
    async getEmployers() {
        const res = await fetch(`${API_BASE}/employers/`);
        return await res.json();
    },
    async addEmployer(data) {
        const res = await fetch(`${API_BASE}/employers/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async updateEmployer(id, data) {
        const res = await fetch(`${API_BASE}/employers/update/${id}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async deleteEmployer(id) {
        const res = await fetch(`${API_BASE}/employers/delete/${id}/`, { method: 'DELETE' });
        return await res.json();
    },

    // Jobs (Module 3)
    async getJobs() {
        const res = await fetch(`${API_BASE}/jobs/`);
        return await res.json();
    },
    async addJob(data) {
        const res = await fetch(`${API_BASE}/jobs/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async updateJob(id, data) {
        const res = await fetch(`${API_BASE}/jobs/update/${id}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async deleteJob(id) {
        const res = await fetch(`${API_BASE}/jobs/delete/${id}/`, { method: 'DELETE' });
        return await res.json();
    },

    // Applications (Module 4)
    async getApplications() {
        const res = await fetch(`${API_BASE}/applications/`);
        return await res.json();
    },
    async addApplication(data) {
        const res = await fetch(`${API_BASE}/applications/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async updateApplication(id, data) {
        const res = await fetch(`${API_BASE}/applications/update/${id}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async deleteApplication(id) {
        const res = await fetch(`${API_BASE}/applications/delete/${id}/`, { method: 'DELETE' });
        return await res.json();
    },

    // Interviews (Module 5)
    async getInterviews() {
        const res = await fetch(`${API_BASE}/interviews/`);
        return await res.json();
    },
    async addInterview(data) {
        const res = await fetch(`${API_BASE}/interviews/add/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async updateInterview(id, data) {
        const res = await fetch(`${API_BASE}/interviews/update/${id}/`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await res.json();
    },
    async deleteInterview(id) {
        const res = await fetch(`${API_BASE}/interviews/delete/${id}/`, { method: 'DELETE' });
        return await res.json();
    },

    // Seed Data
    async seedDatabase() {
        const res = await fetch(`${API_BASE}/seed/`, { method: 'POST' });
        return await res.json();
    }
};

// Session & Auth Helpers
function setSession(type, userObj) {
    State.userType = type;
    State.currentUser = userObj;
    localStorage.setItem('userType', type);
    localStorage.setItem('currentUser', JSON.stringify(userObj));
    updateNavUI();
}

function logout() {
    localStorage.removeItem('userType');
    localStorage.removeItem('currentUser');
    State.userType = 'guest';
    State.currentUser = null;
    showToast('Logged out successfully', 'info');
    setTimeout(() => { window.location.href = 'login.html'; }, 1000);
}

function updateNavUI() {
    const badge = document.getElementById('user-session-badge');
    const authBtn = document.getElementById('nav-auth-btn');
    if (!badge) return;

    if (State.userType !== 'guest' && State.currentUser) {
        let name = State.userType === 'candidate' ? State.currentUser.full_name :
                   State.userType === 'employer' ? State.currentUser.company_name : 'System Admin';
        badge.innerHTML = `👤 <span>${name} (${State.userType.toUpperCase()})</span>`;
        if (authBtn) {
            authBtn.innerText = 'Logout';
            authBtn.href = '#';
            authBtn.onclick = (e) => { e.preventDefault(); logout(); };
        }
    } else {
        badge.innerHTML = `🌐 <span>Guest User</span>`;
        if (authBtn) {
            authBtn.innerText = 'Login';
            authBtn.href = 'login.html';
            authBtn.onclick = null;
        }
    }
}

// Modal helper
function openModal(title, bodyHtml) {
    let overlay = document.getElementById('global-modal-overlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'global-modal-overlay';
        overlay.className = 'modal-overlay';
        overlay.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3 id="modal-title" style="color:white; font-size:1.3rem;"></h3>
                    <button class="modal-close" onclick="closeModal()">&times;</button>
                </div>
                <div id="modal-body"></div>
            </div>
        `;
        document.body.appendChild(overlay);
    }
    document.getElementById('modal-title').innerText = title;
    document.getElementById('modal-body').innerHTML = bodyHtml;
    setTimeout(() => overlay.classList.add('active'), 10);
}

function closeModal() {
    const overlay = document.getElementById('global-modal-overlay');
    if (overlay) {
        overlay.classList.remove('active');
    }
}

// Auto Initialize Page Scripts
document.addEventListener('DOMContentLoaded', () => {
    updateNavUI();
});
