"""
Pacote Core do Template Mentor-IA.
Contém a classe abstrata BaseAgent, rastreador FinOps e Orquestradores.
"""

from core.base_agent import BaseAgent, FinOpsTracker, AgentResult
from core.orchestrator import SequentialOrchestrator, ParallelOrchestrator

__all__ = [
    "BaseAgent",
    "FinOpsTracker",
    "AgentResult",
    "SequentialOrchestrator",
    "ParallelOrchestrator",
]
