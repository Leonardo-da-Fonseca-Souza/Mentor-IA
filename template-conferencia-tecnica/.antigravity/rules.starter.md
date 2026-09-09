# ⚙️ Regras de Engenharia do Starter Kit (`.antigravity/rules.starter.md`)

> **Instrução Educacional:** Estas regras orientam assistentes de IA (Antigravity/Gemini) ao gerar ou refatorar código no repositório.

---

## 1. Padrões de Código Python
- **Versão:** Python 3.12+.
- **Tipagem:** Utilize `type hints` explícitos em todas as assinaturas de funções e classes.
- **Modelos de Dados:** Todos os DTOs e payloads de API devem utilizar **Pydantic v2** com `model_config = ConfigDict(strict=True)`.
- **Assincronismo:** Utilize `async/await` para qualquer operação de I/O (requisições de rede, consultas a banco de dados e chamadas a LLMs).

---

## 2. Governança e FinOps
- Nenhuma chamada de agente pode ignorar o middleware de contagem de tokens (`FinOpsMiddleware`).
- Se a contagem total de tokens exceder o budget estipulado (ex: 8.000 tokens), o código deve lançar a exceção `FinOpsBudgetExceededException`.

---

## 3. Segurança & LGPD
- Nunca persista endereços IP em texto puro. Aplique sempre `SHA-256` truncado.
- Sanitize todas as strings de comentários de usuários contra injeção de HTML/Scripts.
