import numpy as np
import pandas as pd
from sklearn import preprocessing


class Calculate:
    def __init__(self, percentage):
        self.percentage = percentage

    def main(self):
        data = pd.read_csv('df_test_new.csv')
        weights = pd.read_csv('weights_new.csv')

        new_weights = self.update_weights(np.array(weights['Coefficient'][0:39]), self.percentage)

        mult_data = pd.DataFrame(np.asarray(data) * new_weights).T

        next_pred = np.around(np.asarray(mult_data.sum(axis=0) + 87.06051603423542), decimals=2)

        concat_data = pd.concat([mult_data, weights.iloc[0:39, 0:3]], axis=1)
        trans_data = concat_data.groupby(['Axis']).sum().T

        p_p = self.processing(trans_data)

        result = []
        for i in range(0, 148):  # create multiple dictionaries
            result.append({})
        for k, j in enumerate(result):
            j.update({"X": p_p['Performance'].iloc[k]})
            j.update({"Y": p_p['Potential'].iloc[k]})
            j.update({"Brand_Name": weights['New Brand'].iloc[k]})
            j.update({"Sub_Cateogry": weights['Sub Category'].iloc[k]})
            j.update({"Age": int(weights['Age'].iloc[k])})
            j.update({"Price": weights['Price'].iloc[k]})
            j.update({"Next_Year_Price": weights['next_price'].iloc[k]})
            j.update({"Next_Year_Prediction": next_pred[k]})
            j.update({"Price_Growth_CAGR": weights['CAGR'].iloc[k]})

        return result

    def multiply(self, data, new_weights):
        mul_data = np.asarray(data) * new_weights
        mul_data_1 = pd.DataFrame(mul_data).T

        return mul_data_1

    def update_weights(self, weights, percentage):
        emp = []
        updated_weights = []

        emp.append((weights[0:1] * (1 + (int(self.percentage.get("Scarcity")) / 100))).tolist())
        emp.append((weights[1:2] * (1 + (int(self.percentage.get("Transacted_Price")) / 100))).tolist())
        emp.append((weights[2:4] * (1 + (int(self.percentage.get("Scarcity")) / 100))).tolist())
        emp.append((weights[4:6] * (1 + (int(self.percentage.get("Demand")) / 100))).tolist())
        emp.append((weights[6:18] * (1 + (int(self.percentage.get("Category_Outlook")) / 100))).tolist())
        emp.append((weights[18:39] * (1 + (int(self.percentage.get("Brand_Power")) / 100))).tolist())

        for i in range(len(emp)):
            for j in range(len(emp[i])):
                updated_weights.append(emp[i][j])
        return np.array(updated_weights)

    def processing(self, trans_data):
        min_max_scaler = preprocessing.MinMaxScaler()
        vz_minmax = min_max_scaler.fit_transform(trans_data)
        vz_data = pd.DataFrame(vz_minmax, columns=['Performance', 'Potential'])

        return vz_data
