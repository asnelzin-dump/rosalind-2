import itertools
import collections


def change_position(original, positions, exchanges):
    result = list(original)
    for index, char in zip(positions, exchanges):
        result[index] = char
    return ''.join(result)


def generate_neighbors(original, distance):
    result = set()
    alphabet = 'ATGC'
    for d in range(1, distance + 1):
        for p in itertools.combinations(range(len(original)), d):
            for e in itertools.product(alphabet, repeat=d):
                result.add(change_position(original, p, e))
    return result


def main():
    data = input().split()
    text, k, d = data[0], int(data[1]), int(data[2])

    all_neighbors = []
    substrings = []

    for i in range(len(text) - k + 1):
        substring = text[i:i+k]
        substrings.append(substring)
        all_neighbors += generate_neighbors(substring, d)

    counts = collections.Counter(all_neighbors)

    max_value = max(counts.values())

    answer = []
    for item, value in counts.items():
        if value == max_value:
            answer.append(item)

    print(' '.join(answer))

if __name__ == '__main__':
    main()