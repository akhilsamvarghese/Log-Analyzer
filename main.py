import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page title
st.set_page_config(page_title="Interactive Line Graph Plotter", layout="wide")

# Title
st.title("Interactive Line Graph Plotter")

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

    # Select y-axes for multiple graphs
    y_axes = st.multiselect("Select Y-axes for graphs", options=columns)

    if y_axes:
        # Increase the height of each subplot to make graphs bigger
        graph_height = 900  # Increased value for larger graphs

        # Create subplots with shared x-axis but independent y-axes
        fig = make_subplots(
            rows=len(y_axes), 
            cols=1, 
            shared_xaxes=True, 
            vertical_spacing=0.1
        )

        # Add traces
        for i, y_axis in enumerate(y_axes, 1):
            fig.add_trace(
                go.Scatter(x=df[x_axis], y=df[y_axis], mode='lines', name=y_axis),
                row=i, col=1
            )

            # Uniform plotter: Independent scaling for each y-axis, common styling
            fig.update_yaxes(
                fixedrange=False, 
                title_text=y_axis, 
                row=i, col=1
            )

            # Display x-axis values on each subplot
            fig.update_xaxes(
                title_text=x_axis,
                showline=True,
                row=i, col=1
            )

        # Update layout
        fig.update_layout(
            height=graph_height*len(y_axes),  # Adjust total height based on number of graphs
            title_text="Interactive Line Graphs with Uniform Plotter and Visible X-Axis",
            showlegend=False,
            dragmode='zoom',
            hovermode='x unified'
        )

        # Display the figure with a larger container to accommodate bigger graphs
        st.plotly_chart(fig, use_container_width=True, height=graph_height*len(y_axes))

    else:
        st.write("Please select at least one Y-axis to display graphs.")

else:
    st.write("Please upload a CSV file to begin.")