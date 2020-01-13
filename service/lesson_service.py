from sqlalchemy.orm.exc import NoResultFound

from entity.lesson import Lesson, LessonDto
from database import database_connection
from dao import lesson_dao
import logging


def create_lesson(lesson: Lesson) -> bool:
    session = database_connection.get_session()
    is_created = True
    try:
        lesson_dao.create_lesson(lesson, session)
        session.commit()
    except Exception as e:
        logging.error(str(e))
        session.rollback()
        is_created = False
    finally:
        database_connection.Session.remove()
    return is_created


def get_lesson(lesson_id: int) -> LessonDto:
    session = database_connection.get_session()
    lesson_dto = None
    try:
        lesson = lesson_dao.get_lesson(lesson_id, session)
        lesson_dto = LessonDto.from_lesson(lesson)
        session.commit()
    except Exception as e:
        logging.error(str(e))
        session.rollback()
    finally:
        database_connection.Session.remove()
    return lesson_dto


def find_all_lessons() -> list:
    session = database_connection.get_session()
    lessons_dto = []
    try:
        lessons = lesson_dao.get_all_lessons(session)
        for lesson in lessons:
            lessons_dto.append(LessonDto.from_lesson(lesson))
        session.commit()
    except Exception as e:
        logging.error(str(e))
        session.rollback()
    finally:
        database_connection.Session.remove()
    return lessons_dto


def update_lesson_by_id(lesson_id: int, lesson_dict: dict) -> str:
    session = database_connection.get_session()
    result = "updated"
    try:
        lesson = lesson_dao.get_lesson(lesson_id, session)
        if "name" in lesson_dict:
            lesson.name = lesson_dict["name"]
        if "user_id" in lesson_dict:
            lesson.user_id = lesson_dict["user_id"]

        session.commit()
    except Exception as e:
        if type(e) is NoResultFound:
            result = "not found"
        else:
            result = "not updated"
        logging.error(str(e))
        session.rollback()
    finally:
        database_connection.Session.remove()
    return result


def delete_lesson(lesson_id: int) -> str:
    session = database_connection.get_session()
    result = "deleted"
    try:
        lesson_dao.delete(lesson_dao.get_lesson(lesson_id, session), session)
        session.commit()
    except Exception as e:
        if type(e) is NoResultFound:
            result = "not found"
        else:
            result = "not deleted"
        logging.error(str(e))
        session.rollback()
    finally:
        database_connection.Session.remove()
    return result
