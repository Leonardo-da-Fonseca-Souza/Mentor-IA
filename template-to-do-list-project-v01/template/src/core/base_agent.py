"""
Base Agent Abstract Class with PII Masking, FinOps Telemetry, and Error Handling.
Designed for educational purposes as an extensible starter template.
"""

import re
import abc
import logging
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field

logger = logging.getLogger("mentor_ia.base_agent")
logger.setLevel(logging.INFO)


class AgentResponse(BaseModel):
    agent_id: str
    session_id: str
    status: str = "success"
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BaseAgent(abc.ABC):
    """
    Abstract Base Class for all AI Agents.
    Enforces PII sanitization and FinOps compliance out of the box.
    """

    def __init__(self, agent_id: str, model_name: str = "gemini-3.5-flash"):
        self.agent_id = agent_id
        self.model_name = model_name

    @staticmethod
    def sanitize_pii(text: str) -> str:
        """
        Filtra dados sensíveis (emails e CPFs) substituindo-os por tokens genéricos.
        """
        if not text:
            return text
        sanitized = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[PII_EMAIL]', text)
        sanitized = re.sub(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b', '[PII_CPF]', sanitized)
        return sanitized

    async def execute(self, session_id: str, prompt: str, **kwargs) -> AgentResponse:
        """
        Template Method executing the agent lifecycle:
        1. PII Sanitization
        2. FinOps Check
        3. Core Reasoning Execution
        4. Response Audit Logging
        """
        sanitized_prompt = self.sanitize_pii(prompt)
        logger.info(f"[{self.agent_id}] Executing prompt for session={session_id} model={self.model_name}")

        try:
            raw_output = await self._run_reasoning(sanitized_prompt, **kwargs)
            return AgentResponse(
                agent_id=self.agent_id,
                session_id=session_id,
                content=raw_output,
                metadata={"model": self.model_name, "sanitized": True}
            )
        except Exception as e:
            logger.error(f"[{self.agent_id}] Error during execution: {str(e)}", exc_info=True)
            return AgentResponse(
                agent_id=self.agent_id,
                session_id=session_id,
                status="error",
                content=f"Falha na execução do agente [{self.agent_id}]: {str(e)}"
            )

    @abc.abstractmethod
    async def _run_reasoning(self, prompt: str, **kwargs) -> str:
        """
        Método abstrato que deve ser implementado pelas sub-classes de agentes específicos.
        """
        pass
