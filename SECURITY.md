# Security Policy

> **Bilingual documentation scope / 双语文档边界（2026-11-13）**  
> **中文**：安全文档涵盖漏洞报告、权限与敏感数据边界，不代表所有工具链已完成安全审计；历史材料保留其原始截止时间与验证状态  
> **English**: Security guidance covers reporting, permissions and sensitive data, not a blanket security audit of the entire toolchain. Historical material retains its original cutoff and verification status


Please report security-sensitive issues privately to the maintainer rather than opening a public issue.

## Scope

Security reports should concern repository-owned code, automation, parsers, converters, validation logic, workflows, or documentation that could materially mislead users about a security boundary.

Do not include credentials, private data, or exploit details in public issues or pull requests. External tools, source material, and optional dependencies retain their own security and trust boundaries.

Passing repository checks is evidence only for the tested revision and declared scope; it is not a general security certification.
