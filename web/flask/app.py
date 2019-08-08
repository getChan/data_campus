from flask import Flask, render_template
from a import Chat, db
from flask_admin import Admin

app = Flask(__name__)
app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///db/africa")  # 지가 알아서 엔진 만든다.
db.init_app(app)
admin = Admin(app)
admin

@app.route('/')
def hello_world():
    chat = Chat.query.all()
    return render_template('index.html', chat=chat)


if __name__ == "__main__":
    app.run()
