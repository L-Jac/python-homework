# 使用import导入smtplib模块
import smtplib
# 使用 from...import 从 email.header 导入Header
from email.header import Header
# 使用 from...import 从 email.mime.multipart 导入MIMEMultipart
from email.mime.multipart import MIMEMultipart
# 使用 from...import 从 email.mime.text 中导入 MIMEText
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

# 邮箱帐号设置，"aLing@qq.com"赋值给mailUser Aye
mailUser = "lwj-jack@qq.com"
# 邮箱授权码设置，"abcnawckdujkdace"赋值给mailPass
mailPass = "wxszyllauuwtdfgd"

# 使用smtplib.SMTP_SSL(服务器, 端口号),端口号为465，赋值给smtpObj
smtpObj: SMTP_SSL = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 使用login()函数传入邮箱账户和授权码，登录邮箱
smtpObj.login(mailUser, mailPass)

# 发件人、收件人yequbiancheng@baicizhan.com
sender = "lwj-jack@qq.com"
addressee = {"夜曲曲": "yequbiancheng@baicizhan.com"}

for mail in addressee:
    # 实例化 MIMEMultipart 对象，赋值给message
    message = MIMEMultipart()
    # 将发件人信息写入 message["From"]
    message["From"] = Header(f"jack<{sender}>")
    # 将收件人信息写入 message["To"]
    message["To"] = Header(f"{mail}<{addressee[mail]}>")
    # 将主题写入 message["Subject"]
    message["Subject"] = Header("给夜曲编程的一封信——Ajie")
    # 创建 MIMEText 实例，传入三个参数，赋值给 mailContent
    mailContent = MIMEText("HI,夜曲编程\n"
                           "第一次正式学习编程是在高三毕业后的暑假，学的是夜曲编程的python，夜曲编程的python课确实不错，生动形象，"
                           "并且可以提供足够的学习深度，可惜当时学到类的构造函数时卡壳了，当时真的学不明白，感觉理解不了这个东西，就先暂停了学习，"
                           "现在再次打开夜曲编程已经是大二了，这些年，我先后入门了C语言，dart，flutter，Java，再来学python已经轻松了不少，"
                           "真是感慨良多，初学python为我打下了学习语言的基础，对其他的语言有了一定的掌握后，又反哺了对于python的学习。\n"
                           "再见啦夜曲，也许未来我向人工智能领域靠近时会再接触你*(੭*ˊᵕˋ)੭*ଘ\n"
                           "一定要记得给我回信啊！夜曲曲(≧∇≦)ﾉ", "plain", "utf-8")

    # 使用message调用attach，传入参数mailContent
    message.attach(mailContent)
    # 使用sendmail(发送人，收件人，message.as_string())发邮件
    smtpObj.sendmail(sender, addressee[mail], message.as_string())
    # 使用print()输出"发送成功"
    print(f"{mail}发送成功")
