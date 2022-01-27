def name(text):
    text = print(f'Hello, {text}')
    return text
mess = input('enter name: ').split()
for i in mess:
    name(i)