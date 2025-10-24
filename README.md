# Streamlit Applications

This repository contains two Streamlit applications: a Resume Optimizer and a Text-to-Image Generator.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:
   - Create a `.env` file in the root directory.
   - Add your API keys to the `.env` file:
     ```
     OPENAI_API_KEY=your_openai_api_key
     HF_API_KEY=your_hugging_face_api_key
     ```

## Resume Optimizer

This application helps users tailor their resumes to specific job descriptions. By uploading a resume and providing a job description, the tool generates an optimized version of the resume that highlights relevant skills and experiences.

### Features

- **Resume Upload**: Upload your resume in `.docx` format.
- **Job Description Input**: Enter the job description for the position you are applying for.
- **AI-Powered Optimization**: Utilizes OpenAI's GPT-4o to rewrite and tailor your resume.
- **Download Optimized Resume**: Download the optimized resume as a `.docx` file.
- **Preview Changes**: View the optimized resume content before downloading.

### Usage

```bash
streamlit run main.py
```

## Text-to-Image Generator

This application allows users to generate images from text prompts using a Hugging Face model. Users can input a descriptive text, and the application will generate and display an image based on the prompt.

### Features

- **Text-to-Image Generation**: Generate images from text prompts.
- **Hugging Face Model**: Utilizes the `black-forest-labs/FLUX.1-dev` model.
- **Download Generated Image**: Download the generated image as a `.png` file.

### Usage

```bash
streamlit run StreamFlux.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.
