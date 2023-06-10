class Apple:
    ABBREVIATION = 'APL'

    def __init__(self, department_name: str, workers_quantity: int, total_dep_exp : int | float,
                 productivity_percent_of_department: int | float, salary_of_worker: int | float):
        self.__department_name = department_name
        self.__workers_quantity = workers_quantity
        self.__productivity_percent_of_department = productivity_percent_of_department
        self.__total_dep_exp = total_dep_exp
        self.__salary_of_worker = salary_of_worker

    @staticmethod
    def company_palce_in_top_list():
        print('Our company is on the 3rd place')

    @classmethod
    def workers_quantity_predict_in_2_years(cls, department_name: str, workers_quantity: int | float):
        quantity_predict = workers_quantity * 1.75
        return cls(department_name, quantity_predict, None, None, None)

    @classmethod
    def calculate_middle_sal_of_all_dep(cls, department_name: str, workers_quantity: int | float,
                                        salary_of_worker: int|float):
        mid_sal = workers_quantity * salary_of_worker
        return cls(department_name, workers_quantity, mid_sal, None, None)

    @property
    def department_name(self):
        return self.__department_name

    @department_name.setter
    def department_name(self, new_department_name):
        if isinstance(new_department_name, str) and len(new_department_name) < 20:
            self.__department_name = new_department_name
        else:
            print(
                f'Department name should be a string with length less than 20: {type(new_department_name)} : '
                f'{len(new_department_name)}')

    @department_name.deleter
    def department_name(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def workers_quantity(self):
        return self.__workers_quantity

    @workers_quantity.setter
    def workers_quantity(self, new_workers_quantity):
        if isinstance(new_workers_quantity, int | float) and len(str(new_workers_quantity)) <= 6:
            self.__workers_quantity = new_workers_quantity
        else:
            print(f'Workers quantity should be a int or float with length equal or less than 6:'
                  f' {type(new_workers_quantity)} : {len(new_workers_quantity)}')

    @workers_quantity.deleter
    def workers_quantity(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def productivity_percent_of_department(self):
        return self.__productivity_percent_of_department

    @productivity_percent_of_department.setter
    def productivity_percent_of_department(self, new_results_of_department):
        if isinstance(new_results_of_department, int | float) and len(str(new_results_of_department)) <= 7:
            self.__productivity_percent_of_department = new_results_of_department
        else:
            print(f'Results of department should be a int or float with length equal or less than 7:'
                  f' {type(new_results_of_department)} : {len(new_results_of_department)}')
    @productivity_percent_of_department.deleter
    def productivity_percent_of_department(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def total_dep_exp(self):
        return self.__total_dep_exp

    @total_dep_exp.setter
    def total_dep_exp(self, new_total_exp):
        if isinstance(new_total_exp, int | float) and len(str(new_total_exp)) <= 9:
            self.__total_dep_exp = new_total_exp
        else:
            print(f'Total experience of department should be a int or float with length equal or less than 9:'
                  f'{type(new_total_exp)}) : {len(new_total_exp)}')

    @total_dep_exp.deleter
    def total_dep_exp(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    @property
    def salary_of_worker(self):
        return self.__salary_of_worker

    @salary_of_worker.setter
    def salary_of_worker(self, new_salary):
        if isinstance(new_salary, int | float) and len(str(new_salary)) <= 7:
            self.__salary_of_worker = new_salary
        else:
            print(f'Salary of worker should be a int or float with length equal or less than 7:'
                  f'{type(new_salary)}) : {len(new_salary)}')

    @salary_of_worker.deleter
    def salary_of_worker(self):
        raise NotImplementedError('Delete is not supported for this attribute')

    def __str__(self):
        return f"{self.department_name}, {self.workers_quantity}, {self.productivity_percent_of_department}," \
               f"{self.total_dep_exp}"

if __name__ == '__main__':
    Apple.company_palce_in_top_list()
    predict = Apple.workers_quantity_predict_in_2_years('Marketing', 600)
    wage_of_dep = Apple.calculate_middle_sal_of_all_dep('HR', 85, 1200)
    print(wage_of_dep)

