import time
from subprocess import Popen, PIPE

prog = Popen("~/Desktop/Drone/reader.py", shell=True, stdin=PIPE, stdout=PIPE)

prog.stdin.write("This will go to script A\n")
print prog.stdout.read()

prog.wait()
