# my-first-project

大语言模型部署及应用实训 —— 第一周环境验证仓库。

## 环境要求

| 组件 | 版本 |
|---|---|
| 操作系统 | Windows 10 1909（Build 18363） |
| Docker Desktop | 4.20.1（Hyper-V 后端，Client/Server 24.0.2） |
| Miniconda | 26.9.4，安装于 `D:\software\miniconda3` |
| Conda 环境 | `credit-assistant`（Python 3.10.22） |

## 启动方式

```bash
# 1. 启动 Docker Desktop，等待引擎就绪
docker --version
docker compose version

# 2. 激活 Conda 环境
conda activate credit-assistant
python --version

# 3. 环境自检
python check_env.py
```

数据库示例容器：

```bash
docker run -d --name mysql-db -p 9999:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:8.0.45
docker ps
```

## 数据安全约束

- 不在仓库中提交任何 API Key、口令、令牌或连接串明文。
- 示例密码（如 `123456`）仅用于隔离的实训环境，真实项目不得使用弱口令。
- 不提交真实征信数据、个人隐私数据。
- 不提交大体积模型文件（`*.safetensors`、`*.gguf`）与数据库数据目录。
- 删除容器、镜像或数据卷前必须确认目标，数据卷删除不可恢复。

## 目录说明

| 文件 | 说明 |
|---|---|
| `environment.yml` | Conda 环境描述，可用于复现 |
| `check_env.py` | 环境自检脚本 |
| `.gitignore` | 排除缓存、密钥、数据与大文件 |
