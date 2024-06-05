from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()  # ensures the next print is on the next line
for elem in tqdm(range(333)):
    sleep(0.005)