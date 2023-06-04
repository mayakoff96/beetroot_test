class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise TypeError('Only instances of Worker class can be added')

    def __repr__(self):
        return f'Boss {self.id}, {self.name}, {self.company}'


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss


    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss
            boss.add_worker(self)
        else:
            raise TypeError('Boss attribute must be an instance of Boss class')

    def __repr__(self):
        return f'Worker {self.id}, {self.name}, {self.company}, {self.boss}'


boss_1 = Boss(1, 'Georgy', 'Company_name_1')
worker_1 = Worker(2, 'Rabotyaga', 'Company_name_1', boss_1)
print(worker_1.boss)
print(boss_1.workers)

boss_2 = Boss(3, 'Pavlo', 'Company_name_2')
worker_1.boss = boss_2

print(worker_1.boss)
print(boss_2.workers)
print(boss_1.workers)