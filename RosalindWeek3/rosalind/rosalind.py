import itertools
import collections


def skew(i, genome, skews):
    current = 0
    if genome[i - 1] == 'G':
        current = 1
    if genome[i - 1] == 'C':
        current = -1
    return skews[i - 1] + current


def min_skew(genome):
    skews = [0]
    for i in range(1, len(genome)):
        skews.append(skew(i, genome, skews))

    lowest = min(skews)
    return [pos for pos, value in enumerate(skews) if value == lowest]


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


def reverse_pattern(original):
    ans = ''
    for n in reversed(original):
        if n == 'A':
            ans += 'T'
        if n == 'T':
            ans += 'A'
        if n == 'G':
            ans += 'C'
        if n == 'C':
            ans += 'G'
    return ans


def find_dnaa(clump):
    k, d = 9, 1
    all_neighbors = []

    for i in range(len(clump) - k + 1):
        substring = clump[i:i+k]
        all_neighbors += generate_neighbors(substring, d)
        all_neighbors += generate_neighbors(reverse_pattern(substring), d)

    number_of_neighbors = collections.Counter(all_neighbors)

    max_value = max(number_of_neighbors.values())

    answer = []
    for item, value in number_of_neighbors.items():
        if value == max_value:
            answer.append(item)

    return answer


def diff(s1, s2):
    "Return the Hamming distance between equal-length sequences."
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def count(pattern, all_kmers, d):
    answer = 0
    for kmer in all_kmers:
        if diff(pattern, kmer) <= d:
            answer += 1
    return answer - 1


def find_dnaa_wo_generation(clump):
    k, d = 9, 1
    all_kmers = []
    for i in range(len(clump) - k + 1):
        kmer = clump[i:i+k]
        all_kmers.append(kmer)

    counts_kmers = {}
    for kmer in all_kmers:
        if counts_kmers.get(kmer) is None:
            counts_kmers[kmer] = count(kmer, all_kmers, d) + count(reverse_pattern(kmer), all_kmers, d)
    max_value = max(counts_kmers.values())

    answer = []
    for item, value in counts_kmers.items():
        if value == max_value:
            answer.append(item)

    return answer




