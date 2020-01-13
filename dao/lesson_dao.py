from sqlalchemy.orm import Session

from entity.lesson import Lesson


def create_lesson(lesson: Lesson, session: Session) -> None:
    session.add(lesson)


def get_lesson(lesson_id: int, session: Session) -> Lesson:
    return session.query(Lesson).filter(Lesson.id == lesson_id).one()


def get_all_lessons(session) -> list:
    return session.query(Lesson).all()


def delete(lesson: Lesson, session: Session) -> None:
    session.delete(lesson)
