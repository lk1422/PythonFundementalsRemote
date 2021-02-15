'''
In your CodingNomads folder create a new folder. Inside of that folder:

1. Create a new virtual environment
2. Activate the virtual environment
3. Install at least 3 packages in the virtual environment.
4. Freeze the installed packages to a requirements.txt file.
5. Deactivate the virtual environment.
6. Delete the virtual environment.
7. Create a new virtual environment and install the packages from the requirements.txt file.

'''
'''
This lab was completed on CMD
Since i was on windows some pip commands differed 
I also forgot to do it in a new folder so i did it within my lab folder here
The following is a exact copy and paste from my CMD PLZ IGNORE WHEN I MESSED UP :)

C:\Program Files\CMDER
λ cd /

C:\
λ cd Users\lk3on\OneDrive\Documents\CodingNomads\labs\

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs (master -> origin)
λ ls
python_fundamentals-master/

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs (master -> origin)
λ cd python_fundamentals-master\

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master (master -> origin)
λ ls
01_python_fundamentals/  03_more_datatypes/      05_string_formatting/  07_classes_objects_methods/  09_exceptions/  11_venvs/             13_list_comprehensions/  15_aggregate_functions/  17_decorators/  README.md
02_basic_datatypes/      04_conditionals_loops/  06_functions/          08_file_io/                  10_testing/     12_packages_modules/  14_generators/           16_variable_arguments/   18_lambdas/     words.txt

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master (master -> origin)
λ cd 11_venvs\

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ ls
11_01_venv.py

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ python3 -m venv LAB_ENV

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ cd LAB_ENV\Scripts\activate.bat
The directory name is invalid.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ cd LAB_ENV\Scripts\

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs\LAB_ENV\Scripts (master -> origin)
λ ls
activate  activate.bat  Activate.ps1  deactivate.bat  easy_install.exe*  easy_install-3.9.exe*  pip.exe*  pip3.9.exe*  pip3.exe*  python.exe*  pythonw.exe*

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs\LAB_ENV\Scripts (master -> origin)
λ cd../../

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs\LAB_ENV\Scripts (master -> origin)
λ cd ../../

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs\LAB_ENV\Scripts (master -> origin)
λ cd../

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs\LAB_ENV (master -> origin)
λ cd ../

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ LAB_ENV\Scripts\activate.bat

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ pip install django
Collecting django
  Downloading Django-3.1.6-py3-none-any.whl (7.8 MB)
     |████████████████████████████████| 7.8 MB 3.2 MB/s
Collecting asgiref<4,>=3.2.10
  Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 80 kB/s
Collecting pytz
  Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
     |████████████████████████████████| 510 kB 6.4 MB/s
Installing collected packages: asgiref, sqlparse, pytz, django
Successfully installed asgiref-3.3.1 django-3.1.6 pytz-2021.1 sqlparse-0.4.1
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\lk3on\onedrive\documents\codingnomads\labs\python_fundamentals-master\11_venvs\lab_env\scripts\python.exe -m pip install --upgrade pip' command.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ pip install wifiPassword 2.0
Collecting wifiPassword
  Downloading wifiPassword-2.0-py3-none-any.whl (4.5 kB)
ERROR: Could not find a version that satisfies the requirement 2.0 (from versions: none)
ERROR: No matching distribution found for 2.0
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\lk3on\onedrive\documents\codingnomads\labs\python_fundamentals-master\11_venvs\lab_env\scripts\python.exe -m pip install --upgrade pip' command.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ pip install wifiPassword
Collecting wifiPassword
  Using cached wifiPassword-2.0-py3-none-any.whl (4.5 kB)
Collecting colorama>=0.3.7
  Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Installing collected packages: colorama, wifiPassword
Successfully installed colorama-0.4.4 wifiPassword-2.0
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\lk3on\onedrive\documents\codingnomads\labs\python_fundamentals-master\11_venvs\lab_env\scripts\python.exe -m pip install --upgrade pip' command.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ pip install skytap
Collecting skytap
  Downloading skytap-1.4.0.tar.gz (49 kB)
     |████████████████████████████████| 49 kB 1.5 MB/s
Collecting requests
  Downloading requests-2.25.1-py2.py3-none-any.whl (61 kB)
     |████████████████████████████████| 61 kB 4.0 MB/s
Collecting six
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting idna<3,>=2.5
  Downloading idna-2.10-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 3.0 MB/s
Collecting urllib3<1.27,>=1.21.1
  Downloading urllib3-1.26.3-py2.py3-none-any.whl (137 kB)
     |████████████████████████████████| 137 kB 6.4 MB/s
Collecting certifi>=2017.4.17
  Downloading certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
     |████████████████████████████████| 147 kB ...
Collecting chardet<5,>=3.0.2
  Downloading chardet-4.0.0-py2.py3-none-any.whl (178 kB)
     |████████████████████████████████| 178 kB 6.4 MB/s
Using legacy 'setup.py install' for skytap, since package 'wheel' is not installed.
Installing collected packages: idna, urllib3, certifi, chardet, requests, six, skytap
    Running setup.py install for skytap ... done
Successfully installed certifi-2020.12.5 chardet-4.0.0 idna-2.10 requests-2.25.1 six-1.15.0 skytap-1.4.0 urllib3-1.26.3
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\lk3on\onedrive\documents\codingnomads\labs\python_fundamentals-master\11_venvs\lab_env\scripts\python.exe -m pip install --upgrade pip' command.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ pip freeze > requirments.txt

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ ls
11_01_venv.py  LAB_ENV/  requirments.txt

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
(LAB_ENV) λ deactivate
C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ remove LAB_ENV\
'remove' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ rmdir LAB_ENV\
The directory is not empty.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ rm -r LAB_ENV\

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ python3 -m venv Lab_Env2

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ pip -r

Usage:
  C:\Users\lk3on\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe -m pip <command> [options]

no such option: -r

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ pip -r requirments.txt

Usage:
  C:\Users\lk3on\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe -m pip <command> [options]

no such option: -r

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ ptions
'ptions' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ options
'options' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ pip install -r requirments.txt
Collecting asgiref==3.3.1
  Using cached asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting certifi==2020.12.5
  Using cached certifi-2020.12.5-py2.py3-none-any.whl (147 kB)
Collecting chardet==4.0.0
  Using cached chardet-4.0.0-py2.py3-none-any.whl (178 kB)
Collecting colorama==0.4.4
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting Django==3.1.6
  Using cached Django-3.1.6-py3-none-any.whl (7.8 MB)
Collecting idna==2.10
  Using cached idna-2.10-py2.py3-none-any.whl (58 kB)
Collecting pytz==2021.1
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting requests==2.25.1
  Using cached requests-2.25.1-py2.py3-none-any.whl (61 kB)
Collecting six==1.15.0
  Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting skytap==1.4.0
  Using cached skytap-1.4.0.tar.gz (49 kB)
Collecting sqlparse==0.4.1
  Using cached sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting urllib3==1.26.3
  Using cached urllib3-1.26.3-py2.py3-none-any.whl (137 kB)
Collecting wifiPassword==2.0
  Using cached wifiPassword-2.0-py3-none-any.whl (4.5 kB)
Using legacy 'setup.py install' for skytap, since package 'wheel' is not installed.
Installing collected packages: asgiref, certifi, chardet, colorama, pytz, sqlparse, Django, idna, urllib3, requests, six, skytap, wifiPassword
  WARNING: The script chardetect.exe is installed in 'C:\Users\lk3on\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script sqlformat.exe is installed in 'C:\Users\lk3on\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script django-admin.exe is installed in 'C:\Users\lk3on\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
    Running setup.py install for skytap ... done
  WARNING: The script wifiPassword.exe is installed in 'C:\Users\lk3on\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Django-3.1.6 asgiref-3.3.1 certifi-2020.12.5 chardet-4.0.0 colorama-0.4.4 idna-2.10 pytz-2021.1 requests-2.25.1 six-1.15.0 skytap-1.4.0 sqlparse-0.4.1 urllib3-1.26.3 wifiPassword-2.0
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'C:\Users\lk3on\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip' command.

C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ
C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ
C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ
C:\Users\lk3on\OneDrive\Documents\CodingNomads\labs\python_fundamentals-master\11_venvs (master -> origin)
λ pip freeze
asgiref==3.3.1
certifi==2020.12.5
chardet==4.0.0
colorama==0.4.4
Django==3.1.6
idna==2.10
pytz==2021.1
requests==2.25.1
six==1.15.0
skytap==1.4.0
sqlparse==0.4.1
urllib3==1.26.3
wifiPassword==2.0





'''
x=1