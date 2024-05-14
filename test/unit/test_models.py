from models import Student

def test_new_user():
    """
    GIVEN a Student Model
    When a new student is created
    then check the email and password_hashed fields are defined correctly
    """
    student=Student('test123@gmail.com','Thisisatest!')
    assert student.email == 'test123@gmail.com'
    assert student.password != 'Thisisatest!'
