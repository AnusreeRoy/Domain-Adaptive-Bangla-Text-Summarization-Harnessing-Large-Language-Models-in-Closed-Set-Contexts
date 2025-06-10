from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, T5Tokenizer

app = Flask(__name__)

#Load the Bangla text summarization model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('midnightGlow/flant5-bangla-tokenizer')
#tokenizer = T5Tokenizer.from_pretrained('midnightGlow/flant5-bangla-tokenizer')
model = AutoModelForSeq2SeqLM.from_pretrained('midnightGlow/flant5_xlsum_bangla')
#model = AutoModelForSeq2SeqLM.from_pretrained('midnightGlow/flant5-xlsum-bangla-sports-domain_model')

def summarize_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    summary_ids = model.generate(inputs["input_ids"], max_length=50, num_beams=5, early_stopping=True, repetition_penalty=2.0,  # Reduce repetition
    length_penalty=1.5, no_repeat_ngram_size=3, temperature=0.7)  # Encourage longer summaries)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])

def summarize():
    data = request.json
    # bangla_text = data['text']
    bangla_text = data.get('text', '')
    print('Received text:', bangla_text)  # Debug print
    summary = summarize_text(bangla_text)
    print('Generated summary:', summary)  # Debug print
    summary = summarize_text(bangla_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)