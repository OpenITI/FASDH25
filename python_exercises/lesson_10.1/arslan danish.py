Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\hp\Downloads\FASDH25\python_exercises\lesson_10.1\arsalan_danish_6.py
found Jabalia 39 times
found Khan Younis 93 times
found Rafah 98 times
found Nuseirat 41 times
found Bureij 27 times
found Maghazi 41 times
found Shokat as-Sufi 3 times
found Qizan 3 times
found Al-Azhar University 3 times
found Al-Aqsa University 3 times
found Gaza 570 times
found Gaza Strip 72 times
found Gaza City 30 times
Traceback (most recent call last):
  File "C:\Users\hp\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: False

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\hp\Downloads\FASDH25\python_exercises\lesson_10.1\arsalan_danish_6.py", line 85, in <module>
    write_tsv(patterns, columns, tsv_filename)
  File "C:\Users\hp\Downloads\FASDH25\python_exercises\lesson_10.1\arsalan_danish_6.py", line 34, in write_tsv
    df = pd.DataFrame.from_records(items, columns=column_list, index=False)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\frame.py", line 2518, in from_records
    i = columns.get_loc(index)
  File "C:\Users\hp\AppData\Local\Programs\Python\Python313\Lib\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: False
