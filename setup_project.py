#!/usr/bin/env python3
"""
项目初始化脚本
一键设置整个项目环境
"""

import sys
import subprocess
import os
from pathlib import Path


def run_command(command, description):
    """
    运行命令并显示结果
    
    Args:
        command: 要运行的命令
        description: 命令描述
    """
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description}成功")
            if result.stdout.strip():
                print(f"   输出: {result.stdout.strip()}")
        else:
            print(f"❌ {description}失败")
            if result.stderr.strip():
                print(f"   错误: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description}异常: {e}")
        return False
    return True


def create_directories():
    """创建必需的目录结构"""
    print("\n📁 创建项目目录结构...")
    
    project_root = Path(__file__).parent
    directories = [
        "data/config",
        "data/models",
        "data/datasets/train",
        "data/datasets/val", 
        "data/datasets/test",
        "data/parts_info",
        "data/results",
        "data/reference_images",
        "src/models",
        "src/data",
        "src/ui",
        "src/utils",
        "tests",
        "docs",
        "logs"
    ]
    
    for directory in directories:
        dir_path = project_root / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 创建目录: {directory}")
    
    return True


def install_dependencies():
    """安装Python依赖包"""
    print("\n📦 安装Python依赖包...")
    
    # 检查requirements.txt是否存在
    requirements_file = Path(__file__).parent / "requirements.txt"
    if not requirements_file.exists():
        print("❌ requirements.txt文件不存在")
        return False
    
    # 安装依赖包
    return run_command(
        f"pip install -r {requirements_file}",
        "安装依赖包"
    )


def run_environment_check():
    """运行环境检查"""
    print("\n🔍 运行环境检查...")
    
    check_script = Path(__file__).parent / "check_environment.py"
    if not check_script.exists():
        print("❌ 环境检查脚本不存在")
        return False
    
    return run_command(
        f"python {check_script}",
        "环境检查"
    )


def run_basic_tests():
    """运行基础功能测试"""
    print("\n🧪 运行基础功能测试...")
    
    test_script = Path(__file__).parent / "test_basic_setup.py"
    if not test_script.exists():
        print("❌ 基础测试脚本不存在")
        return False
    
    return run_command(
        f"python {test_script}",
        "基础功能测试"
    )


def initialize_git():
    """初始化Git仓库（可选）"""
    print("\n📝 初始化Git仓库...")
    
    # 检查是否已经是Git仓库
    if (Path(__file__).parent / ".git").exists():
        print("✅ Git仓库已存在")
        return True
    
    # 初始化Git仓库
    commands = [
        "git init",
        "git add .",
        "git commit -m 'Initial commit: 项目环境搭建完成'"
    ]
    
    for command in commands:
        if not run_command(command, f"执行: {command}"):
            print("⚠️ Git初始化失败，但不影响项目使用")
            return False
    
    return True


def main():
    """主函数"""
    print("=" * 60)
    print("🚀 五金配件识别系统 - 项目初始化")
    print("=" * 60)
    
    steps = [
        ("创建目录结构", create_directories),
        ("安装依赖包", install_dependencies),
        ("环境检查", run_environment_check),
        ("基础功能测试", run_basic_tests),
        ("Git初始化", initialize_git),
    ]
    
    results = []
    for step_name, step_func in steps:
        try:
            result = step_func()
            results.append((step_name, result))
        except Exception as e:
            print(f"❌ {step_name}异常: {e}")
            results.append((step_name, False))
    
    print("\n" + "=" * 60)
    print("📊 初始化结果汇总:")
    print("=" * 60)
    
    all_success = True
    for step_name, result in results:
        status = "✅ 成功" if result else "❌ 失败"
        print(f"{step_name}: {status}")
        if not result:
            all_success = False
    
    print("\n" + "=" * 60)
    if all_success:
        print("🎉 项目初始化完成！")
        print("\n📋 下一步操作:")
        print("   1. 运行 'python main.py' 启动系统")
        print("   2. 查看 README.md 了解详细使用说明")
        print("   3. 开始实现具体功能模块")
    else:
        print("⚠️ 部分步骤失败，请检查错误信息并手动修复")
        print("\n🔧 常见问题解决:")
        print("   1. 网络问题导致包安装失败 - 尝试使用国内镜像源")
        print("   2. 权限问题 - 确保有足够的文件系统权限")
        print("   3. Python版本问题 - 确保使用Python 3.8+")
    
    print("=" * 60)
    return 0 if all_success else 1


if __name__ == "__main__":
    sys.exit(main())