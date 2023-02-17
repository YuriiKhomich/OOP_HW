import datetime
from datetime import timedelta

class Employee:
    def __init__(self, name_person, salary):
        self.name_person = name_person
        self.salary = salary

    def __str__(self):
        return f'{self.name_person} the Employee.'

    def work(self):
        return f'{self.name_person}: I come to the office.'

    def check_salary(self, days: int = None):
        if days:
            return f'You salary for {days} days:  {self.salary * days} hrn'
        start_day = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, 1)
        finish_day = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month,
                                   datetime.datetime.now().day)
        delta_days = finish_day - start_day
        total_salary = (sum(1 for day in (start_day + timedelta(x) for x in range(delta_days.days))
                            if day.isoweekday() < 6)) * self.salary
        return f'Total salary for {delta_days.days} days:  {total_salary} hrn'

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary


class Recruiter(Employee):
    def work(self):
        return f'{self.name_person}: I come to the office and start hiring.'

    def __str__(self):
        return f'{self.name_person} the Recruiter.'


class Developer(Employee):
    def __init__(self, name_person, salary, tech_stack=None):
        super().__init__(name_person, salary)
        if tech_stack is None:
            tech_stack = ['Molodec']
        self.tech_stack = tech_stack

    def work(self):
        return f'{self.name_person}: I come to the office and start coding.'

    def __str__(self):
        return f'{self.name_person} the Developer.'

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        name_person1 = self.name_person + ' ' + other.name_person
        tech_stack1 = list(set(self.tech_stack + other.tech_stack))
        salary1 = max(self.salary, other.salary)
        person_new = Developer(name_person1, salary1, tech_stack1)
        return person_new


if __name__ == '__main__':
    person = Employee('John', 300)
    person1 = Employee('Jim', 305)
    print(person.work())
    print(person1.work())
    person2 = Recruiter('Bob', 303)
    person3 = Developer('Niki', 320)
    print(person2.work())
    print(person3.work())
    print(person3)
    print(person)
    person4 = Developer('John', 300, ['Basic', 'C+'])
    person5 = Developer("Bobi", 305, ['Python', 'Pascal', 'Cobol'])
    person6 = Developer('Suzi', 298, ['Python', 'English'])
    print(f"{person1}, {person1.check_salary(10)}")
    print(f"{person}, {person.check_salary()}")
    print(person4 < person5)
    person_new = person4 + person5
    print(f'ADD two personas: {person_new} Max salary: {person_new.salary}'
          f' Total skill: {person_new.tech_stack}')
