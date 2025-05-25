"""
Agentic File System Tooling for Modal Deployments

Provides secure, sandboxed file system operations for AI agents and API endpoints.
"""

import os
from pathlib import Path
from typing import List, Optional


class FileSystemTools:
    """Utility class for agentic file system operations."""

    def __init__(self, root: Optional[str] = None):
        self.root = Path(root or os.getcwd()).resolve()

    def list_dir(self, rel_path: str = ".") -> List[str]:
        """List files and directories in a given relative path."""
        path = (self.root / rel_path).resolve()
        if not str(path).startswith(str(self.root)):
            raise PermissionError("Access outside sandbox root is not allowed.")
        return [str(p.name) for p in path.iterdir()]

    def read_file(self, rel_path: str) -> str:
        """Read the contents of a file."""
        path = (self.root / rel_path).resolve()
        if not str(path).startswith(str(self.root)):
            raise PermissionError("Access outside sandbox root is not allowed.")
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    def write_file(self, rel_path: str, content: str, overwrite: bool = True) -> None:
        """Write content to a file (optionally overwrite)."""
        path = (self.root / rel_path).resolve()
        if not str(path).startswith(str(self.root)):
            raise PermissionError("Access outside sandbox root is not allowed.")
        if not overwrite and path.exists():
            raise FileExistsError(f"File {rel_path} already exists.")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def delete_file(self, rel_path: str) -> None:
        """Delete a file."""
        path = (self.root / rel_path).resolve()
        if not str(path).startswith(str(self.root)):
            raise PermissionError("Access outside sandbox root is not allowed.")
        if path.is_file():
            path.unlink()
        else:
            raise FileNotFoundError(f"File {rel_path} not found.")

    def make_dir(self, rel_path: str) -> None:
        """Create a new directory."""
        path = (self.root / rel_path).resolve()
        if not str(path).startswith(str(self.root)):
            raise PermissionError("Access outside sandbox root is not allowed.")
        path.mkdir(parents=True, exist_ok=True)
