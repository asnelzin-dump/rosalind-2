import rosalind.rosalind as rosalind


def main():
    genome = input()
    oriC = min(rosalind.min_skew(genome))
    clump = genome[oriC:oriC + 500]
    print(rosalind.find_dnaa_wo_generation(clump))

if __name__ == '__main__':
    main()