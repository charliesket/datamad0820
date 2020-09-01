
#1
echo "Hello World"
#2
mkdir [new_dir]
#3
rm -r [new_dir]
#4
cp lorem/sed.txt lorem-copy
#5
cp lorem/lorem.txt lorem/at.txt lorem-copy
#6
cat lorem/sed.txt
#7
cat lorem/at.txt lorem/lorem.txt
#8
cat lorem-copy/sed.txt | head -n 3 
#9
cat lorem-copy/sed.txt | tail -n 3 
#10 
echo "Homo homini lupus" >> lorem-copy/sed.txt
#11
cat lorem-copy/sed.txt | tail -n 3 
#12
sed -i "" 's/et/ET/g' "lorem-copy/at.txt"
#13
w
#14
pwd
#15
ls -l -d /Users/Carlos/datamad0820/module-2/lab-bash/lorem/*
#16
wc lorem/sed.txt
#17
ls -iname "lorem"   
#18
grep et lorem/at.txt
#19
grep et lorem/at.txt |wc -l
#20
grep et lorem-copy/* |wc -l


#BONUS
#1
name=Carlos
#2
echo $name
#3
mkdir [Carlos]
#4 
rm -r [Carlos]

"""
#5
files=/Users/Carlos/datamad0820/module-2/lab-bash/lorem
for file in $files
do
echo $file
done
"""
#6
top
ps -e
#7
df

#8 
alias datamad="cd /Users/Carlos/datamad0820"

#9
tar -czvf lorem-compressed.tar.gz lorem lorem-copy

#10
tar -xzvf lorem-compressed.tar.gz lorem-uncompressed


