import json
from json import JSONEncoder

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Lesson(Base):
    __tablename__ = 'lesson'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    user_id = Column(Integer)

    @staticmethod
    def from_json(json_string):
        json_dict = json.loads(json_string)
        return Lesson(**json_dict)


class LessonDto:
    def __init__(self, id, name, user_id):
        self.id = id
        self.name = name
        self.user_id = user_id

    @staticmethod
    def from_lesson(lesson: Lesson):
        return LessonDto(lesson.id, lesson.name, lesson.user_id)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id
        }

    def to_json2(self):
        return self.__dict__


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
