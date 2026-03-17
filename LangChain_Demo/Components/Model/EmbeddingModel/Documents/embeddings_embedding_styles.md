# Embeddings & Embedding Styles (Embeddings.md)

## 1. What are Embeddings?
Embeddings are **numerical vector representations** of data (text, images, audio) that capture meaning and relationships in a continuous vector space.

### Key Idea:
> Similar meaning → Similar vectors (closer in space)

### Example:
- "king" → [0.21, -0.11, 0.87, ...]
- "queen" → [0.19, -0.10, 0.85, ...]

---

## 2. Why Embeddings are Important?
- Enable semantic search
- Power recommendation systems
- Support clustering & classification
- Foundation for Retrieval-Augmented Generation (RAG)

---

## 3. High-Level Diagram

```
Raw Data (Text / Image / Audio)
            │
            ▼
     Embedding Model
            │
            ▼
     Vector Representation
            │
            ▼
   Vector Database / Index
            │
            ▼
   Search / Similarity / ML Tasks
```

---

## 4. Types of Embeddings (by Data Modality)

### 4.1 Text Embeddings
Represent words, sentences, or documents as vectors.

**Examples:** Word2Vec, GloVe, BERT embeddings

---

### 4.2 Image Embeddings
Represent images as vectors capturing visual features.

**Examples:** CNN features, CLIP

---

### 4.3 Audio Embeddings
Represent sound/audio patterns.

**Examples:** Speech2Vec, wav2vec

---

### 4.4 Multimodal Embeddings
Combine multiple data types (text + image, etc.).

**Examples:** CLIP, Gemini-style models

---

## 5. Types of Text Embedding Styles

### Classification Diagram

```
Text Embedding Styles
│
├── 1. Word-Level Embeddings
│   ├── Word2Vec
│   ├── GloVe
│   └── FastText
│
├── 2. Contextual Embeddings
│   ├── BERT
│   ├── RoBERTa
│   └── GPT Embeddings
│
├── 3. Sentence Embeddings
│   ├── Sentence-BERT
│   └── Universal Sentence Encoder
│
└── 4. Document Embeddings
    ├── Doc2Vec
    └── Transformer-based pooling
```

---

## 6. Word-Level Embeddings

- Each word has a fixed vector
- Does not change with context

### Example:
- "bank" (river vs finance) → Same vector ❌

**Models:** Word2Vec, GloVe, FastText

---

## 7. Contextual Embeddings

- Vector depends on context
- Same word → Different vectors

### Example:
- "bank" (river) ≠ "bank" (finance)

**Models:** BERT, GPT

---

## 8. Sentence Embeddings

- Entire sentence represented as a single vector
- Useful for similarity & search

### Example:
- "I love AI" ≈ "I like artificial intelligence"

---

## 9. Document Embeddings

- Represent full paragraphs/documents
- Used in search engines & RAG systems

---

## 10. How Similarity Works

Common similarity measures:

- Cosine Similarity
- Euclidean Distance
- Dot Product

### Example (Cosine Similarity):
```
Similarity(A, B) = (A · B) / (||A|| ||B||)
```

---

## 11. Embeddings Workflow (RAG Example)

```
User Query
   │
   ▼
Convert to Embedding
   │
   ▼
Search in Vector DB
   │
   ▼
Retrieve Similar Documents
   │
   ▼
Pass to LLM
   │
   ▼
Generate Answer
```

---

## 12. Real-World Use Cases

- Semantic search (Google-like search)
- Chatbots with memory (RAG)
- Recommendation systems (Netflix, Amazon)
- Duplicate detection
- Clustering documents

---

## 13. Key Differences (Embedding Types)

| Type | Context Awareness | Level | Example |
|------|------------------|------|--------|
| Word | ❌ No | Word | Word2Vec |
| Contextual | ✅ Yes | Token | BERT |
| Sentence | ✅ Yes | Sentence | SBERT |
| Document | ✅ Yes | Document | Doc2Vec |

---

## 14. Best Practices

- Choose embedding type based on use case
- Use cosine similarity for text
- Normalize vectors when needed
- Store embeddings in vector DB (FAISS, Pinecone, etc.)

---

## 15. Summary

- Embeddings convert data into vectors
- Similar meaning → closer vectors
- Types include text, image, audio, multimodal
- Text embeddings have multiple styles (word, contextual, sentence, document)

---

## 16. Conclusion

Embeddings are a core building block of modern AI systems. They enable machines to understand similarity, meaning, and relationships across different types of data, making them essential for search, recommendation, and LLM-powered applications.

---

**End of File**

