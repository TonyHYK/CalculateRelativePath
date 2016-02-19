# Calculate Relative Paths
Calculate relative paths from current file to other open files.

## Calculate relative paths for all open files
Looks at all other open files and insert their relative paths at the cursor location. 
```{"keys": ["super+shift+1"], "command": "relpathwindow"},```

## Calculate relative paths for selected texts
Loops through each line of selected text and replace them with relative paths if the string matches the path of other open files.
```{"keys": ["super+shift+2"], "command": "relpathselection"},```

