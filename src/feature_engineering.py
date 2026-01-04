import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_categorical_distribution(df, column):
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def plot_numerical_distribution(df, column, bins=30):
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(12, 10))
    correlation_matrix = df.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplot(df, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)
    plt.show()

def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.title(f'Scatter Plot of {y_column} vs {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_missing_values(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    missing_values.sort_values(inplace=True)

    plt.figure(figsize=(10, 6))
    missing_values.plot.bar()
    plt.title('Missing Values in Each Column')
    plt.xlabel('Columns')
    plt.ylabel('Number of Missing Values')
    plt.show()


def plot_trend_line(df, x_column, y_column):
    """
    Vẽ line plot đơn giản theo xu hướng tháng:
    - Chuyển thời gian về monthly bucket (năm-tháng).
    - Tổng hợp theo tháng: nếu y là 'budget' dùng sum, ngược lại dùng mean.
    - Thêm đường rolling mean (cửa sổ 12 tháng) để thể hiện trend.
    """
    dfx = df.copy()
    dfx[x_column] = pd.to_datetime(dfx[x_column], errors='coerce')
    dfx = dfx.dropna(subset=[x_column, y_column])

    dfx['year_month'] = dfx[x_column].dt.to_period('M').dt.to_timestamp()

    numerical_cols = ['budget', 'revenue', 'vote_average', 'vote_count', 'runtime', 'popularity']
    if y_column.lower() in numerical_cols:
        monthly_series = dfx.groupby('year_month')[y_column].sum().sort_index()
    else:
        monthly_series = dfx.groupby('year_month')[y_column].mean().sort_index()

    trend = monthly_series.rolling(window=12, min_periods=3).mean()

    # Vẽ
    plt.figure(figsize=(12, 5))
    plt.plot(monthly_series.index, monthly_series.values, alpha=0.4, label=y_column.capitalize())
    plt.plot(trend.index, trend.values, color='red', linewidth=2, label='Rolling mean')
    plt.title(f'Trend of {y_column}')
    plt.xlabel('Year-Month')
    plt.ylabel(y_column)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_trend_line_log(df, x_column, y_column):
    """
    Vẽ line plot theo xu hướng tháng với log scale:
    - Chuyển thời gian về monthly bucket (năm-tháng).
    - Tổng hợp theo tháng: nếu y là 'budget' dùng sum, ngược lại dùng mean.
    - Thêm đường rolling mean (cửa sổ 12 tháng) để thể hiện trend.
    - Y-axis dùng log scale với đơn vị gốc để dễ đọc.
    """
    dfx = df.copy()
    dfx[x_column] = pd.to_datetime(dfx[x_column], errors='coerce')
    dfx = dfx.dropna(subset=[x_column, y_column])    
    dfx['year_month'] = dfx[x_column].dt.to_period('M').dt.to_timestamp()

    numerical_cols = ['budget', 'revenue', 'vote_average', 'vote_count', 'runtime', 'popularity']
    if y_column.lower() in numerical_cols:
        monthly_series = dfx.groupby('year_month')[y_column].sum().sort_index()
    else:
        monthly_series = dfx.groupby('year_month')[y_column].mean().sort_index()
    
    full_date_range = pd.date_range(start=monthly_series.index.min(), 
                                     end=monthly_series.index.max(), 
                                     freq='MS')
    monthly_series = monthly_series.reindex(full_date_range, fill_value=0)
    
    # Với log scale: dùng giá trị nhỏ thay vì 0 để tính rolling mean tốt hơn
    # Tìm giá trị nhỏ nhất > 0 để làm baseline
    min_positive = monthly_series[monthly_series > 0].min()
    epsilon = min_positive / 10 if min_positive > 0 else 1
    monthly_series_for_trend = monthly_series.replace(0, epsilon) # Thay 0 bằng epsilon (rất nhỏ) thay vì NaN
    
    # Tính rolling mean trên log scale để mượt hơn
    log_series = np.log10(monthly_series_for_trend)
    log_trend = log_series.rolling(window=12, min_periods=3, center=True).mean()
    trend = 10 ** log_trend  # Chuyển về scale gốc
    
    # Chỉ vẽ những điểm > 0
    mask = monthly_series > 0
    monthly_series_plot = monthly_series[mask]
    trend_plot = trend[mask]

    # Vẽ
    plt.figure(figsize=(12, 5))
    plt.plot(monthly_series_plot.index, monthly_series_plot.values, alpha=0.4, label=y_column.capitalize())
    plt.plot(trend_plot.index, trend_plot.values, color='red', linewidth=2, label='Rolling mean (log scale)')
    
    # Dùng log scale cho trục y
    plt.yscale('log')
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:,.0f}'))
    
    plt.title(f'Trend of {y_column} (Log Scale)')
    plt.xlabel('Year-Month')
    plt.ylabel(y_column.capitalize())
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()
