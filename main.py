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

    @abstractmethod
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
        """Return earnings of a Salaried Employee"""
        return self.weekly_salary

    def __repr__(self):
        """Return string representation for repr()"""
        return ('SalariedEmployee:\n' +
                super().__repr__() +
                f'Weekly salary: ${self.weekly_salary}'
                )


class HourlyEmployee(Employee):
    """Class HourlyEmployee"""

    def __init__(self, first, last, ssn, hours, wages):
        """Initialize an HourlyEmployee object"""
        super().__init__(first, last, ssn)
        self.hours = hours
        self.wages = wages

    # getters
    @property
    def hours(self):
        """Return hours"""
        return self._hours

    @property
    def wages(self):
        """Return wages"""
        return self._wages

    # setters
    @hours.setter
    def hours(self, hours):
        """Set and validate hours"""
        if not (0 <= hours <= 168):
            raise ValueError('Hours must be in range 0 to 168')
        self._hours = hours

    @wages.setter
    def wages(self, wages):
        """Set and validate wages"""
        if wages < 0:
            raise ValueError('Wages must be >= 0')
        self._wages = wages

    # methods
    def earnings(self):
        """Return earnings of an hourly Employee"""
        if self.hours <= 40:
            return self.hours*self.wages
        O_RATE = self.wages*1.5
        O_HOURS = self.hours - 40
        return self.wages * 40 + O_RATE * O_HOURS

    def __repr__(self):
        """Return string representation of repr()"""
        return ('HourlyEmployee:\n' +
                super().__repr__() +
                f'Total hours (week): {self.hours}\n' +
                f'Wages per hour: ${self.wages}'
                )


# main function
if __name__ == '__main__':
    """Test employee types"""
    # Raises Type error
    # person1 = Employee('Matthew', 'Crossan', 123123)

    # create employee objects
    person2 = SalariedEmployee('Matthew', 'Crossan', 1231232, 400)
    person3 = HourlyEmployee('Tam', 'Nassorc', 5345345, 50, 15)

    # add objects to employees list
    employees = [person2, person3]

    # iterate through employees and display information
    for employee in employees:
        print(employee)
        print(f'Earnings: ${employee.earnings()}\n')
