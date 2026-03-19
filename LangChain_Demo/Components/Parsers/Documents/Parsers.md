# Parsers in LangChain

## What are Parsers in LangChain?

In **LangChain**, parsers (often called *Output Parsers*) are components that help convert the raw output of a language model (LLM) into a structured and usable format.

LLMs typically return unstructured text. Parsers ensure that this text is transformed into:
- JSON
- Lists
- Python objects
- Custom schemas

This makes it easier to integrate LLM outputs into applications, APIs, and workflows.

---

## Why Use Parsers?

- Ensure consistent output format
- Reduce ambiguity in LLM responses
- Enable automation and downstream processing
- Validate and enforce structure

---

## Types of Parsers in LangChain

### 1. **StrOutputParser**
**Description:**  
The simplest parser that returns raw string output.

**Use Case:**
- When you just need plain text output
- No formatting or structure required

**Example Use Case:**
- Chatbots
- Text generation

---

### 2. **CommaSeparatedListOutputParser**
**Description:**  
Parses output into a list by splitting on commas.

**Use Case:**
- Extracting lists from LLM responses

**Example Use Case:**
- Generating tags, keywords, or items

---

### 3. **StructuredOutputParser**
**Description:**  
Parses output into a predefined structured schema using response schemas.

**Use Case:**
- When you need strongly structured data

**Example Use Case:**
- Extracting user details (name, age, email)
- Form-like outputs

---

### 4. **PydanticOutputParser**
**Description:**  
Uses Pydantic models to validate and parse outputs into Python objects.

**Use Case:**
- Strict validation of output
- Type-safe parsing

**Example Use Case:**
- Backend systems requiring validated data
- API integrations

---

### 5. **JsonOutputParser**
**Description:**  
Ensures the output is valid JSON and parses it accordingly.

**Use Case:**
- When working with APIs or structured pipelines

**Example Use Case:**
- Returning structured responses for frontend apps

---

### 6. **OutputFixingParser**
**Description:**  
Wraps another parser and fixes malformed outputs using an LLM.

**Use Case:**
- When LLM outputs are inconsistent or invalid

**Example Use Case:**
- Fixing broken JSON responses

---

### 7. **RetryOutputParser**
**Description:**  
Retries parsing by re-prompting the LLM if parsing fails.

**Use Case:**
- Improving reliability of structured outputs

**Example Use Case:**
- Critical workflows where correctness matters

---

### 8. **RegexParser**
**Description:**  
Extracts data using regular expressions.

**Use Case:**
- When output follows predictable patterns

**Example Use Case:**
- Extracting emails, phone numbers, IDs

---

## Summary Table

| Parser Type                  | Output Format     | Best Use Case                          |
|----------------------------|------------------|----------------------------------------|
| StrOutputParser            | String           | Simple text output                     |
| CommaSeparatedListParser   | List             | Tags, items                            |
| StructuredOutputParser     | Dict             | Schema-based extraction                |
| PydanticOutputParser       | Python Object    | Validated structured data              |
| JsonOutputParser           | JSON             | API responses                          |
| OutputFixingParser         | Fixed Output     | Correct malformed outputs              |
| RetryOutputParser          | Reliable Output  | Critical systems                       |
| RegexParser                | Custom Extract   | Pattern-based extraction               |

---

## When to Use Which Parser?

- **Simple output →** StrOutputParser  
- **List extraction →** CommaSeparatedListOutputParser  
- **Strict schema →** StructuredOutputParser / PydanticOutputParser  
- **JSON workflows →** JsonOutputParser  
- **Error-prone outputs →** OutputFixingParser / RetryOutputParser  
- **Pattern matching →** RegexParser  

---

## Conclusion

Parsers in LangChain are essential for transforming raw LLM outputs into structured, reliable, and usable data. Choosing the right parser depends on:
- Required structure
- Level of validation
- Reliability needs

They play a critical role in building production-ready AI applications.

---