# Python 書寫規範

## 命名
#### 應該避免的名稱
1. 單字符名稱（a1、a2、...），除了計數器和迭代器。
2. 套件 / 模組中的連字符（-）。
3. 雙底線開頭並結尾的名稱（Python 保留，例如__init__）。

#### 命名約定
1. 將相關的類別和函數放在同一個模組裡。沒必要限制一個類別一個模組。
2. `模組名稱` 使用底線分隔不同單字 `ex: linebot_service.py`
3. `類別名稱` 使用 Pascal 命名法 `ex: class LineUtility（）:`
4. `函數名稱` 使用 Camel 命名法 `ex: def creatConnection（）:`
5. `常數名稱` 使用全大寫英文加上底線 `ex: GET_USER_PROFILE_URL`
6. `變數名稱` 使用小寫英文加上底線 `ex: my_headers`


## 注釋
#### Comment Block & Comment Line
* 最需要寫註釋（comment）的是代碼中那些技巧性的部分，如果你在下次代碼審查的時候必須解釋一下，那麼你應該現在就給它寫註釋。
* 對於複雜的操作，應該在其操作開始前寫上若干行註釋。對於不是一目瞭然的代碼，應在其行尾添加註釋。
* 為了提高可讀性，註釋應該至少離開程式碼 1 個空格。

`EX`
```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.

if i & (i-1) == 0:        # true iff i is a power of 2
```
* 在註釋中，將長的 URL 放在一行上。

`YES`
```python
# See details at
# http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
```
`NO`
```python
# See details at
# http://www.example.com/us/developer/documentation/api/content/\
# v2.0/csv_file_name_extension_full_specification.html
```
* 另一方面，絕不要描述程式碼，假設閱讀程式碼的人比你更懂 Python，他只是不知道你的程式碼要做什麼。
---
#### 文本字串
* Python 有一種獨一無二的的註釋方式：使用文本字串。
* 文本字串是套件、模組、類別或函數里的第一個語句（多行字串），開發者可以滑鼠懸停在函數上觀看其字串。
* 我們對文本字串的慣例是使用三重雙引號，内容包含函數做什麼，以及輸入和輸出的詳細描述。
> Args
> - 列出每個參數的名字，並在名字後使用一個冒號和一個空格分隔對該參數的描述。
   `ex: name: user name`
> 
> Returns
> - 描述返回值的類型和語義，如果函數返回 None，這一部分可以省略。
> 
> Raises
> - 列出與接口有關的所有異常。

`EX`
```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass
```
---
* Python 會將小括號 “()”，中括號 “[]” 和大括號 “{}” 中的行隱性的連接起來。你可以利用這個特點，如果需要，你可以在表達式外圍增加一對額外的小括號。

`EX`
```python
if (width == 0 and height == 0 and
         color == 'red' and emphasis == 'strong'):
```
* 如果一個文本字串在一行放不下，可以使用小括號來實現隱性行連接。

`EX`
```python
x = ('This will build a very long long '
     'long long long long long long string')
```


## TODO
* TODO 註釋應該在所有開頭處包含 ”TODO” 字串，緊跟著是用括號括起來的你的名字，email 地址或其它標識符，然後是一個可選的冒號。
* 接著必須有一行註釋，解釋要做什麼。主要目的是為了有一個統一的 TODO 格式，這樣添加註釋的人就可以搜索到（並可以按需提供更多細節）。
* 寫了 TODO 註釋並不保證寫的人會親自解決問題。當你寫了一個 TODO，請寫上你的名字。

`EX`
```python
# TODO(kl@gmail.com): Use a "*" here for string repetition.
# TODO(Zeke) Change this to use relations.
```
* 如果你的 TODO 是 ”將來做某事” 的形式，那麼請確保你包含了一個指定的日期（“2009 年 11 月解決”）或者一個特定的事件（“等到所有的客戶都可以處理 XML 請求就移除這些代碼”）。

## Class & Function
* 類別應該在其定義下有一個用於描述該類的文檔字串，如果你的類別有公共屬性（Attributes），那麼文檔中應該有一個屬性（Attributes）段，並且應該遵守和函數參數相同的格式。

`EX`
```python
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
```


## 空格
#### 縮排
* 用 Tab 來縮排程式碼，不要與空格鍵混合著用。
---
* 括號內不要有空格。

`YES`
```python
spam(ham[1], {eggs: 2}, [])
```
`NO`
```python
spam( ham[ 1 ], { eggs: 2 }, [ ] )
```
---
* 不要在逗號、分號、冒號前面加空格，但應該在它們後面加（除了在行尾）。

