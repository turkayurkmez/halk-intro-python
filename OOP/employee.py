class Employee:

    min_salary=22000
    max_salary=150000

    def __init__(self, full_name, salary, title, experimentYear = 0):
        self._full_name = full_name
        self._salary = salary
        self._title = title
        self._experimentYear = experimentYear
        self._salary_history = [salary]
        self._score = 5 # 1..10 arası
    
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary < self.min_salary:
            raise ValueError(f"Maaş asgari ücretin ({self.min_salary}) altında olamaz!")
        
        if new_salary > self.max_salary:
            raise ValueError(f"Maaş maksimum  ücretin ({self.max_salary}) üzerinde olamaz!")
        
        old_salary = self._salary
        self._salary = new_salary
        self._salary_history.append(new_salary)

        different = new_salary - old_salary
        if different > 0:
            print(f"{self._full_name} isimli çalışan {different} kadar zam aldı")
        else:
            print(f"{self._full_name} isimli çalışan {different} kadar kesinti aldı")

        
    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, new_name):
        if not new_name:
            raise ValueError("Çalışan adı boş olamaz!")
        if len(new_name) < 3:
            raise ValueError("En az üç karakter girmelisiniz")
        self._full_name = new_name

    @property
    def salary_history(self):
        return self._salary_history


 # public double Salary {get; set;}

        