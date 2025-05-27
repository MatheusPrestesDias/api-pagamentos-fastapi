# API Básica de Pagamento

Este projeto fornece uma API simples de pagamento usando FastAPI, projetada para fácil integração com o Azure API Management.

## Endpoints
- `POST /payments`: Cria um novo pagamento
- `GET /payments/{payment_id}`: Consulta o status de um pagamento
- `GET /payments`: Lista todos os pagamentos

## Como executar a API

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
