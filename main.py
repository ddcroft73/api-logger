
from logger.api_logger import logzz
from time import sleep

if __name__ == "__main__":
    
    # DEMO THE ARCHIVE FEATURE:
    # I have set the file size limit to 20 lines to give a loook at how the archive feature works. 

    sleep(2)
    logzz.print("Working...")

    log_msg: str = 'This is a demo log message to diplay the archive feature. log entry #'
    for i in range(100):
        sleep(.08)
        if i%10==0:
          logzz.print(f'.printing line:{i}.')
        logzz.info(log_msg+str(i))

    logzz.print("Done!", stream=10, timestamp=True)

    # And a few others as well. 
    logzz.warn("THis is a warning log with timestamp."
               " THere is no Log file designated for 'warning',"
               " so it will go in the default log file\n", timestamp=1)    
    logzz.error("An error has occured.")
    logzz.login("Client: 212.456.45.67 logged in @: ", timestamp=1)
    logzz.debug("A message you can use to debug, with timestamp", timestamp=1)
