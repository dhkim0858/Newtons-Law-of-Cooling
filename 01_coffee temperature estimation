import numpy as np
import pandas as pd

Tenv = float(input('주위 온도: '))
T0 = float(input('초기 온도: '))
t = int(input('지난 시간(분): '))
Tt = float(input(str(t)+'분 지난 뒤의 온도: '))

k = np.log((T0-Tenv)/(Tt-Tenv))/t
print('k:', k)

time = np.arange(0, 81, 10)
estimation = Tenv + (T0 - Tenv) * (1/np.exp(k*time))
df = pd.DataFrame({'시간':time,'추정':estimation})
display(df)
