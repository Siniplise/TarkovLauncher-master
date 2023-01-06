import logging

import colorlog

# COLOR CONFIG
Color_MainConfig = {
    'DEBUG': 'white',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}
# GET LOGGER

Log_ClientLoggingHandler = logging.getLogger("CLIENT_LOGGING_HANDLER")
Log_ClientLoggingHandler.setLevel(logging.DEBUG)

Log_ClientConfig = logging.getLogger("CLIENT_CONFIG")
Log_ClientConfig.setLevel(logging.DEBUG)

Log_LauncherCore = logging.getLogger("LAUNCHER_CORE")
Log_LauncherCore.setLevel(logging.DEBUG)

Log_Client = logging.getLogger("CLIENT")
Log_Client.setLevel(logging.DEBUG)

# SET HANDLER

Log_ClientLoggingHandler_Handler = logging.StreamHandler()
Log_ClientLoggingHandler_Handler.setLevel(logging.DEBUG)

Log_ClientConfig_Handler = logging.StreamHandler()
Log_ClientConfig_Handler.setLevel(logging.DEBUG)

Log_LauncherCore_Handler = logging.StreamHandler()
Log_LauncherCore_Handler.setLevel(logging.DEBUG)

Log_Client_Handler = logging.StreamHandler()
Log_Client_Handler.setLevel(logging.DEBUG)

# CREATE FORMATTER

Log_Formatter = logging.Formatter(
    fmt='[%(asctime)s][%(filename)s][%(name)s][%(levelname)s] : %(message)s'
)

# GET COLOR

Log_Formatter_Color = colorlog.ColoredFormatter(
    fmt='%(log_color)s[%(asctime)s][%(filename)s][%(name)s][%(levelname)s] : %(message)s',
    log_colors=Color_MainConfig
)

# SET FORMATTER

Log_ClientLoggingHandler_Handler.setFormatter(Log_Formatter_Color)
Log_ClientConfig_Handler.setFormatter(Log_Formatter_Color)
Log_LauncherCore_Handler.setFormatter(Log_Formatter_Color)
Log_Client_Handler.setFormatter(Log_Formatter_Color)

# PATCHES HANDLER

Log_ClientLoggingHandler.addHandler(Log_ClientLoggingHandler_Handler)
Log_ClientConfig.addHandler(Log_ClientConfig_Handler)
Log_LauncherCore.addHandler(Log_LauncherCore_Handler)
Log_Client.addHandler(Log_Client_Handler)

Log_ClientLoggingHandler.info(msg="日志处理器构建完成")
