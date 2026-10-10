from pprint import pprint

# O()
def nicelySorted[T](k: list[list[T]]) -> list[list[T]]:

    def size_and_content(value: list[T]) -> tuple[int, list[T]]:
        return (len(value), value)

    return sorted(k, key=size_and_content)

# O(2^N)
def combinations[T](k: list[T], v: int) -> list[list[T]]:
    return [t for t in powerSet(k) if len(t) == v]

# O(1)
def insert[T](k: T, v: list[T], h: int) -> list[T]:
    return v[:h] + [k] + v[h:]

# O(N)
def insertEverywhere[T](k: T, v: list[T]) -> list[list[T]]:
    return [insert(k, v, h) for h in range(len(v) + 1)]

# O()
def permute[T](k: list[T]) -> list[list[T]]:
    if not k:
        return [[]]
    empty: list[list[T]] = []
    return nicelySorted(sum([insertEverywhere(k[-1], v) for v in permute(k[:-1])], empty))

def permutations[T](k:list[T], v: int) -> list[list[T]]:
    return sum([permute(e) for e in combinations(k, v)], [])

# O(2 ^ N)
def powerSet[T](k: list[T]) -> list[list[T]]:
    if not k:
        return[[]]
    temp: list[list[T]] = powerSet(k[:-1])
    return temp + [e + [k[-1]] for e in temp]

# O()
def permutations_with_repetition[T](s: list[T], k: int) -> list[list[T]]:
    ...

# O()
def combinations_with_repetition[T](s: list[T], k: int) -> list[list[T]]:
    ...

if __name__ == '__main__':
    # pprint(nicelySorted(powerSet([1, 2, 3, 4])))
    # print()
    # # pprint(nicelySorted(powerSet(['a', 'b', 'c', 'd'])))
    # # print()
    # pprint(combinations([1, 2, 3, 4], 3))
    # print()
    # pprint(permute([1, 2, 3]))
    # print()
    # pprint(permutations([1, 2, 3], 2))
    print()