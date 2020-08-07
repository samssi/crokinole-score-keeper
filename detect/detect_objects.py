from render import hough_circles as renderer
import cv2


def detectCircles(frame):
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # grayscale = cv2.medianBlur(grayscale, 5)
    # grayscaleWithBlur = cv2.GaussianBlur(grayscale, (15,15), 0)

    line15 = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1, 100, param1=50,
                              param2=30, minRadius=130, maxRadius=140)
    line10 = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1, 100, param1=50,
                              param2=47, minRadius=275, maxRadius=280)
    line5 = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1.2, 500, param1=50,
                             param2=30, minRadius=430, maxRadius=435)

    button = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                              param2=30, minRadius=20, maxRadius=25)
    # bank = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=18, maxRadius=30)
    # hole = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=15, maxRadius=17)

    renderer.store_circles(frame, "5", line5, 200, 200, 0)
    renderer.store_circles(frame, "10", line10, 0, 200, 200)
    renderer.store_circles(frame, "15", line15, 200, 0, 200)

    renderer.store_circles(frame, "button", button, 0, 255, 0)
    # renderCircles(frame, bank, 0, 51, 255)
    # renderCircles(frame, hole, 255, 0, 51)

    return frame
