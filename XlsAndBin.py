#-*- coding: utf8 -*-
import xlrd
import xlwt
import os
import struct
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#define your folder name
RC_INC = "/include" #"/inc"
RC_STR = "/rc"      #"/str"

class XlsAndBin():
    def XlsAndBin_xls2bin(self,excelpath , strTargetDirec):
        myworkbook = xlrd.open_workbook(excelpath)
        try:
            mysheet = myworkbook.sheet_by_index(0)
        except:
            print "Could not find out sheet 0."
        #Total row
        intRowCount = mysheet.nrows
        #Total column
        intColumnCount = mysheet.ncols

        #-------------Read all data from excel to mylist
        mylist = []
        for i in range(1,intRowCount):
            mylist.append(mysheet.row_values(i))

        #-------------Sort it by first Column
        mylist_sort = sorted(mylist, key=lambda student : student[0])

        #**************************create directory inc and files in it*************************
        #-------------create directory inc
        strTmpDirectoryPath = strTargetDirec + RC_INC;
        if os.path.exists(strTmpDirectoryPath) == False:
            os.mkdir(strTmpDirectoryPath)

        #--------------------create or open file inc/Str.rc.h & clear it if the file already exists
        strFile = strTmpDirectoryPath + "/Str.rc.h";
        fsStrRcH = open(strFile,'w')

        #--------------------export data of string id (eg, ID_STR_XXX) in Excel to strStrIdArray
        for i in range(1,intRowCount):
            cell_value = mylist_sort[i-1][0]
            fsStrRcH.write("#define " + cell_value + "    " + str(i-1) + '\n')
        fsStrRcH.close

        #**************************create directory src and files in it*************************/
        #-------------create directory src
        strTmpDirectoryPath = strTargetDirec + RC_STR;
        if os.path.exists(strTmpDirectoryPath) == False:
            os.mkdir(strTmpDirectoryPath)

        for i in range(1,intColumnCount):
            strDirectoryPath = strTargetDirec  + RC_STR + "/rc_" + mysheet.cell(0,i).value;
            if os.path.exists(strDirectoryPath) == False:
                os.mkdir(strDirectoryPath)
            #--------------------create file: src/rc_XXX/Str.rc & clear it
            strFile = strDirectoryPath + "/Str.rc";
            fsStrRcH = open(strFile,'w')
            fsStrRcH.truncate()
            intStrByteCount = 0        #the total byte count of the all the string in one language , get ready for \src\rc_XX\bin\Str_res.bin
            for j in range(1,intRowCount):
                if(isinstance(mylist_sort[j-1][i],float)):
                    mylist_sort[j-1][i] = str(int(mylist_sort[j-1][i]))
                fsStrRcH.write(mylist_sort[j-1][0] + ";,\"" + mylist_sort[j-1][i].replace('\n','\\n') + "\"\n")
                str_tmp = mylist_sort[j-1][i].replace("\\n",'\n')
                intStrByteCount += (len(str_tmp.encode('utf_8')) + 1)
            fsStrRcH.close
            #--------------------create file: src/str_XXX/ResProfile and add data to them
            strFile = strDirectoryPath + "/ResProfile";
            fsStrRcH = open(strFile,'w')
            fsStrRcH.truncate()
            fsStrRcH.write("Str;rc_" + mysheet.cell(0,i).value + "/Str.rc\n")
            fsStrRcH.write("Color;rc/Color.rc\n");
            fsStrRcH.write("Image;rc/Image.rc\n");
            fsStrRcH.write("Mba;rc/Mba.rc\n");
            fsStrRcH.write("Num;rc/Num.rc\n");
            fsStrRcH.write("Label;rc_" + mysheet.cell(0,i).value + "/\n");
            fsStrRcH.write("Resolution;1366,768\n");
            fsStrRcH.write("Language;" + mysheet.cell(0,i).value + "\n");
            fsStrRcH.close
            #--------------------create directory: src/str_XXX/bin
            strDirectoryPath = strDirectoryPath + "/bin";
            if os.path.exists(strDirectoryPath) == False:
                os.mkdir(strDirectoryPath)
            #--------------------create file: src/str_XXX/bin/font_res.bin and add data to them
            strFile = strDirectoryPath + "/font_res.bin";
            fsStrRcH = open(strFile,'w')
            fsStrRcH.truncate()
            byteFontResBinHeader = [0x5F, 0x74, 0x73, 0x6D, 0x38, 0x00, 0x00, 0x00,
                                    0x04, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
                                    0xe9, 0xc5, 0x7d, 0xb6, 0x38, 0x00, 0x00, 0x00,
                                    0x38, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                    0x08, 0x5a, 0x0d, 0xb7, 0x88, 0x93, 0xab, 0x0a,
                                    0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00,
                                    0x18, 0x30, 0x6a, 0x0a, 0x00, 0x00, 0x00, 0x00];
            for j in byteFontResBinHeader:
                byte1 = struct.pack("B",j)
                fsStrRcH.write(byte1)
            fsStrRcH.close
            #--------------------create file: src/str_XXX/bin/Str_res.bin and add data to them
            strFile = strDirectoryPath + "/Str_res.bin";
            fsStrResBin = open(strFile,'w')
            fsStrResBin.truncate()
            #---------------------add header datas for src/str_XXX/bin/Str_res.bin
            intTotalbytes = 0x38;   #byte number of bin header 
            intTotalbytes = intTotalbytes + intStrByteCount + (intRowCount-1) * 4;      #the count number of every string 
            fsStrResBin.write(struct.pack("B",0x5F))         #[0x00-0x03]
            fsStrResBin.write(struct.pack("B",0x74))
            fsStrResBin.write(struct.pack("B",0x73))
            fsStrResBin.write(struct.pack("B",0x6D))
            fsStrResBin.write(struct.pack("I",intTotalbytes))#[0x04-0x07],total byte
            fsStrResBin.write(struct.pack("I",0x03));        #[0x08-0x0b]
            fsStrResBin.write(struct.pack("B",0x80));        #[0x0c-0x0f]
            fsStrResBin.write(struct.pack("B",0x0F));
            fsStrResBin.write(struct.pack("B",0xDF));
            fsStrResBin.write(struct.pack("B",0xBF));
            fsStrResBin.write(struct.pack("I",(intRowCount-1) * 4));      #[0x10-0x13]
            fsStrResBin.write(struct.pack("I",0x38));                   #[0x14-0x17]
            fsStrResBin.write(struct.pack("I",0x38));                   #[0x18-0x1b]
            fsStrResBin.write(struct.pack("I",intRowCount-1));            #[0x1c-0x1f],the number of string
            fsStrResBin.write(struct.pack("I",0x00));                                    #[0x20-0x23]
            fsStrResBin.write(struct.pack("I",0x01));                                    #[0x24-0x27]
            fsStrResBin.write(struct.pack("B",0xE9));                    #[0x28-0x2b]
            fsStrResBin.write(struct.pack("B",0xC5));                    #[0x28-0x2b]
            fsStrResBin.write(struct.pack("B",0x7D));                    #[0x28-0x2b]
            fsStrResBin.write(struct.pack("B",0xB6));                    #[0x28-0x2b]
            fsStrResBin.write(struct.pack("I",0x09));                                    #[0x2c-0x0f]
            fsStrResBin.write(struct.pack("B",0x80));                    #[0x30-0x34]
            fsStrResBin.write(struct.pack("B",0x0F));                    #[0x30-0x34]
            fsStrResBin.write(struct.pack("B",0xDF));                    #[0x30-0x34]
            fsStrResBin.write(struct.pack("B",0xBF));                    #[0x30-0x34]
            fsStrResBin.write(struct.pack("B",0xF4));                    #[0x35-0x38]
            fsStrResBin.write(struct.pack("B",0x0F));                    #[0x35-0x38]
            fsStrResBin.write(struct.pack("B",0xA5));                    #[0x35-0x38]
            fsStrResBin.write(struct.pack("B",0xB6));                    #[0x35-0x38]
            for j in range(1,intRowCount):
                str_tmp = mylist_sort[j-1][i].replace("\\n",'\n')
                str_len = len(str_tmp.encode('utf_8')) + 1
                fsStrResBin.write(struct.pack("I",str_len))
                fsStrResBin.write(str_tmp)
                fsStrResBin.write(struct.pack("B",0x00))
            fsStrResBin.close
        print "xls to bin is finished"

    def XlsAndBin_bin2xls(self,strTargetDirec):
        myworkbook = xlwt.Workbook()
        mysheet = myworkbook.add_sheet("str",cell_overwrite_ok=True)

        srcDirectoryPath = strTargetDirec + RC_STR
        if os.path.exists(srcDirectoryPath) == False:
            print("文件夹选择错误！此文件夹下必须有%s文件夹，%s里有一堆rc_XX"%(RC_STR,RC_STR))
            return
        #got a list to save rc_xx folder
        folderlist_tmp = os.listdir(srcDirectoryPath)
        if(len(folderlist_tmp) == 0):
            print "without rc_XX folder..."
            return
        folderlist = []
        for fl in folderlist_tmp:
            folderlist.append(fl[3:])
        #start to write excel for first line
        mysheet.write(0,0,"ID")#first string
        for i in range(0,len(folderlist)):
            mysheet.write(0,i+1,folderlist[i])
        #write excel for first column
        strFile = srcDirectoryPath + "/rc_" + folderlist[0] + "/Str.rc"
        strfileread = open(strFile,'r')
        linecnt = 1
        for strline in strfileread:
            #only save ID. eg: ID_DMP_BGM_OFF
            mysheet.write(linecnt,0,strline[:strline.index(";,")])
            linecnt += 1
        strfileread.close()
        #write all date 
        for rcstrindex in range(0,len(folderlist)):
            strFile = srcDirectoryPath + "/rc_" + folderlist[rcstrindex] + "/Str.rc"
            strfileread = open(strFile,'r')
            linecnt = 1
            for strline in strfileread:
                mysheet.write(linecnt,rcstrindex+1,strline[strline.index(";,")+3:-2].decode('utf_8'))
                linecnt += 1
            strfileread.close()
        #save
        myworkbook.save(strTargetDirec + "/strExcel.xls")
        print "bin to xls is finished"

# myx = XlsAndBin()
# myx.XlsAndBin_bin2xls("/tmp/str_default")
