from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


# --- Model ---
@dataclass
class Post:
    id: int
    title: str
    content: str
    author: str = "Anonymous"
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


# --- Repository ---
class PostRepository:
    def __init__(self) -> None:
        self._posts: List[Post] = []
        self._next_id: int = 1

    def _generate_id(self) -> int:
        """Generate and return the next unique post ID."""
        pid = self._next_id
        self._next_id += 1
        return pid

    def all(self) -> List[Post]:
        """Return all posts sorted by creation date (newest first)."""
        return sorted(self._posts, key=lambda x: x.created_at, reverse=True)

    def get(self, pid: int) -> Optional[Post]:
        """Find a post by its ID, return None if not found."""
        return next((p for p in self._posts if p.id == pid), None)

    def add(self, title: str, content: str, author: str = "Anonymous") -> Post:
        """Create and store a new post."""
        post = Post(
            id=self._generate_id(),
            title=title.strip(),
            content=content.strip(),
            author=author.strip() or "Anonymous",
        )
        self._posts.append(post)
        return post

    def update(
        self, pid: int, title: Optional[str] = None,
        content: Optional[str] = None, author: Optional[str] = None
    ) -> Optional[Post]:
        """Update an existing post."""
        post = self.get(pid)
        if not post:
            return None

        if title is not None:
            post.title = title.strip()
        if content is not None:
            post.content = content.strip()
        if author is not None:
            post.author = author.strip() or "Anonymous"

        post.updated_at = datetime.now()
        return post

    def delete(self, pid: int) -> bool:
        """Delete a post by ID, return True if successful."""
        post = self.get(pid)
        if not post:
            return False
        self._posts.remove(post)
        return True

    def seed(self) -> None:
        """Seed repository with sample data (only if empty)."""
        if self._posts:
            return
        self.add("Welcome to Blog", "This is the first post for Blog Django", "Elvin")
        self.add("Django MVT", "Today we are learning the deepest points of Django", "Aysel")


# Example usage:
repo = PostRepository()
repo.seed()

for post in repo.all():
    print(post)
