import pandas as pd
import ollama
import requests
import json

with open("../data/knowledge/conceitos.json", "r", encoding = "utf-8") as conceitos:
    conhecimento_conceitos = json.load(conceitos)

with open("../data/knowledge/investimentos.json", "r", encoding = "utf-8") as investimentos:
    conhecimento_investimentos = json.load(investimentos)

with open("../data/knowledge/produtos_financeiros.json", "r", encoding = "utf-8") as produtos_financeiros:
    conhecimento_prosutos_fuinanceiros = json.load(produtos_financeiros)

with open("../data/persona/exemplos.json", "r", encoding = "utf-8") as exemplos:
    persona_exemplos = json.load(exemplos)

with open("../data/persona/perfil_conhecimento.json", "r", encoding = "utf-8") as perfil_conhecimento:
    persona_perfil_conhecimento = json.load(perfil_conhecimento)

conhecimento_transacoes = pd.read_csv("../data/knowledge/transacoes.csv")