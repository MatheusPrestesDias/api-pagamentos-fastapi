# Basic Payment API

This project provides a simple payment API using FastAPI, designed for easy integration with Azure API Management.

## Endpoints
- `POST /payments`: Create a new payment
- `GET /payments/{payment_id}`: Retrieve payment status
- `GET /payments`: List all payments

## Running the API

1. Ative o ambiente virtual:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
2. Inicie o servidor:
   ```powershell
   uvicorn main:app --reload
   ```

Acesse a documentação interativa em: [http://localhost:8000/docs](http://localhost:8000/docs)

## Integração com Azure API Management

- Importe o endpoint FastAPI para o Azure API Management.
- Configure políticas de segurança e monitoramento conforme necessário.

---

Este projeto é apenas para fins de demonstração.
