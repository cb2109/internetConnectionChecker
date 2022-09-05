# Internet connection checker
## Install 
Download the two files
main.py and connection_checker.py

Download and install python3 https://www.python.org/downloads/ (3.10 should be fine)

## Running
Run it by opening command prompt

Run commands:
```bash
cd $HOME\Downloads
python main.py
```
You should leave this command prompt open and running in the background
## Reading the output
In the download folder a new file should appear, network.log 

In there you should get two types of log messages:
```
2021-09-16 14:12:35,293 root         INFO     Network connection monitoring started at: ...
```
This one is just a starting message
```
2021-09-16 15:07:42,912 root         ERROR    Network Connection Unavailable at: ....
```
This one is the actual error message that your connection dropped
```
2021-09-16 15:07:42,927 root         INFO     Network Connectivity Restored at: ...
```
This is the restore time
```
2021-09-16 15:07:42,927 root         ERROR    Network Connection was Unavailable for 0:00:00.015486
2021-09-16 15:07:42,927 root         ERROR    Total Time since start 0:00:00.015486
```
Those two error messages give you a summary of how big THAT outage was and how long since you started running the program.
