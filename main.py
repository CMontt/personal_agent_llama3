import os
from agent.agent import run_agent
from agent.runner import load_prompts
from config.settings import PROMPTS_DIR, PROMPTS_FINAL_DIR

PROMPTS = load_prompts(PROMPTS_DIR)
PROMPTS["final"] = load_prompts(PROMPTS_FINAL_DIR)

if __name__ == "__main__":
    while True:
        try:
            question = input("Question: ")
        except EOFError:
            os.system("clear")
            break

        answer = run_agent(question, PROMPTS)
        print(f"\n{answer}\n")
        print("-" * 200) 