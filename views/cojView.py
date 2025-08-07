from django.conf import settings  # 新增导入
from django.shortcuts import render
from django.template.loader import get_template  # 新增导入
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
# from .models import User

# Go to the COJ homepage.
def requestIndex(request):  # 发起请求页面
    return render(request, "cojHtml/requestIndex.html")


# Go to the Learning Data homepage.
def learningData(request):  # 发起请求页面
    context = {
        "d": {
            "TOTAL_NUMS": 42,  # 示例数据（确保是数字）
            "experience": 100,  # 新增示例数据
            "TOTAL_ROW": {
                "era": {
                    "tang": 10,
                    "song": 20,
                    "xian": 30,
                }
            },
        }
    }
    return render(request, "cojHtml/learningData.html", context=context)


# return data from mysql about learningData
def get_learning_data(request):
    # 获取分页参数
    page = int(request.GET.get("page", 1))
    limit = int(request.GET.get("limit", 10))

    # 从数据库查询数据
    all_users = User.objects.all().order_by("id")
    paginator = Paginator(all_users, limit)
    users = paginator.get_page(page)

    # 构建数据列表
    data = []
    for user in users:
        data.append(
            {
                "id": str(user.id),
                "username": user.username,
                "email": user.email,
                "sex": user.sex,
                "city": user.city,
                "sign": user.sign,
                "experience": str(user.experience),
                "ip": user.ip,
                "checkin": str(user.checkin),
                "joinTime": user.joinTime.strftime("%Y-%m-%d"),
            }
        )

    # 计算各时代人物数量（根据用户名判断，实际业务中应该有更好的分类方式）
    tang_users = ["李白", "杜甫"]
    song_users = ["苏轼", "李清照"]
    modern_users = ["冰心", "张三"]

    tang_count = User.objects.filter(username__in=tang_users).count()
    song_count = User.objects.filter(username__in=song_users).count()
    modern_count = User.objects.filter(username__in=modern_users).count()

    # 构建响应数据
    response_data = {
        "code": 0,
        "msg": "",
        "count": all_users.count(),
        "totalRow": {
            "era": {
                "tang": str(tang_count),
                "song": str(song_count),
                "xian": str(modern_count),
            }
        },
        "data": data,
    }

    return JsonResponse(response_data, json_dumps_params={"ensure_ascii": False})
