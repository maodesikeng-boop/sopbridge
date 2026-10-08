# SOPBridge

> 出海中资工厂的多语言作业指导书（SOP）知识库与 AI 助手
>
> 状态：🚧 开发中 · 当前阶段：Sprint 0（项目骨架）

## 简介

在越南等地的中资工厂里，中方管理者用中文编写作业指导书（SOP），一线工人使用越南语。SOPBridge 的工作流程：

1. 管理者上传中文 SOP，系统自动解析为步骤；
2. 大模型按工厂术语表翻译成越南语，双语员工逐段审核；
3. 审核通过后发布为受控版本，在工位张贴二维码；
4. 工人用手机扫码查看越南语版本，也可以用越南语提问，AI 基于 SOP 回答并注明出处。

## 核心功能（MVP）

- 多租户：工厂、成员与角色权限，数据严格隔离
- SOP 上传与异步解析（docx / pdf / md），草稿 → 审核 → 发布的版本管理
- 术语表约束的 AI 翻译，标记低置信度片段，人工逐段审核
- 工人端移动页面：扫码访问，无需注册
- 基于 SOP 的 RAG 问答：回答附出处，资料中没有答案时明确拒答
- 质量与成本：离线评估集与评估报告，大模型调用的成本和延迟监控

## 技术栈

| 层 | 技术 |
|---|---|
| 前端 | TypeScript · React · Next.js · Tailwind CSS · shadcn/ui |
| 后端 | Python · FastAPI · SQLAlchemy · Alembic · Pydantic |
| 数据 | PostgreSQL · pgvector · Redis |
| AI | OpenAI 兼容接口（DeepSeek / 通义千问）· 多语言向量模型 |
| 工程 | Docker Compose · GitHub Actions · uv · pnpm |

选型理由见 [ADR-0001](docs/adr/0001-tech-stack.md)。

## 文档

- [产品需求文档（PRD）](docs/01-prd.md)
- [架构决策记录（ADR）](docs/adr/)
- [Sprint 0 计划](docs/sprints/sprint-0.md)

## 本地开发

Sprint 0 完成后补充。

## 路线图

- [ ] Sprint 0：项目骨架、本地开发环境、CI
- [ ] Sprint 1：账号、多租户与权限
- [ ] Sprint 2：SOP 上传解析、版本管理、后台任务
- [ ] Sprint 3：术语表与 AI 翻译、人工审核
- [ ] Sprint 4：工人端移动页面与二维码
- [ ] Sprint 5：RAG 问答
- [ ] Sprint 6：质量评估与可观测性
- [ ] Sprint 7：生产部署、监控告警、压测与安全检查

## 说明

本项目为个人学习项目，演示数据均为自行编写的示例文件，不包含任何真实企业资料。
