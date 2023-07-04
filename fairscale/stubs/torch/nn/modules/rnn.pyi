# Copyright (c) Facebook, Inc. and its affiliates. All rights reserved.

from ..parameter import Parameter
from .module import Module
from typing import Any, Optional, Tuple, List
from ... import Tensor


def apply_permutation(tensor: Tensor, permutation: Tensor, dim: int = ...) -> Tensor: ...


class RNNBase(Module):
    mode: str = ...
    input_size: int = ...
    hidden_size: int = ...
    num_layers: int = ...
    bias: bool = ...
    batch_first: bool = ...
    dropout: float = ...
    bidirectional: bool = ...

    def __init__(self, mode: str, input_size: int, hidden_size: int, num_layers: int = ..., bias: bool = ...,
                 batch_first: bool = ..., dropout: float = ..., bidirectional: bool = ...) -> None: ...

    def flatten_parameters(self) -> List[Parameter]: ...

    def reset_parameters(self) -> None: ...

    def get_flat_weights(self): ...

    def check_input(self, input: Tensor, batch_sizes: Optional[Tensor]) -> None: ...

    def get_expected_hidden_size(self, input: Tensor, batch_sizes: Optional[Tensor]) -> Tuple[int, int, int]: ...

    def check_hidden_size(self, hx: Tensor, expected_hidden_size: Tuple[int, int, int], msg: str = ...) -> None: ...

    def check_forward_args(self, input: Any, hidden: Any, batch_sizes: Optional[Tensor]) -> None: ...

    def permute_hidden(self, hx: Any, permutation: Any): ...

    def forward(self, input: Tensor, hx: Optional[Any] = ...) -> Any: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Any] = ...) -> Any: ...  # type: ignore

    @property
    def all_weights(self) -> List[Parameter]: ...


class RNN(RNNBase):
    def __init__(self, input_size: int, hidden_size: int, num_layers: int = ..., bias: bool = ...,
                 batch_first: bool = ..., dropout: float = ..., bidirectional: bool = ...,
                 nonlinearity: str = ...) -> None: ...

    def forward(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore


class LSTM(RNNBase):
    def __init__(self, input_size: int, hidden_size: int, num_layers: int = ..., bias: bool = ...,
                 batch_first: bool = ..., dropout: float = ..., bidirectional: bool = ...,
                 nonlinearity: str = ...) -> None: ...

    def check_forward_args(self, input: Tensor, hidden: Tuple[Tensor, Tensor],
                           batch_sizes: Optional[Tensor]) -> None: ...

    def permute_hidden(self, hx: Tuple[Tensor, Tensor], permutation: Optional[Tensor]) -> Tuple[Tensor, Tensor]: ...

    def forward_impl(self, input: Tensor, hx: Optional[Tuple[Tensor, Tensor]], batch_sizes: Optional[Tensor],
                     max_batch_size: int, sorted_indices: Optional[Tensor]) -> Tuple[Tensor, Tuple[Tensor, Tensor]]: ...

    def forward_tensor(self, input: Tensor, hx: Optional[Tuple[Tensor, Tensor]] = ...) -> Tuple[
        Tensor, Tuple[Tensor, Tensor]]: ...

    def forward_packed(self, input: Tuple[Tensor, Tensor, Optional[Tensor], Optional[Tensor]],
                       hx: Optional[Tuple[Tensor, Tensor]] = ...) -> Tuple[
        Tuple[Tensor, Tensor, Optional[Tensor], Optional[Tensor]], Tuple[Tensor, Tensor]]: ...

    def forward(self, input: Tensor, hx: Optional[Tuple[Tensor, Tensor]] = ...) -> Tuple[Tensor, Tuple[Tensor, Tensor]]: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Tuple[Tensor, Tensor]] = ...) -> Tuple[Tensor, Tuple[Tensor, Tensor]]: ...  # type: ignore


class GRU(RNNBase):
    def __init__(self, input_size: int, hidden_size: int, num_layers: int = ..., bias: bool = ...,
                 batch_first: bool = ..., dropout: float = ..., bidirectional: bool = ...,
                 nonlinearity: str = ...) -> None: ...

    def forward(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore


class RNNCellBase(Module):
    input_size: int = ...
    hidden_size: int = ...
    bias: bool = ...
    weight_ih: Parameter = ...
    weight_hh: Parameter = ...
    bias_ih: Parameter = ...
    bias_hh: Parameter = ...

    def __init__(self, input_size: int, hidden_size: int, bias: bool, num_chunks: int) -> None: ...

    def check_forward_input(self, input: Tensor) -> None: ...

    def check_forward_hidden(self, input: Tensor, hx: Tensor, hidden_label: str = ...) -> None: ...

    def reset_parameters(self) -> None: ...


class RNNCell(RNNCellBase):
    nonlinearity: str = ...

    def __init__(self, input_size: int, hidden_size: int, bias: bool = ..., nonlinearity: str = ...) -> None: ...

    def forward(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore


class LSTMCell(RNNCellBase):
    def __init__(self, input_size: int, hidden_size: int, bias: bool = ...) -> None: ...

    def forward(self, input: Tensor, hx: Optional[Tuple[Tensor, Tensor]] = ...) -> Tuple[Tensor, Tensor]: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Tuple[Tensor, Tensor]] = ...) -> Tuple[Tensor, Tensor]: ...  # type: ignore


class GRUCell(RNNCellBase):
    def __init__(self, input_size: int, hidden_size: int, bias: bool = ...) -> None: ...

    def forward(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore

    def __call__(self, input: Tensor, hx: Optional[Tensor] = ...) -> Tensor: ...  # type: ignore
