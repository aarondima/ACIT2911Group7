from models import Student

def test_new_user():
    student=Student('test123@gmail.com', 'Thisisatest!')
    assert student.email == 'test123@gmail.com'
    assert student.password != 'Thisisatest!'