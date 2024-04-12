## API Logger:

A simple logger that organizes all the logs and log entries from the  web micro services I have been building. Basically i needed a way to always know what is going on anywhere in the API because the terminal is in fact unusable for this when being used to spin up a web service.  It's not as technical as the Python logger but its as easy to use as a print function, and it will archive and send the logs where they need to be, the way I intend. No configuring a fucking logger for 20 minutes and then debugging it to make sure its doing as intended then realzing hell, it's not loging the damn `INFO` entries anymore! (I have sene figured it out, but this is just so much easier. it really is. And I don;t need to remeber the configuration when I move from project to project months later.  It sends am entry where I want when I want. ) It allows me to give my APIS an inerface so to speak. I can look back through the log directories and see what happend, and I can set the file length at which to 'archive'. When the file reaches the archive size the file is pushed away and a new empty one is created in its place. I made it when I wrote my first API and its been pretty helpful so far. Currently It is set up to log six different kinds of log entries that i refer to as "Streams". I didn't wnat to use levels because it doesn't work the same way. 

## Log File Archiving:

This is nice feature that deserves some more mention. The way it works is really simple and I included a demo that runs you through it.

When you set the parameters on the logger instantiation, you decide how big you want the files to be before they are archived, as well ass all the names of the log files themseves. Whenever a log eaches that size, it is moved to the archive directory for the stream it represents. and it is renamed. Basically the time and date are just appended to the filename so it is easy to keep them organized. Then a new file is created withthe original name you selected, and logging continues.

## Streams:

Streams are just the files the log entries are sent to. The type of log entry.

- **INFO** : Information. Basic logging.
- **ERROR** : Any and all errors.
- **WARN(ING)** : Warnings.
- **DEBUG** :  Any debugging within the API.
- **INTERNAL** : Any message error, info or other that is derived from the logger class.
- **LOGIN** : Stores info about your clients. Currently I store in dict format.
- **SCREEN**: After all Ive said about APIS logging to the screen, I still feel I need this.

## Singleton Pattern:

I wrote it as a basic Singleton. You will only ever need but one instance and it is created at the bottom of the `api_logger.py` file. (This by itself would probably have been enough but I added more code to implement the pattern) Any change to file names archive sizes can be made there. When I first wrote this I made it so that it got the log directory and archive directory settings from a `Settings()` class. But as I've used this more and more I have discovered that this is not a good idea. If you import the instance into any module that already has `settings` imported you get circular imports. So I just 86'd that and set the directory locations inside the class file. It always puts them in the `./logs` directory. Be aware of this when you start any app that uses it. The removal of the `Setttings` class has rendered this module a lot less modular. ANytime you are forced to add hardcoded information inside a class it's not good. But as it is, witht he use of this logger, V1 it's not that big of a deal. I have bigger plans that will render this insignifigant at best.

## Basic Usage:

Copy the logger directory into the root of your project.  There sould be 3 files present. `__init__.py`,  `api_logger.py`, `file_handler.py`

- **__ init __.py** : The file that designates the directory as a package. This is important because you need this to be able to import the logger into any module you plan to record log entries.
- **api_logger.py** : The logger code.
- **file_handler.py** : This is just a set of classes that adds a layer of abstraction to the file read\write\move\copy operations. It adhears to the searation of concerns principles. However, that being said, If you look deep enough (not really) into the Logger code you will see there are areas where I totally disregarded this. It is useful as well when testing the logger. It allows me to easily mock these operations as needed.

---

Once the directory and files are in place, You need to scroll to the bottome of `api_logger.py` and set the log file names, any other parameters. Thwy are as follows:

* **info_filename** : LOG_Info.log  or anything really.. These are pretty self explanatory.
* **error_filename** :
* **warning_filename** :
* **debug_filename** :
* **login_filename** :
* **archive_log_files** :
* **log_file_max_size** :  Set to equal the max size, or number of lines in a log before archiving.

Now simply run youe API as normal and the log directories will all be created.  

In order to use logger just import the instance that was created at the boittom of `api_logger.py`

```python
from app.logger.api_logger import logzz

def some_function(arg1: str) -> str:
    # Some code you want to log...
    logzz.info(f"arg1: {arg1}", timestamp=True)
    return arg1

```

```python
from app.logger.api_logger import logzz

def some_function2(phone: str, username: str, email: str) -> int:
    # set up a dictionry with multiple pieces of relevent data
    # that need to be displayed and you don't want to use a single line 
    # or line breaks exclusively.
    user_data_dict = {
        "username": username,
        "email": email,
        "phone": phone,
    }
    logzz.info(
        user_data_dict, heading="User Information", dict_to_string=True
    )
  
```

## Latest Changes:

**04/12/2024 -** 

- Formatted dictionary\json logging entries:
  I added support for adding json log entries. Some log entries just look better this way rather than trying to squeeze information on one line.

```python
LOGIN: New Login
{ 
    "username": "john.smith@YoMail.com",
    "time_in": "04/10/2024 20:38:26",
    "ip_address": "172.19.0.1"
}
```

## TODO:

Make the file read write actions asynchronous add aiofiles... no, I have a much beter idea.  This is too easy to implement badly. V1 is pretty much done.

Enter V2: 

1. V2  will use an intergrated Celery app to handle all the logging. This will take care of any async needs and allow for super scalability. V2 will be hyper focused on logging in a manner that will challenge any sized system. It will be made to focus  especially for user based systems.  As such, it will create a directory for each user on the system, and each user will have their own logfiles, and archived logfiles. Since most actions are tied to a specific user, or to the system itself, this will make it much easier to find errors that occured for one user over others.  ANd System errors will be logged as if the system were a user as well. This will make it exceedingly easy to catch any errors that occured for a specific user, and double check  if its going wrong for all users. You can track the actions of individual users, groups of users. Targeting any user actions that are suspicious, or cause for concern. No need to crossrefernec error occurence, or bad actors. V2 Will carry it's own installer. This will make it much easier to use for everyone versus just giving vague instructions on creating a directory for the logger, copy this file, that file, create a Celery app, now configure the app... no. V2 will do this for the end user.
