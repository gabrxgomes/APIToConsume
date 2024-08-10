from flask import Flask, request, jsonify
import json
import uuid
from datetime import datetime

app = Flask(__name__)

# Carrega vagas
def load_jobs():
    with open('data/jobs.json', 'r') as f:
        return json.load(f)

# Salva vagas
def save_jobs(jobs):
    with open('data/jobs.json', 'w') as f:
        json.dump(jobs, f, indent=4)

# Rota para criar uma nova vaga
@app.route('/jobs', methods=['POST'])
def create_job():
    jobs = load_jobs()
    job_data = request.json
    
    # Cria uma nova vaga com dados básicos
    job_id = str(uuid.uuid4())
    job = {
        'id': job_id,
        'created_at': datetime.now().isoformat(),
        'title': job_data['title'],
        'code': job_data['code'],
        'description': job_data['description'],
        'salary': job_data['salary'],
        'sector': job_data['sector']
    }
    
    jobs.append(job)
    save_jobs(jobs)
    return jsonify(job), 201

# Rota para listar todas as vagas
@app.route('/jobs', methods=['GET'])
def list_jobs():
    jobs = load_jobs()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
