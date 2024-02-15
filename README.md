# How to Run

## Setup mysql database
``` 
$ mysql -u root -p 
Enter password: **********
mysql> CREATE DATABASE IF NOT EXISTS dejavu;
```
Configure your database info in `dejavu.cnf.SAMPLE`

## Install Requirements
```
pip install -r requirements.txt
```
## Run the example.py
```
python example.py <path of file you want to test>
```
### Example: 
``` 
python example.py ./test/Walmart_add.mp3
```

### NOTE: All the audios present in the raw folder will be fingerprinted. To add a new audio, just add the file to `raw` folder.`