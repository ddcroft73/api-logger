## API Logger

It's basically a simple logger that organizes all the logs for me. It's not as technical as the Python logger but its as easy to use as a print function, and it will archive and send the logs where they need to be. It allows me to give my APIS an inerface so to speak. I can look back through the log directories and see what happend, and I can set the file length at which to 'archive'. When the file r3eaches the archive size the file is pushed away and a new empty one is creat34ed in its place. I made it when I wrote my first API and its been pretty helpful so far. Currently It is set up to log:

## Streams

Streams are just the files the log entries are sent to. The type of log entry.

- INFO
- ERROR
- WARN(ING)
- DEBUG
- INTERNAL Any message error, info or other that is derived from the logger class.
- LOGIN (New: I Feel the need to log every login attempt, but I am still adding this.)
- SCREEN (After all Ive said about APIS logging to the screen, I still feel I need this.)

