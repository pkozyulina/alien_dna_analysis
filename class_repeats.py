import itertools
x = ["B", "I", "N", "O", "S", "T"]

class Repeats():
    def __init__(self, n, alphabet): # n =  длина повтора, alphabet = алфавит, на основе которого генерим
        self.variants = set(''.join(p) for p in itertools.product(alphabet, repeat=n)) # генерируем рандомные
                                                                    # последовательности заданной длинны из алфавита X
        self.repeats = {} # key = повтор, value = [количество вхождений повтора в А, количество вхождений повтора в B]
        self.freq_a = {}
        self.freq_b = {}
        self.freq = {}
        self.n = n
    def count_repeats(self, a, b): # читаем повторы парных хромосом (a, b)
        for repeat in self.variants:
            a_freq = a.count(str(repeat))
            b_freq = b.count(str(repeat))
            self.repeats[repeat] = [a_freq, b_freq]
            if a_freq in self.freq_a:
                self.freq_a[a_freq].append(str(repeat))
            else:
                self.freq_a[a_freq] = [str(repeat)]
            if b_freq in self.freq_b:
                self.freq_b[b_freq].append(str(repeat))
            else:
                self.freq_b[b_freq] = [str(repeat)]

    def count_repeats_list(self, flist): # считаем повторы из списка фрагментов последовательности
        for repeat in self.variants:
            for fragment in flist:
                freq = fragment.count(str(repeat))
                self.repeats[repeat] = freq
                if freq in self.freq:
                    self.freq[freq].append(str(repeat))
                else:
                    self.freq[freq] = [str(repeat)]

    def max_freq(self, threshhold=10): # определяем наиболее часто встречаемые последовательности для пары хромосом
        max_a = {}
        max_b = {}
        for key in self.freq_a:
            if key > threshhold:
                max_a[key] = self.freq_a[key]
        for key in self.freq_b:
            if key > threshhold:
                max_b[key] = self.freq_b[key]
        return max_a, max_b

    def max_freq_list(self, threshhold=10): # определяем наиболее часто встречаемые последовательности для списка
        max_list = {}
        for key in self.freq:
            if key > threshhold:
                max_list[key] = self.freq[key]
        return max_list
