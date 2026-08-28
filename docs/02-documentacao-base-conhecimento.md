# Base de Conhecimento
## Dados Utilizados

| Arquivo | Formato | Agente | Utilização |
|---------|---------|--------|------------|
| `produtos_financeiros.json` | JSON | FinLearn | Definir os produtos financeiros |
| `investimentos.json` | JSON | FinLearn | Definir os tipos de investimentos |
| `conceitos.json` | JSON | FinLearn | Define conceitos bancários |
| `transacoes.csv` | CSV | FinLearn | Definir as transações feitas pelo usuário |
| `exemplos.json` | JSON | Clara | Exemplos do que responder em algumas perguntas |
| `perfil_conhecimento.json` | JSON | Clara | Define o conhecimento atual do usuário |

---

## Adaptação dos Dados
Os dados presentes no arquivo `produtos_financeiros.json` foram passados para o arquivo `investimentos.json`, pois eles eram exemplos de investimentos, além disso o arquivo `perfil_investidos.json` foi renomeado para `perfil_conhecimento.json`, pois faz mais sentido ter o perfil geral de conhecimento do usuário do que saber qual é o seu perfil de investimento, já que não serão recomendados investimentos.

---

## Estratégia de Integração

### Como os dados são carregados
Na primeira versão os dados serão carregados direto no app.py.

### Como os dados são usados no prompt
Na primeira versão os dados serão passados diretamente no prompt, garantindo que o Agente tenha o melhor contexto possível.

### Exemplos de Contexto Montado

O exemplo de contexto é usado 
```
Produtos financeiros:
- nome: CDB
- categoria: Investimentos
- descrição: Sigla para Certificado de Depósito Bancário. São títulos privados representativos de depósitos a prazo feitos por pessoas físicas ou jurídicas. Podem emitir CDB os bancos comerciais, múltiplos, de investimento, de desenvolvimento e a Caixa Econômica Federal.
- fonte: Banco Central do Brasil

Investimentos:
- nome: Poupança
- risco: Baixo
- descrição: É um tipo de conta bancária que rende com o decorrer do tempo.
- fonte: Banco Central do Brasil

Conceitos:
- nome: inflação
- descrição: A inflação indica o aumento generalizado ou contínuo dos preços de uma série de categorias de bens e serviços, ela implica na diminuição do poder de compra da moeda e é medida pelos índices de preços
- fonte: Banco central do Brasil

Perfil conhecimento:
- nível geral de conhecimento: iniciante
- nível de conhecimento de investimento: iniciante
- nível de conhecimento de credito: iniciante
- nível de conhecimento de planejamento: iniciante

```