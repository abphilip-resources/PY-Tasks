import time
import random

def waiting_game():
    t = random.randint(2,4) 
    print(f'\nYour target time is {t} seconds\n')
    
    input('-------------- Press Enter to Begin --------------')
    s = time.perf_counter()
    input(f'--------- Press Enter again after {t} secs ---------')
    e = time.perf_counter() - s
    
    print('\nElapsed time: {0:.3f} seconds'.format(e))
    if t-0.3 < e < t+0.3: print('(Unbelievable! Perfect timing!)')
    elif e <= t-0.3: print('({0:.3f} seconds too fast)'.format(t - e))
    elif e >= t+0.3: print('({0:.3f} seconds too slow)'.format(e - t))
    
waiting_game()