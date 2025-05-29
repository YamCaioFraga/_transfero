# 🎬 Site de Filmes

Um site de filmes desenvolvido com **Python**, **Django**, **HTML** e **CSS**, que permite aos usuários explorar, visualizar detalhes e avaliar filmes.

## 🎯 Finalidade do Projeto

Este projeto foi criado com o objetivo de praticar e demonstrar habilidades em desenvolvimento web utilizando o framework **Django**. Ele serve como base para estudantes e desenvolvedores que queiram aprender mais sobre:

- Criação de aplicações web com Django
- Integração de templates HTML com dados dinâmicos
- Uso de banco de dados com ORM (Object-Relational Mapping)
- Estruturação de projeto com boas práticas

Ideal como projeto de portfólio, estudo acadêmico ou ponto de partida para projetos maiores.

## 🚀 Tecnologias Utilizadas

- **Python 
- **Django 
- **HTML5**
- **CSS3**
- **SQLite** (banco de dados padrão do Django)

## 📌 Funcionalidades

- Listagem de filmes com pôster e sinopse.
- Página de detalhes com informações completas sobre o filme.
- Sistema de avaliação com estrelas (básico).
- Admin do Django para gerenciamento de filmes.
- Layout responsivo com HTML e CSS.

## 📷 Capturas de Tela
- Página Home!

  
![image](https://github.com/user-attachments/assets/98cb6d0b-045b-4812-a6f9-06e62ccb97d2)


## 🚀 Como rodar o projeto localmente (Django)

### ✅ Pré-requisitos

Antes de começar, você precisa ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/)
- (Opcional) [Virtualenv](https://virtualenv.pypa.io/en/latest/) ou [venv](https://docs.python.org/3/library/venv.html)

---

### 📦 Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

🧪 Crie e ative um ambiente virtual
Com venv:

bash
Copiar
Editar
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

📥 Instale as dependências

bash
Copiar
Editar
pip install -r requirements.txt

⚙️ Configure o ambiente
Crie um arquivo .env na raiz do projeto (caso esteja usando python-decouple, django-environ ou similar). Exemplo básico:

env
Copiar
Editar
DEBUG=True
SECRET_KEY=sua_chave_secreta
ALLOWED_HOSTS=localhost,127.0.0.1

🧱 Execute as migrações
bash
Copiar
Editar
python manage.py migrate

📂 (Opcional) Crie um superusuário para acessar o admin
bash
Copiar
Editar
python manage.py createsuperuser

▶️ Rode o servidor local
bash
Copiar
Editar
python manage.py runserver
A aplicação estará disponível em:

📍 http://127.0.0.1:8000
