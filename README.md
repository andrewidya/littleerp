# PT Commercial Servisindo Prima
## MiniERP

#### Installing Environtment
firstly you need to create working directory, then enter to it
'''sh
mkdir workspace
cd workspace
'''

after that isolate package dependencies needed by creating virtual environtment:
'''sh
virtualenv --python=/usr/bin/python2.7 env
'''

your working directory should like this:
    workspace
    |
    --- env

create directory to put the source into:
    mkdir src

your working directory should looks like this:
    workspace
    |
    --- env
    --- src

go to source directory, then initiate this command:
    git clone htpps://github.com/andrewidya/littleerp.git

activate virtual env by this command:
    source ../env/bin/activate

install all dependency:
    pip install -r requirement.txt

run development server:
    ./manage.py runserver

your server should available on http://127.0.0.1:8000/admin
