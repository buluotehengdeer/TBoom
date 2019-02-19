import os


class Settings(object):
    """
		配置文件
    """
    # 根目录
    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + "/"
    # 登入界面图片
    LOGIN_IMAGE = BASE_DIR + "/image/login.jpeg"
    # 数据库连接信息
    DATABASE = "mysql+pymysql://jake:187187@localhost/gamedb"
