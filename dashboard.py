import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. Load Data ---
# IMPORTANT: Replace this with the actual path to your cleaned CSV file.
# The previous code saved this file as 'merged_clean_bird_data.csv'.
try:
    df = pd.read_csv("merged_clean_bird_data.csv")
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error("Error: 'merged_clean_bird_data.csv' not found. Please ensure the file is in the same directory.")
    st.stop() # Stop the app if the file is not found

# --- 2. Dashboard Title and Introduction ---
st.set_page_config(layout="wide", page_title="Bird Species Observation Analysis Dashboard")
st.title("Bird Species Observation Analysis")
st.markdown("This dashboard provides an interactive exploration of bird species observations across different habitats and environmental conditions.")

st.sidebar.header("Filter Observations")

# --- 3. Sidebar Filters ---
# Create a list of unique values for filters, handling potential NaNs
habitat_options = ['All'] + sorted(df['habitat_type'].unique().tolist())
selected_habitat = st.sidebar.selectbox("Habitat Type:", habitat_options)

season_options = ['All'] + sorted(df['season'].unique().tolist())
selected_season = st.sidebar.selectbox("Season:", season_options)

species_options = ['All'] + sorted(df['common_name'].unique().tolist())
selected_species = st.sidebar.selectbox("Bird Species:", species_options)

# Filter the DataFrame based on the selected options
filtered_df = df.copy()
if selected_habitat != 'All':
    filtered_df = filtered_df[filtered_df['habitat_type'] == selected_habitat]
if selected_season != 'All':
    filtered_df = filtered_df[filtered_df['season'] == selected_season]
if selected_species != 'All':
    filtered_df = filtered_df[filtered_df['common_name'] == selected_species]

st.subheader(f"Analyzing {len(filtered_df)} Observations")

# --- 4. Key Metrics ---
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Observations", len(filtered_df))
with col2:
    st.metric("Unique Species Observed", filtered_df['common_name'].nunique())

st.markdown("---")

# --- 5. Visualizations Section ---
# Use Streamlit expanders to keep the dashboard organized and clean
with st.expander("Species & Habitat Distribution", expanded=True):
    st.subheader("Top 10 Most Observed Bird Species")
    if not filtered_df.empty:
        top_10_species = filtered_df['common_name'].value_counts().nlargest(10).index
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(y='common_name', data=filtered_df, order=top_10_species, palette="viridis", ax=ax)
        ax.set_xlabel("Observation Count")
        ax.set_ylabel("Bird Species")
        st.pyplot(fig)
    else:
        st.info("No data available for the selected filters.")

    st.subheader("Observations by Habitat Type")
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.countplot(x='habitat_type', data=filtered_df, palette="mako", ax=ax)
        ax.set_xlabel("Habitat Type")
        ax.set_ylabel("Number of Observations")
        st.pyplot(fig)
    else:
        st.info("No data available for the selected filters.")

with st.expander("Environmental Conditions", expanded=False):
    st.subheader("Temperature vs. Humidity by Season")
    if not filtered_df.empty and 'temperature' in filtered_df.columns and 'humidity' in filtered_df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(data=filtered_df, x="temperature", y="humidity", hue="season", alpha=0.7, palette="coolwarm", ax=ax)
        ax.set_title("Temperature vs. Humidity by Season")
        ax.set_xlabel("Temperature (°C)")
        ax.set_ylabel("Humidity (%)")
        st.pyplot(fig)
    else:
        st.info("No temperature or humidity data available for the selected filters.")

    st.subheader("Observations by Sky Condition")
    if not filtered_df.empty and 'sky' in filtered_df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x="sky", data=filtered_df, order=filtered_df["sky"].value_counts().index, palette="pastel", ax=ax)
        ax.set_title("Observations by Sky Condition")
        ax.set_xlabel("Sky Condition")
        ax.set_ylabel("Number of Observations")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("No sky condition data available for the selected filters.")

with st.expander("Behavioral & Observer Insights", expanded=False):
    st.subheader("Observation Counts by Identification Method")
    if not filtered_df.empty and 'id_method' in filtered_df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(x="id_method", data=filtered_df, order=filtered_df["id_method"].value_counts().index, ax=ax)
        ax.set_title("Observation Counts by Identification Method")
        ax.set_xlabel("Identification Method")
        ax.set_ylabel("Number of Observations")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("No identification method data available for the selected filters.")