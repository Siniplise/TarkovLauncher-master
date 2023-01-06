import subprocess

import ClientLoggingHandler

ClientLoggingHandler.Log_LauncherCore.info("初始化启动核心")

ClientLoggingHandler.Log_LauncherCore.info("获取塔科夫启动参数")


def Command(maindir, token, url, version):
    ClientLoggingHandler.Log_LauncherCore.info("拼接塔科夫启动命令")

    Dir = maindir + "\\EscapeFromTarkov.exe"

    MainCommand = "\"%s\" -force-gfx-jobs native -token=%s -config={\"BackendUrl\":\"%s\",\"Version\":\"%s\"}" % (
    Dir, token, url, version)

    ClientLoggingHandler.Log_LauncherCore.info(f"塔科夫启动命令拼接完成 : {MainCommand}")

    return MainCommand


ClientLoggingHandler.Log_LauncherCore.info("初始化完成!")

ClientLoggingHandler.Log_LauncherCore.info("构建主启动函数")


def MainLaunch(TarkovLaunchCommand):
    try:
        subprocess.Popen(TarkovLaunchCommand)
        ClientLoggingHandler.Log_LauncherCore.info("已发送启动命令")
        return True
    except Exception:
        ClientLoggingHandler.Log_LauncherCore.critical(f"启动失败!: {Exception}")
        return False

ClientLoggingHandler.Log_LauncherCore.info("主启动函数构建成功")