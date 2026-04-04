# E-Commerce Transaction Analysis Revenue Insights

## 📌 Project Overview
This project performs an end-to-end Exploratory Data Analysis (EDA) on the **[UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)**. Containing over 500,000 real-world transactions from a UK-based online store, the dataset presents realistic challenges such as missing values, inconsistent data types, and cancelled orders. This project is from [Roadmap.sh](https://roadmap.sh/projects/ecommerce-data-analysis)

The primary goal of this analysis is to transform raw, noisy transactional data into actionable business insights, specifically focusing on revenue distribution across different geographic regions.

## 🛠️ Key Features & Workflow
* **Data Sampling:** Efficiently handled large-scale data by sampling 10% of the rows for manageable processing.
* **Robust Data Cleaning:** * Handled null values in critical columns.
    * Filtered out "Returns" (negative quantities) and "Free Items" (zero unit price).
    * Corrected data types for `InvoiceDate` and `CustomerID`.
* **Feature Engineering:** Derived a `Revenue` metric by calculating $Quantity \times UnitPrice$.
* **Geospatial Analysis:** Identified and visualized the **Top 10 Countries** by total revenue.
* **Automated Export:** The system automatically saves high-resolution visualizations (300 DPI) and summary CSVs for reporting.

## 📊 Visualizations
The analysis includes a categorical breakdown of revenue. Below is an example of the generated output:
![Top 10 Countries Revenue](https://github.com/nailatul-fadhilah-R/E-Commerce-Transaction-Analysis-Revenue-Insights/blob/main/top_10_countries_202604d_2254.png)
Based on the generated chart, we can draw the following conclusions:
- **Primary Market Dominance**: The United Kingdom stands as the overwhelming leader in total revenue. This indicates a highly centralized customer base and suggests that the company’s core operations are deeply rooted in the UK domestic market.
- **European Expansion**: Countries like Germany, France, and EIRE (Ireland) appear as the top international markets. This data suggests that these regions are prime candidates for localized marketing campaigns or even regional distribution centers to reduce shipping costs.
- **High-Value Segments**: Even with a 10% sample, the clear distinction between the top 3 and the remaining 7 countries suggests a "Pareto Principle" effect, where a small number of geographical segments drive the majority of the business's international growth.
  
## 🚀 Technologies Used
- **Language:** Python
- **Libraries:** Pandas (Data Manipulation), Matplotlib/Seaborn (Visualization), Openpyxl (Excel Engine), Logging/OS (roduction-grade system monitoring and file management)
- **Environment:** VSCode.
