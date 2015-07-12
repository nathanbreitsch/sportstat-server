# SportStat server

SportStat sports statistics server, data schema, and analytics.

## Install and Setup

### Packages and Dependencies

*kind of optional*

1. create and activate a virtual environment

    - for vanilla Python:

    $ pip install virtualenv
    $ virtualenv sportstat
    $ source sportstat/bin/activate

    - with Anaconda:

    $ conda create -n sportstat anaconda
    $ source activate sportstat

Note: when using Anaconda, you may choose to limit the packages to just those
indicated in the requirements.txt file by specifying:

    $ conda create -n sportstat --file requirements.txt

For developers; to update requirements.txt after installing packages (using 
pip or conda install), run:

    $ conda list -e > requirements.txt

to overwrite the requirements file.


2. Install dependencies

    $ pip install -r requirements.txt


3. Install `sportstat` python package

    - first build the package:

    $ python setup.py build

    - then, if only deploying (not developing):

    $ python setup.py install

    - if developing or testing:

    $ python setup.py develop


### Database

Look into the notebooks directory which contains ipython notebooks with code 
and documentation for creating and populating the database.


## Run/Deploy

1. Run Server

    $ python app/app.py

2. Try out API

visit "http://localhost:1337/api/find/athlete" in the browser

TODO: deployment
