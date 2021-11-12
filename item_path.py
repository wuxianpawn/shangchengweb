import os
"""
目的：通过item_path.py获取整个工程的绝对路径
"""
ABS_PATH = os.path.abspath(__file__)  # 获取当前文件的绝对路径
DIR_NAME = os.path.dirname(ABS_PATH)  # 获取该绝对路径下的文件路径
