# 🤖CHATBOT com API Gemini do Google em Python

<div align="center">
  <img height="180em" src="https://raw.githubusercontent.com/KevinSoffa/API-previdencia-KevinSoffa/refs/heads/develop/img/Kevin%20Soffa%20(2).png"/>
</div>


## Sumário 🔄

1. [Descrição](#descrição-)
2. [Tecnologias](#tecnologias)
3. [Desenvolvimento](#desenvolvimento-)
4. [Configuração do Ambiente](#configuração-do-ambiente)


---
## Descrição 📝
Este projeto é um chatbot baseado na API Gemini do Google, desenvolvido em Python. O chatbot é capaz de responder a perguntas, realizar conversas contextuais e interagir de maneira inteligente com os usuários.

## Tecnologias
<div align="left">
    <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo"/>
    <img src="https://logowik.com/content/uploads/images/google-ai-gemini91216.logowik.com.webp" height="40" alt="Google Logo"/>
</div>

## Desenvolvimento 👨‍💻


### Diretório 🗂️
```plaintext
📦 chatbot_api
 ┣ 📂 controller     # Controladores das rotas
 ┣ 📂 models         # Definições dos modelos e entidades
 ┣ 📂 repository     # Comunicação com o banco de dados (se aplicável)
 ┣ 📂 service        # Lógica de negócios
 ┣ 📂 test           # Testes automatizados
 ┣ 📜 .env           # Configurações do ambiente (API Key, etc.)
 ┣ 📜 .gitignore     # Arquivos ignorados pelo Git
 ┣ 📜 Dockerfile     # Configuração para container Docker
 ┣ 📜 main.py        # Ponto de entrada da aplicação
 ┣ 📜 pytest.ini     # Configurações do Pytest
 ┗ 📜 requirements.txt  # Dependências do projeto
```



### 🔧 Configuração do Ambiente 
#### Instalando bibliotecas necessárias
- 💻 Crie um ambiente virtual
```bash
python -m venv {nome-da-sua-venv}
```

- ▶️ Ative o ambiente virtual
```bash
{nome-da-sua-venv}\Scripts\activate
```

- 🏗️ Instalar todas as bibliotecas nessárias
```bash
pip install -r requirements
```

Antes de executar o projeto, configure as seguintes variáveis de ambiente no seu arquivo `.env` ou diretamente no sistema (toda conexão de banco de dados é feita aqui):

| Variável              | Descrição                                           | tipo        |
|-----------------------|-----------------------------------------------------|-------------|
| API_KEY               |Sua chave de acesso a API                            |  str        |




### 📂 Exemplo de arquivo `.env`
```plaintext
##################################################
### ACESSO A API
##################################################
API_KEY=
```

#### ⚡ Para iniciar  o Chat
```bash
python .\main.py
```

#### Link para documentação da API
```bash
https://aistudio.google.com/prompts/new_chat
```
