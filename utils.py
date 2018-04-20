import torch
import torch.nn as nn
from torch.nn.parameter import Parameter


# Necessary for my KFAC implementation.
class AddBias(nn.Module):
    def __init__(self, bias):
        super(AddBias, self).__init__()
        self._bias = nn.Parameter(bias.unsqueeze(1))

    def forward(self, x):
        if x.dim() == 2:
            bias = self._bias.t().view(1, -1)
        else:
            bias = self._bias.t().view(1, -1, 1, 1)

        return x + bias

# A temporary solution from the master branch.
# https://github.com/pytorch/pytorch/blob/7752fe5d4e50052b3b0bbc9109e599f8157febc0/torch/nn/init.py#L312
# Remove after the next version of PyTorch gets release.
def orthogonal(tensor, gain=1):
    if tensor.ndimension() < 2:
        raise ValueError("Only tensors with 2 or more dimensions are supported")

    rows = tensor.size(0)
    cols = tensor[0].numel()
    flattened = torch.Tensor(rows, cols).normal_(0, 1)

    if rows < cols:
        flattened.t_()

    # Compute the qr factorization
    q, r = torch.qr(flattened)
    # Make Q uniform according to https://arxiv.org/pdf/math-ph/0609050.pdf
    d = torch.diag(r, 0)
    ph = d.sign()
    q *= ph.expand_as(q)

    if rows < cols:
        q.t_()

    tensor.view_as(q).copy_(q)
    tensor.mul_(gain)
    return tensor

def load_ga_model(actor_critic, ga_model_path):
    model = torch.load(ga_model_path)
    actor_critic.conv1.weight = Parameter(model.conv1.weight)
    actor_critic.conv1.bias = Parameter(model.conv1.bias)
    actor_critic.conv2.weight = Parameter(model.conv2.weight)
    actor_critic.conv2.bias = Parameter(model.conv2.bias)
    actor_critic.conv3.weight = Parameter(model.conv3.weight)
    actor_critic.conv3.bias = Parameter(model.conv3.bias)
    actor_critic.linear1.weight = Parameter(model.dense.weight)
    actor_critic.linear1.bias = Parameter(model.dense.bias)
    actor_critic.dist.linear.weight = Parameter(model.out.weight)
    actor_critic.dist.linear.bias = Parameter(model.out.bias)

