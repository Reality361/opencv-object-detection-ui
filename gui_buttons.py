import cv2
import numpy as np

class Buttons:
    def __init__(self):
        """Initialize button attributes and colors."""
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.text_scale = 0.8
        self.text_thickness = 1
        self.padding_x = 15
        self.padding_y = 10
        self.corner_radius = 6
        self.shadow_offset = 2

        self.buttons = {}
        self.button_index = 0
        self.scroll_offset = 0  # Scroll position

        np.random.seed(42)
        self.colors = self.generate_colors(100)

    def generate_colors(self, num_colors):
        """Generate a set of visually distinct colors."""
        return [tuple(np.random.randint(150, 255, size=3).tolist()) for _ in range(num_colors)]

    def add_button(self, label, x, y):
        """Add a new button with dynamic spacing."""
        text_size = cv2.getTextSize(label, self.font, self.text_scale, self.text_thickness)[0]
        width, height = text_size[0] + self.padding_x * 2, text_size[1] + self.padding_y * 2
        right_x, bottom_y = x + width, y + height

        self.buttons[self.button_index] = {
            "label": label,
            "position": [x, y, right_x, bottom_y],
            "active": False
        }
        self.button_index += 1

    def draw_rounded_rectangle(self, img, pt1, pt2, color, thickness=2):
        """Draw a rounded rectangle button with a subtle shadow."""
        x1, y1 = pt1
        x2, y2 = pt2

        # Shadow Effect
        shadow_color = (50, 50, 50) if thickness == -1 else (30, 30, 30)
        cv2.rectangle(img, (x1 + self.shadow_offset, y1 + self.shadow_offset), 
                      (x2 + self.shadow_offset, y2 + self.shadow_offset), shadow_color, -1, cv2.LINE_AA)

        # Main Button
        cv2.rectangle(img, pt1, pt2, color, thickness, cv2.LINE_AA)

    def display_buttons(self, frame):
        """Render scrollable buttons on the frame."""
        for button_id, button_info in self.buttons.items():
            label = button_info["label"]
            x, y, right_x, bottom_y = button_info["position"]

            # Apply scroll offset
            y += self.scroll_offset
            bottom_y += self.scroll_offset

            # Skip rendering if outside viewable area
            if y > frame.shape[0] - 50 or bottom_y < 0:
                continue

            is_active = button_info["active"]
            button_color = (255, 69, 0) if is_active else (70, 130, 180)
            text_color = (255, 255, 255) if is_active else (220, 220, 220)

            # Draw button with rounded edges
            self.draw_rounded_rectangle(frame, (x, y), (right_x, bottom_y), button_color, -1)

            # Add centered text
            text_size = cv2.getTextSize(label, self.font, self.text_scale, self.text_thickness)[0]
            text_x = x + (right_x - x - text_size[0]) // 2
            text_y = bottom_y - (self.padding_y // 2)
            cv2.putText(frame, label, (text_x, text_y), self.font, self.text_scale, text_color, self.text_thickness, cv2.LINE_AA)

        return frame

    def button_click(self, mouse_x, mouse_y):
        """Handle button click events."""
        for button_id, button_info in self.buttons.items():
            x, y, right_x, bottom_y = button_info["position"]

            # Adjust for scrolling
            y += self.scroll_offset
            bottom_y += self.scroll_offset

            if x <= mouse_x <= right_x and y <= mouse_y <= bottom_y:
                button_info["active"] = not button_info["active"]  # Toggle button state

    def active_buttons_list(self):
        """Return a list of currently active buttons."""
        return [info["label"].lower() for info in self.buttons.values() if info["active"]]

    def scroll(self, direction):
        """Scroll the button panel up or down."""
        scroll_step = 50  # Adjust for smoother scrolling
        max_scroll = -(len(self.buttons) * 40) + 400  # Prevent excessive scrolling

        if direction == "up":
            self.scroll_offset = min(self.scroll_offset + scroll_step, 0)
        elif direction == "down":
            self.scroll_offset = max(self.scroll_offset - scroll_step, max_scroll)
