<!-- TITLE: fs -->

#  **`fs[?]+-*`** manage flagspaces


```text
Usage: fs [*] [+-][flagspace|addr] # Manage flagspaces
```


- **`fs`** display flagspaces
- **`fs*`** display flagspaces as r2 commands
- **`fsj`** display flagspaces in JSON
- **`fs *`** select all flagspaces
- **`fs flagspace`** select flagspace or create if it doesn't exist
- **`fs-flagspace`** remove flagspace
- **`fs-*`** remove all flagspaces
- **`fs+foo`** push previous flagspace and set
- **`fs-`** pop to the previous flagspace
- **`fs-.`** remove the current flagspace
- **`fsq`** list flagspaces in quiet mode
- **`fsm [addr]`** move flags at given address to the current flagspace
- **`fss`** display flagspaces stack
- **`fss*`** display flagspaces stack in r2 commands
- **`fssj`** display flagspaces stack in JSON
- **`fsr newname`** rename selected flagspace