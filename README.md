# Calculate Relative Paths

## Calculate relative paths for open files
Looks at open files and calculate relative paths from active window and insert them at the cursor location. 
 {"keys": ["super+shift+1"], "command": "relpathwindow"},

## Calculate relative paths for selected texts
Loops through each line of selected text and replace them with relative paths if the string matches the path of other open files.
 {"keys": ["super+shift+2"], "command": "relpathselection"},

