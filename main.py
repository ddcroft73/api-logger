
from logger.api_logger import logzz as logger

from time import sleep

def do_demo():   
    sleep(2)
    logger.print("Working...")

    log_msg: str = 'This is a demo log message to diplay the archive feature. log entry #'
    for i in range(100):
        sleep(.08)
        if i%10==0:
          logger.print(f'printing line:{i}.')
        logger.info(log_msg+str(i))

    logger.print("Done!", stream=10, timestamp=True)##

    # And a few others as well. 
    logger.warn("This is a warning log with timestamp."
               " There is no Log file designated for 'warning',"
               " so it will go in the default log file\n", timestamp=1)    
    logger.error("An error has occured.")
    logger.login("Client: 212.456.45.67 logged in @: ", timestamp=1)
    logger.debug("A message you can use to debug, with timestamp", timestamp=1)

    # logzz is just the name that was used to instantiate the Class, it can be changed to whatever
    # works best.

if __name__ == "__main__":
    
    # DEMO THE ARCHIVE FEATURE:
    # I have set the file size limit to 20 lines to give a loook at how the archive feature works. 
    # Go into logger.api_logger and at the bottom where the logger is instantiated, all the optioins can be set
    do_demo()
