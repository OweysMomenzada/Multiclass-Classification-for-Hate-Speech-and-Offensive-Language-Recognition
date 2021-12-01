# Multiclass Classification for Hate-Speech and Offensive Language Recognition based on Tweets



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
