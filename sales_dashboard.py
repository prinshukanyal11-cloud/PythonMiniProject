import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# -----------------------------
# 1️⃣ Window Setup
# -----------------------------
ctk.set_appearance_mode("dark")   # "light" or "dark"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("📊 Sales Dashboard")
root.geometry("1300x780")

# -----------------------------
# 2️⃣ Data Setup
# -----------------------------
months = np.array(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
electronics = np.random.randint(20000, 50000, size=12)
clothing = np.random.randint(15000, 40000, size=12)
furniture = np.random.randint(10000, 30000, size=12)

categories = ['Electronics', 'Clothing', 'Furniture']
avg_sales = [np.mean(electronics), np.mean(clothing), np.mean(furniture)]

regions = ['North', 'South', 'East', 'West']
region_sales = np.random.randint(60000, 120000, size=4)

genders = ['Male', 'Female', 'Other']
gender_sales = np.random.randint(40000, 90000, size=3)

total_by_category = [np.sum(electronics), np.sum(clothing), np.sum(furniture)]

# -----------------------------
# 3️⃣ Layout Frames
# -----------------------------
# Sidebar
sidebar = ctk.CTkFrame(root, width=220, corner_radius=0)
sidebar.pack(side="left", fill="y")

# Main chart area
main_frame = ctk.CTkFrame(root, corner_radius=20)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Chart display area
chart_container = ctk.CTkFrame(main_frame, corner_radius=15)
chart_container.pack(fill="both", expand=True, padx=10, pady=10)

# -----------------------------
# 4️⃣ Helper Functions
# -----------------------------
def clear_chart():
    for widget in chart_container.winfo_children():
        widget.destroy()

def fade_in(widget, steps=10, delay=0.03):
    for _ in range(steps):
        root.update()
        time.sleep(delay)

def show_chart(fig):
    clear_chart()
    canvas = FigureCanvasTkAgg(fig, master=chart_container)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    fade_in(chart_container)

# -----------------------------
# 5️⃣ Chart Functions
# -----------------------------
def show_sales_trend():
    plt.close('all')
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(months, electronics, marker='o', label='Electronics')
    ax.plot(months, clothing, marker='s', label='Clothing')
    ax.plot(months, furniture, marker='^', label='Furniture')
    ax.fill_between(months, electronics + clothing + furniture, color='lightblue', alpha=0.2)
    ax.set_title("Monthly Sales Trend", fontsize=13)
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales ($)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.7)
    show_chart(fig)

def show_category_sales():
    plt.close('all')
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(categories, avg_sales, color=['#3498db','#2ecc71','#e67e22'])
    ax.set_title("Average Sales by Product Category", fontsize=13)
    ax.set_ylabel("Average Sales ($)")
    show_chart(fig)

def show_region_sales():
    plt.close('all')
    fig, ax = plt.subplots(figsize=(6,4))
    colors = ['#e74c3c', '#3498db', '#2ecc71', '#f1c40f']
    ax.bar(regions, region_sales, color=colors)
    ax.set_ylabel("Total Sales ($)")
    ax.set_title("Sales by Region", fontsize=13)
    show_chart(fig)

def show_product_pie():
    plt.close('all')
    fig, ax = plt.subplots(figsize=(6,6))
    wedges, texts, autotexts = ax.pie(total_by_category, labels=categories, autopct='%1.1f%%',
                                      startangle=140, colors=['#3498db','#2ecc71','#e67e22'],
                                      textprops={'color':"w"})
    ax.set_title("Sales Distribution by Product Type", fontsize=13)
    show_chart(fig)

def show_gender_pie():
    plt.close('all')
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(gender_sales, labels=genders, autopct='%1.1f%%', startangle=140,
           colors=['#5DADE2','#F1948A','#A9CCE3'], textprops={'color':"w"})
    ax.set_title("Sales by Gender", fontsize=13)
    show_chart(fig)

# -----------------------------
# 6️⃣ Sidebar Buttons
# -----------------------------
ctk.CTkLabel(sidebar, text="📊 Sales Charts", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(20,10))

button_cfg = {"font": ctk.CTkFont(size=15, weight="bold"), "height": 40, "corner_radius": 10}
ctk.CTkButton(sidebar, text="📈 Sales Trend", command=show_sales_trend, **button_cfg).pack(fill="x", padx=15, pady=5)
ctk.CTkButton(sidebar, text="📦 Category Sales", command=show_category_sales, **button_cfg).pack(fill="x", padx=15, pady=5)
ctk.CTkButton(sidebar, text="🌍 Region Sales", command=show_region_sales, **button_cfg).pack(fill="x", padx=15, pady=5)
ctk.CTkButton(sidebar, text="🥧 Product Pie", command=show_product_pie, **button_cfg).pack(fill="x", padx=15, pady=5)
ctk.CTkButton(sidebar, text="👥 Gender Pie", command=show_gender_pie, **button_cfg).pack(fill="x", padx=15, pady=5)

# Appearance mode switch
ctk.CTkLabel(sidebar, text="Theme:", font=ctk.CTkFont(size=14)).pack(pady=(30,5))
theme_switch = ctk.CTkOptionMenu(sidebar, values=["Light", "Dark"],
                                 command=lambda v: ctk.set_appearance_mode(v.lower()))
theme_switch.pack(pady=10)

# Footer
ctk.CTkLabel(sidebar, text="© 2025 Sales Analytics", text_color="#adb5bd",
             font=ctk.CTkFont(size=11)).pack(side="bottom", pady=15)

# -----------------------------
# 7️⃣ Default Chart
# -----------------------------
show_sales_trend()

# -----------------------------
# 8️⃣ Run App
# -----------------------------
root.mainloop()
