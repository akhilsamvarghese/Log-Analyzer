# Importing Libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page title
st.set_page_config(page_title="Log Analyzer", layout="wide")

# Title
st.title("Log Analyzer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Display the dataframe
    st.write("Preview of the data:")
    st.write(df.head())

    # Get list of column names
    columns = df.columns.tolist()

    # Select x-axis
    x_axis = st.selectbox("Select X-axis", options=columns)

    # Select y-axes
    y_axes = st.multiselect("Select Y-axes to plot", options=columns)

    # Option to select the type of plot
    plot_type = st.radio(
        "Choose Plot Type",
        ('Combined Plot', 'Separate Subplots')
    )

    if y_axes:
        if plot_type == 'Combined Plot':
            # Create a figure for the combined plot
            fig = go.Figure()

            # Add a trace for each selected Y-axis
            for y_axis in y_axes:
                fig.add_trace(
                    go.Scatter(x=df[x_axis], y=df[y_axis], mode='lines', name=y_axis)
                )

            # Update layout
            fig.update_layout(
                title_text="Combined Plot of Selected Y-Axes against X-Axis",
                xaxis_title=x_axis,
                yaxis_title="Values",
                hovermode='x unified'
            )

        elif plot_type == 'Separate Subplots':
            # Create subplots with shared x-axis but independent y-axes
            fig = make_subplots(
                rows=len(y_axes), 
                cols=1, 
                shared_xaxes=True, 
                vertical_spacing=0.1
            )

            # Add traces for each selected Y-axis
            for i, y_axis in enumerate(y_axes, 1):
                fig.add_trace(
                    go.Scatter(x=df[x_axis], y=df[y_axis], mode='lines', name=y_axis),
                    row=i, col=1
                )

                # Update y-axis for each subplot with independent scaling
                fig.update_yaxes(title_text=y_axis, row=i, col=1, autorange=True)

            # Update layout
            fig.update_layout(
                height=400 * len(y_axes),  # Adjust height based on number of graphs
                title_text="Separate Graphs with Independent Y-Axis Scaling",
                showlegend=False,
                hovermode='x unified'
            )

        # Display the figure
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.write("Please select at least one Y-axis to plot.")

else:
    st.write("Please upload a CSV file to begin.")