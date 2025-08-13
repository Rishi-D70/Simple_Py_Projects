phrase = str(input('Enter your phrase: '))
def Translator(phrase):
    translation = ""
    for everyletter in phrase:
        if everyletter in "aeiouAEIOU":
            translation += "<3"
        else:
            translation += everyletter
    return translation
print(Translator(phrase))