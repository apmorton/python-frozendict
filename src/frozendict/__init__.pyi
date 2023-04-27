from __future__ import annotations

from typing import TypeVar, overload, Type, Optional

try:
    from typing import Mapping, Sequence, Iterable, Iterator, Tuple
except ImportError:
    from collections.abc import Mapping, Sequence, Iterable, Iterator
    Tuple = tuple

K = TypeVar("K")
V = TypeVar("V")
SelfT = TypeVar("SelfT", bound=frozendict[K, V])

class frozendict(Mapping[K, V]):
    @overload
    def __new__(cls: Type[SelfT], **kwargs: V) -> SelfT: ...
    @overload
    def __new__(cls: Type[SelfT], mapping: Mapping[K, V]) -> SelfT: ...
    @overload
    def __new__(cls: Type[SelfT], iterable: Iterable[Tuple[K, V]]) -> SelfT: ...
    
    def __getitem__(self: SelfT, key: K) -> V: ...
    def __len__(self: SelfT) -> int: ...
    def __iter__(self: SelfT) -> Iterator[K]: ...
    def __hash__(self: SelfT) -> int: ...
    def __reversed__(self: SelfT) -> Iterator[K]: ...
    def copy(self: SelfT) -> SelfT: ...
    def __copy__(self: SelfT) -> SelfT: ...
    def __deepcopy__(self: SelfT) -> SelfT: ...
    def set(self: SelfT, key: K, value: V) -> SelfT: ...
    def setdefault(self: SelfT, key: K, default: V) -> SelfT: ...
    def delete(self: SelfT, key: K) -> SelfT: ...
    def key(self: SelfT, index: int) -> K: ...
    def value(self: SelfT, index: int) -> V: ...
    def item(self: SelfT, index: int) -> Tuple[K, V]: ...
    def __or__(self: SelfT, other: Mapping[K, V]) -> SelfT: ...
    
    @classmethod
    def fromkeys(
        cls: Type[SelfT], 
        seq: Iterable[K], 
        value: Optional[V] = None
    ) -> SelfT: ...


FrozenOrderedDict = frozendict
