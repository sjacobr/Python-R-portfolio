import json

import pytest
import requests

@pytest.fixture()
def user_a():
    return {"email": "jb@gmail.com", "name": "Jason Bourne", "age": 37}

@pytest.fixture()
def session():
    ''' Returns a session with default headers to supply for every http request '''
    sess = requests.Session()

    # The API requires the Content-Type header to be set
    sess.headers.update({'Content-Type': 'application/json'})
    return sess

def test_end_to_end(user_a, session):
    res = session.post("http://localhost:80/user", data=json.dumps(user_a))
    assert res.status_code == 200

    user_id = json.loads(res.text)['id']
    get_response = session.get(f"http://localhost:80/user/{user_id}")
    assert get_response.status_code == 200

    user = json.loads(get_response.text)
    assert user_id == user['id']
    del user['id']

    assert user == user_a

    user_a['id'] = user_id
    user_a['age'] = 38
    resp_patch = session.patch("http://localhost:80/user", data=json.dumps(user_a))
    assert resp_patch.status_code == 200
    updated_user = json.loads(session.get(f"http://localhost:80/user/{user_id}").text)
    assert updated_user['age'] == 38, str(updated_user)

    # DELETE
    resp_delete = session.delete(f"http://localhost:80/user/{user_id}")
    assert resp_delete.status_code == 200

    # querying for the deleted user should now return a 404
    resp_get_2 = session.get(f"http://localhost:80/user/{user_id}")
    assert resp_get_2.status_code == 404
