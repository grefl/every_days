# A list of useful commands to run 



## sed

Search and replace. NOTE: it modifies the file due to the `-i` flag. Otherwise this will only print to stdout
```
sed -i '/pattern/replacement/' filename
```
Same as above but for whole directories of files. NOTE: dangerous. Only do if you have everything in version control 
```
sed -i '/pattern/replacement/' dir/* 
```
