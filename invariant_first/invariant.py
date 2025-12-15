"""
@invariant decorator and metadata.

Allows declaring invariants as decorated functions.
"""

from typing import Callable, Any, Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class InvariantMetadata:
    """
    Metadata attached to invariant functions.
    
    This is the contract between decorated invariants and the engine.
    """
    name: str
    description: str
    check_fn: Callable[[Any, Any], bool]


def invariant(description: str, *, name: Optional[str] = None):
    """
    Decorator for marking invariant checking functions.
    
    Does NOT wrap the function — only annotates it with metadata.
    The function remains directly callable and debuggable.
    
    Args:
        description: Human-readable explanation of the invariant
        name: Stable identifier (defaults to function name)
    
    Usage:
        @invariant("Total balance is conserved")
        def check_balance_conservation(before, after):
            return sum(before.balances.values()) == sum(after.balances.values())
    
    The decorated function should:
    - Take (before_state, after_state) as arguments
    - Return True if the invariant holds, False otherwise
    """
    def decorator(func: Callable[[Any, Any], bool]) -> Callable[[Any, Any], bool]:
        # Don't wrap — just annotate
        invariant_name = name or func.__name__
        
        # Attach metadata directly to the function
        func._is_invariant = True
        func._invariant_name = invariant_name
        func._invariant_description = description
        
        return func
    
    return decorator


def get_invariant_metadata(func: Callable) -> Optional[InvariantMetadata]:
    """
    Extract invariant metadata from a decorated function.
    
    Returns:
        InvariantMetadata if function is an invariant, None otherwise
    """
    if not getattr(func, "_is_invariant", False):
        return None
    
    return InvariantMetadata(
        name=getattr(func, "_invariant_name"),
        description=getattr(func, "_invariant_description"),
        check_fn=func
    )


def is_invariant(func: Callable) -> bool:
    """Check if a function is decorated as an invariant."""
    return getattr(func, "_is_invariant", False)
