import pandas as pd

# Function to generate final output
def generate_final_output(image_path, data):
    # Load the original image
    image = cv2.imread(image_path)

    # Draw bounding boxes and labels
    for object_id, obj_data in data.items():
        box = obj_data['box']
        label = obj_data['description']
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        cv2.putText(image, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Save the annotated image
    output_image_path = 'output_image.jpg'
    cv2.imwrite(output_image_path, image)

    # Create a table of data
    df = pd.DataFrame.from_dict(data, orient='index')
    output_table_path = 'output_table.csv'
    df.to_csv(output_table_path)

    return output_image_path, output_table_path

# Example usage
output_image_path, output_table_path = generate_final_output('input_image.jpg', data)
