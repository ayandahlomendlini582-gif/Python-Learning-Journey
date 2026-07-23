import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Facebook-Like UI")
root.geometry("1000x600")
root.configure(bg='white')

# Top navigation bar (logo, search, profile icon)
def create_navbar(parent):
    navbar = tk.Frame(parent, bg="#4267B2", height=60)  # Facebook blue
    navbar.pack(side="top", fill="x")
    
    # Facebook logo
    logo = tk.Label(navbar, text="Facebook", font=("Arial", 20, "bold"), bg="#4267B2", fg="white")
    logo.pack(side="left", padx=10)
    
    # Search bar
    search_frame = tk.Frame(navbar, bg="#4267B2")
    search_frame.pack(side="left", padx=30)
    
    search_entry = tk.Entry(search_frame, width=40, font=("Arial", 12))
    search_entry.pack(side="left", padx=10)
    
    search_button = tk.Button(search_frame, text="Search", font=("Arial", 10))
    search_button.pack(side="left")
    
    # Profile icon and other options
    profile_icon = tk.Label(navbar, text="Profile", font=("Arial", 12), bg="#4267B2", fg="white")
    profile_icon.pack(side="right", padx=10)
    
    notifications_icon = tk.Label(navbar, text="🔔", font=("Arial", 16), bg="#4267B2", fg="white")
    notifications_icon.pack(side="right", padx=10)
    
    return navbar

# Left sidebar with navigation links
def create_sidebar(parent):
    sidebar = tk.Frame(parent, bg="lightgray", width=200)
    sidebar.pack(side="left", fill="y")
    
    links = ["Home", "Friends", "Groups", "Marketplace", "Watch"]
    
    for link in links:
        link_button = tk.Button(sidebar, text=link, font=("Arial", 12), bg="white", width=20)
        link_button.pack(pady=5, padx=5)
    
    return sidebar

# Main content area (feed)
def create_feed(parent):
    feed = tk.Frame(parent, bg="white")
    feed.pack(side="left", fill="both", expand=True, padx=10)
    
    # Simulated posts (as labels)
    for i in range(5):  # Display 5 sample posts
        post_frame = tk.Frame(feed, bg="lightblue", padx=10, pady=10)
        post_frame.pack(fill="x", pady=10)
        
        post_text = tk.Label(post_frame, text=f"Post {i+1}: This is a sample post content.", font=("Arial", 12), bg="lightblue")
        post_text.pack(anchor="w")
    
    return feed

# Right sidebar (placeholder for ads or chat list)
def create_right_sidebar(parent):
    right_sidebar = tk.Frame(parent, bg="lightgray", width=200)
    right_sidebar.pack(side="right", fill="y")
    
    ads_label = tk.Label(right_sidebar, text="Sponsored", font=("Arial", 12), bg="lightgray")
    ads_label.pack(pady=10)
    
    # Simulated ads
    for i in range(3):
        ad_frame = tk.Frame(right_sidebar, bg="white", padx=10, pady=10)
        ad_frame.pack(fill="x", pady=5)
        
        ad_text = tk.Label(ad_frame, text=f"Ad {i+1}: Check out this product!", font=("Arial", 10), bg="white")
        ad_text.pack(anchor="w")
    
    return right_sidebar

# Create the UI components
create_navbar(root)
create_sidebar(root)
create_feed(root)
create_right_sidebar(root)

# Start the main loop
root.mainloop()


