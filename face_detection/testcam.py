import cv2

## gst-launch-1.0 libcamerasrc ! video/x-raw,format=NV12,width=640,height=480 ! videoconvert ! autovideosink
## python3 -c "import cv2; print(cv2.getBuildInformation())" | grep GStreamer

#def gstreamer_pipeline():
#    return (
#        "libcamerasrc ! video/x-raw,width=640,height=480,framerate=30/1 ! "
#        "videoconvert ! appsink"
#    )

## the gstreamer pipeline config
def gstreamer_pipeline():
    return (
        "libcamerasrc ! video/x-raw,format=NV12,width=640,height=480 ! "
        "videoconvert ! video/x-raw,format=BGR ! appsink"
    )

## Open camera using GStreamer
cap = cv2.VideoCapture(gstreamer_pipeline(), cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("-- ould not open libcamera with GStreamer")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Rpi Camera Preview", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()