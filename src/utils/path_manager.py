"""
路径管理工具
提供项目中各种路径的统一管理
"""

from pathlib import Path
from typing import Union


class PathManager:
    """路径管理器类"""
    
    def __init__(self):
        """初始化路径管理器"""
        # 获取项目根目录
        self.project_root = Path(__file__).parent.parent.parent
        
        # 定义各种路径
        self.data_dir = self.project_root / "data"
        self.src_dir = self.project_root / "src"
        self.tests_dir = self.project_root / "tests"
        self.docs_dir = self.project_root / "docs"
        self.logs_dir = self.project_root / "logs"
        
        # 数据子目录
        self.config_dir = self.data_dir / "config"
        self.models_dir = self.data_dir / "models"
        self.datasets_dir = self.data_dir / "datasets"
        self.parts_info_dir = self.data_dir / "parts_info"
        self.results_dir = self.data_dir / "results"
        self.reference_images_dir = self.data_dir / "reference_images"
        
        # 数据集子目录
        self.train_dir = self.datasets_dir / "train"
        self.val_dir = self.datasets_dir / "val"
        self.test_dir = self.datasets_dir / "test"
        
        # 源码子目录
        self.models_src_dir = self.src_dir / "models"
        self.data_src_dir = self.src_dir / "data"
        self.ui_src_dir = self.src_dir / "ui"
        self.utils_src_dir = self.src_dir / "utils"
    
    def ensure_dir_exists(self, path: Union[str, Path]) -> Path:
        """
        确保目录存在，如果不存在则创建
        
        Args:
            path: 目录路径
            
        Returns:
            Path对象
        """
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        return path
    
    def get_config_file(self) -> Path:
        """获取配置文件路径"""
        return self.config_dir / "config.json"
    
    def get_parts_info_file(self) -> Path:
        """获取配件信息文件路径"""
        return self.parts_info_dir / "hardware_parts.json"
    
    def get_detection_results_file(self) -> Path:
        """获取检测结果文件路径"""
        return self.results_dir / "detection_results.csv"
    
    def get_training_history_file(self) -> Path:
        """获取训练历史文件路径"""
        return self.results_dir / "training_history.json"
    
    def get_model_file(self, model_name: str) -> Path:
        """
        获取模型文件路径
        
        Args:
            model_name: 模型文件名
            
        Returns:
            模型文件路径
        """
        return self.models_dir / model_name
    
    def get_log_file(self, log_name: str) -> Path:
        """
        获取日志文件路径
        
        Args:
            log_name: 日志文件名
            
        Returns:
            日志文件路径
        """
        return self.logs_dir / log_name
    
    def create_all_dirs(self):
        """创建所有必需的目录"""
        dirs_to_create = [
            self.data_dir,
            self.config_dir,
            self.models_dir,
            self.datasets_dir,
            self.parts_info_dir,
            self.results_dir,
            self.reference_images_dir,
            self.train_dir,
            self.val_dir,
            self.test_dir,
            self.logs_dir,
            self.docs_dir
        ]
        
        for dir_path in dirs_to_create:
            self.ensure_dir_exists(dir_path)


# 全局路径管理实例
path_manager = PathManager()