import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import time

from radar import radar_plot

plt.style.use("dark_background")
import random

# Create a sample list
values = [0, 0, 0, 0]
v1 = [values[0]]
v2 = [values[1]]
v3 = [values[2]]
v4 = [values[3]]


# Initialize lists for data
time_increment = 2  # Increment for time values
max_time_window = 25  # Maximum time window to display on the graph

from arduino import *
try:
    gas, temp, hum, tds, times ,radar_value = all_values()
except:
    gas = [0]
    temp = [0]
    hum = [0]
    tds = [0]
    times = [0]
    radar_value = [0, 0]
# gas, temp, hum, tds, times ,radar_value = all_values()


# Function to create gauge plots
def create_gauge(values, name, index, color, max_value=100):
    fig = go.Figure(
        data=[
            go.Indicator(
                mode="gauge+number",
                value=values[index],
                title={"text": name},
                gauge={
                    "axis": {"range": [0, max_value]},
                    "bar": {"color": color},
                    "threshold": None,
                },
            )
        ]
    )
    return fig

# Function to create line plots
def create_line_plot(times, values, name, colour):
    print(values, times, name)
    fig, ax = plt.subplots()
    ax.clear()
    ax.plot(times, values, label=name, color=colour)
    ax.set_title(name)
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")
    # ax.set_facecolor('black')
    ax.legend()
    if values:

        ax.annotate(
            f"{values[-1]}",
            (times[-1], values[-1]),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )
    ax.set_xlim(max(0, times[-1] - max_time_window), times[-1])
    return fig

def first_plot():
    global fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, chart1, chart2, chart3, chart4, line1, line2, line3, line4, col1, col2, col3, col4, col5, col6, col7, col8

    # # Create the gauge plots

    fig1 = create_gauge(gas, "GAS", -1, "red", 100)
    fig2 = create_gauge(hum, "Humidity", -1, "blue", 100)
    fig3 = create_gauge(temp, "Temperature", -1, "green", 100)
    fig4 = create_gauge(tds, "Water", -1, "yellow", 100)

    # # Create the line plots
    fig5 = create_line_plot(times, gas, "Gas", "red")
    fig6 = create_line_plot(times, hum, "Humidity", "blue")
    fig7 = create_line_plot(times, temp, "Temp", "green")
    fig8 = create_line_plot(times, tds, "Water", "yellow")

    # fig1 = create_gauge(values, "GAS", 0, 'red', 100)
    # fig2 = create_gauge(values, "Humidity", 1, 'blue', 100)
    # fig3 = create_gauge(values, "Temperature", 2, 'green', 100)
    # fig4 = create_gauge(values, "value4", 3, 'yellow', 100)

    # fig5 = create_line_plot(times,v1, "Gas", 'red')
    # fig6 = create_line_plot(times,v2, "Humidity", 'blue')
    # fig7 = create_line_plot(times,v3, "Temp", 'green')
    # fig8 = create_line_plot(times,v4, "value4", 'yellow')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        chart1 = st.plotly_chart(fig1, use_container_width=True)
    with col2:
        chart2 = st.plotly_chart(fig2, use_container_width=True)
    with col3:
        chart3 = st.plotly_chart(fig3, use_container_width=True)
    with col4:
        chart4 = st.plotly_chart(fig4, use_container_width=True)

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        line1 = st.pyplot(fig5)
    with col6:
        line2 = st.pyplot(fig6)
    with col7:
        line3 = st.pyplot(fig7)
    with col8:
        line4 = st.pyplot(fig8)

def ploting():
    global fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, chart1, chart2, chart3, chart4, line1, line2, line3, line4, col1, col2, col3, col4, col5, col6, col7, col8,gas,hum,temp,tds,times
    # # Create the gauge plots
    fig1 = create_gauge(gas, "GAS", -1, "red", 150)
    fig2 = create_gauge(hum, "Humidity", -1, "blue", 100)
    fig3 = create_gauge(temp, "Temperature", -1, "green", 100)
    fig4 = create_gauge(tds, "Water", -1, "yellow", 300)

    # # Create the line plots
    fig5 = create_line_plot(times, gas, "Gas", "red")
    fig6 = create_line_plot(times, hum, "Humidity", "blue")
    fig7 = create_line_plot(times, temp, "Temp", "green")
    fig8 = create_line_plot(times, tds, "Water", "yellow")

    # fig1 = create_gauge(values, "GAS", 0, 'red', 100)
    # fig2 = create_gauge(values, "Humidity", 1, 'blue', 100)
    # fig3 = create_gauge(values, "Temperature", 2, 'green', 100)
    # fig4 = create_gauge(values, "value4", 3, 'yellow', 100)

    # fig5 = create_line_plot(times,v1, "Gas", 'red')
    # fig6 = create_line_plot(times,v2, "Humidity", 'blue')
    # fig7 = create_line_plot(times,v3, "Temp", 'green')
    # fig8 = create_line_plot(times,v4, "value4", 'yellow')

    with col1:
        chart1.plotly_chart(fig1, use_container_width=True)
    with col2:
        chart2.plotly_chart(fig2, use_container_width=True)
    with col3:
        chart3.plotly_chart(fig3, use_container_width=True)
    with col4:
        chart4.plotly_chart(fig4, use_container_width=True)
    with col5:
        line1.pyplot(fig5)
    with col6:
        line2.pyplot(fig6)
    with col7:
        line3.pyplot(fig7)
    with col8:
        line4.pyplot(fig8)

    # values[0] += 1
    # values[1] += 2
    # values[2] += 3
    # values[3] += 4
    # v1.append((v1[-1])+ 1)
    # v2.append((v2[-1])+ 2)
    # v3.append((v3[-1])+ 3)
    # v4.append((v4[-1])+ 4)

    gas, temp, hum, tds, times ,_ = all_values()
    # arduino_data()


