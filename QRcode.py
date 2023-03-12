from MyQR import myqr

# 图片的路径
imgPath = "image/yequ_gif/._algo发射爱心.gif"
# 二维码要展示的数据链接
data = "https://shimo.im/docs/nTQ5XVG3NEoyNIGl/readX"
# 二维码要保存的位置
filePath = "D:/pythonworkspace/image"
# 二维码要保存的名称
imgName = "QR1.gif"

# TODO 将制定的图片与数据生成一个彩色的二维码图片myQR.png
version, level, qr_name = myqr.run(
    # 展示的数据
    data,
    # 图片边长1-40
    version=1,
    # 纠错水平
    level='H',
    # 是否与图片结合艺术化（路径）
    picture=imgPath,
    # 生成的二维码颜色：True-彩色
    colorized=True,
    # 图片对比度
    contrast=1.2,
    # 图片亮度
    brightness=1.2,
    # 生成的文件名
    save_name=imgName,
    # 文件保存路径
    save_dir=filePath)
