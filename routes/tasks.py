from flask import request, jsonify, Blueprint
from models.tasks import tasks as model
from models.tasks import db
from logging import exception

app = Blueprint('routes-tasks', __name__)

#add new task
@app.route('/api/tasks', methods=['POST'])
def addTask():
    try:
        name = request.json['name']
        desc = request.json['description']
        data = model(name,desc)
        db.session.add(data)
        db.session.commit()
        toReturn = data.serialize()
        return jsonify({
            "count": 1,
            "message": "Task Added Successfully", 
            "results": toReturn
        }), 200
    except Exception:
        exception("[SERVER]: Error in route /api/tasks [POST] ->")
        return jsonify({"message": "Internal Error"}), 500
#get all tasks
@app.route("/api/tasks", methods=["GET"])
def getTasks():
    try:
        data = model.query.all()
        toReturn = [one.serialize() for one in data]
        if toReturn:
            return jsonify({
                "count": len(toReturn),
                "message":"task's list",
                "results": toReturn
            }), 200
        else:
            return jsonify({
                "count": 0,
                "message":"task's list",
                "results": {}
            }), 200
    except Exception:
        exception("[SERVER]: Error in route /api/tasks ->")
        return jsonify({"message": "Internal Error"}), 500
#get for name task
@app.route("/api/tasks/<string:name>", methods=["GET"])
def getTask(name):
    try:
        data = model.query.filter(model.name.like(f"%{name}%")).first()
        if not data:
            return jsonify({
                "count": 0,
                "message":"task not exist",
                "results": {}
            }), 200
        toReturn = data.serialize()
        return jsonify({
            "count": len(toReturn),
            "message":"task's list",
            "results": toReturn
        }), 200
    except Exception:
        exception("[SERVER]: Error in route /api/tasks/<string:name> ->")
        return jsonify({"message": "Internal Error"}), 500
#update task for id