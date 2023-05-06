from janome.tokenizer import Tokenizer
import markovify
import subprocess
from subprocess import PIPE

file = '/home/mumeinosato/discord-bot/markovi.txt' 
f = open(file, 'r', encoding="utf-8")
text = f.read()

def text_split(text):
    str_table = str.maketrans({
        '。': '',   
        '\n': '。',
        '\r': '',
        '(': '（',
        ')': '）',
        '[': '［',
        ']': '］',
        '"':'”',
        "'":"’",
    })
    text = text.translate(str_table)
    t = Tokenizer()
    tokens = t.tokenize(text, wakati=True)
    splitted_text_list = []
    for i in tokens:
        if i != '。' and i != '！' and i != '？':
            i += ' '
        elif i == '。' or i == '！' or i == '？':
            i = '\n'
        splitted_text_list.append(i)
        splitted_text_str = "".join(splitted_text_list)

    return splitted_text_str

splitted_text_str = text_split(text)
text_model_3 = markovify.NewlineText(splitted_text_str, state_size=3)

for i in range(1):
    out = text_model_3.make_sentence(tries=100)
    print(out)
    f = open('/home/mumeinosato/discord-bot/marukovi_output.txt', 'w')
    f.write(out)
    f.close()
