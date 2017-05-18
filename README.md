# progmon
Python-based progress monitor for time-consuming job

## Features
This script shows the progress of a task by followings periodically:
* Checking the size of a folder
* Checking the number of files in a folder
* Checking user-defined command

## Usage
```
usage: progmon.py [-h] [--path PATH] [--target TARGET] [--command COMMAND]
                  mode

Monitor the progress of a task

positional arguments:
  mode               command mode [filecount|foldersize|custom]

optional arguments:
  -h, --help         show this help message and exit
  --path PATH        Path to count the number of files. It should be set in
                     filecount mode
  --target TARGET    Final number to reach when the progress ends
  --command COMMAND
```

## Example commands
```
python progmon.py filecount --path /path/to/check/files --target target_value
python progmon.py foldersize --path /path/to/check/size --target target_value
python progmon.py custom --command "du -sm /path/to/check/size | cut -f 1" --target target_value
```

## Screenshot
```
$ python progmon.py foldersize --path /backup/database_look/jihoonk/LISA --target 6860516
3705/6860516 (0.05%) 22:03:52.413588
```

