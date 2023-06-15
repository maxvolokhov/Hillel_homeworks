class Worker:
    CONTRACT = 'VALID'

    def __init__(self, name=None, rank=None, experience=None, salary=None):
        self.__name = name
        self.__rank = rank
        self.__experience = experience
        self.__salary = salary

    def promotion(self, name: str, experience: int | float):
        if isinstance(experience, int | float) and experience >= 1.5:
            print(f'Dear {name}, you are ready for promotion, congratulations!')
        else:
            print(f'Dear {name} your {experience} of experience is too less for promotion\n'
                  f'Let\'s come back to this point once you reach no less than 1.5 years of experience')

    @staticmethod
    def bonuses_dates_for_each_worker():
        print('01.02, 01.05, 01.08, 31.12')

    @classmethod
    def convert_salary_to_uah(cls, name: str, salary: int):
        salary_in_uah = salary * 37
        return cls(name, salary_in_uah)

    @classmethod
    def salary_coefficient(cls, name: str, rank: str, experience: float | int, salary: int):
        sal_cof = salary / experience
        return cls(name, sal_cof)

    @classmethod
    def create_worker_with_salary_expectation_in_1_year(cls, name: str, rank: str, experience: float | int,
                                                        salary: int):
        salary_expectation = salary * 1.45
        return cls(name, rank, experience, salary_expectation)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 15:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be a string with length less than 15: {type(new_name)} : {len(new_name)}')

    @name.deleter
    def name(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, new_rank):
        if isinstance(new_rank, str) and len(new_rank) < 15:
            self.__rank = new_rank
        else:
            raise TypeError(f'Rank should be a string with length less than 15: {type(new_rank)} :'
                            f'{len(new_rank)}')

    @rank.deleter
    def rank(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, new_experience):
        if isinstance(new_experience, int | float) and len(str(new_experience)) < 7:
            self.__experience = new_experience
        else:
            print(
                f'Experience should be a number or float with length less than 7: {type(new_experience)} :'
                f'{len(new_experience)}')

    @experience.deleter
    def experience(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int | float) and len(str(new_salary)) <= 7:
            self.__salary = new_salary
        else:
            print(
                f' Salary should be a number or float with length equal or less than 7: {type(new_salary)} :'
                f'{len(new_salary)}')

    @salary.deleter
    def salary(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    def __str__(self):
        return f"name='{self.__name}', rank='{self.__rank}', experience={self.__experience}, " \
               f"salary={self.__salary}"

if __name__ == '__main__':
    tim = Worker('Tim', 'CEO', 15.5, 18000)
    joan = Worker('Joan', 'Director', 8, 10000)
    tim.probation_status = 'passed'
    Worker.bonuses_dates_for_each_worker()
    salary_convert = Worker.convert_salary_to_uah('Tim', 18000)
    new_func = Worker.salary_coefficient('Joan', 'Director', 8, 10000)
    max_ = Worker.create_worker_with_salary_expectation_in_1_year('Max', 'QA Automation', 1.5, 2500)
    print(max_)
    promotion_var = Worker()
    promotion_var.promotion('Ann', 1.4)
