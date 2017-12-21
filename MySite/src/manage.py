#!/usr/bin/env python
import os
import sys
#定制项目的模板，创建一个templates目录，打开配置文件，在TEMPLATES设置中添加一个DIRS选项
#属于特定应用程序的模板应该放在该应用程序的模板目录中，eg：polls/templates
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MySite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
