import os
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers

def preprocess_dataset(file_path, dataset_path) :
    dataset, vocab, max_len = [], set(), 0
    # We will use IAM lines dataset
    sentences = open(os.path.join(file_path, "lines.txt"), "r").readlines()
    for line in sentences:
        if line.startswith("#"):
            continue

        line_split = line.split(" ")
        if line_split[1] == "err":
            continue

        folder1 = line_split[0][:3]
        folder2 = line_split[0][:8]
        file_name = line_split[0] + ".png"
        label = line_split[-1].rstrip('\n')

        label = label.replace('|', ' ')
        #print(label)
        #print(file_name)
        rel_path = os.path.join(dataset_path, folder1, folder2, file_name)
        #print(rel_path)

        if not os.path.exists(rel_path):
            #print("not found")
            continue

        dataset.append([rel_path, label])
        vocab.update(list(label))
        max_len = max(max_len, len(label))

    # Splitting the dataset into training and validation sets
    train_set, val_set = train_test_split(dataset, test_size=0.2, random_state=42)

    return train_set, val_set, max_len, vocab
    

if __name__ == "__main__":
    train_set, val_set, max_len, vocab = preprocess_dataset(".\\dataset\\sum_meta\\", ".\\dataset\\IAM-lines\\") 
    print(val_set)

    ### TEMPLATE NOT WORKING FOR NOW ###
    # Define your model
    model = tf.keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, img_channels)),
        layers.MaxPooling2D((2, 2)),
        # Add more layers as needed, like LSTM or GRU for sequence modeling
        layers.Dense(num_classes, activation='softmax')  # Adjust num_classes as per your dataset
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_images, train_labels, epochs=num_epochs, validation_data=(val_images, val_labels))

    # Evaluate the model
    test_loss, test_acc = model.evaluate(test_images, test_labels)
    print('Test accuracy:', test_acc)

    