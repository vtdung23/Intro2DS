
# 🎬 DỰ ĐOÁN ĐIỂM ĐÁNH GIÁ PHIM TRÊN TMDB

## Đồ án môn học: Nhập môn Khoa học Dữ liệu (Introduction to Data Science)

---

## 📚 1. Giới thiệu nhóm

### 👨‍🏫 Giảng viên hướng dẫn

| STT | Họ và tên | Vai trò |
|-----|-----------|---------|
| 1 | **TS. Lê Ngọc Thành** | Giảng viên lý thuyết |
| 2 | **ThS. Lê Nhựt Nam** | Giảng viên hướng dẫn Lab |
| 3 | **ThS. Huỳnh Lâm Hải Đăng** | Giảng viên hướng dẫn Lab |

### 👥 Thành viên nhóm

| STT | Họ và tên | MSSV |
|-----|-----------|------|
| 1 | [Lê Minh Đức] | [23127351] |
| 2 | [Vũ Tiến Dũng] | [23127354] |
| 3 | [Nguyễn Văn Khánh] | [23127388] |
| 4 | [Nguyễn Đồng Thanh] | [23127538] |

---

## 🎯 2. Giới thiệu bài toán

### 2.1. Mô tả bài toán

**Dự đoán điểm đánh giá phim trên TMDB** là bài toán dự đoán **điểm đánh giá trung bình (vote_average)** của một bộ phim dựa trên các yếu tố có sẵn **trước khi sản xuất** như:

- Ngân sách (budget)
- Thể loại phim (genres)
- Đạo diễn (directors)
- Diễn viên (cast)
- Ngày phát hành (release_date)
- Các thông tin mô tả phim (overview, tagline, keywords)

### 2.2. Mục tiêu

- Xây dựng mô hình Machine Learning để dự đoán điểm rating của phim
- So sánh hiệu quả giữa các mô hình Linear và Tree-based
- Phân tích các yếu tố ảnh hưởng đến điểm rating

### 2.3. Ý nghĩa thực tiễn

- Hỗ trợ các nhà sản xuất phim đánh giá tiềm năng của dự án
- Giúp các nhà đầu tư ra quyết định tài trợ dự án phim
- Cung cấp insight về xu hướng và thị hiếu khán giả

---

## 📊 3. Giới thiệu dữ liệu

### 3.1. Nguồn dữ liệu

Dữ liệu được crawl từ **TMDB (The Movie Database)** API, bao gồm thông tin của hơn **10,000 phim** trong giai đoạn **2000-2025**.

### 3.2. Cấu trúc dữ liệu

```
data/
├── raw/                           # Dữ liệu thô thu thập từ API
│   ├── movies_2000_2015.csv       # Dữ liệu thô giai đoạn 2000-2015
│   ├── movies_2016_2025.csv       # Dữ liệu thô giai đoạn 2016-2025
│   └── raw_data.csv               # Dữ liệu gốc (~21 thuộc tính)
├── cleaned/                       # Dữ liệu đã làm sạch cơ bản
│   ├── data_da_resize.csv         # 10k records được chọn lọc
│   ├── preprocessed_data_v2.csv   # Dữ liệu chứa vote_average khác 0
│   ├── train_raw.csv              # Tập huấn luyện thô
│   └── test_raw.csv               # Tập kiểm tra thô
└── feature_engineering/           # Dữ liệu sau Feature Engineering
    ├── train_fe_data.csv          # Đặc trưng huấn luyện đã biến đổi
    └── test_fe_data.csv           # Đặc trưng kiểm tra đã biến đổi
```

### 3.3. Các thuộc tính chính

| STT | Thuộc tính | Mô tả | Kiểu dữ liệu |
|-----|-----------|-------|--------------|
| 1 | `budget` | Ngân sách sản xuất phim | Numerical |
| 2 | `revenue` | Doanh thu phim | Numerical |
| 3 | `runtime` | Thời lượng phim (phút) | Numerical |
| 4 | `popularity` | Độ phổ biến | Numerical |
| 5 | `vote_count` | Số lượt bình chọn | Numerical |
| 6 | `vote_average` | Điểm đánh giá trung bình (**Target**) | Numerical |
| 7 | `genres` | Thể loại phim | Categorical (Multi-label) |
| 8 | `directors` | Đạo diễn | Categorical |
| 9 | `cast_top5` | Top 5 diễn viên chính | Categorical (Multi-label) |
| 10 | `release_date` | Ngày phát hành | Datetime |
| 11 | `overview` | Mô tả nội dung phim | Text |
| 12 | `tagline` | Khẩu hiệu phim | Text |
| 13 | `keywords` | Từ khóa | Text |
| 14 | `production_companies` | Công ty sản xuất | Categorical |
| 15 | `production_countries` | Quốc gia sản xuất | Categorical |
| 16 | `original_language` | Ngôn ngữ gốc | Categorical |
| 17 | `certification_US` | Phân loại độ tuổi (US) | Ordinal |

---

## 📁 4. Cấu trúc thư mục dự án

```
📦 Intro2DS/
│
├── 📁 data/                              # Thư mục chứa dữ liệu
│   ├── raw/                              # Dữ liệu thô
│   │   ├── movies_2000_2015.csv
│   │   ├── movies_2016_2025.csv
│   │   └── raw_data.csv
│   ├── cleaned/                          # Dữ liệu đã làm sạch
│   │   ├── train_raw.csv
│   │   ├── test_raw.csv
│   │   ├── data_da_resize.csv
│   │   └── preprocessed_data_v2.csv
│   ├── feature_engineering/              # Dữ liệu sau FE
│   │   ├── train_fe_data.csv
│   │   ├── test_fe_data.csv
│   │   ├── fe_data.csv
│   │   ├── feature_importance.csv
│   │   └── selected_features.txt
│   ├── preprocessed_data/                # Dữ liệu theo giả thuyết
│   │   ├── X_train_H*.csv
│   │   ├── X_test_H*.csv
│   │   └── y_train_*.csv
│   └── About_data.md                     # Mô tả dữ liệu
│
├── 📁 notebooks/                         # Jupyter Notebooks
│   ├── 01_data_collection.ipynb          # Thu thập dữ liệu
│   ├── 02_data_cleaning.ipynb            # Làm sạch dữ liệu
│   ├── 03_eda.ipynb                      # Phân tích khám phá
│   ├── 04_feature_engineering_fully.ipynb # Feature Engineering
│   ├── 05_model_fully.ipynb              # Xây dựng mô hình
│   └── 06_optimize_model.ipynb           # Tối ưu mô hình
│
├── 📁 src/                               # Source code
│   ├── crawl_imdb.py                     # Script crawl dữ liệu
│   ├── data_cleaning.py                  # Hàm làm sạch dữ liệu
│   ├── feature_engineering.py            # Hàm xử lý đặc trưng
│   ├── modeling.py                       # Hàm huấn luyện mô hình
│   └── utils.py                          # Hàm tiện ích
│
├── requirements.txt                      # Thư viện cần thiết
└── README.md                             # Tài liệu dự án
```

---

## 🔍 5. Một số Insight từ EDA

### 5.1. Câu hỏi nghiên cứu

Trong quá trình EDA, nhóm đã đặt ra và trả lời 6 câu hỏi ý nghĩa:

1. **Xu hướng qua thời gian** của các features quan trọng (budget, revenue, runtime, vote_average)?
2. **Mối tương quan** giữa điểm rating và các trường khác?
3. **Thể loại phim phổ biến** qua các năm?
4. **Mối tương quan giữa các features** của top thể loại phổ biến?
5. **Rating vs Số phim của đạo diễn**: Có mối tương quan?
6. **ROI (Return on Investment)** ảnh hưởng thế nào đến Rating?

### 5.2. Kết quả phân tích

#### 📈 Phân phối dữ liệu số

| Feature | Phân phối | Xử lý đề xuất |
|---------|-----------|---------------|
| `budget`, `revenue` | Lệch phải (Right-skewed) | Log Transformation |
| `runtime` | Xấp xỉ chuẩn, có outlier | Box-Cox Transformation |
| `popularity` | Multimodal | Log Transformation |
| `vote_average` | Phân phối chuẩn | Không cần xử lý |

#### 🔗 Ma trận tương quan

- **Budget vs Revenue**: Tương quan cao (~0.7)
- **Vote_count vs Popularity**: Tương quan cao
- **Rating vs các biến khác**: Tương quan **thấp đến trung bình** → Mối quan hệ **phi tuyến**

#### 🎭 Thể loại phim phổ biến

**Top 5 thể loại qua các năm:**
1. Drama
2. Comedy
3. Horror
4. Documentary
5. Comedy, Drama (kết hợp)

#### 📊 Xu hướng theo thời gian

- **Budget**: Tăng dần theo thời gian (2000-2021)
- **Runtime**: Ổn định, trung bình ~100 phút
- **Vote_average**: Dao động trong khoảng 5.5-7.0

#### 🎬 Phân tích đạo diễn

- **R² = 0.003**: Không có mối tương quan giữa rating và số lượng phim của đạo diễn
- → Rating phụ thuộc vào nhiều yếu tố khác, không chỉ kinh nghiệm đạo diễn

#### 💰 ROI vs Rating

- **R² rất thấp**: ROI không ảnh hưởng trực tiếp đến Rating
- Phim có lợi nhuận cao không nhất thiết có điểm rating cao

---

## ⚙️ 6. Phương pháp Feature Engineering

### 6.1. Xử lý dữ liệu thời gian (Temporal Features)

**Kỹ thuật:**
- Tách năm, tháng, ngày, quý từ `release_date`
- Tạo feature `release_dayofweek`, `release_is_weekend`
- Tính `movie_age` = năm hiện tại - năm phát hành

### 6.2. Xử lý dữ liệu số (Numerical Transformation)

| Feature | Vấn đề | Kỹ thuật | Công thức |
|---------|--------|----------|-----------|
| `budget`, `revenue` | Phân phối lệch phải | Log Transformation | $x_{new} = \ln(x + 1)$ |
| `runtime` | Lệch phải, có outlier | Box-Cox Transformation | Tự động tìm λ tối ưu |
| `popularity` | Multimodal | Log Transformation | $x_{new} = \ln(x + 1)$ |

### 6.3. Xử lý dữ liệu phân loại (Categorical Encoding)

| Feature | Kỹ thuật | Mô tả |
|---------|----------|-------|
| `genres` | MultiLabelBinarizer | Tạo binary features cho mỗi thể loại + `num_genres` |
| `cast_top5` | Count Encoding | Đếm số lượng cast + `has_cast` binary |
| `directors` | Target Encoding + Smoothing | Encode theo mean revenue với smoothing |
| `certification_US` | Ordinal Encoding | G=1, PG=2, PG-13=3, R=4, NR=0 |
| `original_language` | One-Hot Encoding | Top 15 ngôn ngữ + `language_other` |
| `production_companies` | Smoothed Target Encoding | Encode theo mean revenue |
| `production_countries` | MultiLabelBinarizer | Top 20 quốc gia |

### 6.4. Tạo Feature mới (Feature Creation)

| Feature mới | Công thức | Ý nghĩa |
|-------------|-----------|---------|
| `roi` | revenue / (budget + 1) | Tỷ suất lợi nhuận |
| `profit` | revenue - budget | Lợi nhuận tuyệt đối |
| `budget_revenue_ratio` | budget / (revenue + 1) | Tỷ lệ ngân sách/doanh thu |
| `vote_per_popularity` | vote_count / (popularity + 1) | Tỷ lệ vote/độ phổ biến |
| `revenue_per_runtime` | revenue / (runtime + 1) | Hiệu quả doanh thu/phút |

### 6.5. Xử lý dữ liệu Text (Text Feature Extraction)

| Text Column | Kỹ thuật | Số features |
|-------------|----------|-------------|
| `overview` + `tagline` | TF-IDF + Truncated SVD | 5000 → 200 features |
| `keywords` | TF-IDF + Truncated SVD | 1000 → 100 features |
| `title` | TF-IDF + Truncated SVD | 500 → 50 features |

**Tổng số features sau Feature Engineering: ~400+ features**

---

## 🤖 7. Tóm tắt bước Modeling

### 7.1. Các giả thuyết kiểm chứng

| # | Giả thuyết | Kết quả |
|---|------------|---------|
| H1 | Mối quan hệ rating và numerical features là **phi tuyến** | ✅ Xác nhận |
| H2 | Text features ảnh hưởng đến rating | ✅ Xác nhận |
| H3 | Temporal features ảnh hưởng đến rating | ✅ Xác nhận |
| H4 | Categorical features có thể giảm chiều | ✅ Xác nhận |
| H5 | Có features ảnh hưởng lẫn nhau, có thể loại bỏ | ✅ Xác nhận |
| H6 | Tree-based models tốt hơn Linear models | ✅ Xác nhận |

### 7.2. Phương pháp phân tích

#### 🔍 Phân tích tương quan (Correlation Analysis)

So sánh **Pearson** (linear) vs **Spearman** (non-linear):
- Spearman > Pearson cho hầu hết features → **Mối quan hệ phi tuyến**

#### 📊 So sánh mô hình

| Model | Loại | Test R² | Test RMSE | Ghi chú |
|-------|------|---------|-----------|---------|
| Linear Regression | Linear | Thấp | Cao | Baseline |
| SVM (Linear Kernel) | Linear | Thấp | Cao | |
| Random Forest | Tree-based | **Cao hơn** | **Thấp hơn** | Tốt |
| XGBoost | Tree-based | **Cao nhất** | **Thấp nhất** | **Best** |

### 7.3. Kiểm định thống kê

**Paired t-test** được sử dụng để so sánh performance:
- Linear Regression vs Random Forest: **p < 0.05** → RF tốt hơn có ý nghĩa thống kê
- Linear Regression vs XGBoost: **p < 0.05** → XGBoost tốt hơn có ý nghĩa thống kê

### 7.4. Ablation Study

Kiểm tra ảnh hưởng của từng nhóm features:

| Thí nghiệm | Kết quả |
|------------|---------|
| Model với Text Features vs không | Text features cải thiện R² |
| Model với Temporal Features vs không | Temporal features có ảnh hưởng |
| Model với tất cả Categorical vs Selected | Có thể giảm chiều mà không mất performance |

### 7.5. Kết luận Modeling

1. **Tree-based models** (Random Forest, XGBoost) **tốt hơn** Linear models cho bài toán này
2. **XGBoost** cho kết quả **tốt nhất**
3. **Mối quan hệ phi tuyến** giữa features và target được xác nhận
4. Có thể **giảm chiều features** mà không làm giảm đáng kể performance
5. **Text features** (từ TF-IDF + SVD) có đóng góp vào việc dự đoán

---

## 🚀 Hướng dẫn chạy dự án

### Yêu cầu hệ thống

```bash
Python >= 3.8
```

### Cài đặt

```bash
# Clone repository
git clone <repository-url>
cd Intro2DS

# Cài đặt thư viện
pip install -r requirements.txt
```

### Chạy notebooks

1. **Data Collection**: `notebooks/01_data_collection.ipynb`
2. **Data Cleaning**: `notebooks/02_data_cleaning.ipynb`
3. **EDA**: `notebooks/03_eda.ipynb`
4. **Feature Engineering**: `notebooks/04_feature_engineering_fully.ipynb`
5. **Modeling**: `notebooks/05_model_fully.ipynb`
6. **Optimization**: `notebooks/06_optimize_model.ipynb`

---

## 📚 Tài liệu tham khảo

1. TMDB API Documentation: https://developer.themoviedb.org/docs
2. Scikit-learn Documentation: https://scikit-learn.org/
3. XGBoost Documentation: https://xgboost.readthedocs.io/

---

## 📝 License

Dự án này được phát triển cho mục đích học tập trong khuôn khổ môn học **Nhập môn Khoa học Dữ liệu**.

---

*Cập nhật lần cuối: Tháng 1, 2026*
