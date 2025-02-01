# Content Researcher with API Keys

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
from getpass import getpass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Verify API keys are loaded
if not os.getenv("OPENAI_API_KEY") or not os.getenv("ANTHROPIC_API_KEY"):
    raise ValueError("Please set OPENAI_API_KEY and ANTHROPIC_API_KEY in your .env file")

# After load_dotenv()
if not os.getenv("GOOGLE_API_KEY") or not os.getenv("SEARCH_ENGINE_ID"):
    raise ValueError("Please set GOOGLE_API_KEY and SEARCH_ENGINE_ID in your .env file")

"""## Import Dependencies & Set up AsnycIO"""

from camel.agents.chat_agent import ChatAgent
from camel.configs.openai_config import ChatGPTConfig
from camel.messages.base import BaseMessage
from camel.models import ModelFactory
from camel.tasks.task import Task
from camel.toolkits import (
    SearchToolkit,
)
from camel.types import ModelPlatformType, ModelType
from camel.societies.workforce import Workforce

import nest_asyncio
nest_asyncio.apply()


content = """
[Skip to content](https://github.com/camel-ai/camel/pull/1137#start-of-content)

You signed in with another tab or window. [Reload](https://github.com/camel-ai/camel/pull/1137) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/camel-ai/camel/pull/1137) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/camel-ai/camel/pull/1137) to refresh your session.Dismiss alert

{{ message }}

[camel-ai](https://github.com/camel-ai)/ **[camel](https://github.com/camel-ai/camel)** Public

- [Notifications](https://github.com/login?return_to=%2Fcamel-ai%2Fcamel) You must be signed in to change notification settings
- [Fork\\
730](https://github.com/login?return_to=%2Fcamel-ai%2Fcamel)
- [Star\\
6k](https://github.com/login?return_to=%2Fcamel-ai%2Fcamel)



New issue


**Have a question about this project?** Sign up for a free GitHub account to open an issue and contact its maintainers and the community.


[Sign up for GitHub](https://github.com/signup?return_to=%2Fcamel-ai%2Fcamel%2Fissues%2Fnew%2Fchoose)

By clicking "Sign up for GitHub", you agree to our [terms of service](https://docs.github.com/terms) and
[privacy statement](https://docs.github.com/privacy). We'll occasionally send you account related emails.

Already on GitHub?
[Sign in](https://github.com/login?return_to=%2Fcamel-ai%2Fcamel%2Fissues%2Fnew%2Fchoose)
to your account


[Jump to bottom](https://github.com/camel-ai/camel/pull/1137#issue-comment-box)

# feat: Add support for Qwen model platform (\#1033)\#1137

Merged

[Wendong-Fan](https://github.com/Wendong-Fan)
merged 3 commits into

[master](https://github.com/camel-ai/camel/tree/master "camel-ai/camel:master")

from

[qwen](https://github.com/camel-ai/camel/tree/qwen "camel-ai/camel:qwen")

Nov 1, 2024

Merged

# [feat: Add support for Qwen model platform (\#1033)](https://github.com/camel-ai/camel/pull/1137\#top)\#1137

[Wendong-Fan](https://github.com/Wendong-Fan)
merged 3 commits into

[master](https://github.com/camel-ai/camel/tree/master "camel-ai/camel:master")

from

[qwen](https://github.com/camel-ai/camel/tree/qwen "camel-ai/camel:qwen")

Nov 1, 2024

+403

−2


## Conversation

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](https://github.com/camel-ai/camel/pull/%7B%7B%20revealButtonHref%20%7D%7D)

[![MuggleJinx](https://avatars.githubusercontent.com/u/29347829?s=60&v=4)](https://github.com/MuggleJinx)


Copy link

Collaborator

### ![@MuggleJinx](https://avatars.githubusercontent.com/u/29347829?s=48&v=4)**[MuggleJinx](https://github.com/MuggleJinx)**     commented   [Oct 31, 2024](https://github.com/camel-ai/camel/pull/1137\#issue-2626014614)

## Description

This PR adds support for the [Qwen LLM models](https://help.aliyun.com/zh/model-studio/getting-started/models?spm=a2c4g.11186623.help-menu-2400256.d_0_2.71d755efwQJ2YN&scm=20140722.H_2840914._.OR_help-V_1), including qwen-max, qwen-plus, qwen-turbo, qwen-long. The addition of Qwen-series models enhances the platform's capabilities, providing support for a broader range of language models and enabling users to leverage different performance tiers.

## Motivation and Context

Closes issue [#1033](https://github.com/camel-ai/camel/issues/1033).

## Types of changes

What types of changes does your code introduce? Put an `x` in all the boxes that apply:

- [ ]  Bug fix (non-breaking change which fixes an issue)
- [x]  New feature (non-breaking change which adds core functionality)
- [ ]  Breaking change (fix or feature that would cause existing functionality to change)
- [ ]  Documentation (update in the documentation)
- [ ]  Example (update in the folder of example)

## Implemented Tasks

- [x]  Implement consistent interface for Qwen-series model.
- [x]  Add the corresponding example, and test file.

## Checklist

Go over all the following points, and put an `x` in all the boxes that apply.

If you are unsure about any of these, don't hesitate to ask. We are here to help!

- [x]  I have read the [CONTRIBUTION](https://github.com/camel-ai/camel/blob/master/CONTRIBUTING.md) guide. ( **required**)
- [x]  My change requires a change to the documentation.
- [x]  I have updated the tests accordingly. ( _required for a bug fix or a new feature_)
- [x]  I have updated the documentation accordingly.

Sorry, something went wrong.


All reactions

[![@MuggleJinx](https://avatars.githubusercontent.com/u/29347829?s=40&v=4)](https://github.com/MuggleJinx)

`
          implemet qwen model
        `

Loading

Loading status checks…

`
          cf3e9a0
        `

[![@MuggleJinx](https://avatars.githubusercontent.com/u/29347829?s=40&u=e5c3ab833af7ef7f93f7bb7c141d5724ebb85339&v=4)](https://github.com/MuggleJinx)[MuggleJinx](https://github.com/MuggleJinx)

requested a review
from [Wendong-Fan](https://github.com/Wendong-Fan) [October 31, 2024 05:40](https://github.com/camel-ai/camel/pull/1137#event-15025496902)

[![@Wendong-Fan](https://avatars.githubusercontent.com/u/133094783?s=40&u=ae59dad1440667fa4769b51c666b16198aca134b&v=4)](https://github.com/Wendong-Fan)[Wendong-Fan](https://github.com/Wendong-Fan)

linked an issue
[Oct 31, 2024](https://github.com/camel-ai/camel/pull/1137#event-15025586981)
that may be
closed
by this pull request

[\[Feature Request\] Integrate Qwen model platform\\
#1033](https://github.com/camel-ai/camel/issues/1033)

Closed

2 tasks

[![@Wendong-Fan](https://avatars.githubusercontent.com/u/133094783?s=40&u=ae59dad1440667fa4769b51c666b16198aca134b&v=4)](https://github.com/Wendong-Fan)[Wendong-Fan](https://github.com/Wendong-Fan)

added this to the [Sprint 15](https://github.com/camel-ai/camel/milestone/16) milestone

[Oct 31, 2024](https://github.com/camel-ai/camel/pull/1137#event-15025587239)

[![@Wendong-Fan](https://avatars.githubusercontent.com/u/133094783?s=40&u=ae59dad1440667fa4769b51c666b16198aca134b&v=4)](https://github.com/Wendong-Fan)[Wendong-Fan](https://github.com/Wendong-Fan)

added
the
[Model](https://github.com/camel-ai/camel/labels/Model) Related to backend models
label

[Oct 31, 2024](https://github.com/camel-ai/camel/pull/1137#event-15025587990)

[![@Wendong-Fan](https://avatars.githubusercontent.com/u/133094783?s=40&u=ae59dad1440667fa4769b51c666b16198aca134b&v=4)](https://github.com/Wendong-Fan)[Wendong-Fan](https://github.com/Wendong-Fan)

assigned [MuggleJinx](https://github.com/MuggleJinx) [Oct 31, 2024](https://github.com/camel-ai/camel/pull/1137#event-15025588304)

[![@Wendong-Fan](https://avatars.githubusercontent.com/u/133094783?s=40&v=4)](https://github.com/Wendong-Fan)

`
          update based on comment
        `

Loading

Loading status checks…

"""
needs_research = "needs_research is true, this content needs to be researched for additional context about Qwen models and their integration"

