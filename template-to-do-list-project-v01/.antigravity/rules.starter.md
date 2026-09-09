# 📏 Regras e Convenções de Engenharia para Assistentes de Código

> **Nota Didática:** Este arquivo é utilizado para instruir assistentes de código agênticos (como o Antigravity IDE) sobre as convenções e restrições técnicas do projeto.

---

## 1. Convenções de Código Python

1. **Tipagem Estrita:** Todo o código Python deve utilizar type hints completos (`typing` + Pydantic v2).
2. **Programação Assíncrona:** Operações de I/O, chamadas HTTP e acessos a banco de dados devem utilizar `async/await`.
3. **Tratamento de Exceções:** Trate exceções específicas de API e de governança FinOps. Nunca utilize `except Exception: pass`.

---

## 2. Regras FinOps e Limites

1. **Limite de Tokens:** Nunca permita que chamadas aos modelos ultrapassem **8.192 tokens**.
2. **Modelos Permitidos:** Utilize `gemini-3.5-flash` para rotinas diárias e `gemini-3.5-pro` apenas para geração de relatórios complexos.

---

## 3. Segurança

1. **Sanitização de Dados:** Todo prompt enviado a serviços externos deve passar pela filtragem PII antes da transmissão.
2. **Segurança de Credentials:** Nenhuma chave de API (ex: `GOOGLE_API_KEY`) pode ser commitada no código-fonte.
