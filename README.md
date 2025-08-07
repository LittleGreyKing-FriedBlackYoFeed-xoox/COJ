# COJ 项目说明

本项目为基于 Django + MySQL + 前端框架的在线评测系统。

## 主要结构
- `manage.py`：Django 项目管理脚本
- `web_t/`：Django 主配置目录（含 settings.py、urls.py、wsgi.py）
- `own_models/`：自定义数据模型
- `permission_system/`：权限系统
- `static/`：静态资源目录
- `templates/`：模板目录
- `test_script/`：测试与数据脚本
- `requirements.txt`：依赖包列表
- `.gitignore`：Git 忽略文件

## 快速开始
1. 安装依赖：
   ```shell
   pip install -r requirements.txt
   ```
2. 配置数据库连接，参考 `.env.example` 或 `web_t/settings.py`。
3. 运行数据库迁移：
   ```shell
   python manage.py migrate
   ```
4. 启动开发服务器：
   ```shell
   python manage.py runserver
   ```

## 重要说明
- 请勿提交敏感信息（如真实数据库密码），建议使用 `.env` 文件管理环境变量。
- 生产环境请关闭 DEBUG 并配置安全参数。

## 目录说明
- `SQL/`：数据库初始化及测试脚本
- `test_script/`：批量生成、校验数据的脚本

## 贡献
欢迎提交 issue 和 PR。