Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re
s = "This, is , s, string!"
print(re.split(r",\s+", s))
['This', 'is ', 's', 'string!']
print(re.sub(r",\s*", "\s", s))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(re.sub(r",\s*", "\s", s))
  File "C:\Users\batoo\AppData\Local\Programs\Python\Python313\Lib\re\__init__.py", line 208, in sub
    return _compile(pattern, flags).sub(repl, string, count)
  File "C:\Users\batoo\AppData\Local\Programs\Python\Python313\Lib\re\__init__.py", line 377, in _compile_template
    return _sre.template(pattern, _parser.parse_template(repl, pattern))
  File "C:\Users\batoo\AppData\Local\Programs\Python\Python313\Lib\re\_parser.py", line 1076, in parse_template
    raise s.error('bad escape %s' % this, len(this)) from None
re.PatternError: bad escape \s at position 0

= RESTART: C:\Users\batoo\Downloads\FASDH25\python_exercises\lesson_8.1\zainab_murtazaali_0.py
The path to the article is: aljazeera_articles/2024-03-28_9276.txt


= RESTART: C:\Users\batoo\Downloads\FASDH25\python_exercises\lesson_8.1\zainab_murtazaali_0.py
The path to the article is: aljazeera_articles/2024-03-28_9276.txt

['Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israel', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israeli', 'Israel', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israel', 'Israeli', 'Israeli']
>>> 
= RESTART: C:\Users\batoo\Downloads\FASDH25\python_exercises\lesson_8.1\zainab_murtazaali_0.py
The path to the article is: aljazeera_articles/2024-03-28_9276.txt

2024-03-28_9276.txt contains 54 Israeli? time in the article
['Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israel', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israeli', 'Israel', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israel', 'Israeli', 'Israeli']
>>> 
= RESTART: C:\Users\batoo\Downloads\FASDH25\python_exercises\lesson_8.1\zainab_murtazaali_0.py
The path to the article is: aljazeera_articles/2024-03-28_9276.txt

2024-03-28_9276.txt contains 54 Israeli? time in the article
['Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israel', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israeli', 'Israel', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israeli', 'Israeli', 'Israel', 'Israel', 'Israel', 'Israel', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israeli', 'Israel', 'Israeli', 'Israeli']
>>> 
= RESTART: C:\Users\batoo\Downloads\FASDH25\python_exercises\lesson_8.1\zainab_murtazaali_0.py
The path to the article is: aljazeera_articles/2024-03-28_9276.txt

2024-03-28_9276.txt contains 54 Israeli? time in the article
