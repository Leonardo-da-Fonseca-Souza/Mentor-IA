# 🛠️ Regras de Engenharia do Starter Kit (`.antigravity/rules.starter.md`)

Diretrizes de código, segurança e arquitetura que **TODOS** os copilotos de IA e desenvolvedores devem seguir ao trabalhar neste repositório.

---

## 1. Regras de Código Python

1. **Python 3.11+ & Typing Estrito:** NUNCA escreva funções sem type annotations para argumentos e retorno.
2. **Validação Pydantic v2 Mandatory:** Utilize `pydantic.BaseModel` com `ConfigDict(frozen=True)` para garantir a imutabilidade dos objetos de domínio.
3. **Async First:** Operações de I/O (rede, banco de dados, arquivos) devem ser implementadas como métodos assíncronos (`async def`).

---

## 2. Regras de Governança & FinOps

1. **Registro de Telemetria:** Toda chamada de agente DEVE utilizar a classe `FinOpsTracker` para registrar tokens de entrada, saída e latência.
2. **Tratamento de Exceções Agênticas:** NUNCA engula exceções silenciosamente. Encapsule falhas de agentes em objetos de retorno contendo `success: bool` e `error_message: Optional[str]`.
3. **Sem Credenciais Hardcodeadas:** LER SEMPRE segredos (`API_KEY`, `DATABASE_URL`) das variáveis de ambiente usando `os.environ` ou `pydantic-settings`.

---

## 3. Padrão de Extensão de Código (`TODO` Markers)

Ao expandir o boilerplate, adicione anotações didáticas no padrão:

```python
# TODO(Student): Implementar a chamada ao Servidor MCP do seu domínio aqui
# Dica: Use o decorador @retry_on_exception para resiliência de rede
```
