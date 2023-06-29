# Folk.AI

## Web App for Classifying Between Chhau and Kathakali- Two Folk Dance Forms of India Using Artificial Intelligence

\[**NOTE**: After Heroku's pricing changes, this app is no longer hosted. \]

## About

[Chhau][1] and [Kathakali][2] are two folk dance forms of India. They use
very colorful and exotic costiumes for the dances.

![chhau-dance][3]
*Chhau Dance*- Photo from [Wikimedia Commons][4]

![kathakali-dance][5]
*Kathakali Dance*- Photo from [Wikimedia Commons][6]

### How to Use This App

Go to [folk-ai.herokuapp.com][7] to use this web app.
Upload an image of either Kathakali or Chhau dance, and this web app will
predict the dance form using Artificial Intelligence.

### Technology

This project uses fast.ai and PyTorch libraries. This is a project of
Computer Vision using **Convolutional Neural Network**, specifically, a
**ResNet-34** model.

This project levarages transfer learning.

### Requirements

This project uses older versions of PyTorch, torchvision and fastai library.
See `requirements.txt` file more details.

[1]: https://en.wikipedia.org/wiki/Chhau_dance
[2]: https://en.wikipedia.org/wiki/Kathakali
[3]: https://upload.wikimedia.org/wikipedia/commons/d/d5/Chhau_dance.jpg
[4]: https://en.wikipedia.org/wiki/Chhau_dance#/media/File:Chhau_dance.jpg
[5]: https://upload.wikimedia.org/wikipedia/commons/1/1c/Kadhakali_at_Kerala_state_school_kalothsavam_2019_3.jpg
[6]: https://en.wikipedia.org/wiki/Kathakali#/media/File:Kadhakali_at_Kerala_state_school_kalothsavam_2019_3.jpg
[7]: https://folk-ai.herokuapp.com
