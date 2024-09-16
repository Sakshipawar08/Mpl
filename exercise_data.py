# exercise_data.py

EXERCISES = {
    "squats": {
        "keypoints": ["left_hip", "left_knee", "left_ankle", "right_hip", "right_knee", "right_ankle", "left_shoulder", "right_shoulder"],
        "angles": [
            ("hip_knee_angle", "left_hip", "left_knee", "left_ankle"),
            ("knee_ankle_angle", "left_knee", "left_ankle", "left_hip"),
            ("back_angle", "left_shoulder", "left_hip", "left_knee")
        ],
        "phases": {
            "standing": {
                "hip_knee_angle": {"min": 160, "max": 180},
                "knee_ankle_angle": {"min": 80, "max": 100},
                "back_angle": {"min": 170, "max": 190}
            },
            "squatting": {
                "hip_knee_angle": {"min": 70, "max": 100},
                "knee_ankle_angle": {"min": 60, "max": 80},
                "back_angle": {"min": 170, "max": 190}
            }
        },
        "rep_conditions": {
            "start": "standing",
            "middle": "squatting",
            "end": "standing"
        },
        "mistakes": [
            {
                "name": "not_low_enough",
                "condition": lambda angles, phase: phase == "squatting" and angles["hip_knee_angle"] > 100,
                "message": "Squat lower to reach the correct depth"
            },
            {
                "name": "knees_over_toes",
                "condition": lambda angles, phase: angles["knee_ankle_angle"] < 70,
                "message": "Keep your knees behind your toes"
            },
            {
                "name": "back_not_straight",
                "condition": lambda angles, phase: abs(angles["back_angle"] - 180) > 15,
                "message": "Keep your back straight throughout the movement"
            }
        ]
    },
    "pushups": {
        "keypoints": ["left_shoulder", "left_elbow", "left_wrist", "right_shoulder", "right_elbow", "right_wrist", "left_hip", "right_hip"],
        "angles": [
            ("arm_angle", "left_shoulder", "left_elbow", "left_wrist"),
            ("body_angle", "left_shoulder", "left_hip", "left_ankle")
        ],
        "phases": {
            "up": {
                "arm_angle": {"min": 160, "max": 180},
                "body_angle": {"min": 170, "max": 190}
            },
            "down": {
                "arm_angle": {"min": 70, "max": 110},
                "body_angle": {"min": 170, "max": 190}
            }
        },
        "rep_conditions": {
            "start": "up",
            "middle": "down",
            "end": "up"
        },
        "mistakes": [
            {
                "name": "not_low_enough",
                "condition": lambda angles, phase: phase == "down" and angles["arm_angle"] > 110,
                "message": "Lower your chest closer to the ground"
            },
            {
                "name": "hips_too_high",
                "condition": lambda angles, phase: abs(angles["body_angle"] - 180) > 15,
                "message": "Keep your body in a straight line"
            }
        ]
    }
}