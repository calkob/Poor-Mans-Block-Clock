# Poor-Mans-Block-Clock
 
If you find that the program does not run then you may need to install the requests module. Info below


Requests is not a built in module (does not come with the default python installation), so you will have to install it:

OSX/Linux
Use $ pip install requests (or pip3 install requests for python3) if you have pip installed. If pip is installed but not in your path you can use python -m pip install requests (or python3 -m pip install requests for python3)

Alternatively you can also use sudo easy_install -U requests if you have easy_install installed.

Alternatively you can use your systems package manager:

For centos: yum install python-requests For Ubuntu: apt-get install python-requests

Windows
Use pip install requests (or pip3 install requests for python3) if you have pip installed and Pip.exe added to the Path Environment Variable. If pip is installed but not in your path you can use python -m pip install requests (or python3 -m pip install requests for python3)

Alternatively from a cmd prompt, use > Path\easy_install.exe requests, where Path is your Python*\Scripts folder, if it was installed. (For example: C:\Python32\Scripts)

If you manually want to add a library to a windows machine, you can download the compressed library, uncompress it, and then place it into the Lib\site-packages folder of your python path. (For example: C:\Python27\Lib\site-packages)
