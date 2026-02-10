# 基于YOLOv8的五金配件识别系统

基于深度学习的五金配件识别和分类系统，使用YOLOv8算法实现。这是一个毕业设计项目，旨在通过深度学习技术解决家具配件识别问题。

## 🚀 快速开始

### 环境检查
运行环境检查脚本，确保所有依赖都正确安装：
```bash
python check_environment.py
```

### 基础功能测试
运行基础设置测试，验证项目配置：
```bash
python test_basic_setup.py
```

### 启动系统
运行主程序：
```bash
python main.py
```

## 📁 项目结构

```
hardware_recognition/
├── data/                           # 数据目录
│   ├── config/                    # 配置文件
│   │   └── config.json           # 主配置文件
│   ├── parts_info/                # 五金配件信息
│   │   └── hardware_parts.json   # 配件数据库
│   ├── models/                    # 模型文件
│   ├── datasets/                  # 训练数据集
│   │   ├── train/                # 训练数据
│   │   ├── val/                  # 验证数据
│   │   └── test/                 # 测试数据
│   ├── results/                   # 结果和日志
│   │   ├── detection_results.csv # 检测结果记录
│   │   └── training_history.json # 训练历史
│   └── reference_images/          # 参考图片
├── src/                           # 源代码
│   ├── models/                    # 模型实现
│   ├── data/                      # 数据管理
│   ├── ui/                        # 用户界面
│   └── utils/                     # 工具函数
│       ├── config_loader.py      # 配置管理
│       ├── logger.py              # 日志记录
│       └── path_manager.py       # 路径管理
├── tests/                         # 单元测试
├── docs/                          # 文档
├── logs/                          # 系统日志
├── main.py                        # 主程序入口
├── check_environment.py           # 环境检查脚本
├── test_basic_setup.py           # 基础功能测试
└── requirements.txt               # Python依赖包
```

## 🔧 安装说明

### 1. 环境要求
- Python 3.8+
- PyTorch 2.0+
- OpenCV 4.8+
- Ultralytics YOLOv8

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Windows系统: venv\Scripts\activate
```

### 3. 安装依赖包
```bash
pip install -r requirements.txt
```

### 4. 验证安装
```bash
python check_environment.py
```

## 🎯 支持的五金配件类型

| 配件类型 | 英文标识 | 描述 |
|---------|---------|------|
| 六角螺母 | hex_nut | 标准六角螺母，用于螺栓连接 |
| 十字槽螺丝 | cross_screw | 十字槽圆头螺丝，常用于家具组装 |
| 平垫片 | flat_washer | 平垫片，用于分散螺栓压力 |
| L型角码 | l_bracket | L型角码，用于直角连接 |
| 偏心轮 | eccentric_wheel | 偏心轮，用于家具连接件 |

## ⚡ 主要功能

- ✅ **实时检测**: 基于YOLOv8的实时五金配件检测和分类
- ✅ **批量处理**: 支持批量图片处理功能
- ✅ **性能评估**: 提供准确率、召回率、F1分数等性能指标
- ✅ **模型训练**: 支持自定义数据集的模型训练和微调
- ✅ **图形界面**: 基于Tkinter的用户友好界面
- ✅ **结果导出**: 支持CSV和JSON格式的结果导出
- ✅ **日志记录**: 完整的系统运行日志记录
- ✅ **配置管理**: 灵活的配置文件管理系统

## 🛠️ 核心模块

### 配置管理 (ConfigLoader)
- 统一的配置文件管理
- 支持嵌套配置访问
- 动态配置更新

### 日志系统 (Logger)
- 多级别日志记录
- 文件和控制台双输出
- 自动日志文件管理

### 路径管理 (PathManager)
- 统一的项目路径管理
- 自动目录创建
- 跨平台路径处理

## 📊 数据格式

### 配件信息格式 (hardware_parts.json)
```json
{
  "parts": [
    {
      "id": 0,
      "name": "M6六角螺母",
      "category": "hex_nut",
      "specification": "M6螺纹，对边距离10mm",
      "description": "标准六角螺母，用于螺栓连接",
      "image_path": "data/reference_images/hex_nut.jpg"
    }
  ]
}
```

### 检测结果格式 (detection_results.csv)
```csv
timestamp,image_path,part_category,confidence,bbox_x,bbox_y,bbox_width,bbox_height,detection_time_ms,model_version
```

## 🧪 测试

### 运行环境检查
```bash
python check_environment.py
```

### 运行基础功能测试
```bash
python test_basic_setup.py
```

### 运行单元测试
```bash
pytest tests/
```

## 📝 开发说明

本项目采用模块化设计，遵循以下开发原则：

1. **配置驱动**: 所有配置通过JSON文件管理
2. **日志记录**: 完整的操作日志记录
3. **错误处理**: 完善的异常处理机制
4. **代码规范**: 遵循PEP8代码规范
5. **文档完整**: 详细的代码注释和文档

## 🎓 毕业设计说明

这是一个完整的毕业设计项目，包含：

- ✅ 完整的项目架构设计
- ✅ 深度学习模型集成
- ✅ 数据管理和处理
- ✅ 用户界面设计
- ✅ 性能评估和优化
- ✅ 完整的测试体系
- ✅ 详细的文档说明

## 📄 许可证

本项目作为毕业设计项目开发，仅供学习和研究使用。