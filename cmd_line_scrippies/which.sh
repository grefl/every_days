echo Checking node version
errormessage=$(nod --version 2>&1)
if [ $? -eq 0 ]; then
   echo OK
else
  echo "Nod doesn't exit on your system"
  echo $errormessage
fi
# or this way
nod --version
if [ $? -eq 0 ]; then
   echo OK
else
   echo FAIL
fi
