# PT Commercial Servisindo Prima
## MiniERP

#### Installing Environtment
firstly you need to create working directory, then enter to it
```sh
mkdir workspace
cd workspace
```

after that isolate package dependencies needed by creating virtual environtment:
```sh
virtualenv --python=/usr/bin/python2.7 env
```
your working directory should like this:
```
workspace
|
 --- env
```
create directory to put the source into:
```sh
mkdir src
```
your working directory should looks like this:
```sh
workspace
|
 --- env
 --- src
```
go to source directory, then initiate this command:
```sh
git clone htpps://github.com/andrewidya/littleerp.git
```

activate virtual env by this command:
```sh
source ../env/bin/activate
```
install all dependency:
```sh
pip install -r requirement.txt
```

run development server:
```sh
./manage.py runserver
```
