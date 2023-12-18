from functools import cache

ifile = '2023/input/day12.txt'

@cache
def dp(string, rest, count=0):
    if not rest:
        return '#' not in string
    current, rest = rest[0], rest[1:]
    for i in range(len(string) - current - sum(rest) - len(rest) + 1):
        if "#" in string[:i]:
            break
        if (nxt := i + current) <= len(string) and '.' not in string[i : nxt] and string[nxt : nxt + 1] != "#":
            count += dp(string[nxt + 1:], rest)
    return count

if __name__ == "__main__":
    with open(ifile, "r") as f:
        data = [x.split() for x in f.read().splitlines()]
        p1, p2 = 0, 0
        for e, (string, numbers) in enumerate(data):
            p1 += dp(string, (numbers := tuple(map(int, numbers.split(",")))))
            p2 += dp("?".join([string] * 5), numbers * 5)
    print('Result Part1:',p1)
    print('Result Part2:',p2)
