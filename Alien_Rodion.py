chr1 = ''
chr2 = ''
chr3 = ''
chr4 = ''
chr5 = ''
chr6 = ''


def nucl_count(x):
    dct = {'B': 0, 'I': 0, 'N': 0, 'O': 0, 'S': 0, 'T': 0}
    for j in x:
        dct[j] += 1
    return dct


print(nucl_count(chr1))
print(nucl_count(chr2))
print(nucl_count(chr3))
print(nucl_count(chr4))
print(nucl_count(chr5))
print(nucl_count(chr6))


def nucl_freq(x):
    return {nucl: (x.count(nucl) / float(len(x)) * 100) for nucl in 'BINOST'}


print(nucl_count(chr1))
print(nucl_count(chr2))
print(nucl_count(chr3))
print(nucl_count(chr4))
print(nucl_count(chr5))
print(nucl_count(chr6))


def spatial_distribution(x):
    p = []
    for i in range(0, len(x), 6):
        p.append(x[i:i + 8])
    print(p)


spatial_distribution(chr1)
spatial_distribution(chr2)
spatial_distribution(chr3)
spatial_distribution(chr4)
spatial_distribution(chr5)


def longest_string(chr1, chr2):
    K = [[0] * (1 + len(chr2)) for i in range(1 + len(chr1))]
    long = 0
    long2 = 0
    for x in range(1, 1 + len(chr1)):
        for y in range(1, 1 + len(chr2)):
            if chr1[x - 1] == chr2[y - 1]:
                K[x][y] = K[x - 1][y - 1] + 1
                if K[x][y] > long:
                    long = K[x][y]
                    long2 = x
            else:
                K[x][y] = 0
    return chr1[long2 - long: long2]


def find_common_patterns(chr1, chr2):
    if chr1 == '' or chr2 == '':
        return [], []
    com = longest_string(chr1, chr2)
    if len(com) < 2:
        return ([(0, chr1)], [(0, chr2)])
    chr1_bef, _, chr1_aft = chr1.partition(com)
    chr2_bef, _, chr2_aft = chr2.partition(com)
    before = find_common_patterns(chr1_bef, chr2_bef)
    after = find_common_patterns(chr1_aft, chr2_aft)
    return (before[0] + [(1, com)] + after[0],
            before[1] + [(1, com)] + after[1])


import itertools

x = ["B", "I", "N", "O", "S", "T"]
w2 = [p for p in itertools.product(x, repeat=2)]
w3 = [p for p in itertools.product(x, repeat=3)]
w4 = [p for p in itertools.product(x, repeat=4)]
w5 = [p for p in itertools.product(x, repeat=5)]
w6 = [p for p in itertools.product(x, repeat=6)]
w7 = [p for p in itertools.product(x, repeat=7)]
# w8 = [p for p in itertools.product(x, repeat=8)]
# w9 = [p for p in itertools.product(x, repeat=9)]
# w10 = [p for p in itertools.product(x, repeat=10)]
# w11 = [p for p in itertools.product(x, repeat=11)]
# w12 = [p for p in itertools.product(x, repeat=12)]
# w13 = [p for p in itertools.product(x, repeat=13)]
# w16 = [p for p in itertools.product(x, repeat=16)]

# print(len(w7))
# print(len(w2), len(w3), len(w4), len(w5), len(w6), len(w7))

# print(len(w2), len(w3), len(w4), len(w5), len(w6), len(w7), len(w8), len(w9), len(w10), len(w11), len(w12), len(w13), len(w16))
# количество уникальных n-х буквенных кодонов из 6 букв -
# 36 216 1296 7776 46656




number_of_codons2_in_a = []
number_of_codons2_in_b = []
number_of_codons3_in_a = []
number_of_codons3_in_b = []
number_of_codons4_in_a = []
number_of_codons4_in_b = []
number_of_codons5_in_a = []
number_of_codons5_in_b = []
number_of_codons6_in_a = []
number_of_codons6_in_b = []
number_of_codons7_in_a = []
number_of_codons7_in_b = []
number_of_codons8_in_a = []
number_of_codons8_in_b = []

codons2 = []
for i in w2:
    codons2.append(''.join(i))
# print(codons2)

for i in codons2:
    number_of_codons2_in_a.append(chr1.count(i))
    number_of_codons2_in_b.append(chr2.count(i))
# print(number_of_codons2_in_a, "\n", number_of_codons2_in_b)
print(max(number_of_codons2_in_a), min(number_of_codons2_in_a))
print(max(number_of_codons2_in_b), min(number_of_codons2_in_b))

codons3 = []
for i in w3:
    codons3.append(''.join(i))
# print(codons3)

for i in codons3:
    number_of_codons3_in_a.append(chr1.count(i))
    number_of_codons3_in_b.append(chr2.count(i))
# print(number_of_codons3_in_a, "\n", number_of_codons3_in_b)

print(max(number_of_codons3_in_a), min(number_of_codons3_in_a))
print(max(number_of_codons3_in_b), min(number_of_codons3_in_b))

codons4 = []
for i in w4:
    codons4.append(''.join(i))
# print(codons4)

for i in codons4:
    number_of_codons4_in_a.append(chr1.count(i))
    number_of_codons4_in_b.append(chr2.count(i))
# print(number_of_codons4_in_a, "\n", number_of_codons4_in_b)
print(max(number_of_codons4_in_a), min(number_of_codons4_in_a))
print(max(number_of_codons4_in_b), min(number_of_codons4_in_b))

codons5 = []
for i in w5:
    codons5.append(''.join(i))
# print(codons5)

for i in codons5:
    number_of_codons5_in_a.append(chr1.count(i))
    number_of_codons5_in_b.append(chr2.count(i))
# print(number_of_codons5_in_a,"\n", number_of_codons5_in_b)
print(max(number_of_codons5_in_a), min(number_of_codons5_in_a))
print(max(number_of_codons5_in_b), min(number_of_codons5_in_b))

codons6 = []
for i in w6:
    codons6.append(''.join(i))
# print(codons6)

for i in codons6:
    number_of_codons6_in_a.append(chr1.count(i))
    number_of_codons6_in_b.append(chr2.count(i))
# print(number_of_codons6_in_a,"\n", number_of_codons6_in_b)
print(max(number_of_codons6_in_a), min(number_of_codons6_in_a))
print(max(number_of_codons6_in_b), min(number_of_codons6_in_b))

codons7 = []
for i in w7:
    codons7.append(''.join(i))
print(codons7)

for i in codons7:
    number_of_codons7_in_a.append(chr1.count(i))
    number_of_codons7_in_b.append(chr2.count(i))
print(number_of_codons7_in_a, number_of_codons7_in_b)
