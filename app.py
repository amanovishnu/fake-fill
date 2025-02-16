import streamlit as st

# Define categories and options
categories = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Vegetables": ["Carrot", "Broccoli", "Spinach"],
    "Dairy": ["Milk", "Cheese", "Yogurt"]
}

# Flatten options with categories
options = []
for category, items in categories.items():
    options.append(f"🟢 {category} (category)")  # Category label (non-selectable)
    options.extend([f"↳ {item}" for item in items])  # Indented items

# Multi-select box
selected_items = st.multiselect("Select Items", options, [])

# Filter out category headers (only return actual items)
selected_actual_items = [item.replace("↳ ", "") for item in selected_items if "↳" in item]

st.write("You selected:", selected_actual_items)

import streamlit as st

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)