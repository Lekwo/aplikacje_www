def f(text, letter):
    return text.lower().replace(letter.lower(), "")


text = "Mam na imię Rafał"
letter = "M"
print(f(text, letter))
