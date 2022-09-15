import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"inputs_2016-2021_with_gas_relevant.csv")

plt.plot(data['Gas'])

plt.show()