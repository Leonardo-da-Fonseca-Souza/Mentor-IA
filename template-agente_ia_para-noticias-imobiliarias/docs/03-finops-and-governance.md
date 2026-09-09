# 💰 Playbook 03: FinOps & Governança de Custos de Inferência em IA

> **Módulo:** MLOps & FinOps · **Público:** Engenheiros de IA, Tech Leads & Arquitetos

---

## 1. O que é FinOps para Sistemas Agênticos?

**FinOps (Financial Operations)** em Inteligência Artificial é a disciplina de medir, gerenciar e otimizar continuadamente os custos de inferência de modelos LLM e chamadas de API.

Diferente de software tradicional onde o custo de computação é previsível, sistemas agênticos autônomos podem gerar **explosões de consumo de tokens** se entrarem em loops infinitos de retries ou se utilizarem modelos caros desnecessariamente.

---

## 2. A Fórmula de Cálculo de Custo por Requisição

Cada requisição a uma LLM consome 3 tipos de tokens:

$$\text{Custo Total (USD)} = \frac{\text{Tokens Input} \times P_{\text{input}}}{1.000.000} + \frac{\text{Tokens Cached} \times P_{\text{cached}}}{1.000.000} + \frac{\text{Tokens Output} \times P_{\text{output}}}{1.000.000}$$

Onde $P_{\text{input}}$, $P_{\text{cached}}$ e $P_{\text{output}}$ são as tarifas oficiais por 1 milhão de tokens cobradas pelo provedor.

### Tabela de Referência de Precificação (Exemplo USD / 1M Tokens)

| Modelo | Papel Recomendado | Custo Input / 1M | Custo Cached / 1M | Custo Output / 1M |
|---|---|---|---|---|
| **Gemini 2.0 Flash** | Classificação, Roteamento, Triage | $0.10 | $0.025 | $0.40 |
| **Gemini 1.5 Pro** | Síntese Complexa, Raciocínio Profundo | $1.25 | $0.312 | $5.00 |
| **Claude 3.5 Sonnet** | Redação Jornalística, Refatoração Código | $3.00 | $0.750 | $15.00 |
| **Text Embedding 004** | Vetorização Semântica | $0.025 | N/A | $0.00 |

---

## 3. Matriz de Seleção Pragmática de Modelos

```mermaid
flowchart TD
    Task[Nova Tarefa Agêntica] --> Complexity{Exige raciocínio profundo ou redação longa?}
    Complexity -->|Não| Flash[Usar Gemini 2.0 Flash\n(Custo ~10x menor, latência < 200ms)]
    Complexity -->|Sim| Pro[Usar Gemini 1.5 Pro / Claude 3.5\n(Resumos jornalísticos e códigos)]
```

---

## 4. Onde Aplicar Otimizações FinOps (Táticas Práticas)

### Tática 1: Usar Context Caching
Se a instrução do seu agente (System Prompt) possui mais de 32.000 tokens (ex: manuais extensos de marca ou documentos de compliance), ative o **Context Caching** do provedor. As chamadas subsequentes pagarão até 75% a menos nos tokens de entrada.

### Tática 2: Enforce Token Limits no Pydantic
Defina limites rígidos de geração no payload do modelo:

```python
# Exemplo em Pydantic
class SummarizerRequest(BaseModel):
    max_output_tokens: int = 300  # Evita que a LLM 'alucine' e gere respostas infinitas
```

### Tática 3: Throttling & Rate Limiting Decorator
Aplique rate limiting para evitar estourar as cotas de RPM (Requests Per Minute) do provedor:

```python
import time
from functools import wraps

def finops_rate_limiter(max_rpm: int = 60):
    interval = 60.0 / max_rpm
    last_call = [0.0]

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            elapsed = time.time() - last_call[0]
            if elapsed < interval:
                await asyncio.sleep(interval - elapsed)
            last_call[0] = time.time()
            return await func(*args, **kwargs)
        return wrapper
    return decorator
```

---

## 5. Auditoria e Telemetria

Todo agente DEVE registrar um objeto de telemetria após cada execução. Consulte o arquivo `template/src/core/base_agent.py` deste starter kit para ver a implementação prática da classe `FinOpsTracker`.
