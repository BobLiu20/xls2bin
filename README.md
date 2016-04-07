# xls2bin
Use for Mstar Supernova string translate

1.在QtUI_Project中修改UI
2.然后使用pyuic4 mainwindow.ui -o qtui.py 命令，转换为python文件
3.将生成的qtui.py拷贝到上一级目录，供py使用。


最后，可以使用pyinstaller打包生成对应平台的可执行文件
安装的话使用sudo pip install pyinstaller

用这个生成可执行文件：

pyinstaller main.py


baifang20@qq.com

