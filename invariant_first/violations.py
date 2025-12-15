"""
InvariantViolation exceptions and error handling.
"""

from typing import Any, Callable


class InvariantViolation(Exception):
    """
    Raised when a state transition violates a declared invariant.
    
    This is intentionally loud and non-recoverable.
    Invariant violations indicate a logic error, not a runtime condition.
    """
    
    def __init__(
        self,
        *,
        invariant_name: str,
        invariant_description: str,
        before_state: Any,
        after_state: Any,
        transition: Callable,
    ):
        self.invariant_name = invariant_name
        self.invariant_description = invariant_description
        self.before_state = before_state
        self.after_state = after_state
        self.transition = transition
        
        super().__init__(self._build_message())
    
    def _build_message(self) -> str:
        """Build canonical error message with full context."""
        return (
            f"Invariant violated: {self.invariant_name}\n"
            f"Description: {self.invariant_description}\n"
            f"Transition: {self.transition.__name__}\n"
            f"Before state: {self.before_state}\n"
            f"After state:  {self.after_state}"
        )
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "error": "InvariantViolation",
            "invariant": self.invariant_name,
            "description": self.invariant_description,
            "transition": self.transition.__name__,
            "before_state": str(self.before_state),
            "after_state": str(self.after_state),
        }
