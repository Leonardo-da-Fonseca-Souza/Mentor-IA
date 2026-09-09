"""
🎓 Mentor-IA Starter Kit - Multi-Agent Orchestrator
Exemplo didático de orquestrador hierárquico (Supervisor -> Worker Agents).
"""

import asyncio
from typing import Dict, Any
from src.core.base_agent import BaseAgent, FinOpsMetrics, handle_agent_errors


class SpecializedWorkerAgent(BaseAgent):
    """
    Worker Agent de domínio específico.
    """

    def __init__(self, domain_name: str):
        super().__init__(
            agent_name=f"{domain_name}_worker",
            role_description=f"Especialista no domínio de {domain_name}."
        )
        self.domain_name = domain_name

    @handle_agent_errors
    async def process_message(
        self,
        session_id: str,
        user_message: str,
        metrics: FinOpsMetrics
    ) -> Dict[str, Any]:
        # Simula processamento de LLM / Chamada a ferramenta MCP
        await asyncio.sleep(0.05)
        
        # Registra consumo de tokens (Exemplo: 100 input, 50 output)
        metrics.add_usage(input_t=100, output_t=50)

        return {
            "status": "success",
            "executed_by": self.agent_name,
            "response": f"Processado pelo especialista em {self.domain_name}: '{user_message}'",
            "tokens_consumed": metrics.total_tokens
        }


class SupervisorOrchestrator(BaseAgent):
    """
    Supervisor Agent que classifica intenções e delega o fluxo para Workers.
    """

    def __init__(self):
        super().__init__(
            agent_name="supervisor_router",
            role_description="Supervisor responsável pelo roteamento de intenções."
        )
        # Registra workers disponíveis
        self.workers: Dict[str, BaseAgent] = {
            "search": SpecializedWorkerAgent(domain_name="Busca e Consulta"),
            "feedback": SpecializedWorkerAgent(domain_name="Feedback e Registros")
        }

    def route_intent(self, message: str) -> str:
        """
        Classificador básico de intenção.
        TODO: Em produção, substitua por uma chamada rápida de classificação do Gemini 3.5 Flash.
        """
        msg = message.lower()
        if any(w in msg for w in ["nota", "avaliação", "feedback"]):
            return "feedback"
        return "search"

    @handle_agent_errors
    async def process_message(
        self,
        session_id: str,
        user_message: str,
        metrics: FinOpsMetrics
    ) -> Dict[str, Any]:
        # 1. Roteamento de intenção
        intent = self.route_intent(user_message)
        worker = self.workers.get(intent, self.workers["search"])

        # 2. Registra uso do próprio supervisor (Ex: 50 input tokens)
        metrics.add_usage(input_t=50, output_t=10)

        # 3. Delegamento / Handoff para o worker
        result = await worker.process_message(session_id, user_message, metrics)
        result["routed_intent"] = intent
        return result