ingredients = """

Required Information:

1. Project Contributors
   - Who created or contributed to this PR, with their Github handle
   - Who reviewed and approved the PR

2. Technologies
   - What is the name and purpose of the main framework/platform this PR is adding to, e.g. Can you spell check this? Do you know exactly how they describe themselves
   - What are the names and purposes of the technologies being integrated e.g. do you knowthe key benefits of the integration

3. Integration Purpose
   - What new capabilities does this integration add to the main framework
   - How do the technologies interact with the main framework
   - Who is this integration designed for

4. Documentation Access
   - Link to PR and related issue
   - Where to find usage examples"""


recipe = """Objective: Generate concise, engaging, and technical social media posts promoting AI tools, cookbooks, or integrations. The tone should be action-oriented and clear.

Key features:
Catchy, action-oriented headline: [Begin with an exciting statement to grab attention, showcasing the feature or outcome.]
Overview of benefits: [Explain what users will achieve or learn, focusing on the key value proposition.]
Details of tools/technologies: [Mention tools or components without handles, but include emojis for emphasis.]
Call-to-action: [Provide a link to the relevant resource and invite the audience to explore further.]

Make sure you follow the examples given """


print(content)

"""# Create Worker Agents"""

search_toolkit = SearchToolkit()
search_tools = [
    search_toolkit.search_google,  # Only use Google search
]

content_classifier_agent = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Content Research Planner Agent",
            content=f"""You are a Research Planning Agent that analyzes content against a required ingredients list.

        INPUT FORMAT:
        1. Content: [Original content to analyze]
        2. Ingredients: [List of required information]

        YOUR TASK:
        Analyze the content and create a detailed research plan by:
        1. Reading through the content thoroughly
        2. Comparing against each ingredient in the ingredients list
        3. Categorizing each piece of required information

        Required Ingredients List:
        {ingredients}

        CATEGORIZATION SYSTEM:
        For each ingredient, provide:
        1. Status (one of):
           * KNOWN - Information is explicitly present in content
           * NEEDS_SEARCH - Information is missing but can be researched
           * UNSEARCHABLE - Information cannot be found through research
           * REQUIRES_INPUT - Information needs direct input from content creator

        2. Evidence/Reasoning:
           * For KNOWN: Quote the relevant content section
           * For NEEDS_SEARCH: Explain search strategy
           * For UNSEARCHABLE: Explain why it can't be researched
           * For REQUIRES_INPUT: Explain what input is needed

        OUTPUT FORMAT:
        Provide your analysis in this structure:
        {{
            "ingredient_analysis": [
                {{
                    "ingredient": "[Name of ingredient]",
                    "status": "[KNOWN/NEEDS_SEARCH/UNSEARCHABLE/REQUIRES_INPUT]",
                    "evidence": "[Supporting evidence or explanation]",
                    "action_needed": "[What needs to be done for this ingredient]"
                }}
            ],
            "research_plan": {{
                "known_information": ["List of what we already have"],
                "search_topics": ["List of what needs research"],
                "required_inputs": ["List of what needs direct input"]
            }}
        }}"""
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict(),
    ),
)

research_agent = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Research Agent",
        content="""From the topics listed by the research planner agent as NEEDS_SEARCH, conduct additional research using the search tools provided"""
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict(),
    ),

   tools=search_tools,
)

report_creator_agent = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Report Creator Agent",
        content=f"""You are a Report Creator Agent that synthesizes information into a cohesive report.

        INPUT PROVIDED:
        1. Original Content: {content}
        2. Recipe Format: {recipe}
        3. Research Results (if any)
        4. Required Ingredients List: {ingredients}

        YOUR TASK:
        Create a comprehensive report that:
        1. Combines all available information
        2. Follows the recipe format exactly
        3. Ensures all required ingredients are covered
        4. Maintains consistency and accuracy

        REPORT STRUCTURE:
        1. Overview
           - Main purpose and key points
           - Target audience and use case

        2. Technical Details
           - Tools and technologies
           - Implementation details
           - Performance metrics

        3. Benefits and Results
           - Key advantages
           - User outcomes
           - Performance improvements

        4. Additional Context
           - Documentation links
           - Next steps
           - Related resources

        GUIDELINES:
        - Use only verified information from inputs
        - Follow recipe format strictly
        - Include all required ingredients
        - Note any remaining information gaps
        - Maintain technical accuracy
        - Use clear, engaging language

        OUTPUT FORMAT:
        Provide your report in markdown format with clear sections and subsections."""
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict(),
    ),
)

judge_agent = ChatAgent(
    system_message=BaseMessage.make_assistant_message(
        role_name="Report Quality Judge Agent",
        content=f"""You are a Judge Agent that evaluates reports against required criteria and ingredients.

        INPUT PROVIDED:
        1. Report Content
        2. Required Ingredients List: {ingredients}
        3. Recipe Format: {recipe}

        YOUR TASK:
        Evaluate the report thoroughly by:
        1. Checking if all required ingredients are covered
        2. Assessing if the recipe format is followed
        3. Verifying information accuracy and completeness
        4. Identifying any gaps or missing elements

        EVALUATION CRITERIA:
        1. Completeness:
           - Are all required ingredients addressed?
           - Is each section sufficiently detailed?
           - Are there any missing components?

        2. Format Adherence:
           - Does it follow the recipe structure?
           - Is the presentation clear and organized?
           - Are sections properly formatted?

        3. Information Quality:
           - Is the information accurate and well-sourced?
           - Are claims properly supported?
           - Is technical content precise?

        OUTPUT FORMAT:
        Provide your evaluation in this structure:
        {{
            "overall_assessment": "PASS/NEEDS_REVISION",
            "score": "X/10",
            "criteria_evaluation": {{
                "completeness": {{
                    "score": "X/10",
                    "findings": ["List of findings"],
                    "missing_elements": ["List of gaps"]
                }},
                "format_adherence": {{
                    "score": "X/10",
                    "findings": ["List of findings"],
                    "suggestions": ["List of improvements"]
                }},
                "information_quality": {{
                    "score": "X/10",
                    "strengths": ["List of strengths"],
                    "weaknesses": ["List of weaknesses"]
                }}
            }},
            "recommendations": ["List of specific recommendations"]
        }}"""
    ),
    model=ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O,
        model_config_dict=ChatGPTConfig().as_dict(),
    ),
)

"""## Create Workforce & Add Agents"""

# Create and configure workforce with all agents
workforce = Workforce('Content Analysis and PR Tweet Writing Group')

# Add all agents to the workforce in processing order
workforce.add_single_agent_worker(
    "CContent Research Planner Agent, an agent that plans reseach",
    worker=content_classifier_agent
).add_single_agent_worker(
    "Research Agent, an agent that verifies facts and gathers context based on content type",
    worker=research_agent
).add_single_agent_worker(
    "Report Creator, an agent that synthesizes analysis aligned with content goals",
    worker=report_creator_agent
).add_single_agent_worker(
    "Report Quality Judge, an agent that evaluates report quality and completeness",
    worker=judge_agent
)

"""## Create Task & Assign to Workforce"""

# specify the task to be solved
human_task = Task(
    content=(
"""Your goal is to create a clear report on the provided content. Follow these steps:

1. First analyze the content to identify research needs. Focus on:
   - Technical details of Qwen LLM models
   - Integration benefits and capabilities
   - Similar model integrations in CAMEL
   - Performance metrics and benchmarks

2. Then conduct research on the identified topics using the research agent
   - Search for documentation about Qwen models
   - Find benchmarks and comparisons
   - Look for integration examples
   - Gather user feedback and use cases

3. Finally, create a comprehensive report synthesizing all findings

Use the content research planner agent first, then the research agent, and finally the report creator agent."""
    ),
    additional_info=content,
    id='0',
)

task = workforce.process_task(human_task)

"""## Get the result of the Task"""

print('Final Result of Original task:\n', task.result)