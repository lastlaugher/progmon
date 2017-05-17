import argparse
import subprocess
import time
import datetime

def visualize(status, target=None):
    if target == None:
        str = '%s' % (status)
    else:
        str = '%s/%s (%.2f%%)' % (status, target, float(status)/float(target) * 100)

    print '\x1b[1A' + str, datetime.datetime.today().time()

def progmon(mode, path, target, command):
    if (mode == 'filecount' or mode == 'foldersize') and path == None:
        print 'Path value should be set'
        exit()

    if mode == 'filecount':
        command = 'ls ' + path + ' | wc -l'
    elif mode == 'foldersize':
        command = 'du -sm ' + path + ' | cut -f 1'
    elif mode == 'custom':
        path = ''
    else:
        print 'Mode value is invalid'
        exit()

    print

    while True:
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read().strip()
        visualize(result, target)
        time.sleep(1)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Monitor the progress of a task')
    parser.add_argument('mode', help='command mode [filecount|foldersize|custom]')
    parser.add_argument('--path', help='Path to count the number of files. It should be set in filecount mode')
    parser.add_argument('--target', help='Final number to reach when the progress ends')
    parser.add_argument('--command', help='')

    args = parser.parse_args()

    progmon(args.mode, args.path, args.target, args.command)
