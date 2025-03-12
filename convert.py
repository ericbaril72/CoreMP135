# converting imagesw from this URL: https://notisrac.github.io/FileToCArray/
#
#

outfile=open("./cmd_show_logo.h","w")
outfile.write('uint8_t eb_custom_image[] = {')
with open("./bootpicpng.h") as infile:
    cnt=0
    isdata=False
    newline=''
    while line:=infile.readline():
        cnt+=1
        
        if '0x' in line:
            values=line.split(',')
            newline+="\n      "
            #
            #print(values[:16])
            #print(values[-16:])
            #print("len:",len(values))
            for i in range(0,int(   (len(values))/2)):
                if '0x' in values[i]:
                    value=int(values[i],16)
                    bytes_value='0x{:02X}, 0x{:02X}, '.format(value>>8,value&0xff)
                    newline +=bytes_value
                    
            if cnt<10:
                print(cnt,line)
            
            #print("to:",newline)
            #print("len:",len(newline.split(",")))
            outfile.write(newline[:-2])
            newline=','
            
            
outfile.write('\n};\n')
