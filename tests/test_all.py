#!/usr/bin/env python3
"""auto-doc-engine 综合测试套件"""

import sys, os
try:
    import yaml
    import mistune
    import jinja2
except ImportError as e:
    print(f"⚠️ 缺少依赖: {e}")
    sys.exit(1)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

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
    print("  [OK] AST 解析功能正确 (mistune驱动)")

def test_incremental_diff_paths():
    from core.ast_engine import MarkdownParser
    from core.incremental import DiffTracker
    
    parser = MarkdownParser()
    
    old = "# 报告\n\n进展 80%。\n"
    new = "# 报告\n\n进展 80%。\n\n进展 90%。\n"
    
    old_ast = parser.parse(old)
    new_ast = parser.parse(new)
    
    tracker = DiffTracker(tracker_path="tests/temp_tracker.yaml")
    changes = tracker.compute_diff('test_doc', old_ast, new_ast)
    
    has_add = any(c.action == 'add' and ('paragraph' in c.node_id or 'text' in c.node_id) for c in changes)
    assert has_add, "基于路径的 Diff 应该识别出新插入的段落，而不是哈希冲突"
    
    print("  [OK] 增量差异计算(路径跟踪)正确")
    if os.path.exists("tests/temp_tracker.yaml"):
        os.remove("tests/temp_tracker.yaml")

def test_sync_engine_secure_command():
    from core.sync import SyncEngine
    engine = SyncEngine()
    # 检查命令构造是否是安全的列表形式
    assert isinstance(engine.TARGETS['markdown'].command, list), "命令必须是列表以防注入"
    assert engine.TARGETS['html'].command[0] == 'pandoc', "HTML目标应该调用pandoc"
    print("  [OK] 同步引擎安全策略正确")

def test_data_binding_renderer():
    from core.renderer import DataBindingEngine
    import os
    
    os.makedirs('tests/temp_templates', exist_ok=True)
    with open('tests/temp_templates/test.j2', 'w') as f:
        f.write("# {{ title }}\n{{ data|table(['K', 'V']) }}")

    engine = DataBindingEngine(template_dir='tests/temp_templates')
    result = engine.render('test.j2', {
        'title': '测试绑定',
        'data': [{'K': 'A', 'V': 1}]
    })
    
    assert '# 测试绑定' in result
    assert '| A | 1 |' in result
    print("  [OK] 数据绑定与渲染正确")
    
    import shutil
    shutil.rmtree('tests/temp_templates')

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
