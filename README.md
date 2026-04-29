# DevOpsLab Monitor

Projeto prático focado em fundamentos de DevOps Júnior.

Uma API de monitoramento de serviços com execução automática de checks, persistência em banco de dados e ambiente containerizado.

---

## 🚀 Objetivo

Simular um ambiente real de monitoramento para praticar:

* Git
* Docker e Docker Compose
* CI/CD
* PostgreSQL
* APIs REST
* Variáveis de ambiente
* Logs
* Healthcheck
* Migrations (Alembic)
* Jobs automáticos (scheduler)

---

## 🧱 Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Pytest
* Docker
* GitHub Actions

---

## 🧠 Arquitetura

```
Cliente
  ↓
FastAPI Backend
  ↓
PostgreSQL
```

### Ambiente Docker

```
devopslab-backend -> devopslab-postgres
```

---

## ⚙️ Funcionalidades

### Healthcheck

* `GET /health`

  * status da API
  * status do banco
  * timestamp

---

### Serviços

* `POST /services`
* `GET /services`

---

### Monitoramento

* `POST /checks/run`
* `GET /checks`
* `GET /checks/service/{service_id}`

---

## 🔁 Scheduler automático

O sistema executa checks automaticamente a cada intervalo:

* consulta serviços cadastrados
* faz requisição HTTP
* mede tempo de resposta
* salva resultado no banco

---

## 🐳 Como rodar com Docker

```bash
docker compose up --build
```

Acesse:

* http://localhost:8000/docs
* http://localhost:8000/health

Parar:

```bash
docker compose down
```

Resetar banco:

```bash
docker compose down -v
```

---

## 🧪 Testes

```bash
cd backend
python -m pytest
```

---

## 🗃️ Banco de dados

* PostgreSQL
* Migrations com Alembic

Rodar migrations:

```bash
alembic upgrade head
```

---

## 📊 Logs

Exemplo:

```
method=GET path=/health status_code=200 duration_ms=2.3
```

---

## 🔌 Variáveis de ambiente

Local:

```
DATABASE_URL=postgresql://postgres:123456@localhost:5432/devopslab
```

Docker:

```
DATABASE_URL=postgresql://postgres:123456@postgres:5432/devopslab
```

---

## ⚠️ Observações

* Projeto focado em aprendizado
* Scheduler simples (thread)
* Não preparado para múltiplas instâncias

---

## 📈 Próximos passos

* Deploy no Render
* Logs estruturados
* Dashboard simples

---

## 📌 Status

✔ API funcional
✔ Docker funcionando
✔ Banco integrado
✔ Scheduler automático
✔ Monitoramento básico

---

## 👨‍💻 Autor

Thierre Mota de Almeida