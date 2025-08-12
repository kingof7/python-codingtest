str = "abadabac"  # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

# Create a list of characters with count 1
unique_chars = [v for v in str if str.count(v) == 1]

print(unique_chars)

# Print the first character from the list
if unique_chars:
    print(unique_chars[0])
else:
    print("_")
