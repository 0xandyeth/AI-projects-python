# main.py
import sys
sys.path.append('modules')

from train_module import Train

train = Train("./assets/dress.csv")
results = train.on_train()
print(results)


