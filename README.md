# Data Science & AI - Learning Journey

This is where I'm tracking my path toward becoming a data scientist / ML engineer. I'm not following a fixed day count - some topics take me a few hours, some take a couple of weeks, and that's fine. What matters is what I can actually do by the end of each module, not how fast I got there.

Each folder in this repo has two things:
- notes.md - what I learned, written in my own words
- practice.py (or a notebook) - actual code proving I can use it, not just read about it

Folders are only created once I'm actually working on that topic. The roadmap below is the full plan, but most of it is still just a plan.

## Roadmap

### Phase 1: Foundations
- Python core (syntax, data structures, control flow, functions) - Done
- Error handling and file handling - Next
- (Software basics: git/GitHub, virtual environments, working with APIs - picked up as needed, not a separate phase)

### Phase 2: Data Wrangling
- Pandas and NumPy - loading messy data, cleaning it, answering basic questions
- SQL - querying, joins, working with databases from Python

### Phase 3: Math & Stats
- Linear algebra - vectors, matrices, the basics behind ML math
- Calculus - derivatives, gradients, optimization intuition
- Probability - distributions, Bayes' theorem
- Statistics - the stuff that turns raw numbers into actual conclusions

### Phase 4: ML Core
- ML fundamentals - what ML actually is, types of problems, train/test splits, loss vs metrics
- Feature engineering - turning raw data into something a model can use
- ML algorithms - linear models, trees, ensembles, boosting, clustering, dimensionality reduction
- Advanced concepts - hyperparameter tuning, imbalanced data, interpretability (SHAP/LIME)

### Phase 5: Applied ML
- End-to-end projects - the classics (Titanic, house prices, churn) plus real practice problems
- NLP - text preprocessing, representation (TF-IDF), traditional models, full pipeline
- Computer vision - image basics, feature detection, transformations, full pipeline

### Phase 6: Deep Learning
- Neural network foundations - how they actually learn, backpropagation
- Optimizing a neural network - optimizers, regularization, training practices
- CNNs and transfer learning
- Sequence models - RNN, LSTM, GRU
- Seq2Seq and Transformers - the architecture behind every modern LLM
- PyTorch - actually building and training all of the above
- NLP and computer vision using deep learning - embeddings, object detection, segmentation, ViT

### Phase 7: ML Engineering
- ML system design - problem formulation, data/feature systems, evaluation, serving, monitoring
- MLOps - data versioning, experiment tracking, pipelines, CI/CD, monitoring, retraining
- MLOps for deep learning - distributed training, checkpointing, large model storage, optimized inference

### Phase 8: Modern AI
- LLMs and GenAI - fine-tuning vs prompting, RAG, agents, LangChain, Hugging Face
- Cloud platforms - Azure / AWS / Databricks, running notebooks and tracking experiments at scale

## Why this order

Each phase sits on top of the one before it. You can't do feature engineering well without knowing pandas. You can't do ML system design without having actually built a few models first. Deep learning needs the math from Phase 3. LLMs and GenAI come last on purpose - they're most useful once I understand what's happening underneath, so I can actually direct them instead of blindly trusting them.

## Current focus

Error handling and file handling, right before starting Pandas and NumPy.
