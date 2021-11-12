import pytest
import subprocess
"""
当固定模板，知道改哪个位置就行
"""
if __name__ == '__main__':
    # pytest运行测试用例的命令
    pytest.main(['-sv', './case/test_cart.py', '--alluredir=./reports/shangcheng', '-clean-alluredir'])
    # subprocess，把在终端操作的命令行转移到Python文件中操作,shell=Ture:表示接受这个命令，并以shell脚本形式运行
    subprocess.call('allure generate ./reports/shangcheng -o ./reports/html/ --clean', shell=True)
