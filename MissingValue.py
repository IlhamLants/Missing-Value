import pandas as pd

# untuk membaca file dalam format csv
cd = pd.read_csv('shopping_data_missingvalue.csv')
print('Isi dari shopping_data_missingvalue.csv')

# untuk mengecek null yang ada pada setiap kolom
# column_null = cd.isnull()
# print(column_null.sum())

# untuk mengisikan null yang ada pada kolom 'Age'
rata_umur = cd['Age'].mean()
cd['Age'] = cd['Age'].fillna(rata_umur)

# untuk mengisikan null yang ada pada kolom 'Annual Income (k$)'
income = cd['Annual Income (k$)'].mean()
cd['Annual Income (k$)'] = cd['Annual Income (k$)'].fillna(income)

# untuk mengisikan null yang ada pada kolom 'Spending Score (1-100)'
rata_umur = cd['Spending Score (1-100)'].median()
cd['Spending Score (1-100)'] = cd['Spending Score (1-100)'].fillna(rata_umur)

# untuk memanggil variable cd
print(cd)