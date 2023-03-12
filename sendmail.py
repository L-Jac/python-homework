# 使用import导入smtplib模块
import smtplib
# 使用 from...import 从 email.header 导入Header
from email.header import Header
# 使用 from...import 从 email.mime.application 导入 MIMEApplication
from email.mime.application import MIMEApplication
# 使用 from...import 从 email.mime.multipart 导入MIMEMultipart
from email.mime.multipart import MIMEMultipart
# 使用 from...import 从 email.mime.text 中导入 MIMEText
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

stop

# 邮箱帐号设置，"aLing@qq.com"赋值给mailUser Aye
mailUser = "lwj-jack@qq.com"
# 邮箱授权码设置，"abcnawckdujkdace"赋值给mailPass
mailPass = "wxszyllauuwtdfgd"

# 使用smtplib.SMTP_SSL(服务器, 端口号),端口号为465，赋值给smtpObj
smtpObj: SMTP_SSL = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 使用login()函数传入邮箱账户和授权码，登录邮箱
smtpObj.login(mailUser, mailPass)

# 发件人、收件人
sender = "lwj-jack@qq.com"
addressee = {"zxq": "2903553737@qq.com", "wsf": "1758088628@qq.com", "gaj": "1057518707@qq.com"}

for mail in addressee:

    # 实例化 MIMEMultipart 对象，赋值给message
    message = MIMEMultipart()
    # 将发件人信息写入 message["From"]
    message["From"] = Header(f"jack<{sender}>")
    # 将收件人信息写入 message["To"]
    message["To"] = Header(f"<{addressee[mail]}>")
    # 将主题写入 message["Subject"]
    message["Subject"] = Header(f"{mail}-文件分享")
    # 创建 MIMEText 实例，传入三个参数，赋值给 mailContent
    mailContent = MIMEText(f"txt里是源码\n"
                           f"附件有python，安装教程：\n"
                           f"https://zhuanlan.zhihu.com/p/104502997\n"
                           f"pycharm太大发不动X﹏X，官网\n"
                           f"https://www.jetbrains.com/pycharm/"
                           f"安装教程：\n"
                           f"https://zhuanlan.zhihu.com/p/359897213", "plain", "utf-8")
    # 文件名
    files = {"D:/java_c_python/": "sendmail_python.txt",
             "D:/python/": "python-3.10.9-amd64.exe"}

    for address in files:
        # 将字符串address + files[address]拼接即文件地址，赋值给变量filePath
        filePath = address + files[address]
        if files[address][len(files[address]) - 3:] == "txt":

            # 使用with...as以r方式，打开文本，并赋值给imageFile
            # UnicodeDecodeError: 'gbk' codec can't decode byte 0x8e in position 76: illegal multibyte sequence
            with open(filePath, encoding='gb18030', errors='ignore') as imageFile:
                # 使用read()读取文件内容，赋值给fileContent
                fileContent = imageFile.read()
            # 使用MIMEImage创造实例，传入参数fileContent，赋值给att
            att = MIMEText(fileContent)
            # 调用add_header()方法，传入参数，设置附件标题
            att.add_header("Content-Disposition", "attachment", filename=files[address])
        elif files[address][len(files[address]) - 3:] == "exe":
            # 使用with...as以r方式，打开文本，并赋值给imageFile
            with open(filePath, "rb") as imageFile:
                # 使用read()读取文件内容，赋值给fileContent
                fileContent = imageFile.read()
            # 使用MIMEImage创造实例，传入参数fileContent，赋值给att
            att = MIMEApplication(fileContent)
            # 调用add_header()方法，传入参数，设置附件标题
            att.add_header("Content-Disposition", "attachment", filename=files[address])

        else:
            continue
        # 使用message调用attach，传入参数att
        message.attach(att)
    # 使用message调用attach，传入参数mailContent
    message.attach(mailContent)
    # 使用sendmail(发送人，收件人，message.as_string())发邮件
    smtpObj.sendmail(sender, addressee[mail], message.as_string())
    # 使用print()输出"发送成功"
    print(f"{mail}发送成功")
