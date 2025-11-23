
📦 data-science-imdb-project
├── 📁 data
│   ├── raw/                    # raw crawled data (imdb_movies_15000.csv)
│   ├── cleaned/                # cleaned_data.csv --> sau khi xu ly du lieu thieu
│   ├── processed/              # model-ready data (model_data.csv) --> train validation test 
│   └── About_data.md           # describe data formats
│
├── 📁 notebooks
│   ├── 01_data_collection.ipynb      # crawling, initial raw check
│   ├── 02_data_cleaning.ipynb        # cleaning, preprocessing
│   ├── 03_eda.ipynb                  # visualizations + insights
│   ├── 04_feature_engineering.ipynb  # encoding, transformation
│   ├── 051_modeling.ipynb            # ML models and evaluation (4 models)
│   └── 052_modeling.ipynb            # ML models and evaluation
│
├── 📁 src
│   ├── crawl_imdb.py           # main crawler script 
│   ├── data_cleaning.py        # reusable cleaning functions
│   ├── feature_engineering.py  # reusable feature processing
│   ├── modeling.py             # ML model training functions
│   └── utils.py                # helper functions
│
├── 📁 reports
│   ├── final_report.docx
│   ├── final_report.pdf
│
├── 📁 tests
│   ├── test_cleaning.py
│   ├── test_crawler.py
│   └── test_modeling.py
│
├── .gitignore
├── requirements.txt
├── LICENSE (optional)
└── README.md
