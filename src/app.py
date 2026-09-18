import streamlit as st
import requests
import json

MODELO_LLM = "qwen2.5"
URL_LLM = "http://localhost:11434/api/generate"

with open("./data/knowledge/conceitos.json", "r", encoding = "utf-8") as conceitos:
    conhecimento_conceitos = json.load(conceitos)

with open("./data/knowledge/investimentos.json", "r", encoding = "utf-8") as investimentos:
    conhecimento_investimentos = json.load(investimentos)

with open("./data/persona/perfil_conhecimento.json", "r", encoding = "utf-8") as perfil_conhecimento:
    persona_perfil_conhecimento = json.load(perfil_conhecimento)

with open("./data/knowledge/produtos_financeiros.json", "r", encoding = "utf-8") as produtos_financeiros:
    conhecimento_produtos_financeiros = json.load(produtos_financeiros)

PERSONA_PERFIL_CONHECIMENTO_CONHECIMENTOS = persona_perfil_conhecimento["conhecimentos"]
CONHECIMENTO = f"""
    CONHECIMENTO SOBRE PRODUTOS FINANCEIROS: {conhecimento_produtos_financeiros}

    CONHECIMENTO SOBRE CONCEITOS FINANCEIROS: {conhecimento_conceitos}

    CONHECIMENTO SOBRE INVESTIMENTOS: {conhecimento_investimentos}
"""

PROMPT_SISTEMA = """
    Você é o FinLearn um sistema de educação financeira.

    Seu objetivo é ajudar o usuário a compreender assuntos de economia e finanças de maneira clara, didática e responsável.

    Regras:
    - Explique conceitos financeiros com linguagem acessível.
    - Diferencie fatos, estimativas e opiniões.
    - Não transforme explicações, comparações ou simulações em recomendações personalizadas de investimentos.
    - Quando não souber responder com segurança, informe claramente a sua limitação e, quando apropriado, indique fontes oficiais como o Banco Central do Brasil.
    - NUNCA recomende investimentos específicos. Explique seu funcionamento, características, riscos e limitações de maneira educacional.
"""

CONHECIMENTO_USUARIO = f"""
    CONHECIMENTO DO CLIENTE EM PLANEJAMENTO FINANCEIRO: {PERSONA_PERFIL_CONHECIMENTO_CONHECIMENTOS["planejamento"]}
    CONHECIMENTO DO CLIENTE EM INVESTIMENTOS: {PERSONA_PERFIL_CONHECIMENTO_CONHECIMENTOS["investimento"]}
    CONHECIMENTO DO CLIENTE EM CREDITO: {PERSONA_PERFIL_CONHECIMENTO_CONHECIMENTOS["credito"]}
"""

def perguntar(mensagem):
    prompt = f"""
        {PROMPT_SISTEMA}
        
        Conhecimento do Usuário: {CONHECIMENTO_USUARIO}

        Conhcecimento Necessário: {CONHECIMENTO}

        Pergunta: {mensagem}
    """
    response = requests.post(URL_LLM, json = {"model": MODELO_LLM, "prompt": prompt, "stream": False})
    return response.json()["response"]

st.title("FinLearn, a sua plataforma de educação financeira.")

if pergunta := st.chat_input("Qual é a sua dúvida sobre finanças pessoais"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))