"""环境自检脚本：确认 Python 版本与关键依赖可用。"""

import platform
import sys


def main() -> None:
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"解释器路径: {sys.executable}")
    print(f"操作系统: {platform.system()} {platform.release()}")

    checks = {
        "pymysql": "PyMySQL",
        "cryptography": "cryptography",
        "requests": "requests",
        "sqlalchemy": "SQLAlchemy",
        "dotenv": "python-dotenv",
    }
    print("\n依赖检查:")
    for module, name in checks.items():
        try:
            __import__(module)
            print(f"  [OK] {name}")
        except ImportError:
            print(f"  [缺失] {name}")


if __name__ == "__main__":
    main()
