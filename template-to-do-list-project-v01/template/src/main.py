"""
Interactive CLI Script demonstrating the Supervisor-Worker Agent execution.
Run: python src/main.py
"""

import asyncio
import logging
from src.core.orchestrator import SupervisorOrchestrator

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")


async def main():
    print("=" * 65)
    print("🎓 Mentor-IA Starter Kit: Supervisor-Worker Execution Demo")
    print("=" * 65)

    orchestrator = SupervisorOrchestrator()
    session_id = "session-demo-101"

    test_prompts = [
        "Criar uma tarefa urgente para revisar o relatório financeiro contato@empresa.com",
        "Gerar um relatório detalhado de produtividade do time esta semana"
    ]

    for idx, prompt in enumerate(test_prompts, 1):
        print(f"\n--- Exemplo {idx} ---")
        print(f"Entrada do Usuário: '{prompt}'")
        
        response = await orchestrator.execute(session_id=session_id, prompt=prompt, session_id_arg=session_id)
        
        print("\nResultado:")
        print(response.content)
        print("-" * 65)


if __name__ == "__main__":
    asyncio.run(main())
