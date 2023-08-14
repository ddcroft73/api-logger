
from logger.api_logger import logzz

if __name__ == "__main__":

    # WHen the program is ran all the neccesary directories are created as well as the archive directories
    # if set to True 
    # You can run this file from within the IDE, or use the shell script. The shell script just stops it from writing 
    # the bytecode. 
    
    logzz.info("This is an info log. It will go in the Info log...")

    logzz.warn("This is a warning, log with timestamp."
               " THere is no Log file designated for 'warning',"
               " so it will go in the default log file", timestamp=1)
    
    logzz.error("An error has occur3d.")
    logzz.debug("A message you can use to debug, with timestamp", timestamp=1)
