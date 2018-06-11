

def samp(firm):
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    #線形回帰分析ライブラリ読み込み
    from sklearn.linear_model import LinearRegression
    #ランダムフォレストライブラリ読み込み
    from sklearn.ensemble import RandomForestRegressor
    #グリッドサーチライブラリ読み込み
    from sklearn.model_selection import GridSearchCV
    #標準化ライブラリ読み込み
    from sklearn.preprocessing import StandardScaler
    #%matplotlib inline
    import datetime
    import pandas_datareader.data as web

    df_nikkei = web.DataReader(firm, "morningstar")
    df_nikkei.to_csv("softbank_stock.csv")

    f_s = pd.read_csv("softbank_stock.csv")

    y_train = f_s.loc[:, ['Close']]
    y_train = y_train.shift(-1)
    y_train = y_train.rename(columns={'Close': 'Close1'})
    y_train = y_train.iloc[0:len(y_train)]

    x_train = f_s.iloc[0:len(f_s)]

    df_s = pd.concat([x_train, y_train], axis=1)

    #df_xの欠損値のあるカラムを探し出す
    df_s = df_s.drop("Open", axis=1)
    df_s = df_s.drop("Symbol", axis=1)

    s = df_s['Date'].str.split('-', expand=True)
    df_s = pd.concat([df_s, s], axis=1)

    df_s = df_s.rename(columns={0: 'Year', 1: 'Month',2:'Day'})
    df_s = df_s.drop('Date', axis=1)

    df_s.astype(float)

    #分析手法選択
    clf =LinearRegression()

    df_test = df_s.iloc[len(df_s)-1:len(df_s)]
    df_test = df_test.drop('Close1', axis=1)

    df_x = df_s.loc[: , ['Close', 'High', 'Low', 'Volume', 'Year', 'Month', 'Day']]
    df_x = df_x.iloc[0:len(df_s)-1]

    df_y = df_s.loc[: , ['Close1']]
    df_y = df_y.iloc[0:len(df_s)-1]

    #モデル作成
    clf.fit(df_x,df_y)

    from sklearn.metrics import mean_squared_error
    def rmse(y_true, y_pred):
        return np.sqrt(mean_squared_error(y_true, y_pred))

    #訓練データの予測結果RMSE
    rmse(clf.predict(df_x),df_y)

    df_pre = clf.predict(df_x)

    df_pre = pd.DataFrame(df_pre)
    df_pre = df_pre.rename(columns={0: 'Predict'})

    df_s = pd.concat([df_s, df_pre], axis=1)

    y_pred = clf.predict(df_test)

    predict = y_pred[0]
    pre_day = df_s.loc[:, ['Year', 'Month', 'Day']]
    Year = pre_day.iloc[len(df_s)-1,0]
    Month = pre_day.iloc[len(df_s)-1,1]
    Day = pre_day.iloc[len(df_s)-1,2]
    #pre_day

    predict = predict*109.529025
    
    kekka = str(Year)+"/"+str(Month)+"/"+str(Day)+"の株価予想は"+str(predict)+"円"
    return kekka
