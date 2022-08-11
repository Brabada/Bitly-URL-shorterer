# Bitly URL shorterer

This project accept URLs and returns a bitlink for them.
It can also accept bitlinks and print the number of clicks on bitlink.

### How to install

You should get an access token for bit.ly from [personal profile](https://app.bitly.com/settings/api/).
It's look like that:
```
a18b7a8d412ea74b17bda2a06f1b69fa3805a712
```
After you add token to .env file:
```commandline
BITLINK_ACCESS_TOKEN=a18b7a8d412ea74b17bda2a06f1b69fa3805a712
```
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```commandline
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes.
