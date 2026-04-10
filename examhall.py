import cv2
import time
import winsound

# ---------------- FACE DETECTOR ----------------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- FAST CAMERA START ----------------
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# ---------------- PARAMETERS ----------------
MISSING_FACE_THRESHOLD = 5
SUSPICIOUS_CONFIRM_FRAMES = 1
BEEP_COOLDOWN = 3
SCREENSHOT_DELAY = 5

# ---------------- STATE VARIABLES ----------------
face_missing_frames = 0
suspicious_frames = 0
last_beep_time = 0
last_screenshot_time = 0
confirmed_suspicious = False

# ---------------- MAIN LOOP ----------------
while True:

    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(70, 70)
    )

    # ---------------- CORE LOGIC ----------------
    if len(faces) == 0:
        face_missing_frames += 1
    else:
        face_missing_frames = 0
        suspicious_frames = 0
        confirmed_suspicious = False

    if face_missing_frames > MISSING_FACE_THRESHOLD:
        suspicious_frames += 1
    else:
        suspicious_frames = 0

    confirmed_suspicious = suspicious_frames >= SUSPICIOUS_CONFIRM_FRAMES

    # ---------------- DISPLAY ----------------

    # RED ALERT if suspicious
    if confirmed_suspicious:

        cv2.rectangle(frame,(0,0),(frame.shape[1],60),(0,0,255),-1)

        cv2.putText(
            frame,
            "ALERT: SUSPICIOUS ACTIVITY DETECTED",
            (30,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,255),
            2
        )

    # NORMAL FACE DETECTION
    elif len(faces) > 0:

        x, y, w, h = faces[0]

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(
            frame,
            "NORMAL",
            (x,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    # ---------------- ALERT SYSTEM ----------------
    if confirmed_suspicious:

        now = time.time()

        if now - last_beep_time > BEEP_COOLDOWN:
            winsound.Beep(1500,300)
            last_beep_time = now

        if now - last_screenshot_time > SCREENSHOT_DELAY:
            filename = f"suspicious_{int(now)}.jpg"
            cv2.imwrite(filename, frame)
            last_screenshot_time = now

    # ---------------- INFO PANEL ----------------
    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (20,100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,0),
        2
    )

    cv2.putText(
        frame,
        "AI Exam Hall Monitoring",
        (20,130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (200,200,200),
        2
    )

    # ---------------- SHOW WINDOW ----------------
    cv2.imshow("AI-Based Smart Exam Hall Monitoring", frame)

    # Press ESC to exit
    if cv2.waitKey(1) == 27:
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()