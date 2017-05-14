def most_freq(text, k):
    kmers = {}
    for i in range(len(text) - k + 1):
        key = text[i:i+k]
        if kmers.get(key) is not None:
            kmers[key] += 1
        else:
            kmers[key] = 0
    max_value = max(kmers.values())

    answer = []
    for k, v in kmers.items():
        if v == max_value:
            answer.append(k)
    return answer


def main():
    text = input()
    k = int(input())
    print(' '.join(most_freq(text, k)))


if __name__ == '__main__':
    main()