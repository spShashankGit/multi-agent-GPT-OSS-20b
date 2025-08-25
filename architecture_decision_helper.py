#!/usr/bin/env python3
"""
Architecture Decision Helper

This script helps you decide between multi-agent and multi-tool approaches
based on your specific requirements and thresholds.
"""

def get_user_input():
    """Collect information about the user's use case."""
    print("🏗️  Architecture Decision Helper")
    print("=" * 50)
    print("Answer the following questions to get architectural guidance.\n")
    
    questions = {
        'domains': {
            'question': "How many distinct domains of expertise are required? (e.g., finance, healthcare, logistics)",
            'type': 'int',
            'multi_agent_threshold': 3
        },
        'data_sources': {
            'question': "How many different data sources will you integrate? (APIs, databases, files)",
            'type': 'int', 
            'multi_agent_threshold': 3
        },
        'team_size': {
            'question': "How many development teams will work on this? (1 team = 1-3 developers)",
            'type': 'int',
            'multi_agent_threshold': 3
        },
        'parallel_tasks': {
            'question': "What percentage of tasks can run independently/in parallel? (0-100)",
            'type': 'int',
            'multi_agent_threshold': 50
        },
        'expected_users': {
            'question': "Expected concurrent users at peak?",
            'type': 'int',
            'multi_agent_threshold': 100
        },
        'processing_type': {
            'question': "Is processing primarily sequential (1) or can be parallel (2)?",
            'type': 'choice',
            'choices': {'1': 'sequential', '2': 'parallel'},
            'multi_agent_choice': '2'
        },
        'development_phase': {
            'question': "Development phase: prototype (1) or production (2)?",
            'type': 'choice', 
            'choices': {'1': 'prototype', '2': 'production'},
            'multi_agent_choice': '2'
        },
        'fault_tolerance': {
            'question': "Is fault tolerance critical? (y/n)",
            'type': 'bool',
            'multi_agent_answer': True
        }
    }
    
    responses = {}
    
    for key, config in questions.items():
        print(f"📋 {config['question']}")
        
        if config['type'] == 'int':
            while True:
                try:
                    responses[key] = int(input("   Answer: "))
                    break
                except ValueError:
                    print("   Please enter a valid number.")
        
        elif config['type'] == 'choice':
            print("   Options:")
            for choice_key, choice_value in config['choices'].items():
                print(f"      {choice_key}: {choice_value}")
            while True:
                answer = input("   Answer: ")
                if answer in config['choices']:
                    responses[key] = answer
                    break
                else:
                    print("   Please enter a valid option.")
        
        elif config['type'] == 'bool':
            while True:
                answer = input("   Answer (y/n): ").lower()
                if answer in ['y', 'yes']:
                    responses[key] = True
                    break
                elif answer in ['n', 'no']:
                    responses[key] = False
                    break
                else:
                    print("   Please enter 'y' or 'n'.")
        
        print()
    
    return responses, questions

def calculate_scores(responses, questions):
    """Calculate scores for multi-agent vs multi-tool approaches."""
    
    multi_agent_score = 0
    multi_tool_score = 0
    factors_analyzed = []
    
    # Domain complexity
    domains = responses['domains']
    if domains >= questions['domains']['multi_agent_threshold']:
        multi_agent_score += 3
        factors_analyzed.append(f"✅ {domains} domains favor multi-agent (threshold: 3+)")
    else:
        multi_tool_score += 3
        factors_analyzed.append(f"✅ {domains} domain(s) favor multi-tool (simple domain structure)")
    
    # Data sources
    data_sources = responses['data_sources']
    if data_sources >= questions['data_sources']['multi_agent_threshold']:
        multi_agent_score += 3
        factors_analyzed.append(f"✅ {data_sources} data sources favor multi-agent (threshold: 3+)")
    else:
        multi_tool_score += 2
        factors_analyzed.append(f"✅ {data_sources} data source(s) favor multi-tool (simple integration)")
    
    # Team size
    teams = responses['team_size']
    if teams >= questions['team_size']['multi_agent_threshold']:
        multi_agent_score += 2
        factors_analyzed.append(f"✅ {teams} teams favor multi-agent (clear boundaries)")
    else:
        multi_tool_score += 2
        factors_analyzed.append(f"✅ {teams} team(s) favor multi-tool (simple coordination)")
    
    # Parallel processing
    parallel_pct = responses['parallel_tasks']
    if parallel_pct >= questions['parallel_tasks']['multi_agent_threshold']:
        multi_agent_score += 2
        factors_analyzed.append(f"✅ {parallel_pct}% parallelizable tasks favor multi-agent")
    else:
        multi_tool_score += 2
        factors_analyzed.append(f"✅ {parallel_pct}% parallelizable tasks favor multi-tool (sequential)")
    
    # Scale
    users = responses['expected_users']
    if users >= questions['expected_users']['multi_agent_threshold']:
        multi_agent_score += 2
        factors_analyzed.append(f"✅ {users} concurrent users favor multi-agent (scale needs)")
    else:
        multi_tool_score += 1
        factors_analyzed.append(f"✅ {users} concurrent users favor multi-tool (simple scale)")
    
    # Processing type
    if responses['processing_type'] == questions['processing_type']['multi_agent_choice']:
        multi_agent_score += 2
        factors_analyzed.append("✅ Parallel processing favors multi-agent")
    else:
        multi_tool_score += 2
        factors_analyzed.append("✅ Sequential processing favors multi-tool")
    
    # Development phase
    if responses['development_phase'] == questions['development_phase']['multi_agent_choice']:
        multi_agent_score += 1
        factors_analyzed.append("✅ Production phase favors multi-agent (robustness)")
    else:
        multi_tool_score += 2
        factors_analyzed.append("✅ Prototype phase favors multi-tool (simplicity)")
    
    # Fault tolerance
    if responses['fault_tolerance'] == questions['fault_tolerance']['multi_agent_answer']:
        multi_agent_score += 2
        factors_analyzed.append("✅ Critical fault tolerance favors multi-agent")
    else:
        multi_tool_score += 1
        factors_analyzed.append("✅ Basic fault tolerance needs favor multi-tool")
    
    return multi_agent_score, multi_tool_score, factors_analyzed

def provide_recommendation(multi_agent_score, multi_tool_score, factors_analyzed):
    """Provide architectural recommendation based on scores."""
    
    print("\n" + "=" * 60)
    print("📊 ANALYSIS RESULTS")
    print("=" * 60)
    
    print("\n🔍 Factors Analyzed:")
    for factor in factors_analyzed:
        print(f"  {factor}")
    
    print(f"\n📈 Scores:")
    print(f"  Multi-Agent Score: {multi_agent_score}")
    print(f"  Multi-Tool Score:  {multi_tool_score}")
    
    print(f"\n🎯 RECOMMENDATION:")
    
    if multi_agent_score > multi_tool_score:
        confidence = "High" if multi_agent_score - multi_tool_score > 3 else "Medium"
        print(f"  ➜ USE MULTI-AGENT ARCHITECTURE ({confidence} confidence)")
        print(f"    Reasoning: Your use case shows {multi_agent_score} points favoring")
        print(f"    multi-agent vs {multi_tool_score} for multi-tool approach.")
        
        print(f"\n  📋 Next Steps:")
        print(f"    1. Design agent boundaries around distinct domains")
        print(f"    2. Define communication protocols between agents")
        print(f"    3. Plan for independent deployment and scaling")
        print(f"    4. Consider the master_agent.py example in this repository")
        
    elif multi_tool_score > multi_agent_score:
        confidence = "High" if multi_tool_score - multi_agent_score > 3 else "Medium"
        print(f"  ➜ USE MULTI-TOOL ARCHITECTURE ({confidence} confidence)")
        print(f"    Reasoning: Your use case shows {multi_tool_score} points favoring")
        print(f"    multi-tool vs {multi_agent_score} for multi-agent approach.")
        
        print(f"\n  📋 Next Steps:")
        print(f"    1. Design composable tools with clear interfaces")
        print(f"    2. Create a single agent that orchestrates tool usage")
        print(f"    3. Focus on tool reusability and state management")
        print(f"    4. Consider the ddg_search_tool example in this repository")
        
    else:
        print(f"  ➜ EITHER APPROACH VIABLE (Tie: {multi_agent_score} points each)")
        print(f"    Reasoning: Your requirements don't strongly favor either approach.")
        
        print(f"\n  📋 Recommendation:")
        print(f"    - Start with multi-tool (simpler to implement)")
        print(f"    - Plan migration path to multi-agent if complexity grows")
        print(f"    - Monitor the migration thresholds in ARCHITECTURE_GUIDE.md")
    
    print(f"\n📚 For detailed guidance, see ARCHITECTURE_GUIDE.md")
    print("=" * 60)

def main():
    """Main function to run the architecture decision helper."""
    try:
        responses, questions = get_user_input()
        multi_agent_score, multi_tool_score, factors = calculate_scores(responses, questions)
        provide_recommendation(multi_agent_score, multi_tool_score, factors)
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Run this script again anytime for architectural guidance.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()