import pandas as pd

def delay_analysys(f):
    df = pd.read_csv(f)
    df_nyc = df[df['origin'].isin(['JFK', 'LGA', 'EWR'])]

    top_10_dest = df_nyc['dest'].value_counts().nlargest(10).index.tolist()
    df_top_10 = df_nyc[df_nyc['dest'].isin(top_10_dest)]

    res = []
    for dest in top_10_dest:
      df_dest = df_top_10[df_top_10['dest'] == dest]
      total = len(df_dest)
      delayed = len(df_dest[df_dest['arr_delay'] > 0])
      if total > 0:
        delay_probability = delayed / total
      else:
          delay_probability = 0
      res.append({'Аэропорт': dest, 'Вероятность задержки': delay_probability, 'Всего рейсов': total})

    df_res = pd.DataFrame(res)
    df_res = df_res.sort_values(by='Вероятность задержки', ascending=False)

    the_worst = df_res.iloc[0]['Аэропорт']
    the_best = df_res.iloc[-1]['Аэропорт']

    return df_res, the_worst, the_best



f = 'flights_new.csv'
res, max, min = delay_analysys(f)
if res is not None:
  print("Результаты анализа задержек рейсов:")
  print(res)
  print(f"\nАэропорт с наибольшей вероятностью задержки: {max}")
  print(f"Аэропорт с наименьшей вероятностью задержки: {min}")
