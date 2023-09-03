# 枠で囲む

text = input()

length = len(text)

frame = '+' * (length + 2)

decorated_text = f"+{text}+"

print(frame)
print(decorated_text)
print(frame)