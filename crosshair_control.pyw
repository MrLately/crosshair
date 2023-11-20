import tkinter as tk

def create_crosshair_overlay():
    # Control window
    control_window = tk.Tk()
    control_window.title("Crosshair Control")
    control_window.geometry("150x130")

    # Create a full-screen transparent window for the crosshair
    crosshair_overlay = tk.Toplevel(control_window, bg='white')
    crosshair_overlay.attributes('-fullscreen', True)
    crosshair_overlay.attributes('-transparentcolor', 'white')
    crosshair_overlay.overrideredirect(True)
    crosshair_overlay.attributes('-topmost', True)

    crosshair_size = [15]  # Initial crosshair size
    line_width = 2
    line_color = ['#00FF00']  # Initial crosshair color
    gap_size = [5]  # Size of the gap in the center
    crosshair_type = ['standard', 'gaps', 'circle', 'dot']  # Added new type
    crosshair_visible = [True]  # Track the visibility of the crosshair
    dot_size = 5  # Size of the dot for dot crosshair

    screen_width = crosshair_overlay.winfo_screenwidth()
    screen_height = crosshair_overlay.winfo_screenheight()

    canvas = tk.Canvas(crosshair_overlay, width=screen_width, height=screen_height, bg='white', highlightthickness=0)
    canvas.pack()

    def draw_crosshair():
        canvas.delete("all")  # Clear existing lines
        half_size = crosshair_size[0] / 2
        gap = gap_size[0] / 2
        center_x, center_y = screen_width / 2, screen_height / 2

        if crosshair_type[0] == 'standard':
            # Standard crosshair
            canvas.create_line(center_x - half_size, center_y, 
                               center_x + half_size, center_y, 
                               fill=line_color[0], width=line_width)
            canvas.create_line(center_x, center_y - half_size,
                               center_x, center_y + half_size, 
                               fill=line_color[0], width=line_width)
        elif crosshair_type[0] == 'gaps':
            # Crosshair with gaps
            canvas.create_line(center_x - half_size, center_y, 
                               center_x - gap, center_y, 
                               fill=line_color[0], width=line_width)
            canvas.create_line(center_x + gap, center_y, 
                               center_x + half_size, center_y, 
                               fill=line_color[0], width=line_width)
            canvas.create_line(center_x, center_y - half_size,
                               center_x, center_y - gap, 
                               fill=line_color[0], width=line_width)
            canvas.create_line(center_x, center_y + gap,
                               center_x, center_y + half_size, 
                               fill=line_color[0], width=line_width)
            
        elif crosshair_type[0] == 'circle':
            # Standard crosshair with a circle
            canvas.create_line(center_x - half_size, center_y, center_x + half_size, center_y, fill=line_color[0], width=line_width)
            canvas.create_line(center_x, center_y - half_size, center_x, center_y + half_size, fill=line_color[0], width=line_width)
            canvas.create_oval(center_x - half_size, center_y - half_size, center_x + half_size, center_y + half_size, outline=line_color[0], width=line_width)
            
        elif crosshair_type[0] == 'dot':
            # Dot crosshair
            canvas.create_oval(center_x - dot_size/2, center_y - dot_size/2,
                               center_x + dot_size/2, center_y + dot_size/2,
                               fill=line_color[0])

    draw_crosshair()

    def toggle_crosshair():
        crosshair_visible[0] = not crosshair_visible[0]
        if crosshair_visible[0]:
            crosshair_overlay.deiconify()
            toggle_button.config(text="On")
        else:
            crosshair_overlay.withdraw()
            toggle_button.config(text="Off")

    def increase_size():
        crosshair_size[0] += 2
        draw_crosshair()

    def decrease_size():
        if crosshair_size[0] > 2:
            crosshair_size[0] -= 2
            draw_crosshair()

    def change_color():
        colors = ['#00FF00', '#FF0000', '#0000FF', '#FFFF00']
        current_color_index = colors.index(line_color[0])
        next_color_index = (current_color_index + 1) % len(colors)
        line_color[0] = colors[next_color_index]
        color_button.config(bg=line_color[0])  # Update button background color
        draw_crosshair()

    def switch_crosshair_type():
        types = ['standard', 'gaps', 'circle', 'dot']
        current_type_index = types.index(crosshair_type[0])
        next_type_index = (current_type_index + 1) % len(types)
        crosshair_type[0] = types[next_type_index]
        type_button.config(text=f"{crosshair_type[0]}")
        update_size_buttons_state()
        draw_crosshair()

    def update_size_buttons_state():
        """Update the state of the size buttons based on crosshair type."""
        if crosshair_type[0] == 'dot':
            increase_button.config(state='disabled')
            decrease_button.config(state='disabled')
        else:
            increase_button.config(state='normal')
            decrease_button.config(state='normal')

    # Define buttons
    toggle_button = tk.Button(control_window, text="On", command=toggle_crosshair)
    toggle_button.pack()

    color_button = tk.Button(control_window, text="Color", bg=line_color[0], command=change_color)
    color_button.pack()

    type_button = tk.Button(control_window, text=f"{crosshair_type[0]}", command=switch_crosshair_type)
    type_button.pack()

    increase_button = tk.Button(control_window, text="Bigger", command=increase_size)
    increase_button.pack()
    decrease_button = tk.Button(control_window, text="Smaller", command=decrease_size)
    decrease_button.pack()

    update_size_buttons_state()  # Initial state update for size buttons

    control_window.mainloop()

create_crosshair_overlay()


