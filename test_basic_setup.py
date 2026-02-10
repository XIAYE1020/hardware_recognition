#!/usr/bin/env python3
"""
基础设置测试脚本
测试项目基础功能是否正常工作
"""

import sys
import os
from pathlib import Path

# 添加src目录到Python路径
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_config_loader():
    """测试配置加载器"""
    print("测试配置加载器...")
    try:
        from src.utils.config_loader import config
        
        # 加载配置
        config_data = config.load_config()
        print(f"✅ 配置加载成功，包含 {len(config_data)} 个主要配置项")
        
        # 测试获取特定配置
        model_config = config.model_config
        print(f"✅ 模型配置: {model_config['model_name']}")
        
        class_names = config.class_names
        print(f"✅ 类别数量: {len(class_names)}")
        
        return True
    except Exception as e:
        print(f"❌ 配置加载器测试失败: {e}")
        return False


def test_logger():
    """测试日志记录器"""
    print("\n测试日志记录器...")
    try:
        from src.utils.logger import logger
        
        # 测试各种日志级别
        logger.info("这是一条测试信息")
        logger.warning("这是一条测试警告")
        logger.debug("这是一条测试调试信息")
        
        print("✅ 日志记录器工作正常")
        return True
    except Exception as e:
        print(f"❌ 日志记录器测试失败: {e}")
        return False


def test_path_manager():
    """测试路径管理器"""
    print("\n测试路径管理器...")
    try:
        from src.utils.path_manager import path_manager
        
        # 测试路径获取
        config_file = path_manager.get_config_file()
        parts_file = path_manager.get_parts_info_file()
        
        print(f"✅ 配置文件路径: {config_file}")
        print(f"✅ 配件信息文件路径: {parts_file}")
        
        # 验证文件是否存在
        if config_file.exists():
            print("✅ 配置文件存在")
        else:
            print("❌ 配置文件不存在")
            
        if parts_file.exists():
            print("✅ 配件信息文件存在")
        else:
            print("❌ 配件信息文件不存在")
        
        return True
    except Exception as e:
        print(f"❌ 路径管理器测试失败: {e}")
        return False


def test_core_imports():
    """测试核心库导入"""
    print("\n测试核心库导入...")
    try:
        import cv2
        import numpy as np
        import torch
        from ultralytics import YOLO
        import pandas as pd
        import matplotlib.pyplot as plt
        
        print("✅ OpenCV版本:", cv2.__version__)
        print("✅ NumPy版本:", np.__version__)
        print("✅ PyTorch版本:", torch.__version__)
        print("✅ Pandas版本:", pd.__version__)
        print("✅ Matplotlib版本:", plt.matplotlib.__version__)
        
        return True
    except Exception as e:
        print(f"❌ 核心库导入失败: {e}")
        return False


def test_data_files():
    """测试数据文件"""
    print("\n测试数据文件...")
    try:
        import json
        import pandas as pd
        
        # 测试配置文件
        config_path = Path("data/config/config.json")
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        print(f"✅ 配置文件包含 {len(config_data)} 个配置项")
        
        # 测试配件信息文件
        parts_path = Path("data/parts_info/hardware_parts.json")
        with open(parts_path, 'r', encoding='utf-8') as f:
            parts_data = json.load(f)
        print(f"✅ 配件信息文件包含 {len(parts_data['parts'])} 个配件")
        
        # 测试CSV文件
        csv_path = Path("data/results/detection_results.csv")
        df = pd.read_csv(csv_path)
        print(f"✅ 检测结果CSV文件包含 {len(df.columns)} 列")
        
        return True
    except Exception as e:
        print(f"❌ 数据文件测试失败: {e}")
        return False


def main():
    """主函数"""
    print("=" * 50)
    print("五金配件识别系统 - 基础设置测试")
    print("=" * 50)
    
    tests = [
        ("配置加载器", test_config_loader),
        ("日志记录器", test_logger),
        ("路径管理器", test_path_manager),
        ("核心库导入", test_core_imports),
        ("数据文件", test_data_files),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name}测试异常: {e}")
            results.append((name, False))
    
    print("\n" + "=" * 50)
    print("测试结果汇总:")
    print("=" * 50)
    
    all_passed = True
    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"{name}: {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有基础功能测试通过！项目环境搭建成功。")
    else:
        print("⚠️ 部分测试失败，请检查相关配置。")
    print("=" * 50)
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)