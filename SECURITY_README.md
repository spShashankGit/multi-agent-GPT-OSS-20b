# Prompt Injection Security Guide

This repository now includes comprehensive protection against prompt injection attacks. This document explains how to use the security features and protect your multi-agent AI system.

## Quick Start

### Basic Protection

```python
from security_utils import is_input_safe

# Quick safety check
user_input = "What is the weather in Paris?"
if is_input_safe(user_input):
    # Process the input
    process_safe_input(user_input)
else:
    # Handle suspicious input
    print("Input blocked for security reasons")
```

### Advanced Protection

```python
from security_utils import SecurePromptBuilder

# Create secure prompts
builder = SecurePromptBuilder()
system_prompt = "You are a helpful assistant."
user_input = "Tell me about renewable energy"

secure_prompt, is_safe = builder.build_secure_prompt(
    system_prompt, 
    user_input,
    sanitization_mode="moderate",
    block_suspicious=True
)
```

## Files Overview

### Core Security Files

- **`security_utils.py`** - Main security utilities module
- **`PROMPT_INJECTION_GUIDE.md`** - Comprehensive educational guide
- **`prompt_injection_demo.py`** - Interactive demonstration script
- **`test_security.py`** - Unit tests for security features

### Protected Agent Files

- **`agents/secure_master_agent.py`** - Hardened version of the master agent
- **`agents/master_agent.py`** - Original agent (for comparison)

## Security Features

### 1. Input Validation and Detection

The `PromptInjectionDetector` class identifies suspicious patterns:

```python
from security_utils import PromptInjectionDetector

detector = PromptInjectionDetector()
is_suspicious, patterns = detector.detect_injection(user_input)
```

**Detection Patterns:**
- Instruction override attempts ("ignore previous instructions")
- Role confusion ("you are now acting as")
- Context switching markers ("[SYSTEM]", "---ADMIN---")
- Jailbreaking attempts ("hypothetically speaking")
- Suspicious character sequences (code blocks, HTML tags)

### 2. Input Sanitization

The `InputSanitizer` class cleans potentially dangerous input:

```python
from security_utils import InputSanitizer

sanitizer = InputSanitizer()

# Different sanitization levels
basic_clean = sanitizer.sanitize_input(text, "basic")       # Minimal cleaning
moderate_clean = sanitizer.sanitize_input(text, "moderate") # Balanced approach
strict_clean = sanitizer.sanitize_input(text, "strict")    # Aggressive cleaning
```

### 3. Secure Prompt Building

The `SecurePromptBuilder` combines detection, sanitization, and structured prompting:

```python
from security_utils import SecurePromptBuilder

builder = SecurePromptBuilder()
secure_prompt, is_safe = builder.build_secure_prompt(
    system_prompt="You are a helpful assistant",
    user_input=user_input,
    sanitization_mode="moderate",
    block_suspicious=True
)
```

### 4. Output Validation

Monitor AI responses for signs of successful injection:

```python
from security_utils import validate_model_output

is_safe, concerns = validate_model_output(ai_response)
if not is_safe:
    print(f"Suspicious output detected: {concerns}")
```

## Usage Examples

### Protecting the Master Agent

```python
# Import security utilities
from security_utils import SecurePromptBuilder, validate_model_output

class SecureAgent:
    def __init__(self):
        self.security = SecurePromptBuilder()
    
    def process_query(self, user_input):
        # Validate and secure the input
        secure_prompt, is_safe = self.security.build_secure_prompt(
            "You are a helpful data analyst",
            user_input
        )
        
        if not is_safe:
            return "Query blocked for security reasons"
        
        # Process with LLM
        response = self.llm.invoke(secure_prompt)
        
        # Validate output
        output_safe, concerns = validate_model_output(response)
        if not output_safe:
            print(f"Warning: {concerns}")
        
        return response
```

### Protecting Search Tools

```python
@tool
def secure_search_tool(query: str) -> str:
    """Secure web search tool."""
    
    # Validate search query
    if not is_input_safe(query):
        return "Search query blocked for security reasons"
    
    # Perform search
    results = search_api(query)
    
    # Sanitize results
    clean_results = []
    for result in results:
        # Filter potentially dangerous content
        if not contains_malicious_content(result):
            clean_results.append(result)
    
    return format_results(clean_results)
```

## Testing Security

Run the comprehensive test suite:

```bash
# Run all security tests
python test_security.py

# Run the interactive demonstration
python prompt_injection_demo.py

# Test the secure agent (requires LM Studio running on localhost:1234)
python agents/secure_master_agent.py
```

## Security Best Practices

### For Developers

1. **Always validate input** - Use `is_input_safe()` or `PromptInjectionDetector`
2. **Sanitize when possible** - Use `InputSanitizer` for suspicious but not clearly malicious input
3. **Use structured prompts** - Clearly separate system instructions from user input
4. **Monitor outputs** - Use `validate_model_output()` to catch successful injections
5. **Implement defense in depth** - Multiple security layers are better than one

### For System Administrators

1. **Log security events** - Monitor for attack patterns
2. **Regular updates** - Keep detection patterns current
3. **Security reviews** - Audit prompts and agent behaviors
4. **User education** - Train users on safe AI interaction
5. **Incident response** - Have plans for security breaches

### For Users

1. **Be aware of risks** - Understand what data you're sharing
2. **Verify AI responses** - Don't blindly trust outputs
3. **Report suspicious behavior** - Alert admins to potential attacks
4. **Use official interfaces** - Avoid unofficial or modified AI tools

## Configuration Options

### Detection Sensitivity

Adjust detection patterns in `PromptInjectionDetector`:

```python
detector = PromptInjectionDetector()
# Add custom patterns
detector.injection_patterns.append(r'your_custom_pattern')
detector.compiled_patterns = [re.compile(p, re.IGNORECASE) for p in detector.injection_patterns]
```

### Sanitization Modes

- **basic**: Minimal filtering, removes obvious system markers
- **moderate**: Balanced approach, replaces some patterns
- **strict**: Aggressive filtering, may remove legitimate content

### Response to Threats

Configure how to handle detected threats:

```python
builder = SecurePromptBuilder()
secure_prompt, is_safe = builder.build_secure_prompt(
    system_prompt,
    user_input,
    block_suspicious=True,    # Block obvious attacks
    sanitization_mode="moderate"  # Clean suspicious content
)
```

## Troubleshooting

### False Positives

If legitimate input is being blocked:

1. Check the detection patterns
2. Use a less strict sanitization mode
3. Add custom whitelisting logic
4. Adjust the `block_suspicious` setting

### False Negatives

If malicious input is getting through:

1. Add new detection patterns
2. Use stricter sanitization modes
3. Implement additional output validation
4. Report new attack vectors

### Performance Issues

If security checks are too slow:

1. Cache compiled regex patterns
2. Use basic sanitization mode
3. Implement async validation
4. Optimize detection patterns

## Contributing

To contribute security improvements:

1. Add new attack patterns to the detection list
2. Improve sanitization algorithms
3. Add test cases for new threats
4. Update documentation with new best practices

## References

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Prompt Injection Attack Research](https://arxiv.org/abs/2306.05499)
- [LLM Security Best Practices](https://arxiv.org/abs/2302.12173)

---

**⚠️ Security Notice:** These protections significantly reduce risk but cannot guarantee 100% security. Always implement multiple layers of defense and stay updated with the latest security research.