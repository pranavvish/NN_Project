import pandas as pd

# defining filepath
dir_path = 'Data/Cmaps_Data/'

# defining column names 
index_names = ['unit', 'time_cycles']
setting_names = ['setting_1', 'setting_2', 'setting_3']
sensor_names = ['s_{}'.format(i) for i in range(1, 22)]
col_names = index_names + setting_names + sensor_names

# read data
x_train = pd.read_csv((dir_path + 'train_FD001.txt'), delim_whitespace=True, header=None, names=col_names)
x_test = pd.read_csv((dir_path + 'test_FD001.txt'), delim_whitespace=True , header=None, names=col_names)
y_test = pd.read_csv((dir_path + 'RUL_FD001.txt'), delim_whitespace=True , header=None, names=['RUL'])



print(x_train)
print(x_test)