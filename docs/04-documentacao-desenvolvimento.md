# Passo a Passo de Execução

## Setup do Ollama

```
# Instale o Ollama (https://ollama.com/download)

# Baixe um modelo leve:
ollama pull qwen2.5

# Teste se funciona:
ollama run qwen2.5 "Oi."
```
## Código Completo
Para a primeira versão todo o código estará no arquivo app.py

## Como Executar
```
# Instale as dependencias
pip install streamlit pandas requests json ollama

# Certifique-se de que o Ollama já está iniciado
ollama serve

# Rodar a aplicação
streamlit run ./src/app.py
```

## Evidencia de Execução