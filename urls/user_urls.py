from django.urls import path
from views.userViews import (
    index, register, userList, login, logout_view, 
    addUser, editUser, deleteUser, viewUser, toggleUserStatus, get_users_json
)

app_name = 'user'

urlpatterns = [
    path("", index, name="home"),  # 首页
    path("index/", index, name="index"),
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout_view, name="logout"),
    
    # 用户管理相关URL
    path("userList/", userList, name="userList"),
    path("addUser/", addUser, name="addUser"),
    path("editUser/<int:user_id>/", editUser, name="editUser"),
    path("deleteUser/<int:user_id>/", deleteUser, name="deleteUser"),
    path("viewUser/<int:user_id>/", viewUser, name="viewUser"),
    path("toggleUserStatus/<int:user_id>/", toggleUserStatus, name="toggleUserStatus"),
    path("api/users/", get_users_json, name="get_users_json"),
]