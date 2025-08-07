#!/usr/bin/env python
import os
import sys

"""
# 导入依赖库 
pip install -r requirements.txt # 导入依赖库 

# 运行项目：默认端口 8000
python manage.py runserver

重启项目：
    # 查找占用 8000 端口的进程
    sudo lsof -i:8000

    # 终止进程（将 <PID> 替换为实际的进程ID）
    kill -9 <PID>

    ctrl + c 可以临时退出
    
    deactivate退出虚拟环境，回到正常终端

    # 1. 临时保存所有修改
    git stash
    # 2. 拉取远程代码
    git pull
    # 3. 恢复暂存的修改（可能需解决冲突）
    git stash pop



"""
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_t.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
