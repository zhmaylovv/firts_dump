import pandas as pd
    data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
        index = ['Первый', "Второй", "Третий", "Четвёртый"])


        data.loc[["Первый", "Третий"]]
        data.iloc[[0, 2]]
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

pd.read_csv('Полный_путь_к_файлу/название_файла.csv')
            '''
            sep — разделитель данных, по умолчанию ',' ;
            decimal — разделитель числа на целую и дробную часть, по умолчанию '.' ;
            names — список с названиями колонок, необязательный параметр;
            skiprows — если файл содержит системную информацию, можно её пропустить, необязательный параметр.
            '''
#Строчкой ниже мы выводим первые 5 строк DataFrame:
    display(football.head())
#А здесь — последние 7 строк:
    display(football.tail(7))
    display(football.info())
Метод .describe() показывает основные статистические характеристики данных по каждому числовому признаку.
.max()
.min()
.mean()
.sum()
.count()
.std() стандартное отклонение

Например, хотим определить всех футболистов старше 20 лет:

  football[football.Age > 20]

Группировка
s = df['Nationality'].value_counts() #(normalize=True) проценты
                                    #bins=4 для числе разбивает на 4 равных диапазона

df['Nationality'].unique()
df['Nationality'].nunique()

#Иногда бывает полезно преобразовать серию, получившуюся в
 #результате работы функции valuecounts, в датафрейм.
 #Для этого нужно к получившейся серии применить функцию resetindex:

s = small_df['Nationality'].value_counts()
s_df = s.reset_index()
#ФУНКЦИЯ GROUPBY группировка
 grouped_df = df.groupby(['Club'])['Wage'].sum()

pivot = df.loc[df['Club'].isin(['FC Barcelona','Real Madrid','Juventus','Manchester United'])].pivot_table(values=['Wage'],

                index=['Nationality'],  columns=['Club'], aggfunc='sum')
Для того, чтобы заменить NaN на 0, можно применить дополнительный параметр fill_value.
movies.isna()
ratings['rating'].fillna(0)
###############################################################################
joined = ratings.merge(movies, on='movieId', how='left')
movies.drop_duplicates(subset = 'movieId', keep = 'first', inplace = True)

ratings.query('rating>4')
joined.query('rating>4 & genres in ["Comedy","Action", "Mystery"]')
new_movies = movies[movies.genres.str.contains ("Comedy")] #str.match ("abc")
##############################################################################
df.plot()
import matplotlib.pyplot as plt
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])
axes.scatter(x = df['total_bill'], y = df['tip'], marker = 'o')
axes.hist(df['total_bill'])
axes.set_title('Общая сумма счета')
axes.set_ylabel('Количество заказов')
axes.set_xlabel('Сумма заказа, USD')
axes.legend(loc = 1)
axes.bar(x = tips.index, label = 'Средняя сумма чаевых')
axes.set_ylim(0, 60)


###################NUMPY###############
import numpy as np
a = np.array([10, 8, 5, 1])
b = np.array([5, 15, 9, 7])
print(a+b)
print(a*2)
A = np.matrix("1,-5;2,2;0,3")
B = np.matrix("3,-1;2,6;4,0")
print(A+B)
print(A.T) - транспорирование матрицы - строки в столбцы
abs()sum()prod(имя, ось)sqrt()modf()isnan()
среднее арифметическое (mean), медиана (median), стандартное отклонение (std), корреляция (corrcoef)
###############################################
Дисперсия — сумма квадратов отклонений, деленная на их количество:
стандартное отклонение - корень из дисперсии
