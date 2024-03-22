import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import json
import os

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Initialize Streamlit app
img = Image.open('icon.png')
st.set_page_config(page_title="To-Do-List", page_icon=img)

# UI
st.title("***To-Do List Manager***")
col1, col2 = st.columns([6, 2])
cola, colb = col2.columns([3, 1])

with col1:
    st.subheader("Set and Complete your tasks by making a To-Do list !")

with cola:
    lottie_animation_2 = "https://assets10.lottiefiles.com/packages/lf20_z4cshyhf.json"
    lottie_anime_json2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json2, key="hello")

# Sidebar
st.sidebar.markdown("<h1 style='text-align: center; '>WELCOME! 👋</h1>", unsafe_allow_html=True)
st.sidebar.image("to_do_icon.jpg")

# Local Database
@st.cache(allow_output_mutation=True)
def get_local_data():
    return pd.DataFrame(columns=["Task", "Due date", "Completed"])

data = get_local_data()

# Functions for interacting with local data
def save_local_data():
    data.to_csv("local_data.csv", index=False)

def load_local_data():
    return pd.read_csv("local_data.csv") if "local_data.csv" in os.listdir() else pd.DataFrame(columns=["Task", "Due date", "Completed"])

# Add example to-do list tasks
example_tasks = [
    {"Task": "Start my business",
     "Subtasks": ["Develop business plan",
                   "Register business name",
                   "Secure funding",
                   "Hire employees",
                   "Set up legal structure",
                   "Create marketing strategy",
                   "Build website",
                   "Purchase necessary equipment",
                   "Launch product/service",
                   "Network with potential clients"]},
    {"Task": "Apply for a grant",
     "Subtasks": ["Research available grants",
                   "Check eligibility criteria",
                   "Gather required documents",
                   "Write grant proposal",
                   "Submit application",
                   "Follow up on application status",
                   "Attend interviews/presentations",
                   "Revise proposal if needed",
                   "Accept grant if awarded",
                   "Use grant funds as specified"]},
    {"Task": "Fix my credit",
     "Subtasks": ["Check credit report for errors",
                   "Dispute inaccuracies",
                   "Negotiate with creditors",
                   "Pay off outstanding debts",
                   "Set up automatic payments",
                   "Limit new credit applications",
                   "Increase credit limits",
                   "Diversify credit types",
                   "Keep credit utilization low",
                   "Monitor credit regularly"]},
    {"Task": "Market on social media",
     "Subtasks": ["Choose social media platforms",
                   "Create content calendar",
                   "Design engaging visuals",
                   "Schedule posts",
                   "Interact with followers",
                   "Run ad campaigns",
                   "Analyze engagement metrics",
                   "Collaborate with influencers",
                   "Respond to comments/messages",
                   "Adjust strategy based on performance"]},
    {"Task": "Daily habit tracker",
     "Subtasks": ["List habits to track",
                   "Set specific goals for each habit",
                   "Establish daily tracking routine",
                   "Record progress consistently",
                   "Review performance regularly",
                   "Adjust goals if needed",
                   "Reward yourself for progress",
                   "Share progress with accountability partner",
                   "Stay motivated with reminders",
                   "Celebrate milestones"]}
]

# Display tasks and subtasks
for task_data in example_tasks:
    st.subheader(task_data["Task"])
    subtasks = task_data["Subtasks"]
    for i, subtask in enumerate(subtasks, 1):
        st.write(f"{i}. {subtask}")

st.write("")
st.caption("Made with ❤️ by Ojas Mittal")
