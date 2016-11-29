===============
Getting Started
===============

Installation
============

COPSERP is based on django, therefore to install this program firstly
you need to configure, setup your environmet and install all
dependencies needed.

the source code of COPSERP can be found at this `link <http://github.com/andrewidya/littleerp.git>`_ 

.. note::
   Currently COPSERP has been tested only with python2.7 and django1.8
   if you plan to use another version of python and django
   please contact me in andrywidyaputra@gmail.com when you
   found bugs


Preparing Virtualenv
---------------------

It's recomended to use virtualenv to work with python, so we can isolate
specific enviroment to work with COPSERP::

   $ virtualenv --python=/usr/bin/python2.7 env
   $ source env/bin/activate


Downloading Source Code
-----------------------

Still in the same directory after creating virtualenv, we need to create
workspace folder to download the code::

   $ mkdir copserp
   $ cd copserp
   $ git clone http://github.com/andrewidya/littleerp.git .


Installing Dependencies
-----------------------

All dependencies we need to install is on ``requirement.text``, install
all using pip::

   $ pip install -r requirement.txt

Database Schema Migration
-------------------------

Configure database setting in ``minierp/setting.py``, see `here <https://docs.djangoproject.com/en/1.8/ref/settings/#databases>`_.

.. note::
   You need to install appropirate database driver for your database
   engine. (e.g psycopg for PostgreSQL, MySQL-python for MySQL/MariaDB)

then migrate database and create admin user::
   
   $ python manage.py migrate
     .....
     .. hided

   $ python manage.py createsuperuser

Static Files & Testing
----------------------

Collect static file by invoking ``python manage.py collectstatics``.
now we can run ``python manage.py test`` to test all function routine
works as expected.

.. note::
   Development server is a single threading server bundled with django
   to ease developer to test the application.
   
   Don't use it in production, the easy deploy recomended by official
   django documentation is using Apache and mod_wsgi enabled, see
   `django deploy docs <https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/modwsgi/>`_. for details.

If there are no error found in test, we can start development server by
invoking ``python manage.py runserver 127.0.0.1:8000``
