#!/usr/bin/env python3
"""auto-doc-engine 测试套件"""

import sys, os
try:
    import yaml
except ImportError:
    print("⚠️ 需要安装 PyYAML: pip install pyyaml")
    sys.exit(1)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_manifest_exists():
    assert os.path.exists('MANIFEST.yaml'), "MANIFEST 必须存在"
    print("  [OK] MANIFEST 存在")

def test_core_engines_exist():
    engines = ['ast_engine.py', 'incremental.py', 'sync.py']
    for e in engines:
        path = f'core/{e}'
        assert os.path.exists(path), f"引擎 {e} 必须存在"
    print("  [OK] 所有核心引擎存在")

def test_templates_exist():
    templates = ['weekly_report.j2', 'paper_summary.j2', 'project_status.j2']
    for t in templates:
        path = f'templates/jinja2/{t}'
        assert os.path.exists(path), f"模板 {t} 必须存在"
    print("  [OK] 所有 Jinja2 模板存在")

def test_sync_config_exists():
    assert os.path.exists('sync/targets.yaml'), "sync targets 必须存在"
    print("  [OK] 同步配置存在")

def test_ast_engine_parse():
    from core.ast_engine import MarkdownParser, ASTNode, NodeType
    
    parser = MarkdownParser()
    
    sample = "# 标题\n\n## 子标题\n\n段落内容。\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
    ast = parser.parse(sample)
    
    assert ast.type == NodeType.DOCUMENT, "根节点应为 DOCUMENT"
    assert len(ast.children) > 0, "应解析出子节点"
    
    headings = [c for c in ast.children if c.type == NodeType.HEADING]
    assert len(headings) >= 2, "应解析出至少 2 个标题"
    
    tables = [c for c in ast.children if c.type == NodeType.TABLE]
    assert len(tables) >= 1, "应解析出至少 1 个表格"
    
    print("  [OK] AST 解析功能正确")

def test_ast_engine_render():
    from core.ast_engine import MarkdownParser, ASTNode, NodeType
    
    parser = MarkdownParser()
    
    sample = "# 测试\n\n段落。\n\n- 项1\n- 项2\n"
    ast = parser.parse(sample)
    rendered = parser.render(ast)
    
    assert '# 测试' in rendered, "渲染应包含标题"
    assert '段落' in rendered, "渲染应包含段落"
    
    print("  [OK] AST 渲染功能正确")

def test_incremental_diff():
    from core.ast_engine import MarkdownParser
    from core.incremental import DiffTracker, compute_hash
    
    parser = MarkdownParser()
    
    old = "# 周报\n\n## 概览\n\n进展 80%。\n"
    new = "# 周报\n\n## 概览\n\n进展 90%。\n\n## 新章节\n\n新增内容。\n"
    
    old_ast = parser.parse(old)
    new_ast = parser.parse(new)
    
    tracker = DiffTracker()
    changes = tracker.compute_diff('test_doc', old_ast, new_ast)
    
    assert len(changes) > 0, "应有变更"
    
    has_add = any(c.action == 'add' for c in changes)
    has_modify = any(c.action == 'modify' for c in changes)
    assert has_add or has_modify, "应有新增或修改"
    
    print("  [OK] 增量差异计算正确")

def test_sync_engine_availability():
    from core.sync import SyncEngine
    
    engine = SyncEngine()
    
    # markdown 应始终可用
    assert engine.check_availability('markdown'), "markdown 应始终可用"
    
    print("  [OK] 同步引擎可用性检查正确")

def test_sync_targets_config():
    with open('sync/targets.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    assert 'targets' in config, "应有 targets 字段"
    assert isinstance(config['targets'], list), "targets 应为列表"
    assert len(config['targets']) >= 1, "应至少 1 个目标"
    
    print("  [OK] 同步目标配置正确")

def test_template_bindings():
    with open('templates/jinja2/weekly_report.j2', 'r') as f:
        content = f.read()
    
    assert 'data_source' in content, "模板应声明数据源"
    assert '{{' in content, "模板应使用 Jinja2 语法"
    
    print("  [OK] 模板绑定声明正确")

def test_ast_node_structure():
    from core.ast_engine import ASTNode, NodeType
    
    node = ASTNode(NodeType.HEADING, content="测试", level=2)
    assert node.type == NodeType.HEADING
    assert node.content == "测试"
    assert node.level == 2
    
    d = node.to_dict()
    assert d['type'] == 'heading'
    assert d['content'] == '测试'
    
    print("  [OK] AST 节点结构正确")

if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {t.__name__}: {e}")
            failed += 1
    print(f"\n  {passed}/{passed + failed} passed")
    sys.exit(0 if failed == 0 else 1)
