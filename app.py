from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "troque-esta-chave-em-producao"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///helpdesk.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    chamados = db.relationship("Chamado", backref="solicitante", lazy=True)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    chamados = db.relationship("Chamado", backref="categoria", lazy=True)

class Chamado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(140), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    prioridade = db.Column(db.String(20), nullable=False, default="Média")
    status = db.Column(db.String(20), nullable=False, default="Aberto")
    criado_em = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categoria.id"), nullable=False)

@app.route("/")
def index():
    total = Chamado.query.count()
    abertos = Chamado.query.filter_by(status="Aberto").count()
    andamento = Chamado.query.filter_by(status="Em andamento").count()
    resolvidos = Chamado.query.filter_by(status="Resolvido").count()
    chamados = Chamado.query.order_by(Chamado.criado_em.desc()).all()
    return render_template("index.html", chamados=chamados, total=total,
                           abertos=abertos, andamento=andamento, resolvidos=resolvidos)

@app.route("/chamados/novo", methods=["GET", "POST"])
def novo_chamado():
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    if not usuarios or not categorias:
        flash("Cadastre pelo menos um usuário e uma categoria antes de abrir um chamado.", "warning")
        return redirect(url_for("cadastros"))
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        if not titulo or not descricao:
            flash("Título e descrição são obrigatórios.", "danger")
            return render_template("form_chamado.html", chamado=None, usuarios=usuarios, categorias=categorias)
        chamado = Chamado(
            titulo=titulo,
            descricao=descricao,
            prioridade=request.form.get("prioridade", "Média"),
            status=request.form.get("status", "Aberto"),
            usuario_id=int(request.form["usuario_id"]),
            categoria_id=int(request.form["categoria_id"])
        )
        db.session.add(chamado)
        db.session.commit()
        flash("Chamado cadastrado com sucesso.", "success")
        return redirect(url_for("index"))
    return render_template("form_chamado.html", chamado=None, usuarios=usuarios, categorias=categorias)

@app.route("/chamados/<int:chamado_id>/editar", methods=["GET", "POST"])
def editar_chamado(chamado_id):
    chamado = db.get_or_404(Chamado, chamado_id)
    usuarios = Usuario.query.order_by(Usuario.nome).all()
    categorias = Categoria.query.order_by(Categoria.nome).all()
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        if not titulo or not descricao:
            flash("Título e descrição são obrigatórios.", "danger")
        else:
            chamado.titulo = titulo
            chamado.descricao = descricao
            chamado.prioridade = request.form.get("prioridade", "Média")
            chamado.status = request.form.get("status", "Aberto")
            chamado.usuario_id = int(request.form["usuario_id"])
            chamado.categoria_id = int(request.form["categoria_id"])
            db.session.commit()
            flash("Chamado atualizado com sucesso.", "success")
            return redirect(url_for("index"))
    return render_template("form_chamado.html", chamado=chamado, usuarios=usuarios, categorias=categorias)

@app.route("/chamados/<int:chamado_id>/excluir", methods=["POST"])
def excluir_chamado(chamado_id):
    chamado = db.get_or_404(Chamado, chamado_id)
    db.session.delete(chamado)
    db.session.commit()
    flash("Chamado excluído.", "success")
    return redirect(url_for("index"))

@app.route("/cadastros", methods=["GET", "POST"])
def cadastros():
    if request.method == "POST":
        tipo = request.form.get("tipo")
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        if not nome:
            flash("Informe um nome.", "danger")
        elif tipo == "usuario":
            if not email:
                flash("Informe o e-mail do usuário.", "danger")
            elif Usuario.query.filter_by(email=email).first():
                flash("Já existe um usuário com esse e-mail.", "danger")
            else:
                db.session.add(Usuario(nome=nome, email=email))
                db.session.commit()
                flash("Usuário cadastrado.", "success")
        elif tipo == "categoria":
            if Categoria.query.filter_by(nome=nome).first():
                flash("Essa categoria já existe.", "danger")
            else:
                db.session.add(Categoria(nome=nome))
                db.session.commit()
                flash("Categoria cadastrada.", "success")
        return redirect(url_for("cadastros"))
    return render_template("cadastros.html",
        usuarios=Usuario.query.order_by(Usuario.nome).all(),
        categorias=Categoria.query.order_by(Categoria.nome).all())

@app.route("/usuarios/<int:usuario_id>/excluir", methods=["POST"])
def excluir_usuario(usuario_id):
    usuario = db.get_or_404(Usuario, usuario_id)
    if usuario.chamados:
        flash("Não é possível excluir um usuário que possui chamados vinculados.", "warning")
    else:
        db.session.delete(usuario)
        db.session.commit()
        flash("Usuário excluído.", "success")
    return redirect(url_for("cadastros"))

@app.route("/categorias/<int:categoria_id>/excluir", methods=["POST"])
def excluir_categoria(categoria_id):
    categoria = db.get_or_404(Categoria, categoria_id)
    if categoria.chamados:
        flash("Não é possível excluir uma categoria que possui chamados vinculados.", "warning")
    else:
        db.session.delete(categoria)
        db.session.commit()
        flash("Categoria excluída.", "success")
    return redirect(url_for("cadastros"))

with app.app_context():
    db.create_all()
    if Usuario.query.count() == 0:
        db.session.add_all([
            Usuario(nome="Ana Souza", email="ana.souza@example.com"),
            Usuario(nome="Carlos Lima", email="carlos.lima@example.com")
        ])
    if Categoria.query.count() == 0:
        db.session.add_all([
            Categoria(nome="Hardware"),
            Categoria(nome="Software"),
            Categoria(nome="Acesso")
        ])
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
