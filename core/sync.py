#!/usr/bin/env python3
"""
多格式同步引擎 — 一次 Markdown 定义，多格式并行输出
"""

import subprocess
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class SyncTarget:
    format: str
    extension: str
    command: str
    enabled: bool = True
    requires: Optional[str] = None

class SyncEngine:
    """多格式同步引擎"""
    
    TARGETS = {
        'markdown': SyncTarget('markdown', '.md', 'cp {input} {output}'),
        'html': SyncTarget('html', '.html', 'pandoc {input} -o {output} -f markdown -t html --standalone', requires='pandoc'),
        'docx': SyncTarget('docx', '.docx', 'pandoc {input} -o {output} -f markdown -t docx --reference-doc={reference}', requires='pandoc'),
        'pdf': SyncTarget('pdf', '.pdf', 'pandoc {input} -o {output} -f markdown -t pdf --pdf-engine=xelatex', requires='pandoc'),
        'epub': SyncTarget('epub', '.epub', 'pandoc {input} -o {output} -f markdown -t epub', requires='pandoc'),
    }
    
    def __init__(self, config_path: str = "sync/targets.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        import yaml
        if self.config_path.exists():
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f) or {}
        return {'targets': ['markdown', 'html']}
    
    def check_availability(self, target: str) -> bool:
        """检查目标格式是否可用"""
        if target not in self.TARGETS:
            return False
        
        t = self.TARGETS[target]
        if not t.requires:
            return True
        
        # 检查命令是否存在
        try:
            subprocess.run([t.requires, '--version'], 
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def sync(self, input_path: str, targets: List[str] = None, 
             output_dir: str = "output", reference_doc: str = None) -> Dict[str, str]:
        """同步生成多格式输出"""
        if targets is None:
            targets = self.config.get('targets', ['markdown'])
        
        input_path = Path(input_path)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        results = {}
        
        for target in targets:
            if target not in self.TARGETS:
                results[target] = f"ERROR: 未知格式 {target}"
                continue
            
            if not self.check_availability(target):
                results[target] = f"ERROR: {self.TARGETS[target].requires} 未安装"
                continue
            
            t = self.TARGETS[target]
            output_path = output_dir / (input_path.stem + t.extension)
            
            # 构建命令
            cmd = t.command.format(
                input=input_path,
                output=output_path,
                reference=reference_doc or ''
            )
            
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    results[target] = str(output_path)
                else:
                    results[target] = f"ERROR: {result.stderr}"
            except Exception as e:
                results[target] = f"ERROR: {str(e)}"
        
        return results
    
    def sync_with_fallback(self, input_path: str, targets: List[str] = None,
                           output_dir: str = "output") -> Dict[str, str]:
        """同步生成，对不可用的格式使用降级方案"""
        if targets is None:
            targets = self.config.get('targets', ['markdown'])
        
        results = {}
        
        for target in targets:
            if self.check_availability(target):
                # 正常生成
                r = self.sync(input_path, [target], output_dir)
                results.update(r)
            else:
                # 降级方案
                if target == 'html' and self.check_availability('markdown'):
                    # 用 markdown 生成一个简易 HTML 包装
                    results[target] = self._fallback_html(input_path, output_dir)
                elif target == 'docx' and self.check_availability('markdown'):
                    results[target] = f"WARN: Pandoc 未安装，仅生成 Markdown 版本"
                else:
                    results[target] = f"ERROR: 无法生成 {target}（依赖未安装）"
        
        return results
    
    def _fallback_html(self, input_path: str, output_dir: str) -> str:
        """简易 HTML 降级生成"""
        input_path = Path(input_path)
        output_dir = Path(output_dir)
        output_path = output_dir / (input_path.stem + '.html')
        
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 简易 Markdown → HTML 转换（无 Pandoc 时）
        html = self._simple_md_to_html(md_content)
        
        full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{input_path.stem}</title>
<style>
body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
h1 {{ border-bottom: 2px solid #333; padding-bottom: 10px; }}
h2 {{ border-bottom: 1px solid #ccc; padding-bottom: 5px; }}
table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background-color: #f5f5f5; }}
code {{ background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
</style>
</head>
<body>
{html}
</body>
</html>"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        return str(output_path)
    
    def _simple_md_to_html(self, md: str) -> str:
        """简易 Markdown 到 HTML 转换"""
        import re
        html = md
        
        # 代码块
        html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
        
        # 标题
        html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
        
        # 粗体/斜体
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
        html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
        
        # 表格（简化）
        html = re.sub(r'\|(.+?)\|', r'<td>\1</td>', html)
        
        # 列表
        html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
        
        # 段落
        paragraphs = html.split('\n\n')
        wrapped = []
        for p in paragraphs:
            p = p.strip()
            if p and not p.startswith('<') and not p.startswith('---'):
                p = f'<p>{p}</p>'
            wrapped.append(p)
        html = '\n\n'.join(wrapped)
        
        return html

def demo():
    """演示多格式同步"""
    engine = SyncEngine()
    
    # 创建示例 Markdown
    sample = """# 示例报告

## 概述

这是自动生成的示例报告。

## 数据

| 指标 | 数值 |
|------|------|
| 完成率 | 95% |
| 质量分 | 4.8 |

## 结论

一切正常。
"""
    
    sample_path = Path('output/_sample.md')
    sample_path.parent.mkdir(parents=True, exist_ok=True)
    sample_path.write_text(sample, encoding='utf-8')
    
    print("=== 多格式同步演示 ===")
    
    # 检查可用格式
    for fmt in ['markdown', 'html', 'docx', 'pdf']:
        avail = engine.check_availability(fmt)
        print(f"  {fmt}: {'✅ 可用' if avail else '❌ 不可用'}")
    
    # 同步生成
    results = engine.sync_with_fallback(
        str(sample_path), 
        targets=['markdown', 'html'],
        output_dir='output'
    )
    
    print(f"\n同步结果:")
    for fmt, path in results.items():
        print(f"  {fmt}: {path}")

if __name__ == '__main__':
    demo()
