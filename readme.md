## API Logger

It's basically a simple logger that organizes all the logs and log entries for me. It's not as technical as the Python logger but its as easy to use as a print function, and it will archive and send the logs where they need to be. It allows me to give my APIS an inerface so to speak. I can look back through the log directories and see what happend, and I can set the file length at which to 'archive'. When the file reaches the archive size the file is pushed away and a new empty one is created in its place. I made it when I wrote my first API and its been pretty helpful so far. Currently It is set up to log six different kinds of log entries
that i refer to as "Streams". I didn't wnat to use levels because it doesn't work the same way.

## Streams

Streams are just the files the log entries are sent to. The type of log entry.

- **INFO** : Information. Basic logging.
- **ERROR** : Any and all errors. 
- **WARN(ING)** : Warnings.
- **DEBUG** :  Any debugging within the API.
- **INTERNAL** : Any message error, info or other that is derived from the logger class. 
- **LOGIN** : Stores info about your clients. Currently I store in dict format. 
- **SCREEN**: After all Ive said about APIS logging to the screen, I still feel I need this.

## Singleton Pattern

I wrote it as a basic Singleton. You will only ever need but one instance and it is created at the bottom of the `api_logger.py` file. (This by itself would probably have been enough but I added more code to implement the pattern) Any change to file names archive sizes can be made there. When I first wrote this I made it so that it got the log directory and archive directory settings from a `Settings()` class. But as I've used this more and more I have discovered that this is not a good idea. If you import the instance into any module that already has `settings` imported you get circular imports. So I just 86'd that and set the directory locations inside the class file. It always puts them in the `./logs` directory. Be aware of this when you start any app that uses it.  

## Additional Streams:

It's pretty easy to add more streams if you need more logging types to track. 

1. **Update the Stream** : in api_logger.py edit `class Stream`, and `class Stream.Prefix`. Here you will add the code to represent your new stream. If you want to add a logfile to track client logouts, then add:  `LOGOUT: int = 70` for `class Stream` and ` LOGOUT_PRE: str = "LOGOUT: "`, so on and so forth.
2. **Update Archive Directory**: In `class Archive`, locate`class ArchiveSubDirectories` and add your stream to the class. Sticking with the same LOGOUT addition you would add `LOGOUT_DIR: str = "logout"`.
3. **Update filename in __init__** : In the APILogger __init__ method you will need to add your new file name. Basically look for this line: `self.info_filename = kwargs.get('info_filename')` copy it, and paste it below, then change the filename and attribute to match the new stream. You should have the idea by now... I'm a terrible teacher. email me if you have any issues.
4. **_handle_file_setup** : locate the list `file_names` and add a new name.
5. **Add A new Log Entry Interface** : THis is easier than it sounds. You need to scroll down to line: 396 where the log entry 
interfaces begin. Just copy the entire method: `def error()` and paste it at the bottom, or underneath error. Doesn't really matter. Now change all the references to `error` with the name of your new stream.

### Example
```
def your_stream(self, message: str, timestamp: bool = False) -> None:
        message = f"{Stream.Prefix.YOUR_NEW_STREAM_PRE} {message}"
        self.__save_log_entry(
            message,
            Stream.YOUR_NEW_STREAM,
            timestamp,
            self.your_stream_filename
        )     
```
It looks like a lot but it's really not. If you have any issues reach out to me @ `life.package.web@gmail.com`. I have about 15 different streams on a couple APIS and it never misses a beat. Or It hasn't thus far. which brings me to...

## TODO:

I seriously need to make this entire logging system asynchronous. I've toyed with it a bit and I think I will have to restructure the entire system. The Read write file ops need it definitely. I'm afraid that as my apps get busyier, I may start to miss log entries. 
