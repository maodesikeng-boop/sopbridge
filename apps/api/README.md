# sopbridge-api

SOPBridge 的后端服务，基于 FastAPI。

## 本地开发

以下命令都在 `apps/api` 目录下运行：

| 命令 | 作用 |
|---|---|
| `uv sync` | 安装依赖（第一次运行，或依赖有变化后） |
| `uv run fastapi dev` | 启动开发服务器，接口文档在 http://127.0.0.1:8000/docs（入口在 `pyproject.toml` 的 `[tool.fastapi]` 中配置） |
| `uv run pytest` | 运行测试 |
| `uv run ruff check` | 代码检查 |
| `uv run ruff format` | 格式化代码 |

## 目录结构

代码按"层"组织：

| 位置 | 放什么 |
|---|---|
| `src/sopbridge_api/main.py` | 创建应用、挂载各个路由，不写具体接口 |
| `src/sopbridge_api/routes/` | 接口定义（`APIRouter`），每个功能一个文件 |
| `src/sopbridge_api/schemas/` | Pydantic 模型：接口的请求和响应结构 |
| `src/sopbridge_api/models/` | SQLAlchemy 模型：数据库表（S0-5 开始使用） |
| `src/sopbridge_api/services/` | 业务逻辑，供 routes 调用（出现业务逻辑时再建） |
| `tests/` | 测试 |

约定：

- 同一个功能在各层用同一个文件名，例如 `routes/sops.py`、`schemas/sops.py`、`models/sops.py`、`services/sops.py`
- routes 只负责接收请求、调用 services、返回 schemas 里的模型，业务逻辑放在 services
- 每个接口的返回值都用 schemas 里的模型声明，保证接口文档和前端生成的类型准确