`YES`
```python
if x == 4:
    print x, y
    x, y = y, x
```
`NO`
```python
if x == 4 :
    print x , y
    x , y = y , x
```
---
* 在二元運算符兩邊都加上一個空格。

`YES`
```python
x == 1
```
`NO`
```python
x<1
```
---
* 當 ’=’ 用於指示關鍵字參數或默認參數值時，不要在其兩側使用空格。

`YES`
```python
def complex(real, imag=0.0): return magic(r=real, i=imag)
```
`NO`
```python
def complex(real, imag = 0.0): return magic(r = real, i = imag)
```
---
* 不要用空格來垂直對齊多行間的標記，因為這會成為維護的負擔（適用於 :、#、= 等）。

`YES`
```python
foo = 1000  # comment
long_name = 2  # comment that should not be aligned

dictionary = {
    "foo": 1,
    "long_name": 2,
    }
```
`NO`
```python
foo       = 1000  # comment
long_name = 2     # comment that should not be aligned

dictionary = {
    "foo"      : 1,
    "long_name": 2,
    }
```


## 字串
* 即使參數都是字串，使用 % 操作符或者格式化方法格式化字串。不過也不能一概而論，你需要在 + 和 % 之間好好判定。

`YES`
```python
x = a + b
x = '%s, %s!' % (imperative, expletive)
x = '{}, {}!'.format(imperative, expletive)
x = 'name: %s; score: %d' % (name, n)
x = 'name: {}; score: {}'.format(name, n)
```
`NO`
```python
x = '%s%s' % (a, b)  # use + in this case
x = '{}{}'.format(a, b)  # use + in this case
x = imperative + ', ' + expletive + '!'
x = 'name: ' + name + '; score: ' + str(n)
```
---
* 避免在循環中用 + 和 += 運算子來累加字串，由於字串是不可變的，這樣做會創建不必要的臨時對像，並且導致二次方而不是線性的運行時間。
* 作為替代方案，你可以將每個字串加入列表，然後在迴圈結束後用`.join`連接列表。

`YES`
```python
items = ['<table>']

for last_name, first_name in employee_list:
    items.append('<tr><td>%s, %s</td></tr>' % (last_name, first_name))

items.append('</table>')
employee_table = ''.join(items)
```
`NO`
```python
employee_table = '<table>'

for last_name, first_name in employee_list:
    employee_table += '<tr><td>%s, %s</td></tr>' % (last_name, first_name)

employee_table += '</table>'
```
---
* 在同一個文件中，保持字串引號的一致性，使用單引號 ’ 或者雙引號 ” 之一用以引用字串 **（統一用單引號）**。

`YES`
```python
Python('Why are you hiding your eyes?')
Gollum("I'm scared of lint errors.") # 除非裏面有單引號，外面才用雙引號
Narrator('"Good!" thought a happy Python reviewer.')
```
`NO`
```python
Python("Why are you hiding your eyes?")
Gollum('The lint. It burns. It burns us.')
Gollum("Always the great lint. Watching. Watching.") # 單雙引號交替使用
```
---
* 為多行字串使用三重雙引號 ”“” 而非三重單引號 ’‘’。
* 文本字串必須使用三重雙引號 ”“”。不過要注意。通常用隱性行連接更清晰，因為多行字串與程式其他部分的縮排方式不一致。

`YES`
```python
print ("This is much nicer.\n"
        "Do it this way.\n")
```
`NO`
```python
print """This is pretty ugly.
Don't do this.
"""
```

## Import 格式
* 每個 Import 應該獨佔一行（同一個套件/模組的函數和變數不算）

`YES`
```python
import os
import sys
```
`NO`
```python
import os, sys
```
---
* Import 應該放在文件頂部，位於模組註釋和文本字串之後，全域變數和常數之前。導入應該從最通用到最不通用的順序分組：
1. 標準庫導入
2. 第三方庫導入
3. 應用程序指定導入

```python
import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar
```


## 敘述
* 通常每個敘述應該獨佔一行，不過如果是 if 敘述，只有在沒有 else 時才能這樣做。
* 絕不要對`try/except`這樣做，因為 try 和 except 不能放在同一行。

`YES`
```python
if foo: bar(foo)
```
`NO`
```python
if foo: bar(foo)
else:   baz(foo)

try:               bar(foo)
except ValueError: baz(foo)

try:
    bar(foo)
except ValueError: baz(foo)
```
