# Realtime Hate-Speech and Offensive Language Recognition based on Multiclass Classification

This is a small project for DeepLearning in NLP at the University of Hamburg.
We build a Multi-Classifier for Hate-Speech and Offensive Language detection based on TensorFlow.

##### See \train\"Feature Engeneering & Training & Evaluation.ipynb" for our notebook, which contains data, preprocessing, modelling and evaluation.

#### Requirements
Please install the following python-packages:
```
tensorflow==2.5.0
flask==2.0.2
tweepy==4.3.0
numpy==1.14.6 (or higher)
pandas==0.25.0 (or higher)
scikit-learn==1.0.1
pickle==3.10.0
langdetect==1.0.9
```

#### Get the saved model:
Please pull the directory <i>./train</i> and run the notebook: <i>Feature Engeneering & Training.ipynb</i>. 
To get the pretrained model  this can take up to 60 minutes on CPU or download the tf-files from the link below and the files to the "model_pretrain" directory.
Link to the tf-files: https://drive.google.com/drive/folders/1AbWssjhX21dl0X45d5sJnL_oviEWswPI?usp=sharing


#### Output:
Since we work with a FLASK API we will get an output via endpoint. For example, please see the notebook <i>Application text.ipynb</i>.

The json file output of the API looks as follows:
```
    {'text': texts,
     'label': labels,
     'is_English': english_bool
    }
```

#### Result:
We used a 25% to 75% test-train split. Please note that the given notebook has no evaluation since we only provide this to get the tf-files.
We could recieve an accuracy of over 85% percent.


#### Model:
We could notice that a transformer model, such as BERT, could not increase our accuracy significantly enough. Therefore, we used the 
LSTM model because of the decent results in performance and accuracy.

#### Evaluation:
Since we used different datasets you may think that our model performed bad in some cases. However, we could actually get a decent accuracy (apprx. 90%) on 
all dataset. That means we predicted each dataset as a testset separately. For more insight into that approach, please take a look into the notebook <i> Feature Engineering & Training & Evaluation.ipnby</i>

#### Dataset
We used the following Datasets:
```
@inproceedings{hateoffensive,
  title = {Automated Hate Speech Detection and the Problem of Offensive Language},
  author = {Davidson, Thomas and Warmsley, Dana and Macy, Michael and Weber, Ingmar}, 
  booktitle = {Proceedings of the 11th International AAAI Conference on Web and Social Media},
  series = {ICWSM '17},
  year = {2017},
  location = {Montreal, Canada},
  pages = {512-515}
  }
  
```

```
@misc{qian2019benchmark,
      title={A Benchmark Dataset for Learning to Intervene in Online Hate Speech}, 
      author={Jing Qian and Anna Bethke and Yinyin Liu and Elizabeth Belding and William Yang Wang},
      year={2019},
      eprint={1909.04251},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
