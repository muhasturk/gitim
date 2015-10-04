# Gitim

[![MIT License][License Image]][License]
[![Python Version][Python Image]][Python]
![Project Status: Active][Project Status Image]

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

[License Image]: https://img.shields.io/badge/license-MIT-brightgreen.svg "MIT License"
[License]: https://github.com/muhasturk/gitim/blob/master/LICENSE "MIT License"

[Python Image]: https://img.shields.io/badge/python-3.5-blue.svg "Python Version: 3.5"
[Python]: https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-0-final "Python 3.5 Changelog" 

[Project Status Image]: https://img.shields.io/badge/project-active-green.svg "Project Status: Active"
