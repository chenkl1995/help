
```
    > CUDA_VISIBLE_DEVICES=1 python xxx.py
```

```
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
```

```
import torch
torch.cuda.set_device(device_id)
```
