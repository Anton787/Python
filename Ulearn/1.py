import pandas as pd

df1 = pd.read_csv('student_works/currency.csv')
df2 = pd.read_csv('student_works/correct_result.csv')

if df1.equals(df2):
    print("Содержимое файлов идентично.")
else:
    print("Содержимое файлов различается.")
    # Покажем различия между двумя DataFrame
    differences = df1.compare(df2)
    print("Различия между файлами:")
    print(differences)
