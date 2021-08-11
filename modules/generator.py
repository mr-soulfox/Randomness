from random import randint
import matplotlib.pyplot as graphic


class Generator:
    """DOCUMENTATION... (read Documentation/Generator.txt)"""

    array = []
    result_array = []
    num_max: int
    type: bool

    def __init__(self, repeated: int, num_max: int, with_sum: bool):
        print('Initialize number generator... \n')
        self.clear()
        self.type = with_sum
        self.num_max = num_max
        self.generate_numbers(repeated)
        self.create_graphic()

    def clear(self):
        self.array = []
        self.result_array = []

    def analyse_result(self):
        print(f'Max number in array: {max(self.array)}')

        for i in range(max(self.array) + 1):
            self.result_array.append(self.array.count(i))

        print(f'Amount numbers repeated (0 - {max(self.array)}): {self.result_array}')

        max_result = max(self.result_array)

        print(f'Maximum number in result: {max_result} in position {self.result_array.index(max_result)}')

    def save_number(self, num):
        if self.type:
            num_to_sum = randint(0, self.num_max)
            self.array.append(num + num_to_sum)

        else:
            self.array.append(num)

    def generate_numbers(self, rng):
        for _ in range(rng):
            num: int = randint(0, self.num_max)
            self.save_number(num)

        print(f'Generated array: {self.array}')
        self.analyse_result()

    def create_graphic(self):
        num_max = max(self.result_array) + 50
        labels = []

        for i in range(max(self.array) + 1):
            labels.append(str(i))

        graphic.title('RANDOM GENERATED GRAPHIC')
        graphic.ylabel('REPEATED', color='blue')
        graphic.xlabel('NUMBERS', color='green')
        graphic.axis(ymin=0, ymax=num_max)
        graphic.bar(labels, self.result_array)
        graphic.show()
