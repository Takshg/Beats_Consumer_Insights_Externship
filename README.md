# Consumer Insights Data Analytics Externship of Beats by Dre

This repository showcases my capstone project analyzing consumer sentiment for Beats by Dre Extenship. The project focuses on extracting insights from Amazon product reviews to understand customer preferences, pain points, and satisfaction levels.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Dataset](#dataset)
5. [Key Findings](#key-findings)
6. [Usage Instructions](#usage-instructions)
7. [Dependencies](#dependencies)
8. [Disclaimer](#disclaimer)

---

## Introduction
In the fast-paced tech industry, understanding consumer sentiment is critical for maintaining market leadership. This project provides an in-depth analysis of consumer reviews for Beats by Dre headphones, utilizing both quantitative and qualitative methods to extract actionable insights.

### Objectives:
- Identify trends in customer satisfaction.
- Perform sentiment analysis on review content.
- Provide strategic recommendations for improving products and marketing strategies.

---

## Project Structure
The repository is organized as follows:

```
Beats_Consumer_Insights/
├── data/                   # Raw and mock datasets
├── notebooks/              # Jupyter notebooks for EDA and analysis
├── src/                    # Python scripts for data cleaning and processing
├── README.md               # Project overview and usage instructions
├── requirements.txt        # Python dependencies
└── LICENSE                 # License information
```

---

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/<takshg>/Beats_Consumer_Insights_Externship.git
cd Beats_Consumer_Insights_Externship
```

### Install Dependencies
Install required Python libraries using:
```bash
pip install -r requirements.txt
```

---

## Dataset

Due to privacy and ethical considerations, the original dataset cannot be shared. A **mock dataset** (`data/mock_dataset.csv`) is provided for demonstration purposes. This dataset mimics the structure of the original data while using synthetic values.

### Mock Dataset Structure
| Column Name       | Description                                   |
|-------------------|-----------------------------------------------|
| `review_id`       | Unique identifier for each review            |
| `product_id`      | Unique identifier for each product           |
| `title`           | Review title                                |
| `author`          | Reviewer's name                             |
| `rating`          | Rating given to the product (1-5)           |
| `content`         | Review content                              |
| `timestamp`       | Date of the review                          |
| `is_verified`     | Whether the purchase was verified           |
| `helpful_count`   | Number of helpful votes                     |
| `product_attributes` | Product attributes (e.g., color, style)   |


---

## Key Findings
- **High Customer Satisfaction:** Most reviews have a 4 or 5-star rating.
- **Common Themes:** Customers appreciate sound quality but highlight occasional discomfort and battery life issues.
- **Sentiment Scores:** Sentiment analysis shows a strong positive trend across most reviews.

---

## Usage Instructions

### Run Data Preprocessing
Use the `data_cleaning.py` script to understand the preprocessing tasks used for the dataset:
```bash
python src/data_cleaning.py
```
Note: The steps in the script applies to the real dataset and will not work on the mock dataset. If you are interested in collecting Amazon reviews of your own using the OXYLabs API, you can use the 'JSON_reviews_to_dataframe.ipynb' file to convert the collected reviews to a dataframe in a similar format to mine  

```bash
jupyter data/JSON_reviews_to_dataframe.ipynb
```

### Perform Sentiment Analysis
Run the sentiment analysis script to view generated insights:
```bash
python src/sentiment_analysis.py
```

### Generate Visualizations
Jupyter notebooks in the `notebooks/` folder contain all exploratory data analysis (EDA) and visualizations. Open them using:
```bash
jupyter notebooks/eda_and_visualization.ipynb
```

---

## Dependencies
The project requires the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn
- nltk
- textblob

Install them using:
```bash
pip install -r requirements.txt
```

---

## Disclaimer
> **Disclaimer**: The dataset included in this repository is synthetic and intended for demonstration purposes only. The original dataset is not shared to maintain privacy and ethical standards. If replicating this project, ensure compliance with all relevant data usage guidelines.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Beats by Dre for inspiring the project concept.
- Amazon reviews for the structure of consumer feedback.
- [Oxylabs](https://oxylabs.io/) API for enabling efficient data collection in the original project.
