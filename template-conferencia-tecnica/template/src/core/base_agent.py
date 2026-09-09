"""
🎓 Mentor-IA Starter Kit - Base Agent & FinOps Middleware
Contém a classe base abstrata para agentes com tipagem Pydantic v2 e rastreamento FinOps.
"""

from abc import ABC, abstractmethod
import asyncio
import functools
import logging
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, ConfigDict

logger = logging.getLogger("mentor_ia.base_agent")


class FinOpsBudgetExceededException(Exception):
    """Exceção lançada quando a sessão excede o orçamento de tokens."""
    pass


class FinOpsMetrics(BaseModel):
    """Modelo Pydantic v2 para telemetria de consumo de tokens."""
    model_config = ConfigDict(strict=True)

    session_id: str
    input_tokens: int = Field(default=0, ge=0)
    output_tokens: int = Field(default=0, ge=0)
    total_tokens: int = Field(default=0, ge=0)
    max_token_budget: int = Field(default=8000, ge=100)

    def add_usage(self, input_t: int, output_t: int):
        new_total = self.total_tokens + input_t + output_t
        if new_total > self.max_token_budget:
            raise FinOpsBudgetExceededException(
                f"Budget FinOps estourado! Consumo atual: {new_total} tokens (Limite: {self.max_token_budget})"
            )
        self.input_tokens += input_t
        self.output_tokens += output_t
        self.total_tokens = new_total


def handle_agent_errors(func):
    """Decorator didático para tratamento gracioso de exceções agênticas."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except FinOpsBudgetExceededException as fe:
            logger.error(f"[FINOPS ERROR] {str(fe)}")
            return {"status": "error", "error_type": "FINOPS_LIMIT", "message": str(fe)}
        except Exception as e:
            logger.error(f"[AGENT ERROR] Falha inesperada: {str(e)}")
            return {"status": "error", "error_type": "INTERNAL_ERROR", "message": "Ocorreu um erro ao processar sua solicitação."}
    return wrapper


class BaseAgent(ABC):
    """
    Classe base abstrata educacional para todos os agentes do sistema.
    
    Por que usar uma classe base abstrata?
    - Garante uma interface padronizada (`process_message`).
    - Centraliza a lógica de observabilidade e contagem de tokens.
    """

    def __init__(self, agent_name: str, role_description: str):
        self.agent_name = agent_name
        self.role_description = role_description

    @abstractmethod
    @handle_agent_errors
    async def process_message(
        self,
        session_id: str,
        user_message: str,
        metrics: FinOpsMetrics
    ) -> Dict[str, Any]:
        """
        Método abstrato que todo agente concreto deve implementar.
        """
        pass
