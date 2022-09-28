def palindrome(word: str, idx: int):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"

    first, last = word[idx], word[-1 - idx]

    if first != last:
        return f"{word} is not a palindrome"

    return palindrome(word, idx + 1)
