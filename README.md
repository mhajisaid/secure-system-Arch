# Authentication and authorization between simulated device and controller 

## Authentication and authorization between simulated device and controller prototype to investigate and demonstrate how to reduce the risk of unauthorized users manipulating the system.

## Introduction:

In relation to the system modelled in part 1, this prototype aims to investigate and demonstrate how implementing robust authentication and authorization mechanisms will significantly reduce the risk of unauthorized users manipulating the system. as previously mentioned in the system modelled in part 1, one of the vulnerabilities found was authorization and authentication between device and controller. Poor authorization and authentication protocols enable cybercriminals to manipulate the system and carry out unauthorised actions (Botas, 2016). 
This prototype mitigates this risk by implementing three authentication and authorization methods such as token as another factor of authentication, max tries of 3 before server lock user out and the use of asterisk to mask the password.


## Code decomposition
## Server.py
### Importing modules:

<span class="image fit"><img src="images/modules.PNG" alt="" /></span>

### Create and configure server socket:

<span class="image fit"><img src="images/serversocket.PNG" alt="" /></span>

### Define username and password:

<span class="image fit"><img src="images/unpw.png" alt="" /></span>

### Define maximum login:

<span class="image fit"><img src="images/max.png" alt="" /></span>

### Define token function:

 <span class="image fit"><img src="images/tokenf.png" alt="" /></span>

### Define client handling function:

<span class="image fit"><img src="images/clienthandle.png" alt="" /></span>

### Accepting connection loop:

<span class="image fit"><img src="images/conloop.png" alt="" /></span>

## Server.py

### Pwinput library need to be installed for the application to run:

<span class="image fit"><img src="images/pip.png" alt="" /></span>

### Importing modules:

<span class="image fit"><img src="images/cmod.png" alt="" /></span>

### Create and connect client socket:

<span class="image fit"><img src="images/ccon.png" alt="" /></span>

### Token authentication function:

<span class="image fit"><img src="images/ctoken.png" alt="" /></span>

### Define attempt range:

<span class="image fit"><img src="images/cdrange.png" alt="" /></span>

### Password masking:

<span class="image fit"><img src="images/pwmask.png" alt="" /></span>

### Client interaction:

<span class="image fit"><img src="images/cclienti.png" alt="" /></span>

## program video demonstration 

<img src="images/video.gif">

## usage

1. first launch the server then the client, server will listen for a connection by displaying waiting for a connection... and the client will ask for username.

2. at the client end enter username, then it will request for a password, the password will be masked as asterisk. 

3. if you enter correct username and password client will login successful.

4. if you enter incorrect username or password client will display invalid credentials and the remianing attempts

5. if both username and password is correct client will request for token entry.

6. if token is entered incorrectly, Invalid token! Please try again. message will be displayed 

7. if token is ented correctly, Welcome! You have been authenticated successfully. message will be displayed.

8. The server side will display User mohammed authenticated correctly.

## References: 

* Alvaro Botas, Juan F. Garcıa, Javier Alonso, 2016. Security Assessment Methodology for MobileApplications, University of Leon, Spain Leon, Spain.


