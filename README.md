Part OS JobBOSS SDK (Python)
============================

The JobBOSS Software Development Kit (SDK) enables Python developers to easily
read and write data to a JobBOSS instance by directing running queries on a 
Microsoft SQL Server database instance. This SDK is built on Django's 
[Object-Relational Mapping (ORM)](https://docs.djangoproject.com/en/2.2/topics/db/). 


Prerequisites
-------------

These instructions assume you are running on Windows 10.

First install the latest [Python3](https://www.python.org/downloads/), which 
includes `python3`, `pip`, and `venv`. Add the Python installation folder to 
your system path. 

Create a virtual environment and activate it:

    python -m venv osenv
    osenv\Scripts\activate

Install the required Python packages:

    cd path\to\jobboss-python
    pip install -r requirements.txt

Make sure `jobboss` to your Python path. You can do this using an environment 
variable like this:

    set PYTHONPATH=c:\path\to\jobboss-python
    
or by writing your connector application directly in the jobboss-python folder. 


Specifying SQL Server Credentials
---------------------------------

Microsoft SQL Server credentials must be specified in environment variables
called `JOBBOSS_DB_HOST`, `JOBBOSS_DB_NAME`, `JOBBOSS_DB_USERNAME`, and 
`JOBBOSS_DB_PASSWORD`.

When running a script or application that uses this SDK, consider launching
from a batch file that sets these variables like in this `example.bat`:

     @echo off
     REM example.bat -- JobBOSS script launcher
     set JOBBOSS_DB_HOST=mydbhost
     set JOBBOSS_DB_NAME=mydbname
     set JOBBOSS_DB_USERNAME=mydbuser
     set JOBBOSS_DB_PASSWORD=mydbpassword
     python my_jobboss_script.py


Using the SDK
-------------

### Using ORM Classes

An ORM class can be imported and used like in this example:

    from jobboss.models import Contact
    print(Contact.objects.count())
    
For information on querying and making changes to the database using ORM 
objects, consult the [Django ORM documentation.](https://docs.djangoproject.com/en/2.2/topics/db/).
 

### SDK Queries

The SDK provides queries for common tasks performed by JobBOSS integrations.
These queries are located in the `jobboss/queries/` folder.


Advanced Developer Features
---------------------------

### Running Test Cases

Test cases can be run on any platform using this command:

`python manage.py test`

### Database Shell

A Django ORM shell can be started on Windows like this:

`python manage.py shell`

The environment variables described in the "Connecting to SQL Server" section 
above must be defined in the current shell. 
