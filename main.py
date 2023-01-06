import contur_detection as ctr
import color_detection as clr
import contrast_detection as cst
import depth_estimation as de
import ai_mobilenet as aim
import template_matching as tm
import test_run as tr

# Notice: You can stop the program by pressing "0"

# Choose the method by changing the number corresponding to the entry in the elif-statement
method = 7
# Choose 0 or 1 to change the camera (in some cases it may be 2)
camera = 0

if method == 1:
    print("Using contur_detection:")
    ctr.circles(camera, 2, 400, 250, 20, 8, 12)

    # Parameters are:
    # dp                -->     inverse ratio of the accumulator resolution to the image resolution
    # minDist           -->     minimum distance between the centers of the circles
    # edgeValue         -->     higher threshold of the two passed to the Canny edge detector
    # roundness         -->     the smaller this is, the more false circles may be detected
    # minRadius         -->     minimum circle radius
    # maxRadius         -->     maximum circle radius

elif method == 2:
    print("Using color_detection:")
    clr.color(camera, 50)  # red ball
    # clr.color(camera, 16)  # black ball

    # Parameters are:
    # variance          -->     value distance around average detected color that is classified as valid

elif method == 3:
    print("Using contrast_detection:")
    cst.contrast(camera, 150, 125, 4, 2, 40, 300)  # red ball
    # cst.contrast(camera, 95, 125, 4, 2, 40, 320)  # black ball

    # Parameters are:
    # thresh            -->     lower threshold from which a pixel is displayed white
    # maxval            -->     upper threshold til which a pixel is displayed white
    # order             -->     order of the ellipse matrix, which is used to search
    # iterations        -->     number of iterations to use the bit-mask
    # min_area          -->     minimum area of the circles
    # max_area          -->     maximum area of the circles

elif method == 4:
    print("Using template_matching:")
    tm.matching(camera)

elif method == 5:
    print("Using depth_estimation:")
    de.depth(camera, 2, 400, 250, 50, 8, 30)

    # Parameters are:
    # dp                -->     inverse ratio of the accumulator resolution to the image resolution
    # minDist           -->     minimum distance between the centers of the circles
    # edgeValue         -->     higher threshold of the two passed to the Canny edge detector
    # roundness         -->     the smaller this is, the more false circles may be detected
    # minRadius         -->     minimum circle radius
    # maxRadius         -->     maximum circle radius

elif method == 6:
    print("Using ai_mobilenet:")
    aim.ai(camera, 0.17)

elif method == 7:
    print("Using test_run")
    tr.test(camera)

else:
    print("Please choose an existing method")
    print("1 --> contur_detection")
    print("2 --> color_detection")
    print("3 --> contrast_detection")
    print("4 --> template_matching")
    print("5 --> depth_estimation")
    print("6 --> ai_mobilenet")
    print("7 --> test_run")
