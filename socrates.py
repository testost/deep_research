"""Import Dependencies & Set up AsyncIO"""

from camel.agents.chat_agent import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.tasks.task import Task
from camel.toolkits import SearchToolkit
from camel.types import ModelPlatformType, ModelType
from camel.societies.workforce import Workforce

import nest_asyncio
nest_asyncio.apply()

import os
import argparse
from datetime import datetime
from pathlib import Path
from getpass import getpass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify API keys are loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Please set OPENAI_API_KEY in your .env file")

if not os.getenv("GOOGLE_API_KEY") or not os.getenv("SEARCH_ENGINE_ID"):
    raise ValueError("Please set GOOGLE_API_KEY and SEARCH_ENGINE_ID in your .env file")

# Initialize search toolkit with Google
search_toolkit = SearchToolkit()
search_tools = [
    search_toolkit.search_google
]

# Socratic Research Recipe
recipe = """Socratic Research Methodology:

1. Hypothesis Formulation
   - Initial proposition generation
   - Counterargument anticipation
   - Knowledge domain mapping

2. Elenchus (Cross-Examination)
   - Premise validation through:
     * Source credibility checks
     * Logical consistency analysis
     * Empirical evidence matching

3. Aporia (Puzzle State)
   - Identify contradictions/paradoxes
   - Map knowledge boundaries
   - Highlight cognitive biases

4. Metanoia (Perspective Shift)
   - Alternative interpretations
   - Paradigm challenge exercises
   - Cross-domain analogies

5. Episteme (Verified Knowledge)
   - Evidence-graded conclusions
   - Confidence interval assessment
   - Open questions/research avenues"""

# Universal Research Planner Agent
research_planner = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Universal Research Planner",
        content="""You are a Research Framework Builder that can analyze any query and create an investigation plan:

        YOUR PROCESS:
        1. Query Analysis
           - Extract core concepts
           - Identify domain context
           - Map knowledge requirements

        2. Research Strategy
           - Define search parameters
           - Identify credible sources
           - Plan verification methods

        3. Socratic Implementation
           - Form initial hypotheses
           - Design critical questions
           - Plan contradiction analysis
           - Prepare perspective challenges
           - Structure knowledge validation

        4. Adaptation
           - Adjust depth based on complexity
           - Scale methodology to query scope
           - Balance breadth vs. depth

        OUTPUT:
        Provide a structured research plan following the Socratic method stages."""
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict()
    )
)

# Research Agent
research_agent = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Universal Researcher",
        content="""Execute research plans using available tools and critical thinking:
        
        1. Follow the Socratic method stages
        2. Verify information across multiple sources
        3. Document evidence and reasoning chains
        4. Identify potential biases and limitations
        """
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict()
    ),
    tools=search_tools
)

# Report Creator Agent
report_creator = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Report Synthesizer",
        content=f"""Create comprehensive research reports following this recipe:
        {recipe}
        
        Ensure:
        1. Clear progression through Socratic stages
        2. Evidence-based conclusions
        3. Balanced perspective presentation
        4. Acknowledgment of limitations
        """
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict()
    )
)

def save_results(query, result):
    # Create .results directory if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)

    # Create filename with timestamp and sanitized query
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Sanitize query for filename (remove special chars, limit length)
    safe_query = "".join(c for c in query if c.isalnum() or c in (' ', '-', '_'))[:50]
    safe_query = safe_query.replace(' ', '_')
    
    filename = f"{timestamp}_{safe_query}.md"
    filepath = results_dir / filename

    # Create markdown content
    markdown_content = f"""# Research Report: {query}
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{result}
"""

    # Save to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    return filepath

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Universal Research Assistant using Socratic Method')
    parser.add_argument('--query', type=str, help='Research query to investigate')
    args = parser.parse_args()

    # Get query from command line or prompt
    query = args.query if args.query else input("Enter your research question: ")

    print(f"\nResearching: {query}\n")

    try:
        # Create workforce with just a name
        workforce = Workforce("Universal Research Team")

        # Add agents sequentially
        workforce.add_single_agent_worker(
            "Research Planner Agent",
            worker=research_planner
        ).add_single_agent_worker(
            "Research Agent",
            worker=research_agent
        ).add_single_agent_worker(
            "Report Creator Agent",
            worker=report_creator
        )

        # Create and process task
        task = Task(
            content=query,
            id="research_task"
        )
        
        # Process task and get result
        result = workforce.process_task(task)
        
        # Save results to markdown file
        filepath = save_results(query, result.result)
        
        print("\nFINAL RESEARCH REPORT:")
        print("=" * 80)
        print(result.result)
        print("=" * 80)
        print(f"\nReport saved to: {filepath}")
        
    except Exception as e:
        print(f"Error during research: {str(e)}")

if __name__ == "__main__":
    main()