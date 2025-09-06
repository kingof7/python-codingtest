# # sequential search
# finding_target = 14
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# def is_existing_target_number_sequential(target, array):
#     for number in array:
#         if target == number:
#             return True
#     return False


# result = is_existing_target_number_sequential(finding_target, finding_numbers)
# print(result)

# binary search
# 최대와 최소의 중간을 기준 up down
# 시간 복잡도 O(log n)
# finding_target = 5
# finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# def is_existing_target_number_binary(target, array):
#     cnt = 0
#     current_min = 0
#     current_max = len(array) - 1
#     current_guess = (current_min + current_max) // 2  # 중간값, 정수

#     while current_min <= current_max:
#         cnt += 1
#         if array[current_guess] == target:
#             return cnt
#         elif array[current_guess] < target:  # up
#             cnt += 1
#             current_min = (
#                 current_guess + 1
#             )  # 만약 1 ~ 20 사이인 경우 , 15니까 + 1해서 16을 최소로 잡는다
#         else:  # down
#             cnt += 1
#             current_max = (
#                 current_guess - 1
#             )  # 만약 1 ~ 20 사이인 경우, 15니까 - 1 해서 최대 값으로 잡는다
#         current_guess = (current_min + current_max) // 2  # guess 값을 재정의
#     return False


# result = is_existing_target_number_binary(finding_target, finding_numbers)
# print(result)

# 이진 탐색은 기본적으로 정렬이 되어 있어야 함.

f_t = 3
f_n = [0, 3, 5, 9, 6, 2, 1]

f_n.sort()  # 정렬

print(f"정렬된 배열 : {f_n}")


def is_ext_t_n_binary(target, array):
    cnt = 0
    current_min = 0
    current_max = len(array) - 1
    mid = current_min + current_max // 2
    while current_min <= current_max:
        cnt += 1
        if array[mid] == target:
            return cnt
        elif array[mid] < target:
            cnt += 1
            current_min = mid + 1
        elif array[mid] > target:
            cnt += 1
            current_max = mid - 1
        mid = (current_min + current_max) // 2
    return False


result = is_ext_t_n_binary(f_t, f_n)
print(result)
