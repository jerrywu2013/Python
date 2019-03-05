# Chatbot Startkit in TensorFlow 1.4

The example on how to implement simple chatbot using seq2seq model in the python using tensorflow 1.4 version. This Chatbot example shows
the attention mechanism and bucketing as well.

## Dataset

I've used the Cornell Movie Dialogs corpuse for this example. You can download it: [here](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html) 

## Install

### &nbsp;&nbsp;&nbsp; Supported Python version
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Python version used in this project: 3.5+

### &nbsp;&nbsp;&nbsp; Libraries used

> *  [Pandas](http://pandas.pydata.org) 0.18.0
> *  [Numpy](http://www.numpy.org) 1.10.4
> *  [TensorFlow](https://www.tensorflow.org) 1.4.0

## Code

The core seq2seq model functions are all insude **model_utils.py**.

Data preprocessing and NLP functions are inside **cornell_data_utils.py**.

If you want to play with models hyperparameters use **config.py**.

## Run

To run this project you will need some software, like Anaconda, which provides support for running .ipynb files (Jupyter Notebook).

After making sure you have that, you can run from a terminal or cmd next lines:

`ipython notebook chatbot.ipynb`

or

`jupyter notebook chatbot.ipynb`


## License

IT License

Copyright (c) 2017 Luka Anicin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
