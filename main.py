from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = FastAPI()
class Model(BaseModel):
    text: str

@app.post('/sentiment')
async def sentiment( model:Model):
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(model.text)
    sentiment = None
    if result['compound'] >= 0.05:
        sentiment = 'Positive'
    elif result['compound'] <= 0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return f"the sentiment of your text is {sentiment} with a score of {round(result['compound'],2)}"

if __name__ =='__main__':
    uvicorn.run(app,port=8080,host="0.0.0.0")