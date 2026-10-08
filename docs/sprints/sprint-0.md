# Sprint 0：项目骨架与工程基建

| 项目 | 内容 |
|---|---|
| 目标 | 本地一条命令启动所有依赖服务；浏览器里能看到"前端 → 后端 → 数据库"整条链路正常；每个 PR 自动运行 CI；`main` 分支受保护 |
| 开始日期 | 2026-09-29 |
| 负责人 | maodesikeng-boop |

## 完成标准（Definition of Done）

- [ ] `docker compose up -d` 启动 PostgreSQL（含 pgvector）和 Redis
- [ ] 后端 `GET /healthz` 返回服务和数据库状态，并有自动化测试
- [ ] 前端首页展示后端返回的状态
- [ ] 每个 PR 自动运行后端和前端的 lint、测试和构建，全部通过才能合并
- [ ] `main` 分支禁止直接推送和强制推送
- [ ] README 写明如何在一台新电脑上从零启动项目

## 工单

| 编号 | 分支 | 内容 | 验收标准 | 依赖 |
|---|---|---|---|---|
| S0-1 | `chore/repo-conventions` | 仓库规范：`.gitignore`、PR 模板、本计划；设置合并方式和 `main` 分支保护 | 通过第一个 PR 合并进 `main`；之后直接 `git push` 到 `main` 会被拒绝 | — |
| S0-2 | `feat/api-skeleton` | 用 uv 初始化 FastAPI 项目（`apps/api`）；实现 `GET /healthz`；配置 Ruff 和 pytest | `uv run pytest` 通过；`uv run ruff check` 无报错；本地访问 `/healthz` 返回 200 | S0-1 |
| S0-3 | `ci/backend-checks` | GitHub Actions 在每个 PR 上运行后端 lint 和测试；设为合并前必须通过 | PR 页面能看到检查结果；故意让一个测试失败时，PR 无法合并 | S0-2 |
| S0-4 | `feat/local-infra` | Docker Compose 启动 PostgreSQL（pgvector 镜像）和 Redis；后端通过环境变量读取配置并连接数据库 | `/healthz` 能报告数据库是否连通；仓库里只有 `.env.example`，没有真实密钥；CI 用 PostgreSQL 服务容器跑测试 | S0-3 |
| S0-5 | `feat/db-migrations` | 接入 SQLAlchemy 2 和 Alembic；第一个迁移启用 pgvector 扩展 | 在空数据库上 `alembic upgrade head` 成功；可以回滚；CI 中也执行迁移 | S0-4 |
| S0-6 | `feat/web-skeleton` | 用 create-next-app 初始化前端（`apps/web`）；首页调用后端 `/healthz` 并展示结果；CI 增加前端 lint、类型检查和构建 | `pnpm lint` 和 `pnpm build` 通过；页面能显示后端和数据库状态；CI 的前端检查通过 | S0-3 |

建议顺序：S0-1 → S0-2 → S0-3 → S0-4 → S0-5 → S0-6。CI 在 S0-3 就接入，之后每张工单都要保持 CI 通过，并按需扩展 CI。

## 工作约定

- **一张工单对应一个分支、一个 PR。** 分支命名为 `类型/简短描述`，例如 `feat/api-skeleton`
- **提交信息和 PR 标题**遵循 [Conventional Commits](https://www.conventionalcommits.org/zh-hans/v1.0.0/)：`feat:` 新功能、`fix:` 修复、`docs:` 文档、`test:` 测试、`refactor:` 重构、`ci:` CI 配置、`chore:` 其他杂项
- **只用 Squash and merge 合并**：一个 PR 在 `main` 上只留下一个 commit，提交信息取 PR 的标题和描述
- **review**：每个 PR 由 Claude review，意见处理完再合并
- **不提交密钥**：配置一律通过环境变量传入，仓库里只放 `.env.example`
- **文档跟着代码走**：改了启动方式或命令，同一个 PR 里更新 README
