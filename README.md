# Domain-Adaptive-Bangla-Text-Summarization-Harnessing-Large-Language-Models-in-Closed-Set-Contexts

Created a custom dataset for text summarization on Bangla news from online news media like-‘ BBC Bangla,’ ‘The Daily Star,’ ‘Jugantor’ & Prothom Alo’ by collecting the title and the whole text with the help of ‘Beautiful Soup’- a Python library through web-scraping. The dataset has four columns- category, title, text, and summary (referring to the gist of the text). The category column was manually annotated into seven categories- Sports, International, State, Entertainment, Economy, Education, and Technology. The dataset has 21k rows.
Developed a custom tokenizer for the Bengali language (T5-based).
Developed Bangla text summarization model with LLMs- mT5, flanT5 on xlsum dataset(Bengali).
flanT5 and mT5 Bangla text summarization models were trained for Domain Adaptation on the BanglaMCT7 dataset as a source and the custom dataset as a target. For closed-set domain adaptation, 3 domains were selected- state, international, and sports for both source and target, where the source and target domains share the same categories with no missing or extra label in either of the domains. The models were evaluated on rouge, bleu, and best scores, and the flanT5-sports-domain_model performed well with a competitive rouge score of 0.79.

The models were evaluated on zero-shot settings in 3 domains: state, international, and sports. The flant5-international-domain_model scored a rouge score of 0.67, showing its capability to perform well under zero-shot conditions. 

Datasets:
Custom dataset: https://huggingface.co/datasets/midnightGlow/BanglaSumXL_Categories
BanglaMCT&: https://www.kaggle.com/datasets/shohanursobuj/banglamct

Models Used:
flant5: https://huggingface.co/google/flan-t5-small
mt5: https://huggingface.co/google/mt5-base


