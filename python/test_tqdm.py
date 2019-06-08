from tqdm import tqdm, trange
import time

# for i in trange(100):
    # time.sleep(0.1)


pbar = trange(100)
for i in pbar:  
    # pbar.set_description("desc %s" % i)
    # pbar.set_description_str("desc %s" % i)
    pbar.set_description_str("desc={}".format(i))
    time.sleep(0.01)

