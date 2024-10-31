def palindr(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]
user_input = input("Введите строку: ")
if palindr(user_input):
    print("строка является палиндром")
else:
    print("Эта строка не является палиндром")