# DevOpsLab Monitor

Projeto prático de estudo focado em fundamentos de DevOps Júnior.

A aplicação consiste em uma API de monitoramento básico de serviços, com banco PostgreSQL, Docker, Docker Compose, logs, healthcheck, migrations e pipeline CI.

## Objetivo

Este projeto foi criado para praticar conhecimentos técnicos comuns em vagas de DevOps Júnior:

- Git
- Docker
- Docker Compose
- CI/CD
- PostgreSQL
- API REST
- Variáveis de ambiente
- Logs
- Healthcheck
- Migrations
- Documentação técnica

## Stack

- Backend: FastAPI
- Banco de dados: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Testes: Pytest
- Containerização: Docker
- Orquestração local: Docker Compose
- CI: GitHub Actions

## Arquitetura

```txt
Cliente
  ↓
FastAPI Backend
  ↓
PostgreSQL# DevOpsLab Monitor

Projeto prático de estudo focado em fundamentos de DevOps Júnior.

A aplicação consiste em uma API de monitoramento básico de serviços, com banco PostgreSQL, Docker, Docker Compose, logs, healthcheck, migrations e pipeline CI.

---

## Objetivo

Este projeto foi criado para praticar conhecimentos técnicos comuns em vagas de DevOps Júnior:

- Git
- Docker
- Docker Compose
- CI/CD
- PostgreSQL
- API REST
- Variáveis de ambiente
- Logs
- Healthcheck
- Migrations
- Documentação técnica

---

## Stack

- Backend: FastAPI
- Banco de dados: PostgreSQL
- ORM: SQLAlchemy
- Migrations: Alembic
- Testes: Pytest
- Containerização: Docker
- Orquestração local: Docker Compose
- CI: GitHub Actions

---

## Arquitetura

Cliente  
↓  
FastAPI Backend  
↓  
PostgreSQL  

No ambiente Docker:

devopslab-backend -> devopslab-postgres

---

## Funcionalidades

- GET /health  
  - verifica status da API  
  - verifica conexão com banco  
  - retorna timestamp  

- POST /services  
  - cadastra um serviço monitorado  

- GET /services  
  - lista os serviços cadastrados  

---

## Como rodar com Docker

Na raiz do projeto:

docker compose up --build

Acesse:

API: http://localhost:8000  
Docs: http://localhost:8000/docs  
Healthcheck: http://localhost:8000/health  

Para parar:

docker compose down

Para resetar banco:

docker compose down -v

---

## Testes

Dentro de backend:

python -m pytest

---

## CI/CD

O projeto usa GitHub Actions para:

- rodar testes
- validar build Docker
