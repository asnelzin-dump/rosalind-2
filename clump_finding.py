import sys

def most_freq(text, k, t):
    kmers = {}
    for i in range(len(text) - k + 1):
        key = text[i:i+k]
        if kmers.get(key) is not None:
            kmers[key] += 1
        else:
            kmers[key] = 1

    answer = []
    for k, v in kmers.items():
        if v >= t:
            answer.append(k)
    return answer


def main():
    genome = ''
    try:
        f = open(sys.argv[1], 'r')
        try:
            genome = f.readline()[:-1]
            k, L, t = (int(i) for i in f.readline().split())
        finally:
            f.close()
    except IOError:
        print("Error: Can't find file or read data")

    if genome != '':
        answer = []
        for i in range(len(genome) - L + 1):
            text = genome[i:i+L]
            for item in most_freq(text, k, t):
                if item not in answer:
                    answer.append(item)
        print(' '.join(answer))

if __name__ == '__main__':
    main()