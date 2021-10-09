import os
import cv2

class CreateData:
    def __init__(self, max_count = 100, image_size = 224):
        self.max_count = max_count
        self.image_size = image_size

    def run(self, save_path_dir):
        self._init_dir(save_path_dir = save_path_dir)


    def _init_dir(self, save_path_dir):
        if os.path.isdir(save_path_dir) == False:
            os.mkdir(save_path_dir)

        self.save_path_dir = save_path_dir
        image_count = self._record()

        print(f"Total image saved {image_count}")

    def _record(self):
        image_count = 0
        cam =  cv2.VideoCapture(0)

        while image_count < self.max_count:
            ret, frame = cam.read()

            if ret == False:
                break

            resize_frame =  cv2.resize(frame, (self.image_size, self.image_size))

            cv2.imshow("frame", resize_frame)
            cv2.waitKey(1)

            image_path = os.path.join(self.save_path_dir, f"{image_count}.jpg")
            cv2.imwrite(image_path, resize_frame)

            image_count += 1


            print(f"{image_count} / {self.max_count}")

        return image_count
