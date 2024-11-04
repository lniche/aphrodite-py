# Aphrodite Python API 快速开发脚手架

> Aphrodite 是一个基于 [fastapi-skeleton](https://github.com/kaxiluo/fastapi-skeleton) 开发的模板项目，旨在帮助开发者快速上手，深入理解框架的使用流程。该项目提供了全面的示例代码和配置，涵盖了常见的开发场景，以便于学习和实践。此外，Aphrodite 还包含容器部署模板，使得项目在现代云环境中能够轻松部署与管理，助力开发者高效构建和发布应用。

| 技术                                                      | 说明                                           |
| --------------------------------------------------------- | ---------------------------------------------- |
| [tokio](https://github.com/tokio-rs/tokio)                | 异步运行时，支持多种异步功能和全特性           |
| [clap](https://github.com/clap-rs/clap)                   | 命令行参数解析库，支持衍生宏                   |
| [thiserror](https://github.com/dtolnay/thiserror)         | 错误处理库，提供简洁的错误定义                 |
| [anyhow](https://github.com/dtolnay/anyhow)               | 灵活的错误处理库，适用于简化错误传播           |
| [base64](https://crates.io/crates/base64)                 | Base64 编码和解码库                            |
| [time](https://crates.io/crates/time)                     | 时间处理库，支持宏、本地时区、格式化和解析功能 |
| [serde](https://serde.rs/)                                | 数据序列化和反序列化库，支持衍生宏             |
| [serde_json](https://crates.io/crates/serde_json)         | JSON 数据序列化和反序列化库                    |
| [tracing](https://github.com/tokio-rs/tracing)            | 异步应用日志框架                               |
| [tracing-subscriber](https://github.com/tokio-rs/tracing) | 日志订阅者，支持 JSON 格式                     |

| 功能         | 说明                                     |
| ------------ | ---------------------------------------- |
| 登录授权功能 | 提供基础的用户登录和权限授权功能         |
| 分布式锁     | 基于 Redis 实现的分布式锁                |
| 中间件       | 包含认证、请求日志、跨域中间件           |
| 实用封装     | 提供 AES、Hash、时间格式化等常用工具封装 |
| 统一输出方式 | 简单易用的 API Result 统一输出方式       |

## 模块说明

- app => 应用模块
  - api => 应用模块
  - cmd => 应用模块
  - ent => 应用模块
- pkg => 公共模块

## 本地运行

```bash
# 1. 克隆项目代码库
git clone https://github.com/lniche/aphrodite-py.git
cd aphrodite-py

# 2. 配置文件
cd config
mv .env.example .env

# 3. 添加依赖
pip install -r requirements.txt

# 4. 初始化数据库
deploy/db.sql

# 5. 启动服务
uvicorn main:app
```

## 包管理

https://pypi.org
