import pandas as pd

def add_rul(df):
    
    # Compute the maximum cycle for each unit
    max_cycle = df.groupby(by="unit_nr")["time_cycles"].transform("max")
    # Calculate the remaining useful life for each row
    df["RUL"] = max_cycle - df["time_cycles"]
    # Drop the time_cycles column, as it's no longer needed
    return df.drop("time_cycles", axis=1)

def normalize_data(df):
    # Normalize sensor data

    # separate title information and sensor data
    title = df.iloc[:, 0:2]
    data = df.iloc[:, 2:]

    # min-max normalization of the sensor data
    data_norm = (data - data.min()) / (data.max() - data.min())
    return pd.concat([title, data_norm], axis=1)


def load_data_FD001():
    # Define the file path and column names
    path = "Data/Cmaps_Data/"
    columns = ["unit_nr", "time_cycles", "setting_1", "setting_2", "setting_3"]
    # Only 21 sensor readings are available
    columns += ["s_{i}" for i in range(1, 22)]

    # Load the data
    x_train = pd.read_csv(path + "train_FD001.txt", delim_whitespace=True, header=None, names=columns)
    x_test = pd.read_csv(path + "test_FD001.txt", delim_whitespace=True, header=None, names=columns)
    y_test = pd.read_csv(path + "RUL_FD001.txt", delim_whitespace=True, header=None, names=["RUL"])

    # Remove non-informative sensory readings and settings from the data
    drop_cols = ["setting_1", "setting_2", "setting_3", "s_1", "s_5", "s_6", "s_10", "s_16", "s_18", "s_19"]
    x_train = x_train.drop(drop_cols, axis=1)
    x_test = x_test.drop(drop_cols, axis=1)

    # Compute the remaining useful life for the training data
    x_train = add_rul(x_train)

    # Clip the maximum RUL to 125, as mentioned in the paper
    x_train["RUL"] = x_train["RUL"].clip(upper=125)

    # Normalize the sensor data
    x_train = normalize_data(x_train)
    x_test = normalize_data(x_test)

    # Group the data by unit number
    train_groups = x_train.groupby("unit_nr")
    test_groups = x_test.groupby("unit_nr")

    return train_groups, y_test, test_groups

def load_data_FD002():
    # Define the file path and column names
    path = "Data/Cmaps_Data/"
    columns = ["unit_nr", "time_cycles", "setting_1", "setting_2", "setting_3"]
    # Only 21 sensor readings are available
    columns += ["s_{i}" for i in range(1, 22)]

    # Load the data
    x_train = pd.read_csv(path + "train_FD002.txt", delim_whitespace=True, header=None, names=columns)
    x_test = pd.read_csv(path + "test_FD002.txt", delim_whitespace=True, header=None, names=columns)
    y_test = pd.read_csv(path + "RUL_FD002.txt", delim_whitespace=True, header=None, names=["RUL"])

    # # Remove non-informative sensory readings and settings from the data
    # drop_cols = ["setting_1", "setting_2", "setting_3", "s_1", "s_5", "s_6", "s_10", "s_16", "s_18", "s_19"]
    # x_train = x_train.drop(drop_cols, axis=1)
    # x_test = x_test.drop(drop_cols, axis=1)

    # Compute the remaining useful life for the training data
    x_train = add_rul(x_train)

    # Clip the maximum RUL to 125, as mentioned in the paper
    x_train["RUL"] = x_train["RUL"].clip(upper=125)

    # Normalize the sensor data
    x_train = normalize_data(x_train)
    x_test = normalize_data(x_test)

    # Group the data by unit number
    train_groups = x_train.groupby("unit_nr")
    test_groups = x_test.groupby("unit_nr")

    return train_groups, y_test, test_groups

def load_data_FD003():
    # Define the file path and column names
    path = "Data/Cmaps_Data/"
    columns = ["unit_nr", "time_cycles", "setting_1", "setting_2", "setting_3"]
    # Only 21 sensor readings are available
    columns += ["s_{i}" for i in range(1, 22)]

    # Load the data
    x_train = pd.read_csv(path + "train_FD003.txt", delim_whitespace=True, header=None, names=columns)
    x_test = pd.read_csv(path + "test_FD003.txt", delim_whitespace=True, header=None, names=columns)
    y_test = pd.read_csv(path + "RUL_FD003.txt", delim_whitespace=True, header=None, names=["RUL"])

    # Remove non-informative sensory readings and settings from the data
    drop_cols = ["setting_1", "setting_2", "setting_3", "s_1", "s_5", "s_16", "s_18", "s_19"]
    x_train = x_train.drop(drop_cols, axis=1)
    x_test = x_test.drop(drop_cols, axis=1)

    # Compute the remaining useful life for the training data
    x_train = add_rul(x_train)

    # Clip the maximum RUL to 125, as mentioned in the paper
    x_train["RUL"] = x_train["RUL"].clip(upper=125)

    # Normalize the sensor data
    x_train = normalize_data(x_train)
    x_test = normalize_data(x_test)

    # Group the data by unit number
    train_groups = x_train.groupby("unit_nr")
    test_groups = x_test.groupby("unit_nr")

    return train_groups, y_test, test_groups

def load_data_FD004():
    # Define the file path and column names
    path = "Data/Cmaps_Data/"
    columns = ["unit_nr", "time_cycles", "setting_1", "setting_2", "setting_3"]
    # Only 21 sensor readings are available
    columns += ["s_{i}" for i in range(1, 22)]

    # Load the data
    x_train = pd.read_csv(path + "train_FD004.txt", delim_whitespace=True, header=None, names=columns)
    x_test = pd.read_csv(path + "test_FD004.txt", delim_whitespace=True, header=None, names=columns)
    y_test = pd.read_csv(path + "RUL_FD004.txt", delim_whitespace=True, header=None, names=["RUL"])

    # # Remove non-informative sensory readings and settings from the data
    # drop_cols = ["setting_1", "setting_2", "setting_3", "s_1", "s_5", "s_16", "s_18", "s_19"]
    # x_train = x_train.drop(drop_cols, axis=1)
    # x_test = x_test.drop(drop_cols, axis=1)

    # Compute the remaining useful life for the training data
    x_train = add_rul(x_train)

    # Clip the maximum RUL to 125, as mentioned in the paper
    x_train["RUL"] = x_train["RUL"].clip(upper=125)

    # Normalize the sensor data
    x_train = normalize_data(x_train)
    x_test = normalize_data(x_test)

    # Group the data by unit number
    train_groups = x_train.groupby("unit_nr")
    test_groups = x_test.groupby("unit_nr")

    return train_groups, y_test, test_groups