

# Log Analyzer

**Log Analyzer** is a Streamlit application designed to visualize CSV data with flexible plotting options. It allows users to analyze log data by plotting selected Y-axes against an X-axis either in a combined graph or as separate subplots.

## Features

- **File Upload:** Load your CSV files directly into the application.
- **Data Preview:** View a preview of the uploaded data to confirm it's loaded correctly.
- **Flexible Plotting:**
  - **Combined Plot:** Plot all selected Y-axes against the chosen X-axis on a single graph.
  - **Separate Subplots:** Create separate subplots for each selected Y-axis, all sharing the same X-axis.
- **Interactive Graphs:** Use Plotly for interactive and dynamic visualizations.

## Installation

To run the Log Analyzer locally, you need Python and the required packages. Follow these steps to set up your environment:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages:**

   ```bash
   pip install streamlit pandas plotly
   ```

4. **Run the application:**

   ```bash
   streamlit run main.py
   ```

   Replace `app.py` with the name of your Python script if it's different.

## Usage

1. **Upload a CSV File:**
   - Click on the file uploader to choose a CSV file from your local system.

2. **Select X-axis:**
   - Choose the column to be used as the X-axis.

3. **Select Y-axes:**
   - Select one or more columns to be used as Y-axes for plotting.

4. **Choose Plot Type:**
   - **Combined Plot:** All selected Y-axes will be plotted on a single graph.
   - **Separate Subplots:** Each selected Y-axis will be plotted in its own subplot, sharing the same X-axis.

5. **View and Interact with Plots:**
   - The application will display the plots according to your selections. Interact with the graphs to explore the data.


## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.



## Contact

For any questions or feedback, please contact:

- **Name:** Akhil Sam Varghese
- **Email:** akhilsam.v@gmail.com
- **GitHub:** [github.com/akhilsamvarghese](https://github.com/akhilsamvarghese)
