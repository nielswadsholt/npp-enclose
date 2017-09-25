# npp-enclose
Small collection of Python scripts that enables adding/removing quotes and brackets around selected text in Notepad++

Use with the PythonScript plugin: http://npppythonscript.sourceforge.net.

INSTRUCTIONS:
1. Install PythonScript using Notepad++'s built-in Plugin Manager (Plugins > Plugin Manager)
2. For each script, click Plugins > Python Script > New script, choose an appropriate file name and click 'Save'. This will create an empty .py-file in the PythonScript\scripts folder and open it for editing.
3. Paste the code for the appropriate script, modify as needed and save the file.
4. Select some text in an open file, click Plugins > Python Scripts > Scripts and click on the newly added script name to verify that it works as expected.
5. Click Plugins > Python Scripts > Configuration
6. Select the newly added script in the top window, then click the 'Add' button below it to add it to the main Python Script menu. Leave 'Initialization' set to 'LAZY'.
7. To assign a shortcut to the new script: Restart Notepad++, navigate to Settings > Shortcut Mapper > Plugin commands and locate the script. Click 'Modify' and choose an appropriate shortcut (be sure to check that it is not already taken).
