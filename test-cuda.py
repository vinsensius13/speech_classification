import torch

def test_cuda():
    print("🔥 PyTorch version:", torch.__version__)
    print("🧠 CUDA Available:", torch.cuda.is_available())
    
    if torch.cuda.is_available():
        print("🎮 GPU Name:", torch.cuda.get_device_name(0))
        print("💾 Memory Allocated (MB):", torch.cuda.memory_allocated() / 1024 / 1024)
        print("🧹 Memory Reserved (MB):", torch.cuda.memory_reserved() / 1024 / 1024)
    else:
        print("😭 CUDA nggak tersedia, periksa lagi instalasi kamu!")

if __name__ == "__main__":
    test_cuda()
