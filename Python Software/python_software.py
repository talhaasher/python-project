       
import cv2 as cv
from tkinter import *

def imag_to_sketch():
    image_link=input("image link:")
    image_link = image_link.replace("\\", "/")  # Replace single backslashes with forward slashes
    image_conversion_1 = cv.cvtColor(image_link, cv.COLOR_BGR2GRAY)
    image_invesrion = cv.bitwise_not(image_conversion_1)
    bluriing = cv.GaussianBlur(image_invesrion, (21,21), 0)
    invert_blur = cv.bitwise_not(bluriing)
    sketch = cv.divide(image_invesrion, invert_blur, scale=256.0)
    cv.imwrite("Sketch4.png", invert_blur)

def watermark():
    logos=input("link for logo that will be the watermark:")
    logos = logos.replace("\\", "/")  
    watermark_logo = cv.imread(logos)
    img_to_watermark=input("link for image that will be the watermarked:")
    img_to_watermark = img_to_watermark.replace("\\", "/")  
    img = cv.imread(img_to_watermark)
    h_logos, w_logos, _ = logos.shape
    h_img_to_watermark, w_img_to_watermark, _ = img_to_watermark.shape
    center_y = int(h_logos/2)
    center_x = int(w_logos/2)
    top_y = center_y - int(h_logos/2)
    left_x = center_x - int(w_logos/2)
    bottom_y = top_y + h_logos
    right_x = left_x + w_logos
    final_destination = img[top_y:bottom_y, left_x:right_x]
    fianl_imsge = cv.addWeighted(final_destination, 1, logos, 0.5, 0)
    img[top_y:bottom_y, left_x:right_x] = fianl_imsge
    cv.imwrite("watermarked.jpg", img)
    cv.imshow("Watermarked Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()




def display_menu():
    print("Select an option:")
    print("1. images to sketch ")
    print("2. watermark picture")
    print("0. Exit")

    choice = input("Enter the number of your choice: ")
    return choice


def main():
    while True:
        choice = display_menu()

        if choice == '1':
            imag_to_sketch()
        elif choice == '2':
            watermark()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()