
#The pathlib module provides a way to represent and interact with filesystem paths.

import pathlib
p = pathlib.Path("") #You could also use pathlib.Path.cwd() and get an absolute path directly.
py_files = p.glob("*.py")

#List files ending with 'py' in current directory
print("*.py:", list(py_files)) 

#List files ending with 'py' in current directory including subdirectories
print("**/*.py:", list(p.glob("**/*.py")))

#List all files one level deep that are within the subdirectory
print("*/*:", list(p.glob("*/*")))

#Get only files from path by checking the is_file method
print("Files in */* ", [f for f in p.glob("*/*") if f.is_file()])

#List hidden files (in home directory ) example
p = pathlib.Path.home()
print(list(p.glob(".*")))

'''
The subprocess module allows us to start a new process and communicate with 
other programs on the OS.The return value is an instance of CompletedProcess, 
but the output of the command is sent to standard output in the console.
'''

import subprocess
subprocess.run(["ls"])

#If you want to be able to capture and see the output that our process produced, 
# you need to pass the capture_output argument. This will capture stdout and stderr 
# and make it available in the completedProcess instance returned by run:
result = subprocess.run(["ls"], capture_output=True)
print("stdout: ", result.stdout)
print("stderr: ", result.stderr)

#The stdout and stderr result is a byte string. If you know that the result is text, 
# you can pass the text argument to have it decoded.

result = subprocess.run(["ls"], capture_output=True, text=True)
print("stdout: \n", result.stdout)

#We can pass more arguments, such as -l, to have the files listed with details:
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("stdout: \n", result.stdout)

'''
In some situations, you might want to inspect the return code that our return process has returned. 
In those situations, you can just check the returncode attribute in the returning instance of subprocess.run
0 - Success
1 - Error
'''
result = subprocess.run(["ls", "not_available_file"])
print("return code: ", result.returncode)

'''
If you wanted to make sure that the command succeeded without always having to check that 
the return code was 0 after running, you could use the check=True argument. This will raise 
errors if the program reported any
'''

result = subprocess.run(["ls","not_available_file"], check=True) # Comment this line for below code to work
print("Return code: ", result.returncode)

#Print environment variables
result = subprocess.run(["env"], capture_output=True, text=True)
print("Env details:",result.stdout)