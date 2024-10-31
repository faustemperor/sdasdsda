text = input("Введите текст: ")
reserved_words_input = input("Введите зарезервированные слова, разделённые запятыми: ")
reserved_words = [word.strip() for word in reserved_words_input.split(',')]
for word in reserved_words:
    text = text.replace(word, word.upper())
print("Изменённый текст:")
print(text)