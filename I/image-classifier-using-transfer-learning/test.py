import numpy as np
import matplotlib.pyplot as plt
from train import load_data, create_model, IMAGE_SHAPE, batch_size

# Load the data generators
train_generator, validation_generator, class_names = load_data()

# Construct the model
model = create_model(input_shape=IMAGE_SHAPE)

# Load the optimal weights
model.load_weights("results/MobileNetV2_finetune_last5-loss-0.66.h5")

# Calculate the number of validation steps per epoch
validation_steps_per_epoch = np.ceil(validation_generator.samples / batch_size)

# Print the validation loss & accuracy
evaluation = model.evaluate_generator(validation_generator, steps=validation_steps_per_epoch, verbose=1)
print("Val loss:", evaluation[0])
print("Val Accuracy:", evaluation[1])

# Get a random batch of images
image_batch, label_batch = next(iter(validation_generator))

# Convert the original labels into human-readable text
label_batch = [class_names[np.argmax(label_batch[i])] for i in range(batch_size)]

# Predict the images using the model
predicted_class_names = model.predict(image_batch)
predicted_ids = [np.argmax(predicted_class_names[i]) for i in range(batch_size)]

# Convert the predicted vectors to human-readable labels
predicted_class_names = np.array([class_names[id] for id in predicted_ids])

# Plot the results
plt.figure(figsize=(10, 9))
for n in range(30):
    plt.subplot(6, 5, n + 1)
    plt.subplots_adjust(hspace=0.3)
    plt.imshow(image_batch[n])
    
    # Set the title and color based on correctness
    if predicted_class_names[n] == label_batch[n]:
        color = "blue"
        title = predicted_class_names[n].title()
    else:
        color = "red"
        title = f"{predicted_class_names[n].title()}, correct:{label_batch[n]}"
    
    plt.title(title, color=color)
    plt.axis('off')

_ = plt.suptitle("Model predictions (blue: correct, red: incorrect)")
plt.show()
