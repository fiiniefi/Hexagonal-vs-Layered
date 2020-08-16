from src.courses.models import Course


def course_factory(**kwargs):
    return Course.parse_obj(
        {
            "id": "1",
            "name": "name",
            "semester": 1,
            "date_time": "date_time",
            "type": "seminar",
            **kwargs
        }
    )
