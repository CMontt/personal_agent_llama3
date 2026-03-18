import streamlit as st
from agent.agent import run_agent
from agent.runner import load_prompts
from config.settings import PROMPTS_DIR, PROMPTS_FINAL_DIR

PROMPTS = load_prompts(PROMPTS_DIR)
PROMPTS["final"] = load_prompts(PROMPTS_FINAL_DIR)

st.title("Meu Assistente Pessoal LLM")

# cria o form
my_form = st.form(key="my_form")

# adiciona os elementos ao form
message = my_form.text_input("O que você quer perguntar?", placeholder="")
submit = my_form.form_submit_button("Enviar")

# verifica o submit
if submit:
    st.write("Você enviou:", message)
    response = run_agent(message, PROMPTS)
    # Usa markdown para preservar quebras de linha
    st.markdown(response.replace("\n", "  \n"))