def get_course(api_client, course_id):
    url = f"/courses/{course_id}"
    return api_client.get(url)


def save_course(api_client, course):
    url = "/courses/"
    return api_client.post(
        url, json={"course": course.dict()}
    )
