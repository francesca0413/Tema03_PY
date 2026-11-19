def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word.lower()))
        groups.setdefault(key, []).append(word)
    return list(groups.values())


def main():
    words = input("Words: ").split()
    groups = group_anagrams(words)

    for group in groups:
        print(", ".join(sorted(group, key=str.lower)))

    if groups:
        largest = max(groups, key=len)
        print()
        print(f"Largest group: {', '.join(sorted(largest, key=str.lower))} (size {len(largest)})")


if __name__ == "__main__":
    main()