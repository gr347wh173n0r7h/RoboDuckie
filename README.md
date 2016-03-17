# RoboDuckie

Automated Twitter Bot in CLI

Allows user to specify set a text file of text and image tweets. Bot parses file, determines content, and outputs tweets after a specified interval. 

### Version
0.1 

### Tech

RoboDuckie uses a number of open source projects to work properly:

* [Python] - Programming Language.
* [PIP] - Python Package Manager.
* [Tweepy] - Python Twitter Library.


### Installation

 1- Python comes pre-installed on Ubuntu, if not install Python.
 
 2- Install pip

```sh
~$ sudo apt-get install python-pip python-dev build-essential 
~$ sudo pip install --upgrade pip 
~$ sudo pip install --upgrade virtualenv 
```

3- Install Tweepy Library
```sh
~$ pip install tweepy
```

3- Clone & Open Repository 
```sh
~$ git clone git@github.com:gr347wh173n0r7h/RoboDuckie.git
~$ cd RoboDuckie/
```
#### RUN
1- Add Twitter Keys
* Log into Twitter
* Go to [Twitter](http://apps.twitter.com) and Create new Application, set Access Level to "Read and Write"
* Go to "Keys and Access Tokens" Tab
* Select "Generate Consumer Key and Secret"
* Make note of:
  * Consumer Key (API Key)
  * Consumer Secret (API Secret)
  * Access Token
  * Access Token Secret
  
2- Create a authentication.txt & add Twitter keys (one per line)

~/RoboDuckie/authentication.txt:
```sh
Consumer_Key
Consumer_Secret
Access_Token
Access_Token Secret
```

3- Create a input.txt & add Tweets (one per line), with propper tag . Tag options: 

* "[TXT] <Tweet>"
* "[IMG] #<img_path> <Tweet>"

~/RoboDuckie/input.txt:
```sh
[TXT] Robot Ducks are awesome!
[IMG] #duck.jpg This is a RoboDuckie.
```

4- Run Duckie
```sh
~RoboDuckie/$ python RoboDuckie.py <authentication file> <input file> <sleep time in seconds>
```
ex:
```sh
~RoboDuckie/$ python RoboDuckie.py auth.txt input.txt 60
```
### Future

* Dynamic Input Parsing
* Responsiveness to External Stimulus
* Multi-Threaded Resource Sharing

### License
----

MIT

   [tweepy]: <http://www.tweepy.org/>
   [pip]: <https://pypi.python.org/pypi/pip>
   [python]: <https://www.python.org/>
 

