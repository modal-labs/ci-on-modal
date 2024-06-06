import torch


def has_gpu():
    print(f"Running Torch v{torch.__version__}")
    has_cuda = torch.cuda.is_available()
    print(f"It is {has_cuda} that Torch can access CUDA")

    return has_cuda
