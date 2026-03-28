"""
Portfolio Data Module
====================
Single source of truth for all portfolio content.
Edit this file to update any section of the website.
"""

# ── Personal Info ──────────────────────────────────────────────────────────────
PERSONAL = {
    "name": "Aatif Khan Pathan",
    "title": "Machine Learning Engineer",
    "tagline": "Building the Intelligence of Tomorrow.",
    "sub_tagline": (
        "ML Engineer @ TCS · PyTorch · Computer Vision · LLMs · MLOps"
    ),
    "email": "aatifkhanjodhpur@gmail.com",
    "phone": "+91-9166199786",
    "location": "Gandhinagar, Gujarat, India",
    "linkedin": "https://linkedin.com/in/aatif-khan-pathan-a1674617b",
    "github": "https://github.com/aatif-pathan001",
    "blog": "https://aatifkhan.hashnode.dev",  # placeholder blog URL
    "resume_url": "/static/assets/Aatif_Khan_Pathan_ML_Engineer_Resume.pdf",
    "status": "Open to Senior ML / AI Roles",
    "summary": (
        "Machine Learning Engineer with 3+ years of experience building "
        "production-grade deep learning systems for computer vision, NLP, and "
        "intelligent automation. Proven track record deploying 10+ ML models to "
        "GCP Vertex AI with automated CI/CD pipelines. Expertise in PyTorch, YOLO, "
        "BERT, reinforcement learning, and MLOps best practices."
    ),
}

# ── Stats / Achievements ───────────────────────────────────────────────────────
STATS = [
    {"value": "99.58%", "label": "Image Classification Accuracy"},
    {"value": "92.3%",  "label": "F1 Score – NER"},
    {"value": "70.6%",  "label": "mAP – Object Detection"},
    {"value": "10+",    "label": "Production ML Systems"},
    {"value": "94%",    "label": "Deployment Time Reduction"},
    {"value": "3+",     "label": "Years Experience"},
]

# ── Tech Stack (categorised) ───────────────────────────────────────────────────
TECH_STACK = {
    "ML & Deep Learning": [
        "PyTorch", "Scikit-learn", "CNN", "RNN", "LSTM",
        "Transformers", "Reinforcement Learning", "Transfer Learning",
    ],
    "Computer Vision": [
        "YOLOv8", "OpenCV", "MediaPipe", "ResNet", "EfficientNet",
        "Object Detection", "Image Classification",
    ],
    "NLP & LLMs": [
        "BERT", "Hugging Face", "LangChain", "RAG", "ChromaDB",
        "Gemini/OpenAI API", "GPT", "Prompt Engineering", "LoRA / QLoRA",
    ],
    "MLOps & DevOps": [
        "MLflow", "Docker", "GitHub Actions", "FastAPI",
        "Model Monitoring", "CI/CD", "Google Cloud", "GCP Vertex AI",
    ],
    "Programming": [
        "Python", "NumPy", "Pandas", "Matplotlib",
        "Streamlit", "Gradio", "SQL", "C++", "MATLAB",
    ],
}

# ── Experience / Journey ───────────────────────────────────────────────────────
EXPERIENCE = [
    {
        "role": "Machine Learning Engineer",
        "company": "Tata Consultancy Services",
        "location": "Gandhinagar, Gujarat",
        "period": "Oct 2022 – Present",
        "status": "current",
        "highlights": [
            "Architected production-grade CV systems for automotive applications (1000+ vehicles)",
            "Built RAG system enabling semantic search across 10,000+ technical documents (60% faster retrieval)",
            "Designed driver-safety deep-learning pipelines achieving 30% robustness improvement",
            "LLM-powered engineering workflows processing 500+ documents/month",
            "AUTOSAR-compliant model deployment with MIL/SIL/B2B safety testing",
        ],
    },
    {
        "role": "Deep Learning Intern",
        "company": "CipherSchools",
        "location": "Jodhpur, Rajasthan",
        "period": "Jun 2021 – Jul 2021",
        "status": "past",
        "highlights": [
            "Facial expression recognition CNN — 92% accuracy, <100ms inference",
            "Custom object detection model — 90%+ mAP with transfer learning",
            "NLP sentiment pipeline on 50k+ tweets — 88% F1 score",
            "Spam classifier — 95% accuracy with minimal false positives",
        ],
    },
    {
        "role": "B.Tech – Electrical Engineering",
        "company": "Bikaner Technical University",
        "location": "Jodhpur, Rajasthan",
        "period": "Jul 2018 – Jun 2022",
        "status": "education",
        "highlights": [
            "Core studies in signals, control systems, embedded systems",
            "Transitioned into AI/ML through self-directed learning",
            "Final year project: ML-based control system optimisation",
        ],
    },
]

