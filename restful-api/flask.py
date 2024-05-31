import requests


def test_home_route():
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    assert response.text == "Welcome to the Flask API!"


def test_data_route():
    response = requests.get('http://localhost:5000/data')
    assert response.status_code == 200
    data = response.json()
    assert data == ["jane", "john"]


def test_status_route():
    response = requests.get('http://localhost:5000/status')
    assert response.status_code == 200
    assert response.text == "OK"


def test_user_route():
    response = requests.get('http://localhost:5000/users/jane')
    assert response.status_code == 200
    user = response.json()
    assert user == {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    }


def test_add_user_route():
    new_user = {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    response = requests.post('http://localhost:5000/add_user', json=new_user)
    assert response.status_code == 200
    result = response.json()
    assert result == {
        "message": "User added",
        "user": new_user
    }


if __name__ == "__main__":
    test_home_route()
    test_data_route()
    test_status_route()
    test_user_route()
    test_add_user_route()
    print("All tests passed!")
