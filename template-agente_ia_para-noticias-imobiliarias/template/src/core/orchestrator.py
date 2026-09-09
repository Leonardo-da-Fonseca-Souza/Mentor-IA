"""
Orquestradores Agênticos (SequentialOrchestrator & ParallelOrchestrator).
Demonstra como coordenar múltiplos agentes autônomos em pipeline ou execução concorrente.
"""

import asyncio
import logging
from typing import List, Any
from core.base_agent import BaseAgent, AgentResult

logger = logging.getLogger("MentorIA.Orchestrator")


class SequentialOrchestrator:
    """
    Orquestrador Sequencial de Agentes.
    Executa uma lista de agentes em formato 'linha de montagem' (Pipeline).
    """

    def __init__(self, name: str = "sequential_orchestrator") -> None:
        self.name = name
        self.steps: List[BaseAgent[Any, Any]] = []

    def add_step(self, agent: BaseAgent[Any, Any]) -> "SequentialOrchestrator":
        """Adiciona um agente ao pipeline sequencial."""
        self.steps.append(agent)
        return self

    async def run(self, initial_payload: Any) -> List[AgentResult[Any]]:
        """Executa a sequência de agentes repassando o estado."""
        logger.info(f"[{self.name}] Iniciando pipeline sequencial com {len(self.steps)} passos...")
        results: List[AgentResult[Any]] = []
        current_data = initial_payload

        for idx, agent in enumerate(self.steps, start=1):
            logger.info(f"[{self.name}] Passos {idx}/{len(self.steps)}: Executando {agent.agent_name}...")
            result = await agent.execute(current_data)
            results.append(result)

            if not result.success:
                logger.error(f"[{self.name}] Interrompendo pipeline no passo {idx} devido a erro: {result.error_message}")
                break

            # Se houver dados de saída, atualiza para o próximo agente
            if result.data is not None:
                current_data = result.data

        return results


class ParallelOrchestrator:
    """
    Orquestrador Paralelo de Agentes.
    Dispara múltiplos agentes simultaneamente utilizando asyncio.gather.
    """

    def __init__(self, name: str = "parallel_orchestrator") -> None:
        self.name = name
        self.agents: List[BaseAgent[Any, Any]] = []

    def add_agent(self, agent: BaseAgent[Any, Any]) -> "ParallelOrchestrator":
        """Adiciona um agente à lista de execução concorrente."""
        self.agents.append(agent)
        return self

    async def run_all(self, payload: Any) -> List[AgentResult[Any]]:
        """Executa todos os agentes cadastrados em paralelo."""
        logger.info(f"[{self.name}] Disparando {len(self.agents)} agentes em paralelo...")
        tasks = [agent.execute(payload) for agent in self.agents]
        results = await asyncio.gather(*tasks)
        return list(results)
