from dataclasses import dataclass, field
from typing import Dict, List
from collections import defaultdict

@dataclass
class Session:
    document_data: Dict[int, str] = field(default_factory=dict)
    index_data: Dict[str, List[int]] = field(default_factory=lambda: defaultdict(list))
    phrase_data: Dict[str, int] = field(default_factory=dict)