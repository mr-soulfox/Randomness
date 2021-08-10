from random import randint


class Generator:

    array = []
    result_array = []
    num_max: int
    type: bool

    def __init__(self, repeated: int, num_max: int, with_sum: bool):
        print('Initialize number generator... \n')
        self.type = with_sum
        self.num_max = num_max
        self.generate_numbers(repeated)

    def analyse_result(self):
        print(f'Max number in array: {max(self.array)}')

        for i in range(max(self.array)):
            self.result_array.append(self.array.count(i))

        print(f'Amount numbers repeated (0 - {max(self.array)}): {self.result_array}')

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
