import os
import sqlite3
from uuid import uuid4

# database to store object metadata
conn = sqlite3.connect('objects.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS objects
             (id TEXT PRIMARY KEY, master_id TEXT, label INTEGER, file_path TEXT)''')
conn.commit()

# Function to extract and save objects
def extract_and_save_objects(image_path, masks, boxes, labels):
    master_id = str(uuid4())
    os.makedirs(master_id, exist_ok=True)

    for i in range(masks.shape[0]):
        mask = masks[i, 0]
        masked_image = np.array(Image.open(image_path).convert("RGB"))
        masked_image[mask == 0] = 0
        object_id = str(uuid4())
        object_path = os.path.join(master_id, f'object_{i}.png')
        Image.fromarray(masked_image).save(object_path)

        #  metadata in the database
        c.execute("INSERT INTO objects (id, master_id, label, file_path) VALUES (?, ?, ?, ?)",
                  (object_id, master_id, int(labels[i]), object_path))
        conn.commit()

extract_and_save_objects('input_image.jpg', masks, boxes, labels)
