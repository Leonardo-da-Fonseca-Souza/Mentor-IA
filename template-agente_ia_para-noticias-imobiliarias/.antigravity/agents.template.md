# 🤖 Template Declarativo de Especificação de Agentes (`.antigravity/agents.template.md`)

> **Guia Didático:** Este arquivo serve como blueprint para declarar agentes autônomos. Preencha cada bloco respeitando a tipagem estrita de entradas, saídas e ferramentas autorizadas.

---

## 1. Agente Orquestrador (`example_orchestrator`)

- **Tipo:** `SequentialAgent` | `ParallelAgent` | `LoopAgent`
- **Modelo LLM:** `gemini-2.0-flash` (Recomendado para orquestração de baixa latência)
- **Descrição:** [Explique o papel central do agente orquestrador na solução]
- **System Prompt Base:**
  > [Insira a instrução de alto nível do supervisor, definindo o fluxo mental, handoffs e tratamento de exceções]
- **Inputs (Pydantic Schema):** `OrchestratorInputSchema`
- **Outputs (Pydantic Schema):** `OrchestratorOutputSchema`
- **Ferramentas Autorizadas:** `[log_pipeline_execution, get_system_config]`
- **Regras de Roteamento:**
  - `SE` [Condição A] $\rightarrow$ [Enviar para Agente X]
  - `SE` [Condição B] $\rightarrow$ [Desviar para Fila de Revisão Humana]

---

## 2. Agente Especialista / Worker (`example_worker`)

- **Tipo:** `LlmAgent` | `ToolAgent`
- **Modelo LLM:** `gemini-2.0-flash` (ou `gemini-1.5-pro` conforme complexidade)
- **Descrição:** [Descrição da tarefa especializada executada pelo worker]
- **System Prompt Base:**
  > Você é um especialista em [Domínio da Tarefa].
  > Suas responsabilidades são:
  > 1. Receber o payload de entrada e validar os parâmetros.
  > 2. Executar a extração/análise com base em dados objetivos.
  > 3. Gerar saída estritamente em JSON compatível com o schema definido.
- **Inputs (Pydantic Schema):** `WorkerInputSchema`
- **Outputs (Pydantic Schema):** `WorkerOutputSchema`
- **Ferramentas Autorizadas:** `[fetch_mcp_tool, compute_vector_embedding]`

---

## 💡 Dicas de Engenharia de Prompts para o Template

1. **Evite Ambiguidades:** Use termos imperativos e numerados no System Prompt.
2. **Defina Restrições Negativas:** Especifique claramente o que o agente **NÃO** deve fazer (ex: "NUNCA inventar dados não presentes no texto").
3. **Structured Output Mandatory:** Inclua sempre no prompt a instrução de saída JSON pura sem marcações markdown redundantes fora do bloco JSON.
