# Deploy no Render

## Objetivo

Publicar o backend do DevOpsLab Monitor usando Docker, PostgreSQL gerenciado e variáveis de ambiente.

## Serviços necessários

- Web Service para o backend
- PostgreSQL gerenciado
- Variável de ambiente DATABASE_URL

## Passo 1 — Criar banco PostgreSQL

No Render:

1. New
2. PostgreSQL
3. Nome: devopslab-postgres
4. Database: devopslab
5. User: postgres
6. Copiar a Internal Database URL

## Passo 2 — Criar Web Service

1. New
2. Web Service
3. Conectar o repositório GitHub
4. Runtime: Docker
5. Root Directory: backend
6. Health Check Path: /health

## Passo 3 — Variáveis de ambiente

Adicionar:

DATABASE_URL=<Internal Database URL do Postgres>

## Passo 4 — Deploy

O container executa automaticamente:

python wait_for_db.py
alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8000

## Testes pós-deploy

Acessar:

/health
/docs

Testar:

POST /services
POST /checks/run
GET /checks

## Observação

O plano gratuito do PostgreSQL no Render é útil para estudo e portfólio, mas não deve ser tratado como produção.