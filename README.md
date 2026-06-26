<a id="top"></a>

# 🔍 ScholarOps Extractor — Day 5 Submission

### An intermediate text-processing engine built using Python's native Regular Expressions (`re`) module to sweep, isolate, and format unstructured text blocks.

<p align="center">
  A self-contained data compilation utility parsing variable format emails, complex telephone strings, and standard calendar dates smoothly without breaking runtime threads.
  <br />
  <a href="https://drive.google.com/file/d/12mxfo6DZQfjkeG-RBGXAg356ob71RgZ4/view?usp"><strong>Watch App Demo Video »</strong></a>
  <br />
  <br />
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_5">Explore Codebase</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_5/issues">Report Bug</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_5/issues">Request Feature</a>
</p>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#compiled-regex-patterns">Compiled Regex Patterns</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#usage-and-test-case-matrix">Usage & Test Case Matrix</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    
  </ol>
</details>

---

## About The Project

This project acts as the primary practical task submission for Day 5 of the Python Intermediate Internship framework. It covers advanced token parsing, text cleansing algorithms, character class configurations, and regex pattern substitution matrices.

### Key Highlights:
* **Multi-Format Extraction Blocks:** Uses optimized wildcards and word boundaries to capture structural variations in phone arrays and calendar dates simultaneously.
* **Regex-Driven Data Cleansing:** Leverages substitution functions (`re.sub`) to strip trailing punctuation, parentheses, and dots, transforming messy inputs into a standardized layout.
* **Array Deduplication:** Automatically routes raw list outputs into a native Python `set()` matrix layer to clear away accidental duplicate matches seamlessly.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## 🛠️ Compiled Regex Patterns

To ensure maximum transparency during evaluation, here are the explicit regex configurations engineered into the engine:

### 1. Email Address Matching
* **Pattern:** `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
* **Logic:** Looks for an alphanumeric username block containing standard special symbols, followed by an `@` operator, a domain name, and a trailing top-level domain suffix extending at least 2 characters.

### 2. Robust Telephone Extraction
* **Pattern:** `\+?\d{1,4}[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,5}[-.\s]?\d{3,5}`
* **Logic:** Captures variable configurations by allowing an optional international prefix (`+91`), bracketed regional landline area codes (`(022)`), and numbers split by spaces, dots, or dashes.

### 3. Dual-Format Calendar Tracking
* **Pattern:** `\b\d{2}[-/.]\d{2}[-/.]\d{4}\b|\b\d{4}[-/.]\d{2}[-/.]\d{2}\b`
* **Logic:** Employs word boundaries (`\b`) combined with the OR (`|`) alternator token to safely extract both standard European (`DD/MM/YYYY`) and ISO (`YYYY-MM-DD`) layouts without overlapping.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Regex Module](https://img.shields.io/badge/Module-re_Core-red?style=for-the-badge)](https://docs.python.org/3/library/re.html)

---

## Getting Started

Because this application relies entirely on native modules bundled directly into standard Python environments, **no external third-party installations (`pip install`) are required.**

### Prerequisites
* **Python 3.8 or higher** active on your local computer workspace machine.

### Local Setup Execution

# 1. Clone your project repository workspace
git clone [https://github.com/github_username/unprof.git](https://github.com/github_username/unprof.git) && cd unprof

# 2. Confirm your local Git remote tracking paths
git remote -v

# 3. Boot up the text extraction shell runner
python info_extractor.py




## Roadmap
 Phase 1 Day 3: Build diagnostic exception handling log channels.

 Phase 1 Day 4: Integrate external API requests forecast networks.

 Phase 1 Day 5: Engineer multi-pattern text processing regex engines (re.findall).

 Phase 2: Add local clipboard listeners to automatically read data on hotkey triggers.

 Phase 2: Integrate secure encryption filters to mask private tracking entries upon output.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any improvements you bring to optimizing this operational system workspace are highly valued.

If you have a structural suggestion that would make this model better, please fork the repository workspace and open a clean pull request. You can also simply open an issue ticket flagged with the "enhancement" metadata tag.

Fork the Project Workspace

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your configuration updates safely (git commit -m 'Add some AmazingFeature')

Push code updates directly to your tracking origin (git push origin feature/AmazingFeature)

Open a professional Pull Request
