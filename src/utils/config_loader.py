"""
配置文件加载器
用于加载和管理系统配置
"""

import json
import os
from typing import Dict, Any, Optional
from pathlib import Path


class ConfigLoader:
    """配置文件加载器类"""
    
    def __init__(self, config_path: Optional[str] = None):
        """
        初始化配置加载器
        
        Args:
            config_path: 配置文件路径，默认为 data/config/config.json
        """
        if config_path is None:
            # 获取项目根目录
            project_root = Path(__file__).parent.parent.parent
            config_path = project_root / "data" / "config" / "config.json"
        
        self.config_path = Path(config_path)
        self._config = None
    
    def load_config(self) -> Dict[str, Any]:
        """
        加载配置文件
        
        Returns:
            配置字典
            
        Raises:
            FileNotFoundError: 配置文件不存在
            json.JSONDecodeError: 配置文件格式错误
        """
        if not self.config_path.exists():
            raise FileNotFoundError(f"配置文件不存在: {self.config_path}")
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._config = json.load(f)
            return self._config
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"配置文件格式错误: {e}")
    
    def get_config(self, key: Optional[str] = None) -> Any:
        """
        获取配置项
        
        Args:
            key: 配置键，支持点分隔的嵌套键，如 'model_config.model_name'
                如果为None，返回整个配置
        
        Returns:
            配置值
        """
        if self._config is None:
            self.load_config()
        
        if key is None:
            return self._config
        
        # 支持嵌套键访问
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                raise KeyError(f"配置键不存在: {key}")
        
        return value
    
    def update_config(self, key: str, value: Any) -> None:
        """
        更新配置项
        
        Args:
            key: 配置键，支持点分隔的嵌套键
            value: 新的配置值
        """
        if self._config is None:
            self.load_config()
        
        keys = key.split('.')
        config = self._config
        
        # 导航到目标位置
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        # 设置值
        config[keys[-1]] = value
    
    def save_config(self) -> None:
        """保存配置到文件"""
        if self._config is None:
            return
        
        # 确保目录存在
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self._config, f, ensure_ascii=False, indent=2)
    
    @property
    def model_config(self) -> Dict[str, Any]:
        """获取模型配置"""
        return self.get_config('model_config')
    
    @property
    def class_names(self) -> list:
        """获取类别名称列表"""
        return self.get_config('class_names')
    
    @property
    def training_config(self) -> Dict[str, Any]:
        """获取训练配置"""
        return self.get_config('training_config')
    
    @property
    def data_augmentation_config(self) -> Dict[str, Any]:
        """获取数据增强配置"""
        return self.get_config('data_augmentation')


# 全局配置实例
config = ConfigLoader()