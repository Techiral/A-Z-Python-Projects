<h2>Data preprocessing:</h2>

This part loads the Fashion MNIST dataset using TensorFlow Datasets and applies some preprocessing steps to the data. The steps are:

Scale the image pixel values between 0 and 1.
Cache the dataset in memory.
Shuffle the dataset.
Batch the dataset into batches of 128 images.
Prefetch the dataset to optimize processing.


<h2>Data visualization:</h2>

This part of the code displays a sample of 4 images from the dataset using Matplotlib.
![image](https://user-images.githubusercontent.com/43640144/226197723-a46627e2-69b5-47d5-82b2-e6dd926995d4.png)
These are images that are present in the Fashion dataset.

<h2>Neural Network:</h2>

This part of the code defines the neural network architecture for the GAN model. The architecture consists of two main parts, the generator and the discriminator. The generator generates fake images from random noise, and the discriminator tries to distinguish between the generated fake images and the real images from the dataset. The GAN model trains both the generator and discriminator simultaneously, with the goal of making the generated images indistinguishable from the real images.

<h3>The generator architecture:</h3>

A fully connected layer that takes in 128 random values and reshapes them to 7x7x128.
A leaky ReLU activation function is applied to the fully connected layer output.
The output is then reshaped to 7x7x128.
Two upsampling blocks are added, which double the size of the feature maps.
Two convolutional blocks are added, which perform 2D convolution with 128 filters and 4x4 kernel size, and apply the leaky ReLU activation function to the output.
The final layer is a 2D convolutional layer with 1 filter, 4x4 kernel size, and sigmoid activation function that generates the fake image.
The discriminator architecture:

Two convolutional blocks, each consisting of a 2D convolutional layer with 128 filters, 4x4 kernel size, and leaky ReLU activation function.
Flatten the output of the second convolutional block to a 1D array.
A fully connected layer with 1 output that uses sigmoid activation function to distinguish between the real and fake images.
![image](https://user-images.githubusercontent.com/43640144/226197850-2b41d0a7-1c73-4bc6-bd89-152aa4bd21f3.png)
These are the images that are the output of an untrained generator
<h2>The Discriminator</h2>
 It consists of four convolutional layers followed by two fully connected layers.

The input to the discriminator is an image of size 64x64x3, where 64x64 is the height and width of the image, and 3 represents the RGB color channels. The first convolutional layer has 64 filters of size 4x4 with a stride of 2 and a LeakyReLU activation function. The second convolutional layer has 128 filters of size 4x4 with a stride of 2 and batch normalization. The third convolutional layer has 256 filters of size 4x4 with a stride of 2 and batch normalization. The fourth convolutional layer has 512 filters of size 4x4 with a stride of 2 and batch normalization.

After the fourth convolutional layer, the output is flattened and passed through two fully connected layers. The first fully connected layer has 1024 units with a LeakyReLU activation function and dropout. The output of the first fully connected layer is then passed through another fully connected layer with a single output unit and a sigmoid activation function, which outputs a value between 0 and 1, indicating the probability that the input image is real.

Overall, the discriminator architecture is designed to take an image as input and output a probability indicating whether the image is real or fake. It uses a series of convolutional layers to extract features from the image and then passes those features through two fully connected layers to produce the final output.
<h2>Data training:</h2>

This part of the code trains the GAN model using the Fashion MNIST dataset. The training loop consists of the following steps:

Generate random noise as input for the generator.
Use the generator to generate fake images from the random noise.
Combine the generated fake images with real images from the dataset to form a batch.
Train the discriminator on the batch, using binary cross-entropy loss to classify the images as real or fake.
Generate new random noise for the generator.
Train the GAN model on the new random noise, using binary cross-entropy loss to classify the generated images as real or fake, and using the Adam optimizer to minimize the loss.

<h2> Results</h2>
Overall, the generator seems to perform good after approximately 2000 epochs. The loss of the discriminator and the generator become stable after these number of epochs.

![Screenshot 2023-03-19 234910](https://user-images.githubusercontent.com/43640144/226198493-d56d549c-43ac-4eb7-b9f7-ab575150a071.png)


Thse are the images produced by the GAN model
![image](https://user-images.githubusercontent.com/43640144/226198442-e8a5ff7c-0643-4ebe-957e-b160c8181188.png)


