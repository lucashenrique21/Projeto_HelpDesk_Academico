# DOCUMENTAÇÃO DO PROJETO — HELP DESK ACADÊMICO

> Modelo inicial. Substitua os campos entre colchetes e adapte o texto após testar o sistema.

## Capa
**[NOME DA INSTITUIÇÃO]**  
**[NOME DO CURSO]**

**[NOME DO ALUNO 1]**  
**[NOME DO ALUNO 2, SE HOUVER]**

**HELP DESK ACADÊMICO: SISTEMA DE GERENCIAMENTO DE CHAMADOS DE TI**

[CIDADE]  
2026

## Sumário
1. Introdução  
2. Desenvolvimento  
   2.1 Tecnologias utilizadas  
   2.2 Requisitos funcionais e não funcionais  
   2.3 Casos de uso  
   2.4 Modelo de dados (DER)  
   2.5 Diagrama de atividades  
   2.6 Diagrama de classes  
   2.7 Diagramas de sequência  
3. Conclusão  
4. Referências  

## 1. Introdução
Este projeto apresenta o desenvolvimento de um sistema web de gerenciamento de chamados de Tecnologia da Informação, denominado HelpDesk Acadêmico. O objetivo é organizar solicitações de suporte, permitindo cadastrar chamados, consultar seus dados, alterar prioridade e status e excluir registros quando necessário. Cada chamado é associado a um solicitante e a uma categoria.

A aplicação foi desenvolvida em Python com o framework Flask. A persistência dos dados é realizada em um banco de dados relacional SQLite, acessado por meio do Flask-SQLAlchemy. A interface utiliza HTML, CSS e Bootstrap. O código-fonte e as instruções de execução são disponibilizados em um repositório GitHub.

## 2. Desenvolvimento

### 2.1 Tecnologias utilizadas
- **Python:** linguagem usada na lógica da aplicação.
- **Flask:** framework responsável pelas rotas HTTP e integração entre interface e lógica.
- **SQLite:** banco relacional que armazena usuários, categorias e chamados.
- **Flask-SQLAlchemy:** mapeamento entre classes Python e tabelas do banco.
- **HTML, CSS e Bootstrap:** construção e apresentação da interface.
- **Git e GitHub:** controle de versão e compartilhamento do projeto.
- **PlantUML:** descrição e geração dos diagramas UML.

### 2.2 Requisitos funcionais
- **RF01:** O sistema deve permitir cadastrar um chamado com título, descrição, solicitante, categoria, prioridade e status.
- **RF02:** O sistema deve listar os chamados cadastrados.
- **RF03:** O sistema deve permitir consultar os dados de cada chamado pela listagem.
- **RF04:** O sistema deve permitir editar os dados de um chamado.
- **RF05:** O sistema deve permitir excluir um chamado mediante confirmação.
- **RF06:** O sistema deve permitir cadastrar usuários solicitantes.
- **RF07:** O sistema deve permitir cadastrar categorias.
- **RF08:** O sistema deve permitir visualizar totais de chamados por status.
- **RF09:** O sistema deve impedir a exclusão de usuários ou categorias vinculados a chamados.

### 2.2.1 Requisitos não funcionais
- **RNF01:** A aplicação deve ser acessível por navegador web.
- **RNF02:** Os dados devem ser persistidos em banco de dados relacional SQLite.
- **RNF03:** A interface deve ser responsiva para diferentes tamanhos de tela.
- **RNF04:** Campos obrigatórios devem ser validados antes do cadastro.
- **RNF05:** O código deve ser organizado em arquivos e acompanhado de instruções de instalação.
- **RNF06:** O projeto deve ser versionado em repositório GitHub com acesso concedido ao tutor e a `fernandonakagawa-unifil`.

### 2.3 Casos de uso
Atores:
- **Solicitante/Operador:** representa a pessoa que utiliza o sistema para registrar e acompanhar chamados.
- **Administrador:** mantém cadastros auxiliares de usuários e categorias.

Casos de uso principais (5):
1. UC01 — Cadastrar chamado.
2. UC02 — Consultar/listar chamados.
3. UC03 — Atualizar chamado.
4. UC04 — Excluir chamado.
5. UC05 — Gerenciar usuários e categorias.

### 2.4 Modelo de dados (DER)
O banco possui três entidades:
- **Usuario** (id, nome, email)
- **Categoria** (id, nome)
- **Chamado** (id, titulo, descricao, prioridade, status, criado_em, usuario_id, categoria_id)

Relacionamentos:
- Um usuário pode estar associado a vários chamados; cada chamado possui um solicitante.
- Uma categoria pode classificar vários chamados; cada chamado pertence a uma categoria.

### 2.5 Diagrama de atividades
O fluxo de cadastro de chamado começa quando o usuário seleciona “Novo chamado”, preenche os campos e envia o formulário. O sistema valida os campos obrigatórios. Se os dados forem válidos, grava o chamado no banco e exibe uma mensagem de sucesso; caso contrário, informa o erro e mantém o formulário disponível para correção.

### 2.6 Diagrama de classes
As classes de domínio são Usuario, Categoria e Chamado. Usuario e Categoria possuem relacionamento um-para-muitos com Chamado. A classe Chamado contém as informações da solicitação e chaves estrangeiras para Usuario e Categoria.

### 2.7 Diagramas de sequência
Os arquivos PlantUML correspondentes aos cinco casos de uso estão na pasta `diagramas`. Eles representam as interações entre ator, interface/rota Flask, modelo de domínio e banco de dados.

## 3. Conclusão
> Personalize esta seção com o que você realmente aprendeu e com os testes realizados.

O desenvolvimento do HelpDesk Acadêmico permitiu praticar a construção de uma aplicação web, a separação entre interface e lógica de negócio e a persistência de dados em um banco relacional. A implementação das operações de criação, consulta, atualização e exclusão ajudou a compreender o ciclo CRUD. A modelagem de entidades e relacionamentos também demonstrou a importância de planejar a estrutura dos dados antes da implementação. Como evolução futura, o sistema poderia receber autenticação, perfis de acesso, pesquisa por filtros, histórico de alterações e notificações.

## 4. Referências
- PYTHON SOFTWARE FOUNDATION. **Python Documentation**. Disponível em: https://docs.python.org/3/. Acesso em: [dia mês ano].
- PALLETS PROJECTS. **Flask Documentation**. Disponível em: https://flask.palletsprojects.com/. Acesso em: [dia mês ano].
- SQLALCHEMY. **SQLAlchemy Documentation**. Disponível em: https://docs.sqlalchemy.org/. Acesso em: [dia mês ano].
- GETBOOTSTRAP. **Bootstrap Documentation**. Disponível em: https://getbootstrap.com/docs/. Acesso em: [dia mês ano].
- PLANTUML. **PlantUML Documentation**. Disponível em: https://plantuml.com/. Acesso em: [dia mês ano].

## Checklist antes de entregar
- [ ] Preencher nome da instituição, curso, aluno(s), cidade e data.
- [ ] Rodar a aplicação e testar cadastro, listagem, edição e exclusão.
- [ ] Conferir se todos os diagramas correspondem ao código final.
- [ ] Ajustar paginação, margens, fonte e sumário conforme o padrão pedido pela instituição.
- [ ] Adicionar o tutor e `fernandonakagawa-unifil` como colaboradores do repositório.
- [ ] Incluir no documento o link real do repositório GitHub.
