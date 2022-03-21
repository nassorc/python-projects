from abc import ABC, abstractmethod

# Employee class defition


class Employee(ABC):
    """Class Employee"""

    def __init__(self, first, last, ssn):
        """Initialize an Employee object."""
        self._first = first
        self._last = last
        self._ssn = ssn

    @property
    def first(self):
        """Return first name"""
        return self._first

    @property
    def last(self):
        """Return last name"""
        return self._last

    @property
    def ssn(self):
        """Return ssn"""
        return self._ssn

    # @abstractmethod
    def earnings(self):
        """Calculates earning of an Employee"""

    def __repr__(self):
        """Return string representation for repr()"""
        return(
            f'First name: {self.first}\n' +
            f'Last name: {self.last}\n' +
            f'Social security number: {self.ssn}\n'
        )


class SalariedEmployee(Employee):
    """Class SalariedEmployee"""

    def __init__(self, first, last, ssn, weekly_salary):
        """Initialize an Employee object."""
        super().__init__(first, last, ssn)
        self.weekly_salary = weekly_salary

    @property
    def weekly_salary(self):
        """Return weekly salary"""
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, salary):
        """Sets weekly salary"""
        if salary < 0:
            raise ValueError('Weekly salary must be >= 0')

        self._weekly_salary = salary

    def earnings(self):
        """"""
        return self.weekly_salary

    def __repr__(self):
        """"""
        return ('SalariedEmployee:\n' +
                super().__repr__() +
                f'Weekly salary: ${self.weekly_salary}\n'
                )


class HourlyEmployee(Employee):
    """"""

    def __init__(self, first, last, ssn, hours, wages):
        """"""
        super().__init__(first, last, ssn)
        self.hours = hours
        self.wages = wages

    # getters
    @property
    def hours(self):
        """"""
        return self._hours

    @property
    def wages(self):
        """"""
        return self._wages

    # setters
    @hours.setter
    def hours(self, hours):
        """"""
        if not (0 <= hours <= 168):
            raise ValueError('Hours must be in range 0 to 168')
        self._hours = hours

    @wages.setter
    def wages(self, wages):
        """"""
        if wages < 0:
            raise ValueError('Wages must be >= 0')

    def earnings(self):
        """"""
        pass

    def __repr__(self):
        return 'string from hourly employee'


# person1 = Employee('Matthew', 'Crossan', 123123)
person2 = SalariedEmployee('Matthew', 'Crossan', 1231232, 400)
print(person2)
# print(repr(person2))
