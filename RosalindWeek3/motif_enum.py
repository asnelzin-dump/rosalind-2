import rosalind.rosalind as rosalind
import sys


def is_appears(dna, motif, d):
    k = len(motif)
    all_kmers = [dna[i:i + k] for i in range(0, len(dna) - k + 1)]
    for kmer in all_kmers:
        if rosalind.diff(motif, kmer) <= d:
            return True
    return False


def motif_enumeration(dnas, k, d):
    big_dna = ''.join(dnas)
    all_kmers = [big_dna[i:i + k] for i in range(0, len(big_dna) - k + 1)]
    answer = []
    for kmer in all_kmers:
        neighbors = rosalind.generate_neighbors(kmer, d)
        for motif in neighbors:
            if all([is_appears(dna, motif, d) for dna in dnas]):
                if not motif in answer:
                    answer.append(motif)
    return answer


def main():
    sys.stdin = open('input', 'r')
    k, d = [int(i) for i in input().split()]
    dnas = []
    for line in sys.stdin:
        dnas.append(line[:-1])
    print(' '.join(motif_enumeration(dnas, k, d)))



if __name__ == '__main__':
    main()