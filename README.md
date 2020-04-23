# Gitim

[![MIT License][License Image]][License]
[![Python Version][Python Image]][Python]
![Project Status: Active][Project Status Image]

Clone all your Github repositories.


             .--.         .--. __  __   ___
      .--./) |__|         |__||  |/  `.'   `.
     /.''\  .--.     .|  .--.|   .-.  .-.   '
    | |  | | |  |   .' |_ |  ||  |  |  |  |  |
     \`-' /  |  | .'     ||  ||  |  |  |  |  |
     /("'`   |  |'--.  .-'|  ||  |  |  |  |  |
     \ '---. |  |   |  |  |  ||  |  |  |  |  |
      /'""'.\|__|   |  |  |__||__|  |__|  |__|
     ||     ||      |  '.'
     '. __//       |   /
      `'---'        `'-'

## Installation

```
pip3 install . 
```
or
```
python3 setup.py install
```
or get it as the [archlinux aur package](https://aur.archlinux.org/packages/python-gitim-git/):

```
yaourt -S python-gitim-git
```

### Usage

```
python -m gitim
```

Username and password will be prompted.

If you want to download organization repositories

```
python3 -m gitim -o <Organization> -d <Directory>
```

#### Optional Arguments

```
  -h, --help            show this help message and exit
  -u USER, --user USER  Your github username
  -p PASSWORD, --password PASSWORD
                        Github password
  -t TOKEN, --token TOKEN
                        Github OAuth token
  -o ORG, --org ORG     Organisation/team. User used by default.
  -d DEST, --dest DEST  Destination directory. Created if doesn't exist.
                        [curr_dir]
  --nopull              Don't pull if repository exists. [false]
  --shallow             Perform shallow clone. [false]
  --ssh                 Use ssh+git urls for checkout. [false]
```

##### Licence
MIT

[License Image]: https://img.shields.io/badge/license-MIT-brightgreen.svg "MIT License"
[License]: https://github.com/muhasturk/gitim/blob/master/LICENSE "MIT License"

[Python Image]: https://img.shields.io/badge/python-3.5-blue.svg "Python Version: 3.5"
[Python]: https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-0-final "Python 3.5 Changelog" 

[Project Status Image]: https://img.shields.io/badge/project-active-green.svg "Project Status: Active"
