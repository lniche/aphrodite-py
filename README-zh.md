# Aphrodite FsatAPI Scaffold

[English](README.md) | [简体中文](README-zh.md)

Aphrodite 是一个基于 [Fastapi-skeleton](https://github.com/kaxiluo/fastapi-skeleton) 开发的模板项目，旨在帮助开发者快速上手，深入理解框架的使用流程。该项目提供了全面的示例代码和配置，涵盖了常见的开发场景，以便于学习和实践。此外，Aphrodite 还包含容器部署模板，使得项目在现代云环境中能够轻松部署与管理，助力开发者高效构建和发布应用。

## 技术栈

| 技术                                                   | 说明                                                      |
| ------------------------------------------------------ | --------------------------------------------------------- |
| [APScheduler](https://github.com/agronholm/APScheduer) | Python 中的定时任务调度框架，支持后台作业调度             |
| [FastAPI](https://fastapi.tiangolo.com/)               | 高性能的 Web 框架，支持异步操作，快速构建 API             |
| [JOSE](https://github.com/python-jose/jose)            | 用于处理 JSON Web Tokens (JWT) 的 Python 库               |
| [Loguru](https://github.com/Delgan/loguru)             | 简化的 Python 日志库，提供易用的日志记录和格式化支持      |
| [Peewee](http://docs.peewee-orm.com/en/latest/)        | 简洁的 Python ORM 框架，支持多种数据库操作                |
| [Starlette](https://www.starlette.io/)                 | 用于构建 Web 应用程序的高性能框架，FastAPI 的核心部分     |
| [Uvicorn](https://www.uvicorn.org/)                    | 高性能的 ASGI 服务器，支持异步 Python 应用的运行          |
| [psycopg2](https://github.com/psycopg/psycopg2)        | PostgreSQL 数据库适配器，支持 Python 与 PostgreSQL 的连接 |
| [Passlib](https://passlib.readthedocs.io/en/stable/)   | 密码加密库，支持多种哈希算法及加密方式                    |
| [Pydantic](https://pydantic-docs.helpmanual.io/)       | 数据验证和解析库，基于 Python 类型注解进行验证和解析      |
| [Python-JOSE](https://github.com/mpdavis/python-jose)  | 用于生成和解析 JSON Web Tokens (JWT) 的库，支持加密       |
| [Redis-py](https://github.com/andymccurdy/redis-py)    | Python 客户端库，用于连接和操作 Redis 数据库              |

## 特性

- **用户认证与授权**：提供基础的用户登录和权限授权功能。
- **分布式锁**：基于 Redis 实现的分布式锁，保证分布式环境下的资源安全。
- **中间件支持**：内置常用的中间件，包括认证、请求日志、跨域处理等。
- **统一输出格式**：提供简单易用的 API Result 统一输出方式，标准化 API 响应格式，提升接口一致性。
- **API 模块化设计**：支持模块化的 API 设计，易于扩展和维护。
- **Swagger 文档集成**：自动生成 API 文档，便于前端开发和测试。

## 目录结构

```
.
├── app/                  # 应用核心代码
├── bin/                  # 可执行脚本
├── bootsrap/             # 引导文件
├── database/             # 数据库相关
├── deploy/               # 部署相关文件
├── docs/                 # 项目文档
├── routes/               # 路由文件
├── storage/              # 文件存储
├── tests/                # 测试文件
└── README.md             # 项目说明
```

## 本地运行

```bash
# 1. 克隆项目代码库
git clone https://github.com/lniche/aphrodite-py.git
cd aphrodite-py

# 2. 配置文件
cd config
mv .env.example .env

# 3. 添加依赖
# 确保你已经安装了 python 环境，推荐使用conda
pip install -r requirements.txt

# 4. 初始化数据库
database/init.sql

# 5. 启动服务
uvicorn main:app
```

## Repo Activity

![Alt](https://repobeats.axiom.co/api/embed/57c3b523ffb088038484a6b3883890a2615b3fa5.svg "Repobeats analytics image")

## 贡献

如果你有任何建议或想法，欢迎创建 Issue 或直接提交 Pull Request。

1. Fork 这个仓库。
2. 创建一个新的分支：git checkout -b feature/your-feature
3. 提交你的更改：git commit -m 'Add new feature'
4. 推送到你的分支：git push origin feature/your-feature
5. 提交 Pull Request。

## 许可证

该项目遵循 MIT 许可证。

## 鸣谢

特别感谢所有贡献者和支持者，您的帮助对我们至关重要！
