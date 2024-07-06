class ImageRegion:
    def __init__(
        self, start_x_ratio=0.5, start_y_ratio=0.05, end_x_ratio=0.75, end_y_ratio=0.95
    ):
        self.start_x_ratio = start_x_ratio
        self.start_y_ratio = start_y_ratio
        self.end_x_ratio = end_x_ratio
        self.end_y_ratio = end_y_ratio
