from django import template

register = template.Library()

@register.filter(name='role_text')
def role_text(value):
    """
    将角色代码转换为对应的文本
    1: 学 (学生)
    2: 教 (教师)
    3: 管 (管理员)
    """
    role_map = {
        1: '学',  # 学生
        2: '教',  # 教师
        3: '管'   # 管理员
    }
    return role_map.get(value, '未知')
