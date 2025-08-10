# Bird Species Observation Analysis

## Project Overview

This project focuses on analyzing the distribution and diversity of bird species in distinct ecosystems, namely forests and grasslands. The primary goal is to understand how environmental factors—such as vegetation type, climate, and terrain—influence bird populations and their behaviors. By analyzing provided observational data, the project aims to identify patterns of habitat preference and provide valuable insights for habitat conservation, biodiversity management, and ecological policy support.

---

## Key Features and Analysis

The project includes a comprehensive data analysis and visualization pipeline:

- **Data Cleaning & Preprocessing:**  
  Handling missing values, standardizing data, and consolidating data from multiple Excel sheets representing different administrative units.

- **Exploratory Data Analysis (EDA):**  
  Studying species distribution, observation frequency over time (temporal analysis), and relationships between environmental conditions and bird activity.

- **Species and Behavioral Analysis:**  
  Analyzing species diversity metrics, activity patterns, and the impact of environmental factors like temperature, humidity, and wind.

- **Observer Trends:**  
  Assessing potential observer bias and the effect of repeated visits on species counts.

- **Interactive Dashboard:**  
  A Streamlit dashboard created to visualize key findings with dynamic charts and filters.

---

## Technical Stack

- **Python:** The core programming language for the project.
- **pandas:** Data manipulation, cleaning, and preprocessing.
- **seaborn & matplotlib:** Statistical and interactive visualizations.
- **Streamlit:** Framework used to build the interactive web dashboard.

---

## Data

The project uses the **Bird_Observation_DataSet**, which contains observational data for bird species recorded across various forest and grassland sites. The data is spread across multiple sheets within Excel files, with each sheet corresponding to a specific administrative unit (e.g., ANTI, CATO, CHOH). Columns include location, observation methods, bird species, and environmental conditions.

---

## Project Deliverables

- **Cleaned Dataset:** A final preprocessed dataset ready for analysis.
- **Source Code:** A Python script (`dashboard.py`) containing all the data processing and visualization code.
- **Interactive Dashboard:** A Streamlit web application showcasing key insights with filters and charts.
- **Documentation:** A report explaining the approach, findings, and actionable insights.

---

## How to Run the Project

1. **Install required packages** if not already installed:

    ```bash
    pip install pandas seaborn matplotlib streamlit
    ```

2. **Place data files** (`Bird_Monitoring_Data_FOREST.XLSX` and `Bird_Monitoring_Data_GRASSLAND.XLSX`) and your `dashboard.py` script in the same directory.

3. **Open terminal or command prompt** in the project directory.

4. **Run the Streamlit dashboard:**

    ```bash
    streamlit run dashboard.py
    ```

This will launch the dashboard in your default web browser, allowing you to interact with visualizations and filters.

---

