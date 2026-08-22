import cv2

class ImageProcessor:
    def __init__(self, image_path):
        self.image_path = image_path
        # Read image using OpenCV (BGR format)
        self.img = cv2.imread(self.image_path)
        
        if self.img is None:
            raise FileNotFoundError(f"Could not load image at '{image_path}'. Check path!")

        # Unpack image dimensions: height (y), width (x), channels (color)
        self.height, self.width, self.channels = self.img.shape

    def resize_image(self, scale_percent=50):
        """Resizes the image by a percentage scale."""
        new_width = int(self.width * scale_percent / 100)
        new_height = int(self.height * scale_percent / 100)
        resized_img = cv2.resize(self.img, (new_width, new_height))
        return resized_img

    def split_into_four_quadrants(self):
        """Splits image dynamically into 4 equal quadrant crops."""
        mid_y = self.height // 2
        mid_x = self.width // 2

        quadrants = {
            "Top-Left": self.img[0:mid_y, 0:mid_x],
            "Top-Right": self.img[0:mid_y, mid_x:self.width],
            "Bottom-Left": self.img[mid_y:self.height, 0:mid_x],
            "Bottom-Right": self.img[mid_y:self.height, mid_x:self.width]
        }
        return quadrants

    def process_and_display(self):
        """Displays original, resized, and cropped quadrant windows."""
        print(f"📷 Loaded Image Dimensions: {self.height}x{self.width} ({self.channels} channels)")

        # 1. Display Original
        cv2.imshow("Original Image", self.img)

        # 2. Resize and Display
        resized = self.resize_image(scale_percent=50)
        cv2.imshow("Resized Image (50%)", resized)

        # 3. Dynamic Quadrant Cropping & Display
        crops = self.split_into_four_quadrants()
        for title, crop_img in crops.items():
            cv2.imshow(title, crop_img)

        print("Press any key on an image window to close...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# --- Execution ---
if __name__ == "__main__":
    # Replace with your image file name or path
    image_file = "islamic2.jpg"
    
    try:
        processor = ImageProcessor(image_file)
        processor.process_and_display()
    except Exception as e:
        print(f"Error: {e}")
