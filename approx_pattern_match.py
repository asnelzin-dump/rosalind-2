def edit_diff(str, original):
    count = 0
    chars = list(zip(str, original))
    for a, b in chars:
        if a != b:
            count += 1
    return count


def main():
    pattern = input()
    text = input()
    d = int(input())

    k = len(pattern)
    answer = []
    for i in range(len(text) - k + 1):
        if edit_diff(text[i:i + k], pattern) <= d:
            answer.append(str(i))

    print(' '.join(answer))

if __name__ == '__main__':
    main()