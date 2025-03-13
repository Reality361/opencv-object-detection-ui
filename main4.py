import cv2
from gui_buttons import Buttons


def initialize_buttons():
    """Initialize buttons in a scrollable vertical layout."""
    button = Buttons()
    
    start_x = 20
    start_y = 20
    spacing = 40

    categories = [
        "person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
        "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog",
        "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
        "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite",
        "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle",
        "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
        "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa",
        "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote",
        "keyboard", "phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book",
        "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush", "Cola"
    ]

    for index, label in enumerate(categories):
        y_position = start_y + index * spacing
        button.add_button(label, start_x, y_position)

    return button

'''
def mouse_scroll(event, x, y, flags, param):
    """Handle mouse wheel scrolling."""
    if event == cv2.EVENT_MOUSEWHEEL:
        direction = "up" if flags > 0 else "down"
        param.scroll(direction)
'''


def load_model():
    """Load the YOLO object detection model."""
    net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(320, 320), scale=1/255)
    return model


def load_classes(file_path="dnn_model/classes.txt"):
    """Load class labels from file."""
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


def initialize_camera():
    """Initialize and configure the camera."""
    cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 650)
    return cap


def unified_mouse_callback(event, x, y, flags, param):
    """
    Handle both button clicks and mouse scrolling in a single function.
    """
    button = param

    if event == cv2.EVENT_LBUTTONDOWN:  # Handle button click
        button.button_click(x, y)
    
    elif event == cv2.EVENT_MOUSEWHEEL:  # Handle mouse scroll
        direction = "up" if flags > 0 else "down"
        button.scroll(direction)


def main():
    # Initialization
    button = initialize_buttons()
    model = load_model()
    classes = load_classes()
    cap = initialize_camera()
    colors = button.colors

    print("Available object categories:", classes)

    # Create OpenCV window
    cv2.namedWindow("Object Detection")
    cv2.setMouseCallback("Object Detection", unified_mouse_callback, param=button)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame.")
            break

        # Get active buttons list
        active_categories = button.active_buttons_list()

        # Object detection
        class_ids, scores, bboxes = model.detect(frame, confThreshold=0.3, nmsThreshold=0.4)

        for class_id, score, bbox in zip(class_ids, scores, bboxes):
            x, y, w, h = bbox
            class_name = classes[class_id]
            color = colors[class_id]

            if class_name in active_categories:
                cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 5)

        # Display buttons and frame
        button.display_buttons(frame)
        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
