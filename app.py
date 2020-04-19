from flask import  Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150),nullable = False)
    date = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    def __repr__(self):
        return 'url ' + str(self.id)

@app.route('/' , methods = ["POST","GET"])
def home():
    if request.method=="POST":
        do = request.form["todo-input"]
        data= todo(title = do)
        db.session.add(data)
        db.session.commit()     
    data = todo.query.all()
    return render_template('index.html', Data=data)


@app.route('/delete/<int:id>')
def delete(id):
    post = todo.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')
    
    
    



if __name__ == "__main__":
    app.debug = True
    app.run()