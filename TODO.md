
Make the file read write actions asynchronous add aiofiles

1. **Go all asynchronous**:  THis is pretty tricky. If I want to go async, which is a good idea given the nature of Web APIs I think I need to restructure the classes. It's probably a good idea anyway since I didn't totally adhere to best practices when designing the classes. Separation of concerns and all. 
