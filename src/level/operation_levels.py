operation_levels = {
    # 基础操作
    "读取文件": 3,
    "写入文件": 2,
    "删除文件": 1,
    "创建文件": 2,
    "列出目录内容": 3,
    "修改文件权限": 1,
    "修改文件所有者": 1,
    "修改文件时间戳": 1,
    "打开终端": 2,

    # 压缩与解压
    "压缩文件": 2,
    "解压文件": 2,

    # 程序运行
    "运行程序": 1,

    # 系统信息
    "获取系统信息": 3,
    "监控系统资源": 3,

    # 网络操作
    "检查网络连接": 3,
    "上传文件": 2,
    "下载文件": 2,
    "修改网络配置": 1,

    # 系统管理
    "打开资源管理器": 2,
    "打开任务管理器": 2,
    "打开浏览器": 2,
    "关机": 1,
    "重启系统": 1,
    "定时关机": 0,
    "定时重启": 0,

    # 高危操作
    "删除系统文件": 0,
    "删除根目录": 0,
    "修改分区表": 0,

    # 进程管理
    "列出进程": 3,
    "终止进程": 2,

    # 用户管理
    "创建用户": 1,
    "删除用户": 0,

    # 安全相关
    "检查系统日志": 3,
    "修改防火墙规则": 0,
    "安装pip包": 2,
}