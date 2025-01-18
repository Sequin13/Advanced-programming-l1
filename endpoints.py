from flask import Flask, request, jsonify
from producer import publish_messages, publish_url_image, publish_uploaded_image, publish_image_multiple_times
import json
import os

app = Flask(__name__)

TASK_STATUS_FILE = "task_status.json"
UPLOAD_FOLDER = "input_images"

if os.path.exists(TASK_STATUS_FILE):
    with open(TASK_STATUS_FILE, 'w') as file:
        json.dump({}, file)


@app.route('/get-example_images', methods=['GET'])
def get_example_images():
    publish_messages()
    return jsonify({"status": "started processing images"})


@app.route('/process-url-image', methods=['GET'])
def process_url_image():
    image_url = request.args.get('url')
    if not image_url:
        return jsonify({"error": "URL parameter is missing"}), 400

    message_id = publish_url_image(image_url)
    if message_id:
        return jsonify({"message_id": message_id}), 200


@app.route('/get-task-status', methods=['GET'])
def get_task_status():
    task_id = request.args.get('id')

    with open(TASK_STATUS_FILE, "r") as json_file:
        task_status = json.load(json_file)

    if task_id:
        task_id = str(task_id)
        if task_id in task_status:
            return jsonify({task_id: task_status[task_id]})
        else:
            return jsonify({"error": f"Task ID {task_id} not found."}), 400

    return jsonify(task_status)


@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(file_path)

    message_id = publish_uploaded_image(file_path)
    if message_id:
        return jsonify({"message_id": message_id}), 200
    else:
        return jsonify({"error": "Failed to enqueue task"}), 500



@app.route('/run-multiple', methods=['GET'])
def run_multiple():
    publish_image_multiple_times("input_images\\CrossWalk_(5465840138).jpg", 10)
    return {"running": "ok"}


if __name__ == '__main__':
    app.run(debug=True)
