# PY4J-Bulk 
## Libraries Used
#### 1. Gateway server: Used to pass object of functions
#### 2. Threading: To make threads

_________________________________________________________________________________________________________

## User defined Functions:
### In Java
#### divi: divides the parameter by 2 and return result
#### multi: multiplies parameter by 2 and return result
### In Python
#### divii : Calls java funtions divi
#### multii : Calls java function multi
_________________________________________________________________________________________________________

## Target: Send multiple requests to java program and gets values
_________________________________________________________________________________________________________
## Working of code
#### PingPlayer.java

First two functions divi and multi are made in class PingPlayer.Then create a main function .In main , we create a object y of class Pingplayer .

        PingPlayer y = new Pingplayer();
Now we pass the object y to python program through gateway server and start the server and after starting server we print message

                 GatewayServer gatewayServer = new GatewayServer(y);
                 gatewayServer.start();
                 System.out.println("Gateway Server Started");
#### Test.py

In class Pythonplayer ,there are two functions divii and multii ,these functions call java fuctions divi and multi respectively and store the returned value in 
result and print it.
we will receive object of java function through gateway server by using:

        y=gateway.entry_point

we have to check for multiple requests so we make two threads which will execute divii and multii many times.The below code will call java functions 1000 times

       for i in range(1000):
           t1=Thread(target=pong_player.multii,args=(i,))
           t1.start()
Similarly second thread will execute divii function 100 times.
  
