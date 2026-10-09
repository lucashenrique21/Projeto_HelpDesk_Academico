# HelpDesk Acadêmico — Sistema de Gerenciamento de Chamados

Projeto acadêmico para demonstrar aplicação web, banco de dados relacional e operações CRUD.

## Funcionalidades
- Listar chamados e visualizar contadores por status.
- Criar, consultar, editar e excluir chamados.
- Cadastrar usuários solicitantes e categorias.
- Relacionar cada chamado a um usuário e uma categoria.
- Definir prioridade e status do chamado.

## Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML, CSS e Bootstrap via CDN
- PlantUML para os diagramas

## Como executar
1. Instale Python 3.10 ou superior.
2. Extraia a pasta do projeto.
3. Abra um terminal nessa pasta.
4. Crie e ative um ambiente virtual (opcional, mas recomendado):

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

5. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
6. Execute:
   ```powershell
   python app.py
   ```
7. Abra `http://127.0.0.1:5000` no navegador.

O banco `helpdesk.db` é criado automaticamente na primeira execução.
