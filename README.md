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

## Publicar no GitHub
Crie um repositório vazio no GitHub e execute dentro da pasta:
```bash
git init
git add .
git commit -m "Projeto inicial HelpDesk"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
git push -u origin main
```
Depois, nas configurações do repositório, adicione o tutor e `fernandonakagawa-unifil` como colaboradores conforme as instruções da disciplina.

## Observações acadêmicas
- Substitua os dados da capa e os textos de documentação pelos dados reais do aluno/dupla.
- Revise e teste o sistema antes de entregar.
- Os usuários de exemplo são fictícios.
- Para uso real, seriam necessários autenticação, autorização, proteção CSRF, validação mais completa e configuração segura.
