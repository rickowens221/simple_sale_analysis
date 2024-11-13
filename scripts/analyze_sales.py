import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath):
    """Загрузка данных из CSV файла."""
    try:
        data = pd.read_csv(filepath, parse_dates=['Date'])
        print("Данные успешно загружены.")
        return data
    except FileNotFoundError:
        print(f"Файл {filepath} не найден.")
        return None
    
def clean_data(data):
    initial_shape = data.shape
    data.dropna(inplace=True)
    final_shape = data.shape
    print(f"Удалено {initial_shape[0] - final_shape[0]} строк с пропущенными значениями.")
    return data

def analyze_sales_by_region(data):
    """Анализ продаж по регионам."""
    sales_region = data.groupby('Region')['Total Revenue'].sum().reset_index()
    print("Продажи по регионам:")
    print(sales_region)
    return sales_region

def plot_sales_by_region(sales_region):
    """Визуализация продаж по регионам."""
    plt.figure(figsize=(10,6))
    sns.barplot(x='Region', y='Total Revenue', data=sales_region, palette='viridis')
    plt.title('Общие Продажи по Регионам')
    plt.xlabel('Регион')
    plt.ylabel('Общий Доход')
    plt.tight_layout()
    plt.savefig('../plots/sales_by_region.png')
    plt.show()

def analyze_sales_trend(data):
    """Анализ трендов продаж по времени."""
    sales_trend = data.groupby('Date')['Total Revenue'].sum().reset_index()
    print("Тренды продаж по датам:")
    print(sales_trend.tail())
    return sales_trend

def plot_sales_trend(sales_trend):
    """Визуализация трендов продаж по времени."""
    plt.figure(figsize=(12,6))
    sns.lineplot(x='Date', y='Total Revenue', data=sales_trend, marker='o')
    plt.title('Тренды Продаж по Времени')
    plt.xlabel('Дата')
    plt.ylabel('Общий Доход')
    plt.tight_layout()
    plt.savefig('../plots/sales_trend.png')
    plt.show()

def main():
    # Убедитесь, что директория для графиков существует
    os.makedirs('../plots', exist_ok=True)

    # Загрузка и очистка данных
    data = load_data('E:\\apicore\\simple_sales_analysis\\data\\sales_data.csv')
    if data is None:
        return
    data = clean_data(data)

    # Анализ продаж по регионам
    sales_region = analyze_sales_by_region(data)
    plot_sales_by_region(sales_region)

    # Анализ трендов продаж по времени
    sales_trend = analyze_sales_trend(data)
    plot_sales_trend(sales_trend)

if __name__ == "__main__":
    main()