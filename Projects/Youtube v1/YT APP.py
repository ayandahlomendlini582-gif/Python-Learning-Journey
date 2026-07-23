
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("YouTube-Like UI")
root.geometry("900x600")
root.configure(bg='white')

# Top navigation bar (logo, search, profile icon)
def create_navbar(parent):
    navbar = tk.Frame(parent, bg="lightgray", height=50)
    navbar.pack(side="top", fill="x")
    
    # Logo
    logo = tk.Label(navbar, text="YouTube", font=("Arial", 18, "bold"), bg="lightgray", fg="red")
    logo.pack(side="left", padx=10)
    
    # Search bar
    search_frame = tk.Frame(navbar, bg="lightgray")
    search_frame.pack(side="left", padx=20)
    
    search_entry = tk.Entry(search_frame, width=40, font=("Arial", 12))
    search_entry.pack(side="left", padx=10)
    
    search_button = tk.Button(search_frame, text="Search", font=("Arial", 10))
    search_button.pack(side="left")
    
    # Profile icon
    profile_icon = tk.Label(navbar, text="Profile", font=("Arial", 12), bg="lightgray")
    profile_icon.pack(side="right", padx=10)
    
    return navbar

# Sidebar with categories
def create_sidebar(parent):
    sidebar = tk.Frame(parent, bg="lightgray", width=200)
    sidebar.pack(side="left", fill="y")
    
    categories = ["Home", "Trending", "Subscriptions", "Library", "History"]
    
    for category in categories:
        category_button = tk.Button(sidebar, text=category, font=("Arial", 12), bg="white", width=20)
        category_button.pack(pady=5, padx=5)
    
    return sidebar

# Main video section
def create_video_area(parent):
    video_area = tk.Frame(parent, bg="white")
    video_area.pack(side="right", fill="both", expand=True)
    
    # Create a grid of video thumbnails (as buttons)
    for i in range(2):  # 2 rows of videos
        for j in range(3):  # 3 videos per row
            video_button = tk.Button(video_area, text=f"Video {i*3 + j + 1}", font=("Arial", 12), width=30, height=10)
            video_button.grid(row=i, column=j, padx=10, pady=10)
    
    return video_area

# Create the UI
create_navbar(root)
create_sidebar(root)
create_video_area(root)

# Start the main loop
root.mainloop()
