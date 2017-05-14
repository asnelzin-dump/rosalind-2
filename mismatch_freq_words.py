import itertools
import collections


def change_letters(original, positions, exchanges):
    result = list(original)
    for index, char in zip(positions, exchanges):
        result[index] = char
    return ''.join(result)


def generate_neighbors(original, distance):
    result = set()
    alphabet = 'ATGC'
    for dist in range(1, distance + 1):
        for positions in itertools.combinations(range(len(original)), dist):
            for exchanges in itertools.product(alphabet, repeat=dist):
                result.add(change_letters(original, positions, exchanges))
    return result


def main():
    data = input().split()
    text, k, d = data[0], int(data[1]), int(data[2])

    all_neighbors = []

    for i in range(len(text) - k + 1):
        substring = text[i:i+k]
        all_neighbors += generate_neighbors(substring, d)

    number_of_neighbors = collections.Counter(all_neighbors)

    max_value = max(number_of_neighbors.values())

    answer = []
    for item, value in number_of_neighbors.items():
        if value == max_value:
            answer.append(item)

    print(' '.join(answer))


if __name__ == '__main__':
    main()