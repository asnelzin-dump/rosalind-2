def skew(i, genome):
    prefix = genome[:i]
    return prefix.count('G') - prefix.count('C')


def main():
    genome = input()

    skews = [skew(i, genome) for i in range(len(genome) + 1)]
    min_skew = min(skews)
    answer = []
    for i, val in enumerate(skews):
        if val == min_skew:
            answer.append(str(i))
    print(' '.join(answer))


if __name__ == '__main__':
    main()