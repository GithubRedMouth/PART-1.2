'''
узнал как работать с файлами. то что их нужно закрвыть. как записывать или удалять или добавлять и так же вывордить
'''

f = open('file.txt', 'r', encoding='utf-8')
text = f.read(2)
text2 = f.read(8)
print(f.encoding)
text = f.read()
f.close()
print(text)
print(text2)

f = open('file.txt', 'a', encoding='utf-8')
f.write('Новая строка\n')
f.close()