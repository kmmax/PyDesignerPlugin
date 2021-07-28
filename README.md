# PyDesignerPlagin
# Custom widget for Designer (PySide6)
![application](doc/readme/screens/screen1.png)
## How to use
note: We will work with **env_root** enviroment
#### Prepearing
+ Installing PySide6, cx_Freeze
~~~bash
$ source env_root/Script/activate
(env_root)$ pip install PySide6 cx_Freeze
(env_root)$ deactivate
~~~
+ create folder for designer's plugins **C:\PyQtPlugins\PySide6Designer**
+ create environment variable: **PYSIDE_DESIGNER_PLUGINS** = **C:\PyQtPlugins\PySide6Designer**

#### Development
1. Copy plugins (from **plugins** in to **C:\PyQtPlugins\PySide6Designer\** folder)
2. Copy **led.py** widget from **plugin\** folder to root folder (when all *.py files located)
3. Execute designer (**you need pyside6-designer!!!**)
~~~bash
$ source env_root/Script/activate
(env_root)$ env_root/Scripts/pyside6-designer.exe (maybe you need switch to env_root)
~~~
![application](doc/readme/screens/screen2.png)
2. Save as **ui_byteasbits.ui**
3. Convert ***.ui** file to ***.py** file
~~~bash
$ source env_root/Script/activate
(env_root)$ pyside6-uic ui_byteasbits.ui -o ui_byteasbits.py
~~~



## How to build application
~~~bash
$ source env_root/Script/activate
(env_root)$ python setup.py build
(env_root)$ cp green_led.png red_led.png ./build/exe.win-amd64-3.8/
(env_root)$ deactivate
~~~
