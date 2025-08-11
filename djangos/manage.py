import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangos.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError('无法引用 Django，请检查是否安装或是否开启虚拟环境') from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__': main()
