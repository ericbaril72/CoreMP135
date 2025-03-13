# To convert a Picture ( BMP/jpg/png ) to "C" code structure
#
# 1. Online Converter to .c file
# URL: https://notisrac.github.io/FileToCArray/
# Result is encoded in 16-bits
#
# This script converts online converter result arrays in the form of
#       0xffff, 0x1234, 0xffff, 0xabcd, ...
#
#  to
#       0xff, 0xff, 0x12, 0x34, 0xff, 0xff, 0xab, axcd, ....
#


SRC_H_FILENAME     = "./bootpicpng.h"
TARGET_H_FILENAME  = "./cmd_show_logo.h"
IMG_VARNAME        = 'uint8_t eb_custom_image[]'

outfile=open(TARGET_H_FILENAME,"w")
outfile.write(IMG_VARNAME+' = {')

with open(SRC_H_FILENAME) as infile:
    cnt=0
    isdata=False
    newline=''
    while line:=infile.readline():
        cnt+=1
        
        if '0x' in line:
            values=line.split(',')
            newline+="\n      "
            
            for i in range(0,int(   (len(values))/2)):
                if '0x' in values[i]:
                    value=int(values[i],16)
                    bytes_value='0x{:02X}, 0x{:02X}, '.format(value>>8,value&0xff)
                    newline +=bytes_value
                    
            outfile.write(newline[:-2])
            newline=','

outfile.write('\n};\n')
