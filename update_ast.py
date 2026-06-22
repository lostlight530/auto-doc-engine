import re

with open('core/ast_engine.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a hash/signature property to ASTNode to avoid re-rendering for signature.

new_node_class = """
import hashlib

@dataclass
class ASTNode:
    type: NodeType
    content: Optional[str] = None
    level: Optional[int] = None
    children: List['ASTNode'] = field(default_factory=list)
    attributes: Dict[str, Any] = field(default_factory=dict)

    @property
    def signature(self) -> str:
        # Compute a fast hash of the node's shallow content and attributes for quick equality checks
        data = f"{self.type.value}:{self.content}:{self.level}:{sorted(self.attributes.items())}"
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    def to_dict(self) -> dict:
"""

pattern = re.compile(r'@dataclass\nclass ASTNode:.*?(?=    def to_dict)', re.DOTALL)
new_content = pattern.sub(new_node_class, content)

with open('core/ast_engine.py', 'w', encoding='utf-8') as f:
    f.write(new_content)
