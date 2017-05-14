masses = [[57], [71], [87], [97], [99], [101], [103], [113],
          [114], [115], [128], [129], [131], [137], [147],
          [156], [163], [186]]


def generate_subpeptides(peptide):
    answer = list()
    size = len(peptide)
    for i in range(1, size):
        for j in range(size):
            subpeptide = []
            for k in range(i):
                subpeptide.append(peptide[(j + k) % size])
            answer.append(subpeptide)
    return answer


def cyclospectrum(peptide):
    subpeptides = generate_subpeptides(peptide)
    spectrum = list()

    spectrum.append(0)
    for i in subpeptides:
        spectrum.append(sum(i))
    spectrum.append(sum(peptide))
    return spectrum


def expand(leader_board, spectrum):
    result = list()
    for peptide, _ in leader_board:
        for addition in masses:
            item = peptide.copy()
            item.append(addition[0])
            result.append([item, score(item, spectrum)])
    return result


def score(peptide, spectrum):
    result = 0
    peptide_spectrum = cyclospectrum(peptide)
    for i in spectrum:
        for j in peptide_spectrum[:]:
            if i == j:
                result += 1
                peptide_spectrum.remove(j)
    return result


def cut(leader_board, N):
    if not leader_board:
        return []

    sorted_board = sorted(leader_board, key=lambda x: x[1], reverse=True)
    max_score = sorted_board[0][1]
    if len(sorted_board) < N:
        return sorted_board
    else:
        last_score = sorted_board[N - 1][1]
        if last_score == max_score:
            return sorted_board[:N]
        else:
            result = []
            for peptide, rate in sorted_board:
                if rate < last_score:
                    return result
                else:
                    result.append([peptide, rate])
            return result


def cyclopeptide_sequencing(spectrum, N):
    parent_mass = spectrum[-1]
    leader_board = [[peptide, score(peptide, spectrum)] for peptide in masses]
    leader_peptide = []
    leader_score = 0

    while leader_board:
        print(len(leader_board))
        for peptide, peptide_score in leader_board[:]:
            mass_peptide = sum(peptide)
            if mass_peptide == parent_mass:
                if peptide_score > leader_score:
                    leader_peptide = peptide
                    leader_score = peptide_score
            elif mass_peptide > parent_mass:
                leader_board.remove([peptide, peptide_score])

        leader_board = cut(leader_board, N)
        leader_board = expand(leader_board, spectrum)

    return leader_peptide


def main():
    N = int(input())
    data = input()
    spectrum = [int(mass) for mass in data.split()]
    print(cyclopeptide_sequencing(spectrum, N))


if __name__ == '__main__':
    main()