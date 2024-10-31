import re

text = input("Введите текст: ")
sentences = re.split(r'[.!?]+', text)
sentence_count = len([s for s in sentences if s.strip()])
print("Количество предложений в тексте:", sentence_count)