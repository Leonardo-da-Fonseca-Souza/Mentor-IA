"""
Classe Base Abstrata para Agentes Autônomos (BaseAgent).
Fornece infraestrutura pronta de FinOps, resiliência a erros e tipagem estrita.
"""

from abc import ABC, abstractmethod
import time
import logging
from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel, Field, ConfigDict

logger = logging.getLogger("MentorIA.BaseAgent")

InputT = TypeVar("InputT", bound=BaseModel)
OutputT = TypeVar("OutputT", bound=BaseModel)


class FinOpsTracker(BaseModel):
    """Objeto de telemetria e rastreamento de custos por execução agêntica."""
    agent_name: str
    model_name: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    latency_ms: int = 0
    estimated_cost_usd: float = 0.0


class AgentResult(BaseModel, Generic[OutputT]):
    """Container genérico padronizado para o retorno de qualquer agente."""
    success: bool
    data: Optional[OutputT] = None
    error_message: Optional[str] = None
    telemetry: FinOpsTracker


class BaseAgent(ABC, Generic[InputT, OutputT]):
    """
    Classe base educacional para agentes autônomos.
    
    Toda subclasse deve implementar o método abstrato `_execute_internal(self, payload: InputT) -> OutputT`.
    A classe base gerencia automaticamente:
    - Medição de tempo e latência
    - Captura e tratamento de exceções
    - Registro de telemetria FinOps
    """

    def __init__(self, agent_name: str, model_name: str = "gemini-2.0-flash") -> None:
        self.agent_name = agent_name
        self.model_name = model_name

    async def execute(self, payload: InputT) -> AgentResult[OutputT]:
        """Ponto de entrada público para execução do agente com governança acoplada."""
        start_time = time.time()
        logger.info(f"[{self.agent_name}] Iniciando execução com modelo '{self.model_name}'...")

        try:
            # Executa a lógica de negócio implementada pela subclasse
            output_data = await self._execute_internal(payload)

            latency_ms = int((time.time() - start_time) * 1000)
            telemetry = self._calculate_finops(prompt_tokens=400, completion_tokens=80, latency_ms=latency_ms)

            logger.info(f"[{self.agent_name}] Execução concluída com sucesso em {latency_ms}ms.")
            return AgentResult[OutputT](
                success=True,
                data=output_data,
                telemetry=telemetry
            )

        except Exception as exc:
            latency_ms = int((time.time() - start_time) * 1000)
            logger.error(f"[{self.agent_name}] Falha durante execução: {str(exc)}", exc_info=True)
            telemetry = FinOpsTracker(agent_name=self.agent_name, model_name=self.model_name, latency_ms=latency_ms)
            return AgentResult[OutputT](
                success=False,
                error_message=str(exc),
                telemetry=telemetry
            )

    @abstractmethod
    async def _execute_internal(self, payload: InputT) -> OutputT:
        """
        Método abstrato que contém a regra de negócio do agente.
        
        TODO(Student): Implemente a lógica específica do seu agente aqui!
        Exemplo: Chamada à API da LLM, consulta MCP ou processamento de dados.
        """
        pass

    def _calculate_finops(self, prompt_tokens: int, completion_tokens: int, latency_ms: int) -> FinOpsTracker:
        """Calcula o custo estimado em dólares com base na precificação do modelo."""
        # Tarifas aproximadas por 1M tokens ($0.10 input, $0.40 output)
        cost_input = (prompt_tokens / 1_000_000) * 0.10
        cost_output = (completion_tokens / 1_000_000) * 0.40
        total_cost = round(cost_input + cost_output, 6)

        return FinOpsTracker(
            agent_name=self.agent_name,
            model_name=self.model_name,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            latency_ms=latency_ms,
            estimated_cost_usd=total_cost
        )
