import sensor
import time
import ml
import image

# -------------------------
# Camera setup
# -------------------------
sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)  # ✅ GRAYSCALE
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time=2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)

# -------------------------
# Load model
# -------------------------
model = ml.Model("/flash/gesture_model.lite")
print(model)

labels = ["neutral", "finger_mouth", "thumbs_up"]
MODEL_SIZE = 96

clock = time.clock()

while True:
    clock.tick()

    img = sensor.snapshot()

    # Edge Impulse: Fit shortest axis
    w = img.width()
    h = img.height()
    min_dim = min(w, h)

    x = (w - min_dim) // 2
    y = (h - min_dim) // 2

    square = img.copy(roi=(x, y, min_dim, min_dim))


    probs = model.predict([roi])[0].flatten().tolist()

    scores = sorted(zip(labels, probs), key=lambda x: x[1], reverse=True)

    label, confidence = scores[0]

    img.draw_string(
        5, 5,
        "%s: %.2f" % (label, confidence),
        color=255,
        scale=2
    )

    print(clock.fps(), "fps\t", label, confidence)
