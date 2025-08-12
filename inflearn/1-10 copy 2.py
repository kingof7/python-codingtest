def find_not_repeating_first_character(string):
    alpha_array = [0] * 26

    # O(N), string의 길이 만큼
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alpha_array[arr_index] += 1

    not_repeat_array = []

    # O(1), alpha_array의 길이는 항상 26이므로
    for index in range(len(alpha_array)):
        alpha_count = alpha_array[index]
        if alpha_count == 1:
            not_repeat_array.append(chr(index + ord("a")))

    # O(N), string의 길이 만큼
    for char in string:
        if char in not_repeat_array:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))
