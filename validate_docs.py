#!/usr/bin/env python3
"""
Validation script to ensure all documentation examples and links are working correctly.
"""

import os
import sys

def check_file_exists(filepath, description):
    """Check if a file exists and report status."""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - FILE NOT FOUND")
        return False

def check_documentation_structure():
    """Validate that all documentation files are properly structured."""
    
    print("🔍 Validating Documentation Structure")
    print("=" * 50)
    
    all_good = True
    
    # Check main documentation files
    files_to_check = [
        ("readme.md", "Main README"),
        ("ARCHITECTURE_GUIDE.md", "Comprehensive Architecture Guide"),
        ("QUICK_REFERENCE.md", "Quick Reference Guide"),
        ("architecture_decision_helper.py", "Interactive Decision Helper"),
        ("agents/master_agent.py", "Example Agent Implementation")
    ]
    
    for filepath, description in files_to_check:
        if not check_file_exists(filepath, description):
            all_good = False
    
    # Check for key content in files
    print(f"\n🔍 Checking File Contents")
    print("-" * 30)
    
    # Check README has key sections
    try:
        with open("readme.md", "r") as f:
            readme_content = f.read()
            
        required_sections = [
            "Multi-Agent Approach",
            "Multi-Tool Approach", 
            "Interactive Decision Helper",
            "ARCHITECTURE_GUIDE.md",
            "QUICK_REFERENCE.md"
        ]
        
        for section in required_sections:
            if section in readme_content:
                print(f"✅ README contains: {section}")
            else:
                print(f"❌ README missing: {section}")
                all_good = False
                
    except Exception as e:
        print(f"❌ Error reading README: {e}")
        all_good = False
    
    # Check architecture guide has decision criteria
    try:
        with open("ARCHITECTURE_GUIDE.md", "r") as f:
            guide_content = f.read()
            
        required_content = [
            "Decision Criteria and Thresholds",
            "Choose Multi-Agent When",
            "Choose Multi-Tool When", 
            "Migration Thresholds",
            "Performance Considerations"
        ]
        
        for content in required_content:
            if content in guide_content:
                print(f"✅ Architecture Guide contains: {content}")
            else:
                print(f"❌ Architecture Guide missing: {content}")
                all_good = False
                
    except Exception as e:
        print(f"❌ Error reading Architecture Guide: {e}")
        all_good = False
    
    # Test decision helper syntax
    try:
        import py_compile
        py_compile.compile("architecture_decision_helper.py", doraise=True)
        print("✅ Decision Helper: Valid Python syntax")
    except py_compile.PyCompileError as e:
        print(f"❌ Decision Helper: Syntax error - {e}")
        all_good = False
    except Exception as e:
        print(f"❌ Decision Helper: Compilation error - {e}")
        all_good = False
    
    print(f"\n{'='*50}")
    if all_good:
        print("🎉 All documentation validation checks passed!")
        print("🚀 The architectural guidance is ready for use.")
        return True
    else:
        print("❌ Some validation checks failed.")
        print("🔧 Please review and fix the issues above.")
        return False

def main():
    """Main validation function."""
    print("📋 Documentation Validation Tool")
    print("=" * 50)
    
    if not os.path.exists("readme.md"):
        print("❌ This script must be run from the repository root directory.")
        sys.exit(1)
    
    success = check_documentation_structure()
    
    if success:
        print(f"\n🎯 Quick Start:")
        print(f"  1. Read QUICK_REFERENCE.md for decision matrix")
        print(f"  2. Run: python architecture_decision_helper.py")
        print(f"  3. See ARCHITECTURE_GUIDE.md for detailed guidance")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()