from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Define o caminho base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configura o banco de dados para ser salvo na mesma pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'notes.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    color_bg = db.Column(db.String(7), nullable=False, default='#ffffff')
    color_text = db.Column(db.String(7), nullable=False, default='#000000')
    color_title = db.Column(db.String(7), nullable=False, default='#000000')

    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_title = request.form['title']
        note_content = request.form['content']
        note_color_bg = request.form['color_bg']
        note_color_text = request.form['color_text']
        note_color_title = request.form['color_title']

        new_note = Note(title=note_title, content=note_content, color_bg=note_color_bg, color_text=note_color_text, color_title=note_color_title)

        try:
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "Houve um erro ao adicionar sua nota."
    else:
        all_notes = Note.query.order_by(Note.id.desc()).all()
        return render_template('index.html', notes=all_notes)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    note_to_edit = Note.query.get_or_404(id)

    if request.method == 'POST':
        note_to_edit.title = request.form['title']
        note_to_edit.content = request.form['content']
        note_to_edit.color_bg = request.form['color_bg']
        note_to_edit.color_text = request.form['color_text']
        note_to_edit.color_title = request.form['color_title']

        try:
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "Houve um problema ao editar a nota."
    else:
        return render_template('edit.html', note=note_to_edit)

@app.route('/delete/<int:id>')
def delete(id):
    note_to_delete = Note.query.get_or_404(id)
    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "Houve um problema ao deletar a nota."

# Esta parte garante que o banco de dados seja criado antes do primeiro request
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)