# 📝 Template Declarativo de Agentes (`.antigravity/agents.template.md`)

> **Instrução Educacional:** Use este arquivo como guia didático para definir novas personas agênticas no seu projeto. Copie o bloco YAML abaixo e ajuste as variáveis para criar novos agentes.

---

## Template de Agente

```yaml
# ── IDENTIFICAÇÃO DO AGENTE ─────────────────────────────
agent_id: nome_do_seu_agente           # Identificador minúsculo sem espaços (ex: search_assistant)
type: SpecializedLlmAgent              # Tipos: LlmSupervisor, SpecializedLlmAgent, TransactionalLlmAgent
model: gemini-3.5-flash               # Modelo base configurado no ecossistema
temperature: 0.1                       # 0.0 a 0.2 para tarefas determinísticas / 0.7 para criatividade

# ── LIMITES FINOPS ─────────────────────────────────────
max_tokens_per_session: 8000           # Teto preventivo de tokens por sessão de conversa
description: "Descrição sucinta da responsabilidade do agente para roteamento do supervisor."

# ── PROMPT DE SISTEMA (PERSONA & INSTRUÇÕES) ───────────
system_prompt: |
  Você é o agente especialista responsável por [DEFINIR A MISSÃO DO AGENTE].
  
  SUAS REGRAS DE EXECUÇÃO:
  1. Sempre responda em Português do Brasil com tom profissional e direto.
  2. Nunca invente dados. Caso não possua a informação, acione as ferramentas autorizadas.
  3. [ADICIONE REGRAS ESPECÍFICAS DO SEU DOMÍNIO AQUI]

# ── FERRAMENTAS AUTORIZADAS (MCP / FUNCTION TOOLS) ──────
authorized_tools:
  - minha_ferramenta_mcp_1             # Nome da função python exposta via MCP
  - minha_ferramenta_mcp_2

# ── SUB-AGENTES (APENAS PARA SUPERVISOR) ─────────────────
sub_agents: []                         # Caso seja um supervisor, liste os agent_ids dos workers
```