# ── Projects ───────────────────────────────────────────────────────────────────
PROJECTS = [
    {
        "id": 1,
        "title": "Custom YOLO Object Detection System",
        "category": "Computer Vision",
        "tags": ["PyTorch", "YOLOv8M", "GCP Vertex AI", "FastAPI", "Docker"],
        "description": [
            "Trained YOLOv8M (25.9M params) achieving 70.6% mAP@0.5. ",
            "Real-time 20-25 FPS on CPU.",
            "Automated CI/CD cut deployment from 2h → 8 min."
],
        "metrics": ["70.6% mAP@0.5", "20-25 FPS", "145ms avg latency"],
        "github": "#",
        "demo": "#",
        "featured": True,
    },
    {
        "id": 2,
        "title": "BERT NER + Multi-Task NLP API",
        "category": "NLP / LLMs",
        "tags": ["BERT", "Transformers", "Hugging Face", "FastAPI", "GCP"],
        "description": [
            "Fine-tuned bert-base-cased on CoNLL-2003 achieving 92.3% F1. ",
            "Unified multi-task API: NER, sentiment, topic classification, QA."
        ],
        "metrics": ["92.3% F1", "91.9% Precision", "1000+ predictions/day"],
        "github": "#",
        "demo": "#",
        "featured": True,
    },
    {
        "id": 3,
        "title": "LSTM + Prophet Time Series Forecasting",
        "category": "Forecasting",
        "tags": ["PyTorch", "Prophet", "Streamlit", "Yahoo Finance API"],
        "description": [
            "LSTM with 60-day lookback achieving ~2% MAPE for stock forecasting. ",
            "Interactive Streamlit dashboard with 30-day confidence intervals."
        ],
        "metrics": ["~2% MAPE", "30x faster with Prophet", "30-day forecasts"],
        "github": "#",
        "demo": "#",
        "featured": True,
    },
    {
        "id": 4,
        "title": "Production RAG System",
        "category": "NLP / LLMs",
        "tags": ["LangChain", "ChromaDB", "Gemini 2.5 Flash", "Sentence Transformers"],
        "description": [
            "RAG pipeline over 100-150 markdown chunks with semantic search. ",
            "95% accuracy improvement over base LLM, 2-5s response time."
        ],
        "metrics": ["95% accuracy boost", "2-5s response", "500-char chunking"],
        "github": "#",
        "demo": "#",
        "featured": False,
    },
    {
        "id": 5,
        "title": "Reinforcement Learning Suite",
        "category": "Reinforcement Learning",
        "tags": ["PyTorch", "Gymnasium", "Q-Learning", "DQN", "REINFORCE"],
        "description": [
            "Q-Learning (100% FrozenLake)", 
            "DQN (215 avg reward CartPole)",
            "REINFORCE for continuous action spaces — robotics foundation."
        ],
        "metrics": ["100% FrozenLake", "215 avg reward", "DQN + Policy Gradients"],
        "github": "#",
        "demo": "#",
        "featured": False,
    },
    {
        "id": 6,
        "title": "Electrical Equipment Image Classifier",
        "category": "Computer Vision",
        "tags": ["ResNet50", "PyTorch", "Transfer Learning", "AdamW"],
        "description": [
            "Transfer learning with ResNet50: feature extraction (95.83%) → fine-tuning (99.58%). ",
            "Custom electrical equipment dataset with AdamW + LR scheduling."
        ],
        "metrics": ["99.58% accuracy", "ResNet50", "Strategic layer unfreezing"],
        "github": "#",
        "demo": "#",
        "featured": True,
    },
    {
        "id": 7,
        "title": "Driver Drowsiness Detection (Edge)",
        "category": "Computer Vision",
        "tags": ["EfficientNet-B0", "OpenCV", "PyTorch", "Raspberry Pi"],
        "description": [
            "Real-time drowsiness detection (alert/drowsy/sleeping) with 93% accuracy.",
            "Quantised for edge deployment on Raspberry Pi."
        ],
        "metrics": ["93% accuracy", "Edge-optimised", "3-class classification"],
        "github": "#",
        "demo": "#",
        "featured": False,
    },
    {
        "id": 8,
        "title": "End-to-End MLOps Pipeline",
        "category": "MLOps",
        "tags": ["MLflow", "FastAPI", "Docker", "GitHub Actions", "GCP Vertex AI"],
        "description": [
            "Complete pipeline: ingest → validate → train → evaluate → register → deploy → monitor.",
            "15+ model versions, A/B testing, zero-downtime deployments."
        ],
        "metrics": ["15+ model versions", "Zero-downtime CI/CD", "P50/P95/P99 monitoring"],
        "github": "#",
        "demo": "#",
        "featured": True,
    },
    {
        "id": 9,
        "title": "LLM Fine-Tuning with LoRA/QLoRA",
        "category": "NLP / LLMs",
        "tags": ["LoRA", "QLoRA", "Hugging Face", "PEFT"],
        "description": [
            "Parameter-efficient fine-tuning: 99% parameter reduction via LoRA. ",
            "QLoRA 4-bit quantisation: memory from 14GB → 4GB with no performance loss."
        ],
        "metrics": ["99% param reduction", "14GB → 4GB RAM", "PEFT techniques"],
        "github": "#",
        "demo": "#",
        "featured": False,
    },
    {
        "id": 10,
        "title": "AI Financial News & Trading Insights",
        "category": "NLP / LLMs",
        "tags": ["PyTorch", "Gemini API", "BeautifulSoup", "Gradio"],
        "description": [
            "Scrapes 50+ financial articles daily.",
            "Gemini LLM generates summaries and actionable trading signals",
            "Cutting manual analysis by 60%."
        ],
        "metrics": ["50+ articles/day", "60% time saved", "Real-time signals"],
        "github": "#",
        "demo": "#",
        "featured": False,
    },
]
