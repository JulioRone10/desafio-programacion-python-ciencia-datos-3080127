import pandas as pd
file = pd.read_csv('empleados.csv', delimiter=";")

print(file.shape)
NaN = file.isnull().sum()
print(NaN)

NNan = file.notnull().sum()
printe(NNaN)

}
