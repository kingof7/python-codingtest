str = "aabbccdd"  # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

unique_list = [v for v in str if str.count(v) == 1]

if unique_list:
    print(unique_list[0])
else:
    print("_")
