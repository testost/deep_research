# Welcome to Deep Research

A multi-agent AI research system designed to know what it knows (and doesn't know) when conducting research.

[![Deep Research Demo](assets/YouTube.png)](https://www.youtube.com/watch?v=mGET1RKXW3o)

## The Vision

Currently, AI research agents have significant limitations - they often make assumptions, fabricate information, or miss crucial context. This project was heavily inspired by two groundbreaking works:

1. ["TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation"](https://arxiv.org/abs/2410.03608) by Cook et al., which demonstrated how structured checklists can significantly improve LLM evaluation and generation quality.

2. [NVIDIA's Nemotron-4 340B Reward Model](https://build.nvidia.com/nvidia/nemotron-4-340b-reward), which pioneered techniques for reward modeling in the loop. Their work on reward-based learning has influenced our approach to quality assessment and continuous improvement in research tasks.

This might seem like a small thing within research, but if you really think about it, this is the start of something much bigger. If the agents can understand what they don't know—just like a human—they can reason about what they need to learn. This has the potential to make the process of agents acquiring information much, much faster and in turn being much smarter.

## System Architecture

![Deep Research Team Architecture](assets/diogram.png)

This project is built on [CAMEL-AI's Workforce system](https://docs.camel-ai.org/key_modules/workforce.html), which provides a robust framework for coordinating multiple AI agents. The workforce architecture enables our agents to work together seamlessly, with built-in task management and failure handling.

## Connect & Learn More

👋 Stay updated with the latest developments:
- 📺 [YouTube Tutorials & Updates](https://www.youtube.com/@omni_georgio)
- 🎥 [Watch the Deep Research Demo](https://www.youtube.com/watch?v=mGET1RKXW3o)
- 🐦 [Follow on X (Twitter)](https://x.com/home)

Your feedback and contributions help make this project better!

## How It Works

The system operates through 5 key components:

### 1. Recipes
Think of these as detailed instructions for the research process. While currently manual, future versions will aim to automate recipe generation. Recipes specify:
- Required information ("ingredients")
- Output format
- Example outputs
- Research parameters

### 2. Research Intelligence Planning Agent
The first step in our research pipeline:
- Analyzes input content against recipe requirements
- Maps known vs unknown information
- Creates structured research plans
- Identifies which gaps can be filled through research

### 3. Deep Search Agent
Our dedicated researcher:
- Executes research plans
- Uses Google search strategically
- Verifies information from multiple sources
- Documents findings and confidence levels

### 4. Report Creator Agent
Our content synthesizer:
- Combines original content with research findings
- Follows recipe format requirements
- Maintains clear sourcing
- Highlights any remaining uncertainties

### 5. The Judge Agent
Our final quality check:
- Evaluates output completeness
- Checks adherence to recipe
- Validates information accuracy
- Provides detailed quality metrics

## Prerequisites

- Python 3.8+
- OpenAI API key
- Anthropic API key
- Google API key
- Google Search Engine ID

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your API keys:
```bash
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
GOOGLE_API_KEY=your_google_key
SEARCH_ENGINE_ID=your_search_engine_id
```

## Usage

### Basic Input Format

The tool accepts two main inputs:

```python
{
    "content": "", # Content to be researched/analyzed
    "recipe_id": "23634687939724" # Optional recipe ID from database
}
```

### Recipe Structure

When using a recipe ID, the following data structure is retrieved:

```python
{
    "recipe": "Format instructions for the output",
    "examples": "Example outputs showing desired format",
    "ingredients": "List of required information to include",
    "needs_research": "TRUE/FALSE" # Whether additional research is needed
}
```

### How It Works

1. **Research Intelligence Planning Phase**
   - The Content Research Planner Agent analyzes the input content
   - Identifies missing information and research needs
   - Creates a structured research plan

2. **Deep Search Phase**
   - The Deep Search Agent performs targeted searches using Google
   - Verifies facts and gathers additional context
   - Documents findings and sources

3. **Report Creation Phase**
   - Report Creator Agent synthesizes all information
   - Follows specified recipe format
   - Ensures all required ingredients are covered

4. **Judgment Phase**
   - The Judge Agent evaluates the output
   - Checks completeness and accuracy
   - Provides quality scores and recommendations

### Example Output

```python
{
    "overall_assessment": "PASS",
    "score": "9/10",
    "report": {
        "overview": "...",
        "technical_details": "...",
        "benefits": "...",
        "additional_context": "..."
    },
    "quality_metrics": {
        "completeness": "9/10",
        "format_adherence": "10/10",
        "information_quality": "8/10"
    }
}
```

## The Bigger Picture

While this might seem like a focused solution for research tasks, it represents something much more significant. By creating agents that understand their knowledge boundaries - just like humans do - we're taking a step toward more reliable AI systems.

The ability to reason about what they don't know and need to learn could dramatically improve how AI systems:
- Acquire new information
- Validate their knowledge
- Make reliable decisions
- Learn continuously

## Current Limitations

It's important to note that this is v0, and there are known limitations:
- Research quality varies by topic
- Some context nuances may be missed
- Recipe creation requires manual input
- Search capabilities are constrained by available APIs

## Future Directions

Our roadmap for improving the system includes:

### Research Intelligence
- **Adaptive Tool Selection**
  - Dynamic selection of research tools based on content type
  - Integration with GitHub for code research
  - YouTube API for tutorial/demo content
  - Academic paper databases for scholarly research
  - Automatic tool selection based on query type

### Quality Assessment
- **Enhanced Judge Agent Criteria**
  - More sophisticated evaluation metrics
  - Domain-specific assessment criteria
  - Confidence scoring improvements
  - Source credibility weighting

### Model Support
- **Better Open-Model Support**
  - Broader compatibility with open-source models
  - Easy integration of new models
  - Performance comparison framework
  - Cost-effective model selection

### Research Optimization
- **Smarter Research Depth Handling**
  - Automatic depth determination
  - Resource optimization
  - Context-aware search strategies
  - Priority-based research planning

### Automation
- **Automated Instruction Generation**
  - Self-generating research recipes
  - Dynamic task definition
  - Autonomous research planning
  - Continuous learning from past tasks

### Current Development
- Automated recipe generation
- Enhanced source validation
- Expanded search capabilities
- Better context understanding
- More sophisticated knowledge mapping

## Configuration

The tool uses several AI agents, each configurable through environment variables:
- Content Research Planner Agent
- Research Agent
- Report Creator Agent
- Report Quality Judge Agent

---

> "I don't know everything, I only know what I know"  
> — o3  
> — FriskyFennecFox

## License

MIT License


