#!/usr/bin/env python3
"""
hello.py - 最小示例：向指定名字打招呼

演示一个带类型注解和文档字符串的小函数，
并通过 ``if __name__ == "__main__":`` 守卫运行入口。

Usage:
    python s05_todo_write/hello.py
"""


def greet(name: str) -> None:
    """向 ``name`` 打招呼并打印到标准输出。

    Args:
        name: 被问候者的名字。

    Returns:
        None。结果直接打印到标准输出。

    Examples:
        >>> greet("World")
        Hello, World
    """
    message: str = f"Hello, {name}"
    print(message)


def main() -> None:
    """程序入口：使用默认名字调用 :func:`greet`。"""
    greet("World")


if __name__ == "__main__":
    main()
