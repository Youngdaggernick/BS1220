import tkinter as tk
import math
import datetime
from tkinter import ttk
from tkinter import messagebox


#Base Class
class Page(tk.Frame):
    def __init__(self, parent, controller, title):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title = title

    def show(self):
        self.controller.title(self.title)
        self.tkraise()

#Start Page
class PageOne(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

    #Labels
        label = tk.Label(self, text="Gift Wrapping", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)

    #Buttons
        button = tk.Button(self, text="Get Started", font=("Arial", 16), command=lambda: controller.show_page(PageTwo))
        button.place(x=170, y=480, width=160, height=80)

    #Canvas
        canvas = tk.Canvas(self)
        canvas.place(x=150, y=200, width=300, height=300)
        canvas.create_rectangle(40, 40, 160, 150, outline="black", width=10)
        canvas.create_line(100, 40, 100, 150, width=10)
        canvas.create_line(40, 95, 160, 95, width=10)
        canvas.create_oval(85, 27, 115, 45, fill="black")
        canvas.create_polygon(70, 20, 130, 50, 130, 20, 70, 50, fill="black")

#Enter Name Page
class PageTwo(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

    #Labels
        label = tk.Label(self, text="Please Enter Your Name", font=("Arial Bold", 20))
        label.place(x=0, y=0, width=500, height=50)
        enter_first_name_label = tk.Label(self, text="First Name:", font=("Arial", 16))
        enter_first_name_label.place(x=150, y=250, width=200, height=50)
        enter_last_name_label = tk.Label(self, text="Last Name:", font=("Arial", 16))
        enter_last_name_label.place(x=150, y=360, width=200, height=50)

    #Inputs
        self.enter_first_name = tk.Entry(self)
        self.enter_first_name.place(x=150, y=300, width=200, height=50)
        self.enter_last_name = tk.Entry(self)
        self.enter_last_name.place(x=150, y=410, width=200, height=50)

    #Buttons
        button = tk.Button(self, text="Next", font=("Arial", 16), command=self.on_next_clicked)
        button.place(x=170, y=480, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageOne))
        back_button.place(x=0, y=0, width=50, height=50)

    #Error Handling
    def on_next_clicked(self):
        if self.confirm_name():
            self.controller.show_page(PageThree)

    def confirm_name(self):
        first_name = self.enter_first_name.get().strip()
        last_name = self.enter_last_name.get().strip()
        if not first_name or not last_name:
            messagebox.showerror("Error", "Both first and last name are required.")
            return False  
        self.controller.set_input_value('name', 'first_name', first_name)
        self.controller.set_input_value('name', 'last_name', last_name)
        return True
    
    #reset
    def reset(self):
        self.enter_first_name.delete(0, tk.END)
        self.enter_last_name.delete(0, tk.END)

#Choose Shape Page
class PageThree(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")
        label = tk.Label(self, text="Choose A Shape", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Cube", command=lambda: controller.show_page(PageFour))
        button.place(x=50, y=350, width=100, height=40)
        button = tk.Button(self, text="Cuboid", command=lambda: controller.show_page(PageFive))
        button.place(x=200, y=350, width=100, height=40)
        button = tk.Button(self, text="Cylinder", command=lambda: controller.show_page(PageSix))
        button.place(x=350, y=350, width=100, height=40)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageTwo))
        back_button.place(x=0, y=0, width=50, height=50)

#Cube Dimensions
class PageFour(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

    #Labels
        label = tk.Label(self, text="Enter Gift Dimensions", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        enter_cube_height_label = tk.Label(self, text="Enter Height:", font=("Arial", 16))
        enter_cube_height_label.place(x=150, y=250, width=200, height=50)

    #Inputs
        self.cube_height = tk.Entry(self)
        self.cube_height.place(x=150, y=300, width=200, height=50)

    #Buttons
        button = tk.Button(self, text="Next", command=self.on_next_clicked)
        button.place(x=170, y=500, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageThree))
        back_button.place(x=0, y=0, width=50, height=50)

    def on_next_clicked(self):
        if self.confirm_cube_dimensions():
            self.controller.show_page(PageSeven)

    def confirm_cube_dimensions(self):
        try:
            cube_height = float(self.cube_height.get())
            if cube_height <= 0:
                raise ValueError("The Cube height must be a positive number.")
            self.controller.set_input_value('gift', 'shape', "Cube")
            self.controller.set_input_value('gift', 'dimensions', {'cube_height': cube_height})
            
            return True
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return False
    
    #reset
    def reset(self):
        self.cube_height.delete(0, tk.END)


#Cuboid Dimensions
class PageFive(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

    #Labels
        label = tk.Label(self, text="Enter Gift Dimensions", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        enter_cuboid_height_label = tk.Label(self, text="Enter Height:", font=("Arial", 16))
        enter_cuboid_height_label.place(x=150, y=200, width=200, height=50)
        enter_cuboid_length_label = tk.Label(self, text="Enter Length:", font=("Arial", 16))
        enter_cuboid_length_label.place(x=150, y=300, width=200, height=50)
        enter_cuboid_width_label = tk.Label(self, text="Enter Width", font=("Arial", 16))
        enter_cuboid_width_label.place(x=150, y=400, width=200, height=50)

    #Inputs
        self.cuboid_height = tk.Entry(self)
        self.cuboid_height.place(x=150, y=250, width=200, height=50)
        self.cuboid_length = tk.Entry(self)
        self.cuboid_length.place(x=150, y=350, width=200, height=50)
        self.cuboid_width = tk.Entry(self)
        self.cuboid_width.place(x=150, y= 450, width=200, height=50)

    #Buttons
        button = tk.Button(self, text="Next", command=self.on_next_clicked)
        button.place(x=170, y=550, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageThree))
        back_button.place(x=0, y=0, width=50, height=50)

    def on_next_clicked(self):
        if self.confirm_cuboid_dimensions():
            self.controller.show_page(PageSeven)

    def confirm_cuboid_dimensions(self):
        try:
            height = float(self.cuboid_height.get())
            length = float(self.cuboid_length.get())
            width = float(self.cuboid_width.get())
            if height <= 0 or length <= 0 or width <= 0:
                raise ValueError("Dimensions must be positive numbers.")
            self.controller.set_input_value('gift', 'shape', "Cuboid")
            self.controller.set_input_value('gift', 'dimensions', {
                'cuboid_height': height,
                'cuboid_length': length,
                'cuboid_width': width
            })
            
            return True
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return False
        
    #reset
    def reset(self):
        self.cuboid_height.delete(0, tk.END)
        self.cuboid_length.delete(0, tk.END)
        self.cuboid_width.delete(0, tk.END)

#Cylinder Dimensions
class PageSix(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

    #Labels
        label = tk.Label(self, text="Enter Gift Dimensions", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        cylinder_height_label = tk.Label(self, text="Enter Height:", font=("Arial Bold", 16))
        cylinder_height_label.place(x=150, y=260, width=200, height=50)
        cylinder_radius_label = tk.Label(self, text="Enter Radius:", font=("Arial Bold", 16))
        cylinder_radius_label.place(x=150, y=360, width=200, height=50)
    #Inputs
        self.cylinder_height = tk.Entry(self)
        self.cylinder_height.place(x=150, y=300, width=200, height=50)
        self.cylinder_radius = tk.Entry(self)
        self.cylinder_radius.place(x=150, y=400, width=200, height=50)

    #Buttons
        button = tk.Button(self, text="Next", command=self.on_next_clicked)
        button.place(x=170, y=480, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageThree))
        back_button.place(x=0, y=0, width=50, height=50)

    def on_next_clicked(self):
        if self.confirm_cylinder_dimensions():
            self.controller.show_page(PageSeven)

    def confirm_cylinder_dimensions(self):
        try:
            height = float(self.cylinder_height.get())
            radius = float(self.cylinder_radius.get())
            if height <= 0 or radius <= 0:
                raise ValueError("Height and radius must be positive numbers.")
            self.controller.set_input_value('gift', 'shape', "Cylinder")
            self.controller.set_input_value('gift', 'dimensions', {
                'cylinder_height': height,
                'cylinder_radius': radius
            })
            
            return True
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            return False
        
    #reset
    def reset(self):
        self.cylinder_height.delete(0, tk.END)
        self.cylinder_radius.delete(0, tk.END)

#Choose Pattern Page
class PageSeven(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

        pattern1_price= 0.4
        pattern2_price = 0.75
        # Canvas
        canvas1 = tk.Canvas(self, width=150, height=150)
        canvas1.place(x=50, y=100)
        canvas2 = tk.Canvas(self, width=150, height=150)
        canvas2.place(x=300, y=100)

        # Labels
        label = tk.Label(self, text="Choose A Pattern and Colour", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        label_color = tk.Label(self, text="Select a color:", font=("Arial Bold", 16))
        label_color.place(x=150, y=285)
        label_pattern = tk.Label(self, text="Choose A Pattern:", font=("Arial Bold", 16))
        label_pattern.place(x=150, y=360)
        pattern1_price = tk.Label(self, text=f"Pattern 1: {pattern1_price} p/cm^2")
        pattern1_price.place(x=50, y=260, width=150, height=30)
        pattern2_price = tk.Label(self, text=f"Pattern 2: {pattern2_price} p/cm^2")
        pattern2_price.place(x=300, y=260, width=150, height=30)

        # Inputs
        self.selected_colour = tk.StringVar()
        self.selected_colour.set("Purple")
        combobox_colour = ttk.Combobox(self, textvariable=self.selected_colour, font=("Arial", 14), values=["Purple", "DarkSlateGray4", "deep sky blue", "light sea green", "VioletRed", "gold"])
        combobox_colour.place(x=150, y=320, width=200, height=35)
        self.selected_pattern = tk.StringVar()
        self.selected_pattern.set("Pattern 1")
        combobox_pattern = ttk.Combobox(self, textvariable=self.selected_pattern, font=("Arial", 14), values=["Pattern 1", "Pattern 2"])
        combobox_pattern.place(x=150, y=395, width=200, height=35)

        #Draw Patterns
        def update_pattern(event=None):
            #Pattern1
            canvas1.delete("all")
            
            square_size = 30
            colours = [self.selected_colour.get(), "White"]

            for row in range(5):
                for col in range(5):
                    colour_index = (row + col) % 2
                    x0 = col * square_size
                    y0 = row * square_size
                    x1 = x0 + square_size
                    y1 = y0 + square_size
                    canvas1.create_rectangle(x0, y0, x1, y1, fill=colours[colour_index], outline="Black")

            #Pattern2
            canvas2.delete("all")
            canvas2.create_rectangle(2, 2, 150, 150, fill="white", outline="Black")

            number_of_triangles = 5
            y_offsets = [(30, 75), (60, 15), (120, 75), (90, 135)]
        
            for i in range(number_of_triangles):
                for y_start, y_tip in y_offsets:
                    canvas2.create_polygon(i * 30, y_start, 30 + i * 30, y_start, 15 + i * 30, y_tip, fill=self.selected_colour.get())


        update_pattern()
        combobox_colour.bind("<<ComboboxSelected>>", update_pattern)

        # Buttons
        button = tk.Button(self, text="Next", command=lambda: (controller.show_page(PageEight), self.confirm_pattern()))
        button.place(x=170, y=480, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageThree))
        back_button.place(x=0, y=0, width=50, height=50)

    def confirm_pattern(self):
        self.controller.set_input_value('gift', 'colour', self.selected_colour.get())
        self.controller.set_input_value('gift', 'pattern', self.selected_pattern.get())

        print("Confirmed Pattern and Color")


#Customization Page
class PageEight(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")

        #Labels
        label = tk.Label(self, text="Add Customization", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        checkbox_label = tk.Label(self, text="Add Bow", font=("Arial Bold", 14))
        checkbox_label.place(x=200, y=180, width=100, height=20)
        enter_text_label= tk.Label(self, text="Enter Gift Tag Text(2p/character):", font=("Arial Bold", 14))
        enter_text_label.place(x=85, y=320,width=340)

        #Inputs
        self.add_bow_var = tk.BooleanVar()
        bow_checkbox = tk.Checkbutton(self, variable=self.add_bow_var)
        bow_checkbox.place(x=240, y=200)

        # Gift Message Entry
        self.message_entry = tk.Entry(self, font=("Arial", 14))
        self.message_entry.place(x=150, y=350, width=200)

        #Buttons
        button = tk.Button(self, text="Next", command=self.on_next_click)
        button.place(x=170, y=480, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageSeven))
        back_button.place(x=0, y=0, width=50, height=50)

    #error handling
    def on_next_click(self):
        self.confirm_customisation()
        self.controller.show_page(PageNine)

    def confirm_customisation(self):

        add_bow = bool(self.add_bow_var.get())
        gift_tag_text = self.message_entry.get()
        add_gift_tag = bool(gift_tag_text)

        self.controller.set_input_value('customization', 'add_bow', add_bow)
        self.controller.set_input_value('customization', 'add_gift_tag', add_gift_tag)
        self.controller.set_input_value('customization', 'gift_tag_text', gift_tag_text)

        print(f"Add Bow: {add_bow}")
        print(f"Gift Tag: {add_gift_tag}")
        print(f"Characters: {len(gift_tag_text)}")
        print(f"Message: {self.message_entry.get()}")

    #reset
    def reset(self):
        self.add_bow_var.set(False)
        self.message_entry.delete(0, tk.END)


#Order Summary Page
class PageNine(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")
        label = tk.Label(self, text="Order Summary", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Next", command=lambda: controller.show_page(PageTen))
        button.place(x=170, y=480, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageEight))
        back_button.place(x=0, y=0, width=50, height=50)

    def refresh(self, controller):

        #Prevents widget duplication
        for widget in self.winfo_children():
            if not isinstance(widget, tk.Button):  
                widget.destroy()

        #Retreive Values
        input_values = controller.get_input_values()

        chosen_shape = input_values['gift']['shape']
        add_bow = input_values['customization']['add_bow']
        add_gift_tag = input_values['customization']['add_gift_tag']

        customization = input_values['customization']
        message = customization.get('gift_tag_text')
        if message is not None:
            character_length = len(message)

        #Selected Pattern values
        if 'pattern' in input_values['gift']:
            selected_pattern = input_values['gift']['pattern']
        else:
            selected_pattern = "None"

        #Pattern Price

        pattern1_price = 0.4
        pattern2_price = 0.75

        if selected_pattern == "Pattern 1":
            pattern_price = pattern1_price

        else:
            pattern_price = pattern2_price

        bow_price = 1.50
        gift_tag_flat = 0.50
        character_rate = 0.02

        total_price = 0
        print(f"shape: {chosen_shape}")

        if chosen_shape == "Cube":
            #get shape dimensions
            cube_height = int(input_values['gift']['dimensions']['cube_height'])

            #calculations
            paper_required = (cube_height * 4 + 6) * (cube_height * 3 + 6)
            paper_price = round(((paper_required * pattern_price)/100), 2)
            total_price += paper_price

            #Show order summary
            paper_required_label = tk.Label(self, text=(f"Paper Required: {paper_required} cm^2"), font=("Arial"))
            paper_required_label.pack(pady= 10)

            paper_price_label = tk.Label(self, text=(f"Paper Price: £{paper_price:.2f}"), font=("Arial"))
            paper_price_label.pack(pady= 10)

            if add_bow:
                total_price += bow_price
                bow_required_label = tk.Label(self, text=(f"Add Bow: £ {bow_price:.2f} "), font=("Arial"))
                bow_required_label.pack(pady= 10)

            if add_gift_tag == True:
                gift_tag_cost = round((gift_tag_flat + character_rate * character_length), 2)
                total_price += gift_tag_cost
                print("Add Gift Tag: Yes")
                gift_tag_price_label = tk.Label(self, text=(f"Gift Tag: £{gift_tag_cost:.2f}"), font=("Arial"))
                gift_tag_price_label.pack(pady=10)

            total_price_label = tk.Label(self, text=(f"Total Price: £{total_price:.2f}"), font=("Arial Bold", 14))
            total_price_label.place(x=50, y=400)

            self.controller.set_input_value('order', 'total_price', total_price)

        elif chosen_shape == "Cuboid":
            #get values
            cuboid_height = int(input_values['gift']['dimensions']['cuboid_height'])
            cuboid_length = int(input_values['gift']['dimensions']['cuboid_length'])
            cuboid_width = int(input_values['gift']['dimensions']['cuboid_width'])

            #calculations
            paper_required = ((cuboid_width*2 + cuboid_height*2) + 6)*((cuboid_length + cuboid_height*2) + 6)
            paper_price = round((paper_required * pattern_price)/100, 2)
            total_price += paper_price

            #Show summary
            paper_required_label = tk.Label(self, text=(f"Paper Required: {paper_required} cm^2"), font=("Arial"))
            paper_required_label.pack(pady=10)

            paper_price_label = tk.Label(self, text=(f"Paper Price: £{paper_price:.2f}"), font=("Arial"))
            paper_price_label.pack(pady=10)

            if add_bow:
                total_price += bow_price
                bow_required_label = tk.Label(self, text=(f"Add Bow: £ {bow_price:.2f} "), font=("Arial"))
                bow_required_label.pack(pady=10)

            if add_gift_tag == True:
                gift_tag_cost = round((gift_tag_flat + character_rate * character_length), 2)
                total_price += gift_tag_cost
                print("Add Gift Tag: Yes")
                gift_tag_price_label = tk.Label(self, text=(f"Gift Tag: £{gift_tag_cost:.2f}"), font=("Arial"))
                gift_tag_price_label.pack(pady=10)

            total_price_label = tk.Label(self, text=(f"Total Price: £{total_price:.2f}"), font=("Arial Bold", 14))
            total_price_label.place(x=50, y=400)

            self.controller.set_input_value('order', 'total_price', total_price)


        elif chosen_shape == "Cylinder":
            #Get shape dimensions
            cylinder_height = int(input_values['gift']['dimensions']['cylinder_height'])
            cylinder_radius = int(input_values['gift']['dimensions']['cylinder_radius'])

            #Calculations
            paper_required = (cylinder_height + (4 * cylinder_radius) + 6) * ((cylinder_radius * 2 * math.pi) + 6)
            paper_price = round(((paper_required * pattern_price) / 100), 2)
            total_price += paper_price

            #Show summary
            paper_required_label = tk.Label(self, text=(f"Paper Required: {paper_required:.2f} cm^2"), font=("Arial"))
            paper_required_label.pack(pady=10)

            paper_price_label = tk.Label(self, text=(f"Paper Price: £{paper_price:.2f}"), font=("Arial"))
            paper_price_label.pack(pady=10)

            if add_bow:
                total_price += bow_price
                bow_required_label = tk.Label(self, text=(f"Add Bow: £ {bow_price:.2f} "), font=("Arial"))
                bow_required_label.pack(pady=10)

            if add_gift_tag == True:
                gift_tag_cost = round((gift_tag_flat + character_rate * character_length), 2)
                total_price += gift_tag_cost
                print("Add Gift Tag: Yes")
                gift_tag_price_label = tk.Label(self, text=(f"Gift Tag: £{gift_tag_cost:.2f}"), font=("Arial"))
                gift_tag_price_label.pack(pady=10)

            total_price_label = tk.Label(self, text=(f"Total Price: £{total_price:.2f}"), font=("Arial Bold", 14))
            total_price_label.place(x=50, y=400)

            self.controller.set_input_value('order', 'total_price', total_price)


#Booking Slot Page
class PageTen(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")
        #Labels
        label = tk.Label(self, text="Booking", font=("Arial Bold", 20))
        label.pack(pady=10, padx=10)

        drop_off_label = tk.Label(self, text="Drop Off", font=("Arial", 16))
        drop_off_label.place(x=200, y=70, width=100, height=20)
        pick_up_label = tk.Label(self, text="Pick Up", font=("Arial", 16))
        pick_up_label.place(x=200, y=180, width=100, height=20)

        self.days = list(range(1, 32))
        self.months = list(range(1, 13))
        self.years = list(range(2024, 2029))

        #Inputs
        #Drop off
        self.drop_year_entry = ttk.Combobox(self, values=self.years, width=6)
        self.drop_year_entry.set('Year')
        self.drop_year_entry.place(x=170, y=150, width=50)

        self.drop_month_entry = ttk.Combobox(self, values=self.months, width=4)
        self.drop_month_entry.set('Month')
        self.drop_month_entry.place(x=220, y=150, width=60)


        self.drop_day_entry = ttk.Combobox(self, values=self.days, width=4)
        self.drop_day_entry.set('Day')
        self.drop_day_entry.place(x=280, y=150, width=50)



        self.time_slots = [f"{hour}:{minute:02} {'AM' if hour < 12 else 'PM'}"
                           for hour in range(8, 21)
                           for minute in (0, 30) if not (hour == 20 and minute == 30)]

        self.drop_time_entry = ttk.Combobox(self, values=self.time_slots)
        self.drop_time_entry.set('Select Time')
        self.drop_time_entry.place(x=170, y=100, width=160, height=20)


        #Pick up
        self.pick_year_entry = ttk.Combobox(self, values=self.years, width=6)
        self.pick_year_entry.set('Year')
        self.pick_year_entry.place(x=170, y=260, width=50)

        self.pick_month_entry = ttk.Combobox(self, values=self.months, width=4)
        self.pick_month_entry.set('Month')
        self.pick_month_entry.place(x=220, y=260, width=60)

        self.pick_day_entry = ttk.Combobox(self, values=list(range(1, 32)), width=4)
        self.pick_day_entry.set('Day')
        self.pick_day_entry.place(x=280, y=260, width=50)

        self.pick_time_entry = ttk.Combobox(self, values=self.time_slots)
        self.pick_time_entry.set('Select Time')
        self.pick_time_entry.place(x=170, y=210, width=160, height=20)

        #Buttons

        button = tk.Button(self, text="Next", command=self.on_next_clicked)
        button.place(x=170, y=480, width=160, height=80)
        back_button = tk.Button(self, text="Back", command=lambda: controller.show_page(PageNine))
        back_button.place(x=0, y=0, width=50, height=50)

    def on_next_clicked(self):
        if self.save_order_data():
            self.controller.show_page(PageEleven)

    def save_order_data(self):
    # Collect input data
        first_name = self.controller.input_values['name']['first_name']
        last_name = self.controller.input_values['name']['last_name']
        order_total = self.controller.input_values['order']['total_price']
        chosen_shape = self.controller.input_values['gift']['shape']
        chosen_pattern = self.controller.input_values['gift']['pattern']
        chosen_colour = self.controller.input_values['gift']['colour']
        add_bow = self.controller.input_values['customization']['add_bow']
        add_gift_tag = self.controller.input_values['customization']['add_gift_tag']
        gift_tag_text = self.controller.input_values['customization']['gift_tag_text']

        drop_year = self.drop_year_entry.get()
        drop_month = self.drop_month_entry.get()
        drop_day = self.drop_day_entry.get()
        drop_time = self.drop_time_entry.get()

        pick_year = self.pick_year_entry.get()
        pick_month = self.pick_month_entry.get()
        pick_day = self.pick_day_entry.get()
        pick_time = self.pick_time_entry.get()

        # Validate inputs
        if not (drop_year and drop_month and drop_day and drop_time):
            messagebox.showerror("Error", "All date and time fields must be filled out.")
            return False  

        try:
            drop_date = datetime.date(int(drop_year), int(drop_month), int(drop_day))
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date: {e}")
            return False
        
        if not (pick_year and pick_month and pick_day and pick_time):
            messagebox.showerror("Error", "All date and time fields must be filled out.")
            return False  

        try:
            pick_date = datetime.date(int(pick_year), int(pick_month), int(pick_day))
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid date: {e}")
            return False
        
        if pick_date <= drop_date:
            messagebox.showerror("Error", "Pick-up date must be after the drop-off date.")
            return False

        # Proceed if valid
        drop_date_str = f"{drop_year}-{drop_month.zfill(2)}-{drop_day.zfill(2)}"
        drop_time_str = drop_time

        pick_date_str = f"{pick_year}-{pick_month.zfill(2)}-{pick_day.zfill(2)}"
        pick_time_str = pick_time
        
        filename = f"{first_name}_{last_name}_{drop_date_str}.txt"
        filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c in '._-']).rstrip()

        with open(filename, 'w') as file:
            file.write("Booking Information: \n")
            file.write("============================\n")
            file.write(f"Chosen Shape: {chosen_shape}\n")
            file.write(f"Pattern Choice: {chosen_pattern}\n")
            file.write(f"Colour Choice: {chosen_colour}\n")
            if add_bow == True:
                file.write("Add Bow: Yes\n")
            if add_gift_tag == True:
                file.write("Add Gift Tag: Yes\n")
                file.write(f"Message: {gift_tag_text}\n")
            file.write(f"Drop-Off Date: {drop_date_str}\n")
            file.write(f"Drop-Off Time: {drop_time_str}\n")
            file.write(f"Pick-Up Date: {pick_date_str}\n")
            file.write(f"Pick-Up Time: {pick_time_str}\n")
            file.write(f"Order Total: £ {order_total:.2f}\n")
            file.write("\n")
            file.write(f"Customer Information\n")
            file.write("============================\n")
            file.write(f"First Name: {first_name}\n")
            file.write(f"Last Name:{last_name}")

            print(f"Order data saved to {filename}.")
        return True
    
#Complete Page
class PageEleven(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller, "Gift Wrapping Service")
        label = tk.Label(self, text="Order Complete!", font=("Arial Bold", 25))
        label.pack(pady=200, padx=10)
        back_button = tk.Button(self, text="Exit", command=self.controller.reset_app)
        back_button.place(x=0, y=0, width=50, height=50)


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.input_values = {
            'name': {
                'first_name': None,
                'last_name': None
            },
            'gift': {
                'shape': None,
                'dimensions': {}
            },
            'wrapping': {
                'colour': None,
                'pattern': None
            },
            'customization': {
                'add_bow': None,
                'add_gift_tag': None,
                'gift_tag_text': None
            },
            'order': {
                'total_price': None,
                'slot_booked': {}
            }
        }

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}
        for PageClass in (PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine, PageTen, PageEleven):
            page = PageClass(container, self)
            page.grid(row=0, column=0, sticky="nsew")
            self.pages[PageClass] = page

        self.show_page(PageOne)

    def reset_app(self):
    
        self.input_values = {
            'name': {
                'first_name': None,
                'last_name': None
            },
            'gift': {
                'shape': None,
                'dimensions': {}
            },
            'wrapping': {
                'colour': None,
                'pattern': None
            },
            'customization': {
                'add_bow': None,
                'add_gift_tag': None,
                'gift_tag_text': None
            },
            'order': {
                'total_price': None,
                'slot_booked': {}
            }
        }

        for page in self.pages.values():
            if hasattr(page, 'reset'):
                page.reset()
    
        self.show_page(PageOne)

    def show_page(self, page):
        frame = self.pages[page]
        if hasattr(page, 'refresh'):
            frame.refresh(self)
        self.pages[page].show()

    def set_input_value(self, category, key, value):
        self.input_values[category][key] = value

    def get_input_values(self):
        return self.input_values


if __name__ == "__main__":
    try:
        app = MainApp()
        app.geometry("500x700")
        app.resizable(False, False)
        app.mainloop()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")