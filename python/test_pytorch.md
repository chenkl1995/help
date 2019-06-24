### multigpu training
- console
    ```
    > CUDA_VISIBLE_DEVICES=1 python xxx.py
    ```
- python
    ```
    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "2"
    ```

    ```
    import torch
    torch.cuda.set_device(device_id)
    ```

### SyncBN
- [https://hangzhang.org/PyTorch-Encoding/notes/syncbn.html](https://hangzhang.org/PyTorch-Encoding/notes/syncbn.html)