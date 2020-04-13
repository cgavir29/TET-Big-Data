from mrjob.job import MRJob


class SalarioPromedioSector(MRJob):
    def mapper(self, _, line):
        (idemp, sececon, salary, year) = line.split(',')
        yield sececon, int(salary)

    def reducer(self, key, values):
        yield key, sum(values) 


class SalarioPromedioEmpleado(MRJob):
    def mapper(self, _, line):
        (idemp, sececon, salary, year) = line.split(',')
        yield idemp, int(salary)

    def reducer(self, key, values):
        yield key, sum(values)

class SectorPorEmpleado(MRJob):
    def mapper(self, _, line):
        (idemp, sececon, salary, year) = line.split(',')
        yield idemp, 1

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    SalarioPromedioSector.run()
    SalarioPromedioEmpleado.run()
    SectorPorEmpleado.run()
