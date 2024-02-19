from main import StudentsInMLOps

class TestStudentsInMLOps:
    @staticmethod
    def test_enrollStudents():
        ml_ops_class = StudentsInMLOps()
        ml_ops_class.enrollStudents(10)
        assert ml_ops_class.getTotalStrength() == 10

    @staticmethod
    def test_dropStudents():
        ml_ops_class = StudentsInMLOps()
        ml_ops_class.enrollStudents(10)
        ml_ops_class.dropStudents(5)
        assert ml_ops_class.getTotalStrength() == 5

    @staticmethod
    def test_getTotalStrength():
        ml_ops_class = StudentsInMLOps()
        ml_ops_class.enrollStudents(15)
        assert ml_ops_class.getTotalStrength() == 15

    @staticmethod
    def test_getClassName():
        ml_ops_class = StudentsInMLOps()
        assert ml_ops_class.getClassName() == "MLOps"


# Run the tests
if __name__ == "__main__":
    test = TestStudentsInMLOps()
    test.test_enrollStudents()
    print("test_enrollStudents: Passed")

    test.test_dropStudents()
    print("test_dropStudents: Passed")

    test.test_getTotalStrength()
    print("test_getTotalStrength: Passed")

    test.test_getClassName()
    print("test_getClassName: Passed")

