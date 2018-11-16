pgbackup
========

eclipse Challenge:
Direction Controller
You are to design a set of python scripts to control the movement of a robot. The client script will act as the bot.
This task should be completed in Python version 3.

Preparing for Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``gti clone git@github.com:example/pgbackup``
3. Fetch development dependencies : ``make install``


Usage
-----

Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local Example w/local path:

    $pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql


Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::
    $make
If virtulenv isn't active then use:

    $ pipenv run make



