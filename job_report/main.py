import requests

API_URL = "http://127.0.0.1:5000/jobs"

# Consome a API para obter as vagas
response = requests.get(API_URL)
jobs = response.json()


#após fazer o consumo vamos fazer um print via console
#para observar os dados via console

data = response.json()

print(data)


# Organiza as vagas por setor
report = {}
for job in jobs:
    sector = job['sector']
    if sector not in report:
        report[sector] = []
    report[sector].append(job)

# Gera um relatório em um arquivo de texto
with open('report/sector_report.txt', 'w') as f:
    for sector, jobs in report.items():
        f.write(f"Setor: {sector}\n")
        for job in jobs:
            f.write(f"  - Código: {job['code']}, Título: {job['title']}, Salário: {job['salary']}, Matrícula: {job['registration']}, Criado em: {job['created_at']}\n")
        f.write("\n")
