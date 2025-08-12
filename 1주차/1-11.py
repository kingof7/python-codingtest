# 소수 나열하기
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

# input = 20


# def find_prime_list_under_number(number):
#     # 입력된 숫자가 2보다 작으면 빈 리스트 반환
#     if number < 2:
#         return []

#     # 소수를 저장할 리스트 초기화
#     primes = []
#     for x in range(2, number + 1):
#         # 소수는 1과 자기 자신만으로 나누어 떨어지는 수
#         is_prime = True
#         for j in range(2, x // 2 + 1):
#             if x % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(x)
#     return primes


# result = find_prime_list_under_number(input)
# print(result)

# 강사 풀이
input = 20

# 소수의 수학적 개념 : 자기 자신과 1 외에는 아무것도 나눌 수 없다.
prime_list = []


def find_prime_list_under_number(number):
    prime_list = []

    # 2-20까지 찾아서 이것들이 소수인가? 소수라면 prime_list에 넣어라
    for n in range(2, number + 1):  # 2부터 n까지의
        # print(n)
        # 소수로만 나눠보면 됨,2,3,4,5,6, 다나눌필요없음
        for i in prime_list:  # 앞서 찾은 소수들로 나눠보면됨
            if (
                i * i <= n and n % i == 0
            ):  # N의 제곱근보다 크지 않은 어떤 소수로도 나누어 떨어지지 않는다.
                break
        else:
            prime_list.append(n)
    print(prime_list)


find_prime_list_under_number(input)
