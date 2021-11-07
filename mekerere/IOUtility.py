import cv2 as cv


def crop_and_resize_on_bounding_box(filename, x_coord, y_coord, height, width):
    image = cv.imread(filename)
    cropped_image = image[y_coord:y_coord + height, x_coord:x_coord + width]
    width = int(image.shape[1])
    height = int(image.shape[0])
    dimension = (width, height)
    resized = cv.resize(cropped_image, dimension, interpolation=cv.INTER_AREA)
    return resized
