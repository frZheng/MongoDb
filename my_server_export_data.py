
import os
tables = ["apply",
 "ballot",
 "db_position",
"IPO",
"mac_addr",
"today_apply",
 "today_trade",
"user_info",
 ]

for table in tables:
    # table = "db_position"
    # 需要下载mongodb-database-tools-windows-x86_64-100.5.2,解压后添加到系统变量path里面
    # mongoimport 只能在命令行执行
    # db_cmd = 'mongoexport --host  127.0.0.1 --port 27017 -d kzz -c db_position -o "E:\dataBase_back\momgodb\db_position.json"'
    # db_cmd = 'mongoexport --host  127.0.0.1 --port 27017 -d kzz -c {} -o "E:\dataBase_back\momgodb\{}.json"'.format(table,table)
    db_cmd = 'mongoimport --host  127.0.0.1 --port 27017 -d kzz -c {} --file "E:\dataBase_back\momgodb\{}.json" --type=json'.format(table,table)
    # os.system(db_cmd)
    print(db_cmd)

    """
    VBoxManage export 000_001_0001 -o C:\test\000_001_0001.ova
    vboxmanage import C:\test\000_001_0001.ova 
    """