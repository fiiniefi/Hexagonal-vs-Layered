import json


def get_registration(api_client, course_id, student_id):
    url = f"/registry/{course_id}/{student_id}/"
    return api_client.get(url)


def register_student(api_client, course_id, student):
    url = "/registry/"
    return api_client.post(
        url,
        params={"course_id": course_id},
        data=json.dumps({"course_id": course_id, **dict(student)}),
    )
