"""
Script Principal / Ponto de Entrada CLI (`main.py`).
Demonstra a execução ponta a ponta de um pipeline agêntico multi-estágio.
"""

import asyncio
import logging
import sys
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List

# Ajusta sys.path para importar o pacote core localmente
sys.path.insert(0, str(Path(__file__).parent))

from core.base_agent import BaseAgent
from core.orchestrator import SequentialOrchestrator

# Configuração de Logging Educacional
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("MentorIA.Main")


# ==============================================================================
# 1. Definição dos Schemas de Dados (Pydantic v2)
# ==============================================================================

class InputDocument(BaseModel):
    title: str = Field(..., min_length=5)
    raw_text: str = Field(..., min_length=20)
    source_name: str


class ScoredDocument(BaseModel):
    input_doc: InputDocument
    score: int = Field(..., ge=0, le=100)
    category: str
    is_approved: bool


class FinalSummary(BaseModel):
    scored_doc: ScoredDocument
    summary_paragraph: str
    words_count: int


# ==============================================================================
# 2. Definição dos Agentes Especializados (Herdeiros de BaseAgent)
# ==============================================================================

class ClassificationAgent(BaseAgent[InputDocument, ScoredDocument]):
    """Agente especialista em classificação e scoring de relevância."""

    def __init__(self):
        super().__init__(agent_name="classifier_agent", model_name="gemini-2.0-flash")

    async def _execute_internal(self, payload: InputDocument) -> ScoredDocument:
        # TODO(Student): Substituir pela chamada real da LLM usando a API Gemini ou OpenAI
        await asyncio.sleep(0.05)  # Simula latência de chamada de rede

        text_lower = payload.raw_text.lower()
        score = 85 if "tecnologia" in text_lower or "ia" in text_lower or "inovação" in text_lower else 45
        category = "Inovação Tech" if score >= 70 else "Geral"

        return ScoredDocument(
            input_doc=payload,
            score=score,
            category=category,
            is_approved=score >= 70
        )


class SummarizationAgent(BaseAgent[ScoredDocument, FinalSummary]):
    """Agente especialista em síntese em linguagem natural."""

    def __init__(self):
        super().__init__(agent_name="summarizer_agent", model_name="gemini-1.5-pro")

    async def _execute_internal(self, payload: ScoredDocument) -> FinalSummary:
        # TODO(Student): Implementar a prompt de síntese customizada
        await asyncio.sleep(0.08)

        text = payload.input_doc.raw_text
        summary = f"O artigo da fonte '{payload.input_doc.source_name}' destaca que: {text[:120]}..."
        word_count = len(summary.split())

        return FinalSummary(
            scored_doc=payload,
            summary_paragraph=summary,
            words_count=word_count
        )


# ==============================================================================
# 3. Execução Principal (CLI)
# ==============================================================================

async def main() -> None:
    logger.info("==========================================================")
    logger.info("🎓 Iniciando Demonstração do Starter Kit Agêntico Mentor-IA")
    logger.info("==========================================================")

    # Documento de Exemplo
    doc = InputDocument(
        title="Avanços em Orquestração Agêntica Corporativa com IA",
        raw_text="Adoção de arquiteturas multi-agente impulsiona a eficiência operacional reduzindo o tempo de triagem de dados complexos através do uso de ferramentas MCP e validação estrita.",
        source_name="Tech Innovation Weekly"
    )

    # Instancia os agentes e o orquestrador sequencial
    classifier = ClassificationAgent()
    summarizer = SummarizationAgent()

    orchestrator = SequentialOrchestrator(name="main_news_pipeline")
    orchestrator.add_step(classifier).add_step(summarizer)

    # Executa o pipeline
    results = await orchestrator.run(doc)

    # Exibe os resultados e telemetria FinOps
    logger.info("----------------------------------------------------------")
    logger.info("📊 RESUMO DE EXECUÇÃO E TELEMETRIA FINOPS")
    logger.info("----------------------------------------------------------")

    total_cost = 0.0
    for idx, res in enumerate(results, start=1):
        if res.success:
            total_cost += res.telemetry.estimated_cost_usd
            logger.info(
                f"Passo {idx} [{res.telemetry.agent_name}]: Status=SUCESSO | "
                f"Latência={res.telemetry.latency_ms}ms | Custo=${res.telemetry.estimated_cost_usd:.6f}"
            )
            if res.data and hasattr(res.data, "summary_paragraph"):
                logger.info(f"📝 Resultado do Resumo: {res.data.summary_paragraph}")
        else:
            logger.error(f"Passo {idx}: Erro={res.error_message}")

    logger.info(f"💰 Custo Total Estimado do Ciclo: ${total_cost:.6f} USD")
    logger.info("==========================================================")


if __name__ == "__main__":
    asyncio.run(main())
