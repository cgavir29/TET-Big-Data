from mrjob.job import MRJob


def avg(values):
    total = 0
    count = 0

    for value in values:
        total += value
        count += 1

    return total / count


class AverageSalaryBySector(MRJob):
    def mapper(self, _, line):
        _, sector, salary, _ = line.split(',')

        yield sector, int(salary)

    def reducer(self, sector, salary):
        avg_salary = avg(salary)

        yield sector, avg_salary


class AverageSalaryByEmployee(MRJob):
    def mapper(self, _, line):
        user, _, salary, _ = line.split(',')

        yield user, int(salary)

    def reducer(self, user, salary):
        avg_salary = avg(salary)

        yield user, avg_salary


class SectorsPerEmployee(MRJob):
    def mapper(self, _, line):
        user, sector, _, _ = line.split(',')

        yield user, sector

    def unique_sectors(self, sectors):
        return len(set(sectors))

    def reducer(self, user, sector):
        total_sectors = self.unique_sectors(sector)

        yield user, total_sectors


if __name__ == '__main__':
    print('Average Salary By Sector')
    AverageSalaryBySector.run()
    print()

    print('Average Salary By Employee')
    AverageSalaryByEmployee.run()
    print()

    print('Sectors Per Employee')
    SectorsPerEmployee.run()
    print()
