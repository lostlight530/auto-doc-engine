#!/usr/bin/env python3
"""
多格式同步引擎 — 一次 Markdown 定义，多格式并行输出
安全升级版：弃用 shell=True，防止注入攻击
"""

import subprocess
import shlex
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class SyncTarget:
    format: str
    extension: str
    command: List[str]  # 改为列表形式，杜绝 Shell 注入
    enabled: bool = True
    requires: Optional[str] = None

class SyncEngine:
    TARGETS = {
        'markdown': SyncTarget('markdown', '.md', ['cp', '{input}', '{output}']),
        'html': SyncTarget('html', '.html', ['pandoc', '{input}', '-o', '{output}', '-f', 'markdown', '-t', 'html', '--standalone'], requires='pandoc'),
        'docx': SyncTarget('docx', '.docx', ['pandoc', '{input}', '-o', '{output}', '-f', 'markdown', '-t', 'docx'], requires='pandoc'),
        'pdf': SyncTarget('pdf', '.pdf', ['pandoc', '{input}', '-o', '{output}', '-f', 'markdown', '-t', 'pdf', '--pdf-engine=xelatex'], requires='pandoc'),
        'epub': SyncTarget('epub', '.epub', ['pandoc', '{input}', '-o', '{output}', '-f', 'markdown', '-t', 'epub'], requires='pandoc'),
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
        if target not in self.TARGETS:
            return False
        
        t = self.TARGETS[target]
        if not t.requires:
            return True
        
        try:
            subprocess.run([t.requires, '--version'], 
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def sync(self, input_path: str, targets: List[str] = None, 
             output_dir: str = "output", reference_doc: str = None) -> Dict[str, str]:
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
            
            # 构建安全的命令列表
            cmd = []
            for arg in t.command:
                if arg == '{input}':
                    cmd.append(str(input_path))
                elif arg == '{output}':
                    cmd.append(str(output_path))
                elif arg == '{reference}' and reference_doc:
                    cmd.append(reference_doc)
                elif '{' not in arg:
                    cmd.append(arg)
            
            # 对 docx 特殊处理 reference
            if target == 'docx' and reference_doc:
                cmd.append(f'--reference-doc={reference_doc}')

            try:
                # 弃用 shell=True
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    results[target] = str(output_path)
                else:
                    results[target] = f"ERROR: {result.stderr}"
            except Exception as e:
                results[target] = f"ERROR: {str(e)}"
        
        return results
    
    def sync_with_fallback(self, input_path: str, targets: List[str] = None,
                           output_dir: str = "output") -> Dict[str, str]:
        if targets is None:
            targets = self.config.get('targets', ['markdown'])
        
        results = {}
        
        for target in targets:
            if self.check_availability(target):
                r = self.sync(input_path, [target], output_dir)
                results.update(r)
            else:
                if target == 'html' and self.check_availability('markdown'):
                    results[target] = self._fallback_html(input_path, output_dir)
                elif target == 'docx' and self.check_availability('markdown'):
                    results[target] = f"WARN: Pandoc 未安装，仅生成 Markdown 版本"
                else:
                    results[target] = f"ERROR: 无法生成 {target}（依赖未安装）"
        
        return results
    
    def _fallback_html(self, input_path: str, output_dir: str) -> str:
        input_path = Path(input_path)
        output_dir = Path(output_dir)
        output_path = output_dir / (input_path.stem + '.html')
        
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        import mistune
        html = mistune.html(md_content)
        
        full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>{input_path.stem}</title>
<style>
body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background-color: #f5f5f5; }}
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

def demo():
    engine = SyncEngine()
    sample = "# 示例报告\n\n## 数据\n\n| 指标 | 数值 |\n|---|---|\n| 进度 | 90% |\n"
    
    sample_path = Path('output/_sample2.md')
    sample_path.parent.mkdir(parents=True, exist_ok=True)
    sample_path.write_text(sample, encoding='utf-8')
    
    print("=== 多格式同步安全版本演示 ===")
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