# st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
# st.set_page_config(layout="wide")
# Create the sidebar named "radar"
graphs_button = st.sidebar.button("Graphs", help="Gauge and Line Plots", use_container_width=True)
radar_button = st.sidebar.button("Radar", help="Radar System", use_container_width=True)
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
st.sidebar.text("")
rrr = 0
# For Laser Sidebar systemm
with st.sidebar:
    st.markdown(
        "<h2 style='text-align: center;font-size: 40px;'>Laser System</h2>",
        unsafe_allow_html=True,
    )
    status_laser = st.markdown(
        "<p style='text-align: center;font-size: 15px;'>Laser Status: <span id='laser-status' style='font-weight: bold;color: green;'>ON</span></p>",
        unsafe_allow_html=True,
    )
    laser_control(1)
    on, off = st.columns([1, 1])  # Adjust column widths as needed
    with on:
        if st.button("ON", use_container_width=True):
            laser_control(1)
            status_laser.markdown(
                "<p style='text-align: center;font-size: 15px;'>Laser Status: <span id='laser-status' style='font-weight: bold;color: green;'>ON</span></p>",
                unsafe_allow_html=True,
            )
            
    with off:
        if st.button("OFF", use_container_width=True):
            laser_control(0)
            status_laser.markdown(
                "<p style='text-align: center;font-size: 15px;'>Laser Status: <span id='laser-status' style='font-weight: bold;color: red;'>OFF</span></p>",
                unsafe_allow_html=True,
            )


with st.sidebar:
    st.markdown(
        "<h2 style='text-align: center;font-size: 40px;'>Gate System</h2>",
        unsafe_allow_html=True,
    )
    status_rfid = st.markdown(
        "<p style='text-align: center;font-size: 15px;'><span id='gate-status' style='font-weight: bold;color: green;'>    </span></p>",
        unsafe_allow_html=True,
    )

    while True:
        break

    if rrr == 1:
        status_rfid.markdown(
            "<p style='text-align: center;font-size: 15px;'><span id='gate-status' style='font-weight: bold;color: green;'>Authorised</span></p>",
            unsafe_allow_html=True,
        )
        time.sleep(3)
        rrr = 0
        status_rfid.markdown(
            "<p style='text-align: center;font-size: 15px;'><span id='gate-status' style='font-weight: bold;color: green;'>    </span></p>",
            unsafe_allow_html=True,
        )
    elif rrr == 2:
        status_rfid.markdown(
            "<p style='text-align: center;font-size: 15px;'><span id='gate-status' style='font-weight: bold;color: red;'>Unauthorized</span></p>",
            unsafe_allow_html=True,
        )
        time.sleep(3)
        rrr = 0
        status_rfid.markdown(
            "<p style='text-align: center;font-size: 15px;'><span id='gate-status' style='font-weight: bold;color: green;'>    </span></p>",
            unsafe_allow_html=True,
        )
    rfid_system = st.button("Manual Open", help="5s opening", use_container_width=True)
    if rfid_system:
        laser_control(2)

# import threading

# thread = threading.Thread(target=auth)
# thread.daemon = True  # Allow thread to exit when main program exits
# thread.start()
# authorized = st.empty()
# if auth() == "Authorized access":
#     authorized.markdown(
#         "<h2 style='text-align: center;font-size: 40px;'>Authorized</h2>",
#         unsafe_allow_html=True,
#     )
# elif auth() == "Access denied":
#     authorized.markdown(
#         "<h2 style='text-align: center;font-size: 40px;'>Access denied</h2>",
#         unsafe_allow_html=True,
#     )
# else:
#     authorized.markdown(
#         "<h2 style='text-align: center;font-size: 40px;'>--</h2>",
#         unsafe_allow_html=True,
#     )



flag = 0
if graphs_button:
    st.title("Gauge Plots")
    # st.write("This app updates gauge plots every second.")
    first_plot()
    while True:
        ploting()
        # time.sleep(0.1)
if radar_button:
    # st.title("RADAR")
    st.title("                                                     ")
    st.title("                                                     ")
    st.title("                                                     ")
    st.title("                                                     ")
    st.title("                                                     ")
    radar_plot()
   
