import pytest
from jose import jwt
from app import schemas
from app.config import settings


def test_create_user(client):
    res = client.post(
        '/users/', json={'email': 'abc@abc.com', 'password': 'abc123'})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'abc@abc.com'
    assert res.status_code == 201


def test_login_user(client, test_user):
    res = client.post(
        '/login', data={'username': test_user['email'], 'password': test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,
                         settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get('user_id')
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200


@pytest.mark.parametrize('email, password, status_code', [
    ('wrong@gmail.com', 'def123', 403),
    ('def@def.com', 'wrongPassword', 403),
    ('wrong@gmail.com', 'wrongPassword', 403),
    (None, 'def123', 422),
    ('def@def.com', None, 422)
])
def test_incorrect_login(client, test_user, email, password, status_code):
    res = client.post(
        '/login', data={'username': email, 'password': password})
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid credentials'
