# Bitly URL shorterer

This project accept URLs and returns a bitlink for them.
It can also accept bitlinks and print the number of clicks on bitlink.

### How to install

You should get an access token for bit.ly from [personal profile](https://app.bitly.com/settings/api/).
It's look like that:
```
a18b7a8d412ea74b17bda2a06f1b69fa3805a712
```
After you add token to .env file:
```commandline
BITLINK_ACCESS_TOKEN=a18b7a8d412ea74b17bda2a06f1b69fa3805a712
```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```shell
$ pip install -r requirements.txt
```

### How to launch
At first you should jump to directory where *main.py* was placed.
```shell
$ cd C:/path_to_dir_with_program
```
After that you can launch program in two modes:
1. Generating bitlink for your URL.
```shell
$ python main.py https://yourlinkhere.ru
bit.ly/3vCwvtU
```
2. Returning number of clicks for bitlink.
```shell
$ python main.py bit.ly/3vCwvtU
Количество переходов по ссылке битли: 1
```

### Troubleshooting
Type *-h* or *--help* for detail info:
```shell
$ python main.py -h
usage: main.py [-h] url

Программа принимает ссылки и возвращает на них битлинк.Так же принимает 
битлинки возвращает количество заходов по ссылке

positional arguments:
  url         Адрес сайта или битлинк

options:
  -h, --help  show this help message and exit
```
If you entered wrong URL or bitlink format: 
```shell
$ python main.py www.ya.ru
Вы ввели ссылку некорректного формата
```
Standart format is `http[s]://link-or-bitlink/yada/yada`.


### Project Goals

The code is written for educational purposes.
