from flask import Flask, jsonify
from models.tasks import db
from routes.tasks import app as tasks_bp

#app = Flask(__name__, static_url_path="/static")
SQLITE_DB_URI = "sqlite:///db\\tasks.db"
POSTGRES_DB_URI = "postgresql://postgres:root@postgres/tasksAPI"
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_DB_URI

db.init_app(app)
#TEST CONECTION

@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except Exception:
        print("[SERVER]: Error at create_tables()")

# Aquí empiezan las rutas
#default check rest api route
@app.route('/ping')
def ping():
    #create_tables()
    db.create_all()
    return jsonify({"message": "Pong!"})
#add routes tasks
app.register_blueprint(tasks_bp)

#if __name__ == "__main__":
#    app.run(debug=True, port=4000)