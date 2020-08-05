def get_course_registration(api_client, course_id):
    url = f"/registry/{course_id}"
    return api_client.get(url)
