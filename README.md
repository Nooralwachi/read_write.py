# read_write.py

Please write two functions:
1) function named write_list(filename, lines, interval)
    filename: the file you want to write to
    lines: a list of strings you want to append to end of the file
    interval: an integer indicates the interval (in seconds) you write a line to the file
 
2) function named read_end(filename, interval, times)
    filename: the file you want to read from
    interval: an integer for the interval (in seconds) you read the last line from the file
    times: an integer for how many times you want to read the last line from the file
 
Note: only read the last end when there's new line written; You might need to use threading if you use Python
 
example:
lines = ["this is line1\n", "this is line2\n", "this is line3\n", "this is line4\n"]
file1 = /path/to/file
 
Output:
this is line1
this is line2
this is line3
this is line4
