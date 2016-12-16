## This assembler is an unfinished vertion of graph assembler that is able to assemble only 4 alien chromosomes out of 6.

class Graph:
    def __init__(self):
        self.forward = {}
        self.seqf = []

    def add_edge(self, a, b):
        if a in self.forward:
            if b not in self.forward[a]:
                self.forward[a].append(b)
        else:
            self.forward[a] = [b]
        if b not in self.forward:
            self.forward[b] = []

    # идем по дереву вправо и влево
    def get_v(self, kmer):
        cnt = 0
        start = kmer
        path = [kmer]
        print('Assembling sequence...')
        print(path)
        print('kmer = ', kmer)
        while kmer in self.forward:
            cnt += 1
            if len(self.forward[kmer]) == 1:
                if cnt % 10000 == 0:
                    print('len(self.forward[kmer]) == 1')
                nt = ''.join(self.forward[kmer])
                path.append(nt[-1])
                kmer = nt
                if kmer not in self.forward or len(self.forward[kmer]) == 0 or kmer == start:
                    break
            elif len(self.forward[kmer]) > 1:
                print('len(self.forward[kmer]) > 1')
                print(self.forward[kmer])
                shortest = []
                for el in self.forward[kmer]:
                    if el == start:
                        return path
                    print('el = ', el)
                    tmp = self.get_v(el)
                    #print('tmp = ', tmp)
                    if el in path:
                        return path
                    elif len(tmp) > 0:
                        #print(path)
                        newpath = path + tmp
                        if not shortest:
                            shortest = newpath
                        elif len(newpath) < len(shortest):
                            shortest = newpath
                    else:
                        break
                path = shortest

            if kmer == start:
                break
        print("Finished assembling")
        return path

    def get_seq(self, kmer):
        return ''.join(self.get_v(kmer))

    def stats(self):
        stats_f = {}
        starts = []
       for key, value in self.forward.items():
            if len(value) == 0:
                stats_f[key] = 0
            elif len(value) > 1:
                stats_f[key] = [len(value)]
                stats_f[key].extend(value)
            else:
                nt = ''.join(value)
                if nt not in self.forward:
                    starts.append(nt)
        return '%s\n%s' % (stats_f , starts) #stats_r

    def __str__(self):
        return ''.join(self.seqf)
        #return '%s%s' % (''.join(self.seqr), ''.join(self.seqf))

    def __len__(self):
        return len(self.forward)


k = 35
chr = Graph()

with open('alien.dna') as file, open('assembled4.txt', 'w') as outp:
    x = 0
    for read in file:
        # Нарезаем наши риды на k-меры и добавляем в словарь-граф
        read = read.strip()
        x += 1
        i = 0
        while i < len(read) - (k+1):
            sample1 = read[i:(i + k)]
            sample2 = read[i+1:(i + k+1)]
            chr.add_edge(sample1, sample2)
            i += 1
    print('Finished graph generation')
    print(x, 'reads')
    stats = chr.stats()
    print(stats)
    #kmer = 'TNIBTTITIIBSSOTTSBONNOTISSOSNISOINS' #2
    #kmer = 'ONONITSSSOITNNNSNNINNTNONIBISBSBTBB' #1
    #kmer = 'OBSBOBOOSSTSOOSISSNNOINIITOIONOSIBB' #3
    kmer = 'SSOSOTISISOSSBSIISSTONNISSTOSNSOOII' #4
    #kmer = 'NOOBIBBBOOTSBTNNBOTONTBNOBONNNNONOT' #5
    #kmer = 'NOIBIOOOSOSIINOTOOSTONOSNTBTNBBNSBB' #6

    assembled = chr.get_seq(kmer)
    print(len(assembled))
    outp.write('%i\n%s\n' % (len(assembled), assembled))
    #print('File Alien.dna.aligned has been written successfully!')
