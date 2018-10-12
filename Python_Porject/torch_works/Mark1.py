import time
import torch

for i in range(1,10):
    start = time.time()
    a = torch.FloatTensor(i*100,1000,1000)
    a = torch.matmul(a,a)
    end = time.time()-start
    print(end)