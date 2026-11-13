# Security Policy


Please report security-sensitive issues privately to the maintainer rather than opening a public issue.

### 中文敏感信息与生成产物边界 / Sensitive data in generated artifacts

不得在 public PR、CLI 日志、SARIF 输出、RO-Crate 包装或 Pages 页面包含凭据、私人输入或未经修复漏洞详情；公开格式有效性不能证明没有敏感数据泄漏，安全检查需说明实际测试对象与权限

Do not expose credentials, private inputs or unpatched exploit details in public PRs, CLI logs, SARIF outputs, RO-Crate packages or Pages. Format validity cannot certify absence of data leakage; security reviews must identify tested objects and permissions

## Scope

Security reports should concern repository-owned code, automation, parsers, converters, validation logic, workflows, or documentation that could materially mislead users about a security boundary.

Do not include credentials, private data, or exploit details in public issues or pull requests. External tools, source material, and optional dependencies retain their own security and trust boundaries.

Passing repository checks is evidence only for the tested revision and declared scope; it is not a general security certification.
