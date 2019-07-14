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

### Optimizer
- [https://blog.csdn.net/google19890102/article/details/69942970](https://blog.csdn.net/google19890102/article/details/69942970)
- SGD
```
    for i in range(num_epochs):
        params_grad = evaluate_gradient(loss_func, `data`, params)
        params = params - lr * params_grad

    for i in range(num_epochs):
        np.random.shuffle(data)
        for example in data:
            params_grad = evaluate_gradient(loss_func, `example`, params)
            params = params - lr * params_grad

    for i in range(num_epochs):
        np.random.shuffle(data)
        for batch in get_batches(data, batch_size):
            params_grad = evaluate_gradient(loss_func, `batch`, params)
            params = params - lr * params_grad
```
- Nesterov
- Adagrad
- Adadelta
- RMSProp
- Adam


#### Nvidia Cuda Mem Leak
```
    > fuser -v /dev/nvidia*
    > sudo kill -9 <pid>
```