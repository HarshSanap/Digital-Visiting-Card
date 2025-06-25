import tkinter as tk
from tkinter import ttk, messagebox, colorchooser

class VisitingCardGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Visiting Card Generator")
        self.root.geometry("700x600")
        
        # default design settings
        self.bg_color = "#f0f0f0"
        self.text_color = "black"
        self.border_color = "black"
        self.font_style = "Arial"
        self.font_size = 10
        
        # main containers
        self.create_input_section()
        self.create_design_section()
        self.create_card_display()
        self.create_buttons()
        
        # Draw initial empty card
        self.draw_card_border()
    
    def create_input_section(self):
        input_frame = ttk.LabelFrame(self.root, text="Personal Information", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Personal details
        ttk.Label(input_frame, text="Full Name:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(input_frame, text="Job Title:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.title_entry = ttk.Entry(input_frame)
        self.title_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(input_frame, text="Company:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.company_entry = ttk.Entry(input_frame)
        self.company_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        
        # Contact information
        contact_frame = ttk.LabelFrame(self.root, text="Contact Information", padding=10)
        contact_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(contact_frame, text="Phone:").grid(row=0, column=0, sticky="e", padx=5, pady=2)
        self.phone_entry = ttk.Entry(contact_frame)
        self.phone_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(contact_frame, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=2)
        self.email_entry = ttk.Entry(contact_frame)
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
        
        ttk.Label(contact_frame, text="Address:").grid(row=2, column=0, sticky="e", padx=5, pady=2)
        self.address_entry = ttk.Entry(contact_frame)
        self.address_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
        
        # Configure column weights
        input_frame.columnconfigure(1, weight=1)
        contact_frame.columnconfigure(1, weight=1)
    
    def create_design_section(self):
        design_frame = ttk.LabelFrame(self.root, text="Card Design", padding=10)
        design_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Color selection
        ttk.Label(design_frame, text="Background:").grid(row=0, column=0, padx=5, pady=2)
        self.bg_btn = ttk.Button(design_frame, text="Choose", command=lambda: self.choose_color("bg"))
        self.bg_btn.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(design_frame, text="Text Color:").grid(row=1, column=0, padx=5, pady=2)
        self.text_btn = ttk.Button(design_frame, text="Choose", command=lambda: self.choose_color("text"))
        self.text_btn.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(design_frame, text="Border Color:").grid(row=2, column=0, padx=5, pady=2)
        self.border_btn = ttk.Button(design_frame, text="Choose", command=lambda: self.choose_color("border"))
        self.border_btn.grid(row=2, column=1, padx=5, pady=2)
        
        # Font selection
        ttk.Label(design_frame, text="Font Style:").grid(row=0, column=2, padx=5, pady=2)
        self.font_combo = ttk.Combobox(design_frame, values=["Arial", "Times New Roman", "Courier", "Verdana"])
        self.font_combo.set("Arial")
        self.font_combo.grid(row=0, column=3, padx=5, pady=2)
        self.font_combo.bind("<<ComboboxSelected>>", self.update_font_style)
        
        ttk.Label(design_frame, text="Font Size:").grid(row=1, column=2, padx=5, pady=2)
        self.font_slider = ttk.Scale(design_frame, from_=8, to=16, orient=tk.HORIZONTAL, command=self.update_font_size)
        self.font_slider.set(10)
        self.font_slider.grid(row=1, column=3, padx=5, pady=2, sticky="ew")
        
        # Configure column weights
        design_frame.columnconfigure(1, weight=1)
        design_frame.columnconfigure(3, weight=1)
    
    def create_card_display(self):
        self.card_frame = ttk.LabelFrame(self.root, text="Card Preview", padding=10)
        self.card_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.canvas = tk.Canvas(self.card_frame, bg="white", bd=2, relief=tk.GROOVE)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=5)
    
    def create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Generate Card", command=self.generate_card).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save Image", command=self.save_image).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.RIGHT, padx=5)
    
    def draw_card_border(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        padding = 10
        self.canvas.create_rectangle(
            padding, padding, 
            width-padding, height-padding,
            outline=self.border_color, width=2, fill=self.bg_color
        )
    
    def choose_color(self, element):
        current_color = getattr(self, f"{element}_color")
        color = colorchooser.askcolor(title=f"Choose {element} color", initialcolor=current_color)
        
        if color[1]:  # If color was selected
            setattr(self, f"{element}_color", color[1])
            getattr(self, f"{element}_btn").config(text=color[1])
            self.generate_card()
    
    def update_font_style(self, event=None):
        self.font_style = self.font_combo.get()
        self.generate_card()
    
    def update_font_size(self, value):
        self.font_size = int(float(value))
        self.generate_card()
    
    def generate_card(self):# Get all entered values
        name = self.name_entry.get()
        title = self.title_entry.get()
        company = self.company_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        # Clear and redraw border
        self.draw_card_border()
        
        # Get canvas dimensions
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        center_x = width / 2
        current_y = 30  # Starting Y position
        
        # Add information to card
        if name:
            self.canvas.create_text(
                center_x, current_y, 
                text=name, 
                font=(self.font_style, self.font_size+4, "bold"), 
                fill=self.text_color
            )
            current_y += 30
        
        if title:
            self.canvas.create_text(
                center_x, current_y, 
                text=title, 
                font=(self.font_style, self.font_size), 
                fill=self.text_color
            )
            current_y += 25
        
        if company:
            self.canvas.create_text(
                center_x, current_y, 
                text=company, 
                font=(self.font_style, self.font_size), 
                fill=self.text_color
            )
            current_y += 25
        
        # Contact information on left side
        contact_info = []
        if phone: contact_info.append(f"Phone: {phone}")
        if email: contact_info.append(f"Email: {email}")
        if address: contact_info.append(f"Address: {address}")
        
        for i, info in enumerate(contact_info):
            self.canvas.create_text(
                30, current_y + i*25, 
                text=info, 
                font=(self.font_style, self.font_size), 
                fill=self.text_color,
                anchor="w"
            )
    
    def save_image(self):
        try:
            ps = self.canvas.postscript(colormode='color')
            
            # Convert to image (requires PIL)
            from PIL import Image
            import io
            
            img = Image.open(io.BytesIO(ps.encode('utf-8')))
            
            # Ask for save location
            file_path = tk.filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")],
                title="Save Card As"
            )
            
            if file_path:
                img.save(file_path)
                messagebox.showinfo("Success", f"Card saved successfully as {file_path}")
        except ImportError:
            messagebox.showerror("Error", "Pillow library is required to save images.\nInstall it with: pip install pillow")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {str(e)}")
    
    def clear_all(self):
        for entry in [self.name_entry, self.title_entry, self.company_entry, 
                     self.phone_entry, self.email_entry, self.address_entry]:
            entry.delete(0, tk.END)
        
        # Reset to default design
        self.bg_color = "#f0f0f0"
        self.text_color = "black"
        self.border_color = "black"
        self.font_style = "Arial"
        self.font_size = 10
        
        # Update buttons and combobox
        self.bg_btn.config(text=self.bg_color)
        self.text_btn.config(text=self.text_color)
        self.border_btn.config(text=self.border_color)
        self.font_combo.set(self.font_style)
        self.font_slider.set(self.font_size)
        
        self.draw_card_border()
        messagebox.showinfo("Cleared", "All fields have been reset to defaults.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VisitingCardGenerator(root)
    root.mainloop()