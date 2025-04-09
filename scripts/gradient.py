import torch
import torch.nn.functional as F

from functools import partial


class MLP(object):
    """self-implemented MLP model, used for teaching and homework checking"""

    def __init__(
        self,
        in_dim: int,
        mlp_dims: list[int],
        out_dim: int,
        acts: list[callable],
    ):
        """
        For a simple implementation, length of `acts` is equal to number of layers
        We use provided init_weights for model initialization, details in `initialize`
        """

        self.num_layers = len(mlp_dims) + 1
        assert len(acts) == self.num_layers

        for i in range(self.num_layers):
            in_features = in_dim if i == 0 else mlp_dims[i - 1]
            out_features = out_dim if i == self.num_layers - 1 else mlp_dims[i]
            self.__setattr__(
                f"linear{i}",
                torch.randn((out_features, in_features), dtype=torch.float, requires_grad=True),
            )
            self.__setattr__(f"act{i}", acts[i])

    def initialize(
        self,
        layer_idx: int,
        weight: torch.Tensor,
    ):
        assert layer_idx < self.num_layers
        assert weight.shape == self.__getattribute__(f"linear{layer_idx}").shape
        assert weight.requires_grad
        self.__setattr__(f"linear{layer_idx}", weight)

    @torch.no_grad()
    def gradients(self):
        for i in range(self.num_layers):
            print(f"Gradient of linear layer {i}:")
            print(self.__getattribute__(f"linear{i}").grad)

    @torch.no_grad()
    def weights(self):
        for i in range(self.num_layers):
            print(f"Weight of linear layer {i}:")
            print(self.__getattribute__(f"linear{i}"))

    @torch.no_grad()
    def update(self, lr: float = 1.0, gamma: float = 1.0, momentum: list[torch.Tensor] = None):
        for i in range(self.num_layers):
            weight = self.__getattribute__(f"linear{i}")
            grad = self.__getattribute__(f"linear{i}").grad
            if momentum is not None:
                m = gamma * momentum[i] + (1 - gamma) * grad
                print(f"momentum {i} = {m}")
                self.__setattr__(f"linear{i}", weight - lr * m)
            else:
                self.__setattr__(f"linear{i}", weight - lr * grad)

    def __call__(
        self,
        inputs: torch.Tensor,
        targets: torch.Tensor,
        loss_fn: callable,
        show_steps: bool = False,
    ) -> torch.Tensor:
        x: torch.Tensor = inputs

        if show_steps:
            print(f"-------- model forward start --------")

        for i in range(self.num_layers):
            x = self.__getattribute__(f"linear{i}") @ x
            if show_steps:
                print(f"W x = {x}")
            x = self.__getattribute__(f"act{i}")(x)
            if show_steps:
                print(f"act(x) = {x}")

        if show_steps:
            print(f"-------- model forward ended --------")

        loss: torch.Tensor = loss_fn(x.flatten(), targets)
        return loss


mse_loss_fn = lambda p, t: 0.5 * ((p - t) ** 2).sum()
ce_loss_fn = lambda p, t: -(t * p.log()).sum()

if __name__ == "__main__":
    in_dim = 2
    mlp_dims = [3]
    out_dim = 2
    acts = [F.relu, partial(F.softmax, dim=0)]

    model = MLP(in_dim, mlp_dims, out_dim, acts)

    model.initialize(
        0,
        torch.tensor(
            [
                [-0.3, 0.5],
                [0.1, -0.3],
                [-0.1, 0.2],
            ],
            dtype=torch.float,
            requires_grad=True,
        ),
    )
    model.initialize(
        1,
        torch.tensor(
            [
                [0.5, 0.7, -0.2],
                [0.3, -0.6, 0.3],
            ],
            dtype=torch.float,
            requires_grad=True,
        ),
    )

    inputs = torch.tensor([[1], [1]], dtype=torch.float, requires_grad=True)
    targets = torch.tensor([1, 0], dtype=torch.float)

    loss = model(inputs, targets, ce_loss_fn, show_steps=True)
    print(f"==> loss: {loss:.4f}")

    print("==> Before back propagation:")
    model.weights()
    model.gradients()

    loss.backward()

    print("==> After back propagation:")
    model.gradients()

    momentum = [
        torch.tensor([[0.03, 0.001], [-0.009, 0.0014], [0.0001, -0.0002]]),
        torch.tensor([[0.004, 0.002, -0.006], [0.001, 0.001, -0.008]]),
    ]
    model.update(0.8, 0.8, momentum)
    print("==> After weight update:")
    model.weights()
