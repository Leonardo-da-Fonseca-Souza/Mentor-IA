"""
🎓 Mentor-IA Starter Kit - Interactive CLI Entry Point
Execute este script para testar interativamente a orquestração agêntica e o middleware FinOps.
"""

import asyncio
import os
import sys
import uuid

# Adiciona o diretório atual ao sys.path para importações relativas limpas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.base_agent import FinOpsMetrics
from src.core.orchestrator import SupervisorOrchestrator


async def main():
    print("=" * 60)
    print("🎓 Mentor-IA Starter Kit - Engine Multi-Agente & FinOps")
    print("=" * 60)
    print("Digite 'sair' para encerrar a sessão.\n")

    orchestrator = SupervisorOrchestrator()
    session_id = str(uuid.uuid4())
    metrics = FinOpsMetrics(session_id=session_id, max_token_budget=2000)

    print(f"Sessão iniciada: {session_id}")
    print(f"Token Budget Máximo: {metrics.max_token_budget} tokens\n")

    while True:
        try:
            user_input = input("Você > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("\nEncerrando sessão do Mentor-IA. Até logo!")
                break

            print("\n🤖 [Supervisor] Processando e roteando solicitação...")
            result = await orchestrator.process_message(
                session_id=session_id,
                user_message=user_input,
                metrics=metrics
            )

            if result.get("status") == "error":
                print(f"❌ [ERRO] {result.get('message')}\n")
                if result.get("error_type") == "FINOPS_LIMIT":
                    print("Sessão interrompida preventivamente pelo Middleware FinOps.")
                    break
            else:
                print(f"✅ [{result.get('executed_by')}] Resposta: {result.get('response')}")
                print(f"📊 [FinOps Telemetria] Consumo acumulado: {metrics.total_tokens} / {metrics.max_token_budget} tokens\n")

        except KeyboardInterrupt:
            print("\nSessão encerrada.")
            break


if __name__ == "__main__":
    asyncio.run(main())
