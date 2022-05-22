import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5, min_tracking_confidence=0.5, static_image_mode=True
)

# Calculate Angles
def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(
        a[1] - b[1], a[0] - b[0]
    )
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


class Exercise:
    def __init__(self, frame, reps, prev_state):
        self.frame = frame
        self.reps = reps
        self.state = None
        self.prev_state = prev_state
        self.form_hint = None
        self.statemap = [None] * 181
        if self.angles:
            for angle in self.angles:
                state = angle[0]
                angle_range = angle[1]
                for i in range(angle_range[0], angle_range[1] + 1):
                    self.statemap[i] = state
        results = pose.process(self.frame)

        if not results.pose_landmarks:
            return
        landmarks = results.pose_landmarks.landmark
        p1 = [landmarks[self.landmarks[0]].x, landmarks[self.landmarks[0]].y]
        p2 = [landmarks[self.landmarks[1]].x, landmarks[self.landmarks[1]].y]
        p3 = [landmarks[self.landmarks[2]].x, landmarks[self.landmarks[2]].y]

        # calculate angle between self.landmarks
        angle = int(calculate_angle(p1, p2, p3))

        # get current state with self.statemap[angle]
        self.state = self.statemap[angle]

        # set self.reps and self.form_hint
        if self.state:
            self.process(landmarks)

    def process(self, landmarks):
        if self.state == "up" and self.prev_state == "down":
            self.reps += 1
        self.prev_state = self.state


class Pushup(Exercise):
    landmarks = [
        mp_pose.PoseLandmark.LEFT_SHOULDER.value,
        mp_pose.PoseLandmark.LEFT_ELBOW.value,
        mp_pose.PoseLandmark.LEFT_WRIST.value,
    ]
    angles = [("down", (0, 100)), ("up", (150, 180))]

    def process(self, landmarks):
        p1 = [
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
        ]
        p2 = [
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
        ]
        p3 = [
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
        ]
        back_angle = calculate_angle(p1, p2, p3)
        if back_angle < 130:
            self.form_hint = "Straighten your back"
            return
        if self.state == "up" and self.prev_state == "down":
            self.reps += 1
        self.prev_state = self.state
        self.form_hint = None


class Situp(Exercise):
    landmarks = [
        mp_pose.PoseLandmark.LEFT_SHOULDER.value,
        mp_pose.PoseLandmark.LEFT_HIP.value,
        mp_pose.PoseLandmark.LEFT_KNEE.value,
    ]
    angles = [("down", (100, 180)), ("up", (0, 70))]

    def process(self, landmarks):
        if self.state == "down" and self.prev_state == "up":
            self.reps += 1
        self.prev_state = self.state


class BicepCurl(Exercise):
    landmarks = [
        mp_pose.PoseLandmark.LEFT_SHOULDER.value,
        mp_pose.PoseLandmark.LEFT_ELBOW.value,
        mp_pose.PoseLandmark.LEFT_WRIST.value,
    ]
    angles = [("down", (160, 180)), ("up", (0, 30))]


class LegRaise(Exercise):
    landmarks = [
        mp_pose.PoseLandmark.LEFT_SHOULDER.value,
        mp_pose.PoseLandmark.LEFT_HIP.value,
        mp_pose.PoseLandmark.LEFT_KNEE.value,
    ]
    angles = [("down", (160, 180)), ("up", (0, 110))]

    def process(self, landmarks):
        p1 = [
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
        ]
        p2 = [
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
        ]
        p3 = [
            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
            landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
        ]
        knee_angle = calculate_angle(p1, p2, p3)
        if knee_angle < 130:
            self.form_hint = "Straighten your knee"
            return
        if self.state == "up" and self.prev_state == "down":
            self.reps += 1
        self.prev_state = self.state
        self.form_hint = None


class Squat(Exercise):
    landmarks = [
        mp_pose.PoseLandmark.LEFT_HIP.value,
        mp_pose.PoseLandmark.LEFT_KNEE.value,
        mp_pose.PoseLandmark.LEFT_ANKLE.value,
    ]
    angles = [("down", (0, 120)), ("up", (150, 180))]


class_map = {
    "pushup": Pushup,
    "situp": Situp,
    "leg_raise": LegRaise,
    "squat": Squat,
    "bicep_curl": BicepCurl,
}
