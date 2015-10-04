# Gitim

[![GitHub license](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/muhasturk/gitim/blob/master/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.5-blue.svg)](https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-0-final)

```
         .--.         .--. __  __   ___
  .--./) |__|         |__||  |/  `.'   `.
 /.''\\  .--.     .|  .--.|   .-.  .-.   '
| |  | | |  |   .' |_ |  ||  |  |  |  |  |
 \`-' /  |  | .'     ||  ||  |  |  |  |  |
 /("'`   |  |'--.  .-'|  ||  |  |  |  |  |
 \ '---. |  |   |  |  |  ||  |  |  |  |  |
  /'""'.\|__|   |  |  |__||__|  |__|  |__|
 ||     ||      |  '.'
 \'. __//       |   /
  `'---'        `'-'
```

Tüm Github hesabınızdaki depolarınızı istediğiniz dizine klonlayabileceğiniz veya eiştleyebileceğiniz bir araçtır.

### Requirements

```python
pip install pygithub
```

### Usage
```
./gitim
```

#### Arguments

* -u, --username KullaniciAdi 
* -p, --password Şifreniz
* --nopull       
Daha önce klonlanmış depolarınızı güncellemez.
* -d, --dest Dizin
Verdiğiniz dizine klonlar
* -t, --token TOKEN 
Auth token. Şifre ile doğrulamanın alternatifi olarak kullanabilirsiniz.

##### Licence
MIT