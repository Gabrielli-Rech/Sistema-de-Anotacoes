# 🗒️ Sistema de Anotações

Bem-vindo ao **Sistema de Anotações**, uma aplicação web simples desenvolvida com Python e Flask que permite aos usuários criar, visualizar e excluir anotações de forma prática e eficiente.

---

## 🔧 Funcionalidades

- **Criar Anotações**: Adicione novas anotações com título e conteúdo.
- **Visualizar Anotações**: Consulte todas as anotações cadastradas.
- **Excluir Anotações**: Remova anotações que não são mais necessárias.
- **Armazenamento Local**: As anotações são salvas em um banco de dados SQLite para persistência de dados.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para desenvolvimento da aplicação.
- **SQLite**: Banco de dados para armazenamento das anotações.
- **HTML/CSS/JavaScript**: Tecnologias utilizadas para construção da interface do usuário.

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/Gabrielli-Rech/Sistema-de-Anotacoes.git
2. Navegue até a pasta do projeto:
  cd Sistema-de-Anotacoes

3. Instale as dependências:
  pip install -r requirements.txt

4. Execute o servidor Flask:
  python app.py

5. Abra o navegador e acesse:
  http://127.0.0.1:5000


## 📂 Estrutura do Projeto

Sistema-de-Anotacoes/<br>
├── app.py                  # Script principal da aplicação Flask<br>
├── notes.db                # Banco de dados SQLite<br>
├── static/                 # Arquivos estáticos (CSS, JavaScript)<br>
├── templates/              # Templates HTML<br>
└── README.md               # Este arquivo<br>
