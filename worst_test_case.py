import csv


class WorstTestCase:
    def __init__(self, num_param):
        self.num_param = num_param
        self.boundary_values = []
        self.extreme_values = []
        self.table = []

    def input_data(self):
        for i in range(self.num_param):
            a = int(input(f'parameter {i+1} lower bound : '))
            b = int(input(f'parameter {i+1} upper bound : '))
            self.boundary_values.append([a, b])
        # print(self.boundary_values)

    def calculate_extreme_values(self):
        for i in range(self.num_param):
            min = self.boundary_values[i][0]
            max = self.boundary_values[i][1]
            nom = int((min+max)/2)
            self.extreme_values.append([min, min+1, max, max-1, nom])

    def formating_data(self):
        header = ["test case"]
        for i in range(self.num_param):
            header.append(f'param{i+1}')
        header.append("expected output")
        self.table.append(header)
        for i in range(self.num_param):
            for j in range(4):
                for k in range(4):
                    


    def get_csv(self):
        self.input_data()
        self.calculate_extreme_values()
        self.formating_data()
        with open('worst.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            for x in self.table:
                wr.writerow(x)


if __name__ == '__main__':
    n = int(input("Enter number of parameter: "))
    bvc = WorstTestCase(n)
    bvc.get_csv()