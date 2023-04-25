from unittest import main, TestCase
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student('Alex')
        self.student_with_course = Student('Filip', {'math': ['some note']})

    def test_correct_initialization(self):
        self.assertEqual(self.student.name, 'Alex')
        self.assertEqual({}, self.student.courses)
        self.assertEqual(self.student_with_course.courses, {'math': ['some note']})

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.enroll('math', ['first note', 'second note'])
        self.assertEqual(self.student_with_course.courses['math'], ['some note', 'first note', 'second note'])

        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student.enroll('python', ['python is really cool'])

        self.assertEqual(self.student.courses['python'], ['python is really cool'])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_notes_to_non_existing_course_with_third_param_y(self):
        result = self.student.enroll('python', ['python is really cool'], 'Y')

        self.assertEqual(self.student.courses['python'], ['python is really cool'])
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll('python', ['python is really cool'], 'k')
        self.assertEqual(self.student.courses['python'], [])
        self.assertEqual(result, "Course has been added.")

    def test_add_note_from_existing_course(self):
        result = self.student_with_course.add_notes('math', 'that\'s a new note')
        self.assertEqual(['some note', 'that\'s a new note'], self.student_with_course.courses['math'])
        self.assertEqual(result, "Notes have been updated")

    def test_add_note_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', 'some note')

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course('math')
        self.assertEqual(self.student_with_course.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_none_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_with_course.leave_course('something')

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")



if __name__ == '__main__':
    main()
