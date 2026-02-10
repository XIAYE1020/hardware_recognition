#!/usr/bin/env python3
"""
环境检查脚本
检查项目运行所需的依赖包和环境配置
"""

import sys
import importlib
import subprocess
from pathlib import Path


def check_python_version():
    """检查Python版本"""
    print("检查Python版本...")
    version = sys.version_info
    print(f"当前Python版本: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("[X] Python版本过低，需要Python 3.8或更高版本")
        return False
    else:
        print("[OK] Python版本符合要求")
        return True


def check_package(package_name, import_name=None):
    """
    检查包是否安装
    
    Args:
        package_name: 包名称
        import_name: 导入名称（如果与包名不同）
    """
    if import_name is None:
        import_name = package_name
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"[OK] {package_name}: {version}")
        return True
    except ImportError:
        print(f"[X] {package_name}: 未安装")
        return False


def check_required_packages():
    """检查必需的包"""
    print("\n检查必需的Python包...")
    
    packages = [
        ('ultralytics', 'ultralytics'),
        ('opencv-python', 'cv2'),
        ('numpy', 'numpy'),
        ('Pillow', 'PIL'),
        ('torch', 'torch'),
        ('torchvision', 'torchvision'),
        ('pandas', 'pandas'),
        ('matplotlib', 'matplotlib'),
        ('pytest', 'pytest'),
        ('hypothesis', 'hypothesis'),
        ('pyyaml', 'yaml'),
        ('tqdm', 'tqdm'),
        ('scikit-learn', 'sklearn'),
    ]
    
    all_installed = True
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_installed = False
    
    return all_installed


def check_optional_packages():
    """检查可选的包"""
    print("\n检查可选的Python包...")
    
    optional_packages = [
        ('seaborn', 'seaborn'),
        ('plotly', 'plotly'),
        ('black', 'black'),
        ('flake8', 'flake8'),
    ]
    
    for package_name, import_name in optional_packages:
        check_package(package_name, import_name)


def check_tkinter():
    """检查tkinter是否可用"""
    print("\n检查GUI框架...")
    try:
        import tkinter as tk
        # 尝试创建一个简单的窗口来测试
        root = tk.Tk()
        root.withdraw()  # 隐藏窗口
        root.destroy()
        print("[OK] tkinter: 可用")
        return True
    except ImportError:
        print("[X] tkinter: 不可用")
        return False
    except Exception as e:
        print(f"[!] tkinter: 可能存在问题 - {e}")
        return False


def check_cuda():
    """检查CUDA是否可用"""
    print("\n检查CUDA支持...")
    try:
        import torch
        if torch.cuda.is_available():
            device_count = torch.cuda.device_count()
            device_name = torch.cuda.get_device_name(0) if device_count > 0 else "Unknown"
            print(f"[OK] CUDA: 可用 ({device_count} 个设备)")
            print(f"   主设备: {device_name}")
            return True
        else:
            print("[!] CUDA: 不可用，将使用CPU模式")
            return False
    except Exception as e:
        print(f"[X] CUDA检查失败: {e}")
        return False


def check_project_structure():
    """检查项目目录结构"""
    print("\n检查项目目录结构...")
    
    project_root = Path(__file__).parent
    required_dirs = [
        "data",
        "data/config",
        "data/models", 
        "data/datasets",
        "data/parts_info",
        "data/results",
        "src",
        "src/models",
        "src/data",
        "src/ui",
        "src/utils",
        "tests",
        "logs"
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"[OK] {dir_path}/")
        else:
            print(f"[X] {dir_path}/ (缺失)")
            all_exist = False
    
    return all_exist


def check_config_files():
    """检查配置文件"""
    print("\n检查配置文件...")
    
    project_root = Path(__file__).parent
    config_files = [
        "data/config/config.json",
        "data/parts_info/hardware_parts.json",
        "data/results/detection_results.csv",
        "data/results/training_history.json"
    ]
    
    all_exist = True
    for file_path in config_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"[OK] {file_path}")
        else:
            print(f"[X] {file_path} (缺失)")
            all_exist = False
    
    return all_exist


def main():
    """主函数"""
    print("=" * 50)
    print("五金配件识别系统 - 环境检查")
    print("=" * 50)
    
    checks = [
        ("Python版本", check_python_version),
        ("必需包", check_required_packages),
        ("可选包", check_optional_packages),
        ("GUI框架", check_tkinter),
        ("CUDA支持", check_cuda),
        ("项目结构", check_project_structure),
        ("配置文件", check_config_files),
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"[X] {name}检查失败: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("检查结果汇总:")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "[OK] 通过" if result else "[X] 失败"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("所有检查都通过了！环境配置正确。")
    else:
        print("部分检查失败，请根据上述信息修复问题。")
        print("\n安装缺失包的命令:")
        print("pip install -r requirements.txt")
    print("=" * 50)


if __name__ == "__main__":
    main()