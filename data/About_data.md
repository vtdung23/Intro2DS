data/
├── raw/                           # Dữ liệu thô thu thập từ API
    ├── movies_2000_2015.csv       # Dữ liệu thô Dũng thu thập
    ├── movies_2016_2025.csv       # Dữ liệu thô Khánh thu thập
│   └── raw_data.csv               # Dữ liệu gốc crawl từ TmDB (với ~21 thuộc tính)
├── cleaned/                       # Dữ liệu đã làm sạch cơ bản
    ├── data_da_resize.csv         # 10k records được chọn lọc
    ├── preprocessed_data_v2.csv   # Dữ liệu chứa vote_average khác 0
│   ├── train_raw.csv              # Tập huấn luyện thô (đã điền giá trị thiếu)
│   └── test_raw.csv               # Tập kiểm tra thô (đã điền giá trị thiếu)
└── preprocessed/                  # Dữ liệu sau Feature Engineering
    ├── X_train_fe.csv             # Đặc trưng huấn luyện đã biến đổi theo giả thuyết
    ├── y_train_fe.csv             # Biến mục tiêu tập huấn luyện
    ├── X_test_fe.csv              # Đặc trưng kiểm tra đã biến đổi theo giả thuyết
    └── y_test_fe.csv              # Biến mục tiêu tập kiểm tra