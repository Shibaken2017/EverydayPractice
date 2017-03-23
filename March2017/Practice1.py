'''
Introduction to Algorithm(MIT Press) p18のpesudo codeの実装

'''


class InsertionSort():
    def __init__(self):
        self.num_list = []

    def load_file(self, input_fname):
        self.num_list = []
        with open(input_fname, "r", encoding="UTF-8")as reader:
            for line in reader:
                tmp = line.replace("\n", "")
                if (len(tmp) > 0):
                    self.num_list.append(int(tmp))

    def sort(self):

        for j in range(1, len(self.num_list)):

            tmp = self.num_list[j]
            i = j - 1
            while i >= 0 and self.num_list[i] > tmp:
                self.num_list[i + 1] = self.num_list[i]
                i = i - 1
            self.num_list[i + 1] = tmp

    def writeTxt(self, output_fname):
        with open(output_fname, "w", encoding="UTF-8")as writer:
            for num in self.num_list:
                writer.write(str(num) + "\n")

    def exec(self, input_fname, output_fname):
        self.load_file(input_fname)
        self.sort()
        self.writeTxt(output_fname)


if __name__ == '__main__':
    input_fname = r'C:\Users\kentaro\PycharmProjects\Practice\TestData\num.txt'
    output_fname = r'C:\Users\kentaro\PycharmProjects\Practice\TestData\sortedNum.txt'
    sort = InsertionSort()
    sort.exec(input_fname, output_fname)
