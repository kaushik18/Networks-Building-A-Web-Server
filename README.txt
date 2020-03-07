- Script Name: webServer.py

Executing the script:
- Ensure you are in the same directory where the script is located.
- Ensure that the attached .html and .txt file are in the same directory as the script

Run the script
- python2 webServer.py (Please click allow if asked "Do you want the application “Python.app” to accept incoming network connections?")

The above command will execute the script and connect to the server. Then please open the browser to access from client-side the files

Go to the following in the browser:

- http://localhost:8080/index.html
- http://localhost:8080/index.txt

These commands will let you access the files through the server.

You can try to access other files through this port and you should end up with a 404 not found error message. 

- 2 files are included in the zip folder: index.html and index.txt and these files can be accessed through the server and TCP connection. Any other file being accessed will return a 404 not found. 

