from flask import Flask, render_template, request, jsonify, send_from_directory
from ultralytics import RTDETR
import os

app = Flask(__name__)

# Load trained RT-DETR model
model = RTDETR("model/best.pt")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():

    image = request.files.get("image")

    if image is None:
        return jsonify({
            "message": "No image received"
        })

    # Create folders
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("results", exist_ok=True)

    # Save uploaded image
    image_path = os.path.join("uploads", image.filename)
    image.save(image_path)

    print("Image received:", image.filename)

    # Run RT-DETR detection
    results = model.predict(
        source=image_path,
        conf=0.45
    )

    result = results[0]

    # Count detected packets
    count = len(result.boxes)

    print("Packets detected:", count)

    # Create annotated image
    annotated_image = result.plot()

    # Save annotated image
    result_filename = "detected_" + image.filename
    result_path = os.path.join("results", result_filename)

    import cv2
    cv2.imwrite(result_path, annotated_image)

    print("Processed image saved:", result_path)

    return jsonify({
        "message": "Detection completed!",
        "count": count,
        "result_image": result_filename
    })
@app.route("/results/<path:filename>")
def results(filename):
    return send_from_directory("results", filename)

if __name__ == "__main__":
    app.run(debug=True)