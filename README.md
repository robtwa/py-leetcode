"""
# My Python Project

## Setup

创建虚拟环境

```bash
python -m venv venv
```

**激活 venv**

CMD：

```bash
.venv\Scripts\activate
```


Mac / Linux

```bash
source .venv/bin/activate
```


**安装依赖**



```bash
pip install -r requirements.txt
```

## 创建一个“软链接”（editable install）

installs the project in editable mode by creating a link in site-packages instead of copying files, so changes to the source code take effect immediately without reinstalling.

它不是“安装代码”，而是“把你的项目路径加入 Python 环境”

```bash
pip install -e .
```

## Run Tests

```bash
pytest
```

## Features
- Basic calculator functions
- Unit tests using pytest
"""
