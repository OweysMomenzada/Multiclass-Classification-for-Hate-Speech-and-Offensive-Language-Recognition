from model import hate_offensive_model
from Crawler import twitterCrawler

from flask import Flask, render_template, request, abort, jsonify

from langdetect import detect
import warnings


app = Flask(__name__)


@app.route("/api", methods=["POST"])
def get_json():
    if request.method == "POST":
        if request.json:
            request_json = request.json
            if 'text' in request_json and 'num_tweets' in request_json:
                json_result = results_json(request_json['text'], request_json['num_tweets'])
                return jsonify(json_result)
            abort(400, 'JSON data missing text field.')
        abort(415)
    abort(405)


def is_english(text: str):
    if detect(text) == 'en':
        return True
    else:
        return False


def get_offensive_hate(tweet: str):
    return hate_offensive_model.predict_lang(tweet)


def get_tweets(hashtag: str, tweets_num: int):
    tweets = twitterCrawler.getTweets(hashtag, max_results=tweets_num)
    tweets = [tweet['text'] for tweet in tweets]
    return tweets


def neutralize_score(valence_hate, valence_offensive, neutral_score):
    if valence_hate > neutral_score:
        valence_hate = valence_hate - neutral_score
    else:
        valence_hate = 0

    if valence_offensive > neutral_score:
        valence_offensive = valence_offensive - neutral_score
    else:
        valence_offensive = 0

    return {'hate': valence_hate, 'offensive': valence_offensive}


def cal_score_labels(label: str, score):
    if score <= 0.7 and score >= 0.5:
        return {"valence_label": 'likely ' + label}
    elif score >= 0.7:
        return {"valence_label": label}
    else:
        return {"valence_label": 'neither'}


def cal_labels(pred):
    neutralized = neutralize_score(pred['hate'], pred['offensive'], pred['neither'])

    if neutralized['hate'] > pred['neither'] and neutralized['hate'] > neutralized['offensive']:
        label = cal_score_labels('hate', neutralized['hate'])
        return label

    if neutralized['offensive'] > pred['neither'] and neutralized['offensive'] > neutralized['hate']:
        label = cal_score_labels('offensive', neutralized['offensive'])
        return label

    if pred['neither'] > neutralized['offensive'] and pred['neither'] > neutralized['hate']:
        label = cal_score_labels('neither', pred['neither'])
        return label


def results_json(hashtag: str, tweets_num: int):
    try:
        twitterCrawler.getTweets(hashtag, max_results=tweets_num)
    except:
        tweets_num = 10
        warnings.warn("tweets must be over or equal to 10. tweets_num is now set to 10.")

    texts = get_tweets(hashtag, tweets_num)
    preds = [get_offensive_hate(text) for text in texts]
    labels = [cal_labels(pred) for pred in preds]
    english_bool = [is_english(text) for text in texts]

    json_res = {'text': texts,
                'label': labels,
                'is_English': english_bool
                }

    return json_res


if __name__ == '__main__':
    app.run(port=9000, debug = True)
