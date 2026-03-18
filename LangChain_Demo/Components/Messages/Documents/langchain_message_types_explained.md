# LangChain Message Types Explained in Plain English

LangChain uses **messages** to represent parts of a conversation. Think of them like labeled chat bubbles. Each type has a different job.

## The Main Message Types

In everyday use, there are **5 common message types**:

1. **System message**
2. **Human message**
3. **AI message**
4. **Tool message**
5. **Function message**

Depending on the version and setup, you may mostly see the first **4**. The **Function message** is older and is less common in newer workflows.

---

## 1) System Message

A **System message** tells the assistant how to behave.

It is like giving instructions before the chat starts.

### Simple example

- “Answer in simple English.”
- “Be polite and keep replies short.”
- “You are a travel helper.”

### Real-life use case

A company wants its chatbot to always sound professional and friendly.

So it adds a system message like:

> You are a customer support assistant. Explain things clearly and politely.

### Why it matters

It helps keep the assistant’s style and role consistent.

---

## 2) Human Message

A **Human message** is the user’s input.

It is simply what the person asks or says.

### Simple example

- “What is cloud storage?”
- “Write a leave application.”
- “Summarize this paragraph.”

### Real-life use case

A student types:

> Explain photosynthesis in simple words.

That student request is a human message.

### Why it matters

This is the main thing the assistant responds to.

---

## 3) AI Message

An **AI message** is the assistant’s reply.

It contains the answer, explanation, or next step.

### Simple example

User asks:

> What is cloud storage?

Assistant replies:

> Cloud storage means saving your files on the internet instead of only on your computer.

That reply is an AI message.

### Real-life use case

A shopping helper bot answers:

> This phone is a good choice for daily use because it has a long battery life.

### Why it matters

It is the response shown back to the user.

---

## 4) Tool Message

A **Tool message** is information returned from a helper tool.

A tool can do something extra, such as:

- search the web
- check a database
- do a calculation
- read a file

### Simple example

User asks:

> What is 25 × 18?

The assistant may use a calculator tool.

The tool returns:

> 450

That returned result is a tool message.

### Real-life use case

A travel assistant checks a weather tool and gets:

> Tomorrow in Delhi: 32°C, clear sky.

That weather result is a tool message.

### Why it matters

It lets the assistant use outside help instead of guessing.

---

## 5) Function Message

A **Function message** is an older way of passing back results from a called function.

In plain terms, it is very similar to a tool message.

### Simple example

A helper function looks up order status and returns:

> Order #1024 is out for delivery.

That can be stored as a function message in older setups.

### Real-life use case

A company chatbot checks an order system and gets shipping details.

### Why it matters

You may still see it in older examples or older LangChain code.

---

## Easy Way to Remember

You can remember the flow like this:

- **System** = rules for the assistant
- **Human** = user speaks
- **AI** = assistant answers
- **Tool** = outside helper gives data
- **Function** = older helper-result format

---

## A Small Full Example

Here is a simple conversation flow:

### Step 1: System message

> You are a helpful teacher. Explain things in simple English.

### Step 2: Human message

> What is a black hole?

### Step 3: AI message

> A black hole is a place in space where gravity is so strong that even light cannot easily escape.

### Step 4: Tool message (optional)

If the assistant checks a science source, the returned result from that source would be a tool message.

---

## Which Message Types Are Most Important?

For most beginners, the most important ones are:

- **System message**
- **Human message**
- **AI message**
- **Tool message**

These are the ones you are most likely to use in modern LangChain work.

---

## Final Answer

So, in simple terms, LangChain commonly has **4 main message types in modern use**:

1. System
2. Human
3. AI
4. Tool

And you may also see **Function message** in older examples, making it **5 types** in total if you include older usage.

---

## Quick Summary Table

| Message Type | What it means | Example |
|---|---|---|
| System | Instructions for the assistant | “Answer politely.” |
| Human | Message from the user | “What is Python?” |
| AI | Reply from the assistant | “Python is a programming language.” |
| Tool | Result from a helper tool | “Search result: ...” |
| Function | Older helper-result message | “Order shipped.” |

---

## Bottom Line

If someone asks, **“How many message types are in LangChain?”**, the best plain-English answer is:

> **Usually 4 main ones in modern use, and 5 if you include the older Function message type.**

