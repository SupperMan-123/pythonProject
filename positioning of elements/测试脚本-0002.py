from pywinauto.application import Application

# app = Application(backend="uia").start("WinSCP.exe")

app = Application(backend="uia").start(r"C:\Program Files (x86)\WinSCP\WinSCP.exe")

# 通过窗口标题去 选择窗口 --打开应用
dlg = app["WinSCP"]

# 打印窗口上的控件
# dlg.print_control_identifiers()
# 关闭窗口
# dlg.close()

# # 选择菜单栏--方式 1
# menu = dlg["菜单"]
menu = dlg["TThemePageControl"]
# print(menu.print_control_identifiers())

# 选择菜单项目:通过 child_window方法 指定 菜单栏里的 会话 项
file = menu.child_window(title="新建会话")
# print(menu.print_control_identifiers())


# 选择控件中的子控件--方式 2
# file = menu.child_window(title="会话(S)", control_type="MenuItem")
# file.print_control_identifiers()
# -------------------- 菜单控件相关操作--------------------
# 获取菜单的所有子菜单项目
# print(menu.items())
# 选择子菜单项--通过下标选择----item_by_index()
# m = menu.item_by_index(4)
# print(m)
# 选择子菜单--通过路径选择---item_by_path("")
# m = menu.item_by_path("会话(S)")
# print(m)
# 点击菜单项
file.click_input()
# menu.item_by_path("会话(S)->新建会话(N)...").click.input()

# 等待机制
new_dlg = app["新建会话"]
# 等待窗口处于可见状态
new_dlg.wait(wait_for="ready", timeout=10, retry_interval=1)
# print("等待通过")
