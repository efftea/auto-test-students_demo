import requests
import pytest
import datetime

payload_git={
    "filter": {
        "fgit": {
            "hasGit": True
        }
    }
}

payload_contact={
    "filter": {
        "fcontact": {
            "hasContact": True
        }
    }
}

payload_git_contact={
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload_nogit_contact={
    "filter": {
        "fcontact": {
            "hasContact": True
        },
        "fgit": {
            "hasGit": False
        }
    }
}

payload_git_nocontact={
    "filter": {
        "fcontact": {
            "hasContact": False
        },
        "fgit": {
            "hasGit": True
        }
    }
}

payload_nogit_nocontact={
    "filter": {
        "fcontact": {
            "hasContact": False
        },
        "fgit": {
            "hasGit": False
        }
    }
}

payload_list={
    "version": "string",
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_page_three={
    "version": "string",
    "pagination": {
        "count": 20,
        "number": 3,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_200_students={
    "version": "string",
    "pagination": {
        "count": 200,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_50_page={
    "version": "string",
    "pagination": {
        "count": 20,
        "number": 50,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_7_students={
    "version": "string",
    "pagination": {
        "count": 7,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_list_git={
    "version": "string",
    "filter": {
        "fgit": {
            "hasGit": 'true'
        }
    },
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_list_contact={
    "version": "string",
    "filter": {
        "fcontact": {
            "hasContact": 'true'
        }
    },
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_list_git_contact={
    "version": "string",
    "filter": {
        "fgit": {
            "hasGit": 'true'
        },
        "fcontact": {
            "hasContact": 'true'
        }
    },
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_list_nogit_contact={
    "version": "string",
    "filter": {
        "fgit": {
            "hasGit": 'false'
        },
        "fcontact": {
            "hasContact": 'true'
        }
    },
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_list_git_nocontact={
    "version": "string",
    "filter": {
        "fgit": {
            "hasGit": 'true'
        },
        "fcontact": {
            "hasContact": 'false'
        }
    },
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

payload_list_nogit_nocontact={
    "version": "string",
    "filter": {
        "fgit": {
            "hasGit": 'false'
        },
        "fcontact": {
            "hasContact": 'false'
        }
    },
    "pagination": {
        "count": 20,
        "number": 0,
        "random": 'false',
        "orderDesc": 'true'
    }
}

BASE_URL = 'http://192.168.0.16:8080/students/general/get-student-list'
BASE_URL_2 = 'http://192.168.0.16:8080/students/general/get-student-count'

def test_get_student_count():
    response = requests.post(BASE_URL_2)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:" , response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_count_git():
    response = requests.post(BASE_URL_2, json=payload_git)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:" , response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_count_contact():
    response = requests.post(BASE_URL_2, json=payload_contact)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:" , response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_count_git_contact():
    response = requests.post(BASE_URL_2, json=payload_git_contact)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:" , response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_count_nogit_contact():
    response = requests.post(BASE_URL_2, json=payload_nogit_contact)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:" , response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_count_git_nocontact():
    response = requests.post(BASE_URL_2, json=payload_git_nocontact)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:" , response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_count_nogit_nocontact():
    response = requests.post(BASE_URL_2, json=payload_nogit_nocontact)
    response_body = response.json()
    assert response.status_code == 200
    print("\nКолличество записей:", response_body["resultData"])
    print("Время проведения теста: ", datetime.datetime.now())

def test_get_student_list():
    response = requests.post(f'{BASE_URL}', json=payload_list)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())

def test_get_student_list_page_three():
    response = requests.post(f'{BASE_URL}', json=payload_page_three)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())

def test_get_student_list_200_students():
    response = requests.post(f'{BASE_URL}', json=payload_200_students)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())

def test_get_student_list_50_page():
    response = requests.post(f'{BASE_URL}', json=payload_50_page)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())

def test_get_student_list_7_students():
    response = requests.post(f'{BASE_URL}', json=payload_7_students)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())

def test_get_student_list_git():
    response = requests.post(f'{BASE_URL}', json=payload_list_git)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())
    for student in response_body["info"][:20]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"

def test_get_student_list_contact():
    response = requests.post(f'{BASE_URL}', json=payload_list_contact)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())
    for student in response_body["info"][:20]:
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_git_contact():
    response = requests.post(f'{BASE_URL}', json=payload_list_git_contact)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())
    for student in response_body["info"][:20]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_nogit_contact():
    response = requests.post(f'{BASE_URL}', json=payload_list_nogit_contact)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())
    for student in response_body["info"][:20]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == True, "Поле контакты пустое"

def test_get_student_list_git_nocontact():
    response = requests.post(f'{BASE_URL}', json=payload_list_git_nocontact)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())
    for student in response_body["info"][:20]:
        assert student["fgit"]["hasGit"] == True, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты пустое"

def test_get_student_list_nogit_nocontact():
    response = requests.post(f'{BASE_URL}', json=payload_list_nogit_nocontact)
    response_body=response.json()
    assert response.status_code==200
    print("\nВремя проведения теста: ", datetime.datetime.now())
    for student in response_body["info"][:20]:
        assert student["fgit"]["hasGit"] == False, "Поле Гит пустое"
        assert student["fcontact"]["hasContact"] == False, "Поле контакты пустое"

if __name__ == '__main__':
    pytest.main([__file__])