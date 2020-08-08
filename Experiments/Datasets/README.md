Datasets
===
For the following experiments, two datasets (directory data) covering two classes of datasets were selected – consistent and inconsistent. The first dataset (see Section 3.1.1 about Consistent dataset - Macy’s (e-commerce)) represents a class of datasets, where the values in a column are homogeneous (e.g. similar length of individual records, fewer missing records) and have a more transparent format. In contrast, the second dataset (see Section 3.1.2 about Inconsistent dataset - Open Food Facts) represents a class of inconsistent datasets whose values are mostly of different nature within a column (e.g. unclear formats, lengths of column values). To the best of my knowledge, there is no labelled dataset for data quality or data quality measurement. For this reason, both datasets were enriched with synthetic data quality issues within the domain context of the dataset and data quality labels for experimental purposes (directory notebooks).

Consistent dataset - Macy’s (e-commerce)
---

* https://www.kaggle.com/PromptCloudHQ/innerwear-data-from-victorias-secret-and-others?select=macys_com.csv
* Macy’s dataset was found on the Kaggle datasets repository. Macy’s is an American department store selling products such as clothing, footwear or accessories. The dataset contains innerwear and swimwear products. The dataset has 40897 records and 14 columns (e.g. product_name, price, pdp_url, brand_name, rating) in CSV format. More detailed information about the dataset can be found in Table 3.1 and in the Dataset Kaggle link. 

Inconsistent dataset - Open Food Facts
---

* https://documenter.getpostman.com/view/8470508/SVtN3Wzy?version=latest
* Open Food Facts is a free, open, collaborative project that gathers information and data on food products from around the world. The dataset contains information such as ingredients, allergens, nutrition facts and information that can be found on product labels. The dataset has 1356289 records and 181 columns (e.g. code, created_datetime, product_name, countries, additives, glucose_100g, sodium_100g, energy_100g) in TSV format. The dataset has a significant number of missing or inconsistent values, that is caused by the collaboration of users on the dataset. More detailed information about the dataset can be found in Table 3.1 and in the Open Food Facts data link. Information on the different fields for the CSV exports is available in the following link.