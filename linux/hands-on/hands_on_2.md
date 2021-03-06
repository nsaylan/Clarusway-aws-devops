Hands-on Linux-02 : Linux Environment Variables
Purpose of the this hands-on training is to teach the students how to use environment variables.

Learning Outcomes
At the end of the this hands-on training, students will be able to;

explain environment variables.

understand Quoting with Variables.

Outline
Part 1 - Common Environment Variables & Accessing Variable

Part 2 - Path Variable

Part 3 - Quoting with Variables

Part 4 - Sudo Command

Part 1 - Common Environment Variables & Accessing Variable
​

Difference between "env" and "printenv" commands.​
env
printenv
printenv HOME
echo $HOME
env HOME
​

Create a shell variable.​
CLARUS=way
env
set
set | grep CLARUS
echo $CLARUS
​

Create an environment variable.​
export WAY=clarus
env
​

Difference between shell and environment variables. Create a user, name it "user1", switch to user1, check the environment and shell variables.​
export WAY=clarus
sudo su
useradd user1
passwd user1
exit
su user1
env | grep WAY
set | grep CLARUS
​

Change the environment value.​
export WAY=linux
env
export WAY=script
env
​

Remove the environment variable.​
export WAY=clarusway
env | grep WAY
unset WAY
env | grep WAY
​

Part 2 - Path Variable
​

PATH variable.​
printenv PATH
cd /bin
ls
ls c*
​

Add a path to PATH variable for running a script.​
cd
mkdir test
cd test
nano test.sh
echo "hello world"
chmod +x test.sh
./test.sh
cd
./test.sh
./test/test.sh
printenv PATH
cd test
pwd
export PATH=$PATH:/home/ec2-user/test
printenv PATH
cd
test.sh
cd /
test.sh
​

Using the environment variable in the script.​
cd test
export CLARUS=env.var
WAY=shell.var
cd test
nano test1.sh
chmod +x test1.sh
./test1.sh
​

Part 3 - Quoting with Variables
​

Double Quotes.​
MYVAR=my value
echo MYVAR
MYVAR="my value"
echo $MYVAR
MYNAME=timothy
MYVAR="my name is $MYNAME"
echo $MYVAR
​
MYNAME="timothy"
MYVAR="hello $MYNAME"
echo $MYVAR
MYVAR="hello \$MYNAME"
echo $MYVAR
​

Single Quotes.​
echo '$SHELL'
echo 'My\$SHELL'
​

Part 4 - Sudo Command
​

Sudo Command.​
yum update
sudo yum update
cd /
mkdir testfile
sudo su
sudo -s
sudo su -