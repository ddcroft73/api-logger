
from logger.api_logger import logzz
from time import sleep

if __name__ == "__main__":

    # WHen the program is ran all the neccesary directories are created as well as the archive directories
    # if set to True 
    # You can run this file from within the IDE, or use the shell script. The shell script just stops it from writing 
    # the bytecode. 
    
    # make sure the logfiles are created.
    sleep(2)
    #TODO: Come p with a creatve way to demo this class!
    log_msg: str = 'This is a demo log message to diplay the archive feature. Line #'
    for i in range(70):
        sleep(.05)
        logzz.info(log_msg+str(i))



    #logzz.info("This is an info log. It will go in the Info log...")

    logzz.warn("This is a warning, log with timestamp."
               " THere is no Log file designated for 'warning',"
               " so it will go in the default log file", timestamp=1)
    
    logzz.error("An error has occur3d.")
    logzz.debug("A message you can use to debug, with timestamp", timestamp=1)

# Demo out the archive feature:
# App starts: DEmo the archiving for INFO:
# loop out 100 lines of log info for the INFO Level 3 times to see the app create and move the files:
#   