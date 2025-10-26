# Hanzi IDC Sort<br>汉字结构判别分拣

## 简介<br>Introduction

### 功能<br>Function

![P_0](P_0.png)

输入汉字列表（txt格式），根据[IDS数据库](https://github.com/yi-bai/ids)（txt格式）检测对应序列中的第一个[IDC](https://www.qiuwenbaike.cn/wiki/表意文字描述字符)符号，进而判别汉字结构完成分拣。

Input a list (txt) of Chinese characters, detect the first [IDC](https://en.wikipedia.org/wiki/Ideographic_Description_Characters) in the sequence in the [IDS database](https://github.com/yi-bai/ids) (txt), and then determine the structure to complete the sorting.

![P_1](P_1.png)

在判别中，为保证左中右、上中下结构的可见度，就`搿	⿰龵㧱(.);⿰𭠫手(H);⿲龵合.手(J)`这样的序列而言，⿲/⿳的优先级要高于⿰/⿱。但这也可能使`脔	⿱𰁜肉(.);⿱亦H肉(H);⿱亦J肉(J);⿳亠.⿰丿小s肉(T)`等引发误导。

In sorting, ⿲/⿳ takes precedence over ⿰/⿱ in sequences like `搿 ⿰龵㧱(.);⿰𭠫手(H);⿲龵合.手(J)` to ensure greater visibility of the Left-to-Middle-and-Right and Above-to-Middle-and-Below structures. However, this may also make `脔 ⿱𰁜肉(.);⿱亦H肉(H);⿱亦J肉(J);⿳亠.⿰丿小S肉(T)` etc. be misleading.

### 下载<br>Download

在[Releases](https://github.com/Fisher4124/Hanzi-IDC-Sort/releases)页面下载`Hanzi-IDC-Sort.exe`（或[百度网盘](https://pan.baidu.com/s/11NToCQO79YeWIPNwfjWkXw)）。

Download `Hanzi-IDC-Sort.exe` from the [Releases](https://github.com/Fisher4124/Hanzi-IDC-Sort/releases) page.

### 结构数据<br>IDS.txt

[白易](https://github.com/yi-bai)所提供的[IDS.txt](https://github.com/yi-bai/ids)。

[IDS.txt](https://github.com/yi-bai/ids) by [Yi Bai](https://github.com/yi-bai).



## 著作权声明<br>Copyright

基于[MIT License](https://opensource.org/license/MIT)协议发布。

Released under the [MIT License](https://opensource.org/license/MIT).
