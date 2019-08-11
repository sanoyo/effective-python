from weakref import WeakKeyDictionary


class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, isinstance_type):
        if isinstance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


# 結果確認
first_exam = Exam()
first_exam.writing_grade = 55
second_exam = Exam()
second_exam.writing_grade = 20
third_exam = Exam()
third_exam.writing_grade = 90
print('First ', first_exam.writing_grade) # 55
print('Second ', second_exam.writing_grade) # 20
print('Third ', third_exam.writing_grade) # 90