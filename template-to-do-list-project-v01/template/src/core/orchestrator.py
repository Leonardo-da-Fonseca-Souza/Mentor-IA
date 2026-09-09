"""
Supervisor Orchestrator Implementation.
Demonstrates the Supervisor-Worker pattern for routing user intentions to specialized workers.
"""

from typing import Dict
from src.core.base_agent import BaseAgent, AgentResponse


class TaskWorkerAgent(BaseAgent):
    """Worker especializado no gerenciamento e criação de tarefas."""

    def __init__(self):
        super().__init__(agent_id="task_worker", model_name="gemini-3.5-flash")

    async def _run_reasoning(self, prompt: str, **kwargs) -> str:
        # TODO: Integrar com a chamada real da API ou servidor MCP
        return f"Worker [task_worker] processou a solicitação de tarefa: '{prompt}'"


class ReportingWorkerAgent(BaseAgent):
    """Worker especializado em geração de relatórios e análises."""

    def __init__(self):
        super().__init__(agent_id="reporting_worker", model_name="gemini-3.5-pro")

    async def _run_reasoning(self, prompt: str, **kwargs) -> str:
        # TODO: Integrar com a chamada de agregação de métricas
        return f"Worker [reporting_worker] gerou o relatório para: '{prompt}'"


class SupervisorOrchestrator(BaseAgent):
    """
    Agente Supervisor responsável por classificar a intenção e delegar a execução
    para os Workers especialistas cadastrados.
    """

    def __init__(self):
        super().__init__(agent_id="supervisor_orchestrator", model_name="gemini-3.5-flash")
        self.workers: Dict[str, BaseAgent] = {
            "task": TaskWorkerAgent(),
            "reporting": ReportingWorkerAgent()
        }

    def route_intent(self, prompt: str) -> str:
        """Classificação simples de intenção baseada em palavras-chave."""
        text_lower = prompt.lower()
        if any(w in text_lower for w in ["relatório", "métrica", "resumo", "desempenho"]):
            return "reporting"
        return "task"

    async def _run_reasoning(self, prompt: str, **kwargs) -> str:
        session_id = kwargs.get("session_id", "demo-session")
        target_worker_key = self.route_intent(prompt)
        worker = self.workers.get(target_worker_key)

        if not worker:
            return "Nenhum worker adequado foi encontrado para esta solicitação."

        worker_response = await worker.execute(session_id=session_id, prompt=prompt)
        return (
            f"[Supervisor] Intenção identificada como '{target_worker_key}'.\n"
            f"[Handoff] -> Resposta do Worker: {worker_response.content}"
        )
