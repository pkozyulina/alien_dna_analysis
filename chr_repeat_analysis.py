from repeats import Repeats

# Читаем последовательность ДНК из файла
ch = []
with open("alien_chromosomes_final.txt") as f:
    for line in f:
        ch.append(line.strip())

# Разбиваем на хромосомы
fst = ch[0]
sec = ch[1]
sec = sec[166103:] + sec[:166103]
th = ch[2]
fo = ch[3]
fi = ch[4]
si = ch[5]

# Анализируем пары хромосом при помощи функций класса Repeats
a = fst
b = sec

with open('repeats_fst_sec.txt', 'w') as file:

    print('<<<<<<<<<<< 6x repeats >>>>>>>>>>>')
    rep6 = Repeats(6, x)
    rep6.count_repeats(a, b)
    max6_a, max6_b = rep6.max_freq(100)
    print(max6_a)
    print(max6_b)
    print(max6_a.keys())
    print(max6_b.keys())
    file.write('%s\n%s\n%s\n%s\n' % (max6_a.keys(), max6_b.keys(), max6_a, max6_b))

    print('<<<<<<<<<<< 7x repeats >>>>>>>>>>>')
    rep7 = Repeats(7, x)
    rep7.count_repeats(a, b)
    max7_a, max7_b = rep7.max_freq(50)
    print(max7_a)
    print(max7_b)
    print(max7_a.keys())
    print(max7_b.keys())
    file.write('%s\n%s\n%s\n%s\n' % (max7_a.keys(), max7_b.keys(), max7_a, max7_b))

    print('<<<<<<<<<<< 8x repeats >>>>>>>>>>>')
    rep8 = Repeats(8, x)
    rep8.count_repeats(a, b)
    max8_a, max8_b = rep8.max_freq(50)
    print(max8_a)
    print(max8_b)
    print(max8_a.keys())
    print(max8_b.keys())
    file.write('%s\n%s\n%s\n%s\n%s\n' % ('<<<<<<<<<<< 8x repeats >>>>>>>>>>>', max8_a.keys(), max8_b.keys(), max8_a, max8_b))

