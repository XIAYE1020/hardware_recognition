#!/usr/bin/env python3
"""
Hardware Parts Recognition System
基于YOLOv8的五金配件识别系统

Main entry point for the application.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """主应用程序入口点"""
    print("Hardware Parts Recognition System")
    print("基于YOLOv8的五金配件识别系统")
    print("=" * 50)
    
    try:
        # 导入工具模块
        from src.utils import config, logger, path_manager
        
        # 初始化日志
        logger.info("系统启动中...")
        
        # 确保所有必需目录存在
        path_manager.create_all_dirs()
        logger.info("项目目录结构检查完成")
        
        # 加载配置
        config_data = config.load_config()
        logger.info("配置文件加载成功")
        
        print(f"✅ 模型配置: {config.model_config['model_name']}")
        print(f"✅ 支持的配件类别: {', '.join(config.class_names)}")
        print(f"✅ 置信度阈值: {config.model_config['confidence_threshold']}")
        
        # TODO: 根据命令行参数初始化GUI或CLI界面
        print("\n🎉 系统初始化成功！")
        print("📋 可用功能:")
        print("   - 单张图片检测")
        print("   - 批量图片处理")
        print("   - 模型训练")
        print("   - 性能评估")
        print("   - GUI界面")
        
        logger.info("系统初始化完成，等待用户操作")
        
        return 0
        
    except Exception as e:
        print(f"❌ 系统初始化失败: {e}")
        if 'logger' in locals():
            logger.error(f"系统初始化失败: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())