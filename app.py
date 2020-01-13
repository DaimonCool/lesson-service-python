from flask import Flask, jsonify, abort, make_response, request
from service import lesson_service
from entity.lesson import Lesson
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# lessons = [Lesson(id=1, name="Биология", user_id=2), Lesson(id=2, name="География", user_id=2)]


@app.route('/lessons', methods=['GET'])
def index():
    lessons_dto = lesson_service.find_all_lessons()
    if not lessons_dto:
        abort(404)
    return jsonify([lesson_dto.to_json2() for lesson_dto in lessons_dto])
    # return jsonify(lessons[0].to_json())


@app.route('/lessons/<int:lesson_id>', methods=['GET'])
def get_task(lesson_id):
    lesson_dto = lesson_service.get_lesson(lesson_id)
    if lesson_dto is None:
        abort(404)
    return jsonify(lesson_dto.to_json2())


@app.route('/lessons', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    # lesson = Lesson(name=request.json['name'], user_id=request.json['user_id'])
    lesson = Lesson.from_json(json.dumps(request.json))
    is_created = lesson_service.create_lesson(lesson)
    if not is_created:
        return "Some exception has occured", 500
    return "", 201


@app.route('/lessons/<int:lesson_id>', methods=['PUT'])
def update_task(lesson_id):
    result = lesson_service.update_lesson_by_id(lesson_id, request.json)
    if result == "not updated":
        return "Some exception has occured", 500
    elif result == "not found":
        abort(404)
    return "", 200


# TODO
@app.route('/lessons/<int:lesson_id>', methods=['DELETE'])
def delete_task(lesson_id):
    result = lesson_service.delete_lesson(lesson_id)
    if result == "not deleted":
        return "Some exception has occured", 500
    elif result == "not found":
        abort(404)
    return "", 200


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
