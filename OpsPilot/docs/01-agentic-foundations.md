# OpsPilot — Agentic AI Foundations

## 1. Project Goal

OpsPilot is an AI-powered IT support agent designed to act as a first-line troubleshooting assistant for organizations.

When an employee reports an IT incident, OpsPilot analyzes the request, identifies the problem, and gathers any missing information. Rather than simply providing predefined answers, it actively investigates incidents by retrieving relevant technical documentation, selecting appropriate diagnostic tools, and analyzing their results.

Based on its observations, the agent adapts its troubleshooting strategy, develops possible solutions, and tracks the progress of each investigation. It can recommend corrective actions, request human approval before executing consequential operations, create support tickets after obtaining user confirmation, or escalate complex incidents to IT technicians.

Its goal is to reduce manual IT support workload, improve troubleshooting efficiency, and provide reliable, structured, and traceable incident resolution while maintaining controlled and responsible AI autonomy.

## 2. Why an Agent?

A traditional chatbot mainly responds to user questions by generating text. Although it can provide troubleshooting instructions, it cannot independently investigate an incident or interact with diagnostic systems without additional capabilities.

A fixed workflow can automate predefined troubleshooting steps, but it may struggle with incidents that require different actions depending on previous results, missing information, or unexpected situations.

An AI agent is more suitable for OpsPilot because IT incidents are not always predictable. The agent can interpret the reported problem, determine what information is missing, select appropriate diagnostic tools, analyze their results, and adapt its troubleshooting strategy accordingly.

Unlike a simple chatbot, an agent can interact with external tools and use their results to decide what to do next.

Unlike a strictly predefined workflow, it can dynamically select different troubleshooting paths based on the context of each incident.

OpsPilot therefore combines agent-driven decision-making with deterministic workflows and application controls to provide flexible but controlled incident investigation.

## 3. Agent Capabilities

OpsPilot is designed to support multiple IT incident categories, including network connectivity, account access, software-related issues, and hardware-related problems.

Its main capabilities include:

### Incident Understanding and Classification
- Understand incoming incident descriptions.
- Identify the incident category.
- Extract relevant information.
- Determine whether additional information is required.

### Clarification and Context Gathering
- Ask users clarifying questions.
- Identify missing diagnostic information.
- Maintain the context of an ongoing investigation.

### Knowledge Retrieval
- Retrieve relevant technical documentation using Retrieval-Augmented Generation (RAG).
- Use ChromaDB as the vector database.
- Provide answers supported by retrieved documentation and references.

### Diagnostic Tool Selection
- Identify appropriate diagnostic tools.
- Select tools based on the incident and previous observations.
- Execute approved, non-destructive diagnostic operations automatically.

### Troubleshooting and Planning
- Analyze diagnostic results.
- Develop troubleshooting strategies.
- Adapt the investigation when new information becomes available.
- Recommend corrective actions.

### Ticket Management
- Prepare support ticket information.
- Request user confirmation before creating a ticket.
- Create and update tickets through controlled backend operations.

### Resolution Verification and Escalation
- Check whether the proposed solution actually resolved the issue.
- Avoid marking incidents as resolved without sufficient evidence.
- Escalate unresolved or complex incidents to human technicians.

## 4. Agent Boundaries

OpsPilot follows a bounded-autonomy approach. The agent can make decisions within predefined permissions, but it cannot independently override application security rules or perform unrestricted operations.

### 4.1 What the Agent Can Do Independently

- Classify incoming incidents.
- Retrieve relevant technical documentation.
- Ask clarifying questions.
- Select approved diagnostic tools.
- Execute non-destructive simulated diagnostics within predefined limits.
- Analyze diagnostic results.
- Develop and adapt troubleshooting plans.
- Recommend solutions.
- Prepare support ticket information.

### 4.2 What Requires Deterministic Validation

The trusted application backend is responsible for validating:

- Tool arguments and input formats.
- Whether a requested tool is permitted.
- User permissions and access rights.
- Ticket information before database operations.
- Approval requirements for consequential actions.
- Execution limits, retries, and timeouts.
- Evidence required before an incident can be marked as resolved.

### 4.3 What Requires Human or User Approval

- Creating a support ticket requires explicit user confirmation.
- Consequential operations that could affect users or infrastructure require appropriate human approval.
- Actions outside the agent's predefined permissions must be rejected or escalated.

Approval must be associated with the exact proposed action rather than treated as unrestricted permission.

## 5. Hybrid Architecture

OpsPilot uses a hybrid architecture combining AI-driven reasoning with deterministic application logic.

The agent is responsible for flexible decision-making and investigation, while the application backend enforces security, authorization, validation, and controlled execution.

### 5.1 Agent Responsibilities

The Python and LangGraph service handles:

- Agent orchestration.
- Incident investigation.
- Reasoning and decision-making.
- Tool selection.
- Troubleshooting planning.
- RAG-based knowledge retrieval.
- Investigation state and workflow progression.
- Controlled loops and escalation decisions.

### 5.2 Backend Responsibilities

The ASP.NET Core backend handles:

- API endpoints and application logic.
- Authentication and authorization.
- Incident and ticket management.
- Database operations.
- Tool execution permissions.
- Human approval enforcement.
- User confirmation before ticket creation.
- Validation of agent requests.
- Communication between the frontend and agent service.

### 5.3 Supporting Technologies

| Technology | Responsibility |
|---|---|
| React + TypeScript | Frontend and user interface |
| ASP.NET Core + C# | Main application backend |
| Python + LangGraph | Agent orchestration |
| ChromaDB | Vector storage for knowledge retrieval |
| PostgreSQL | Transactional application data |
| MCP | Standardized tool integration |
| Docker | Application containerization and deployment |

### 5.4 Why This Separation Matters

An LLM is useful for flexible reasoning, but it should not be trusted to enforce security policies or execute unrestricted operations.

Keeping authentication, authorization, validation, and approval enforcement inside the trusted backend makes the application more secure, predictable, and auditable.

The agent can propose an action, but the application determines whether that action is permitted and whether it can be executed.

## 6. Example Scenario — VPN Connectivity Issue

### Incident

An employee reports:

"I cannot connect to the company VPN, and I need it to access my work."

### Investigation Process

1. **Incident reception:** OpsPilot receives the employee's incident description.

2. **Classification:** The agent identifies the incident as a network/VPN connectivity issue.

3. **Information gathering:** It identifies missing information, such as the employee's device or the error message, and asks clarifying questions.

4. **Knowledge retrieval:** It searches the technical knowledge base for relevant VPN troubleshooting documentation using ChromaDB.

5. **Diagnostic selection:** Based on the available information, the agent selects an appropriate diagnostic tool.

6. **Backend validation:** The backend validates the requested tool, its arguments, and the applicable execution permissions.

7. **Diagnostic execution:** An approved, non-destructive simulated diagnostic tool is executed.

8. **Result analysis:** The agent interprets the diagnostic results and determines the next appropriate step.

9. **Adaptive troubleshooting:** Depending on the observations, the agent can select another diagnostic, retrieve additional documentation, or recommend a solution.

10. **Approval and confirmation:** Consequential actions require appropriate human approval. If a support ticket is needed, the agent presents its details and requests explicit user confirmation before creation.

11. **Resolution verification:** The system checks whether the problem has actually been resolved using observable results.

12. **Escalation:** If the issue remains unresolved or requires intervention, OpsPilot escalates it to a human IT technician.

### Expected Outcome

OpsPilot provides a structured troubleshooting experience, maintains the investigation context, and uses diagnostic evidence to guide its decisions.

It either helps the employee resolve the incident or escalates it to a human technician with the relevant investigation details.

The incident is only marked as resolved when sufficient evidence confirms that the problem has been fixed.

## 7. Key Design Principles

### 1. Bounded Autonomy
The agent operates within clearly defined permissions and execution limits.

### 2. Validated Tool Execution
All tool inputs and outputs must be validated before being trusted or used.

### 3. Human Oversight
Consequential operations require appropriate approval. Support ticket creation also requires explicit user confirmation.

### 4. Security by Design
The agent must not have unrestricted access to infrastructure, databases, or sensitive information.

### 5. Observability
Agent decisions, tool calls, diagnostic results, and outcomes should be traceable.

### 6. Resolution Verification
A successful tool call or a generated recommendation does not automatically mean that an incident is resolved.

### 7. Controlled Recovery
Failed operations must have safe retry, recovery, or escalation paths.

### 8. Untrusted External Data
Retrieved documents and tool outputs must be treated as untrusted data. They cannot override application instructions, permissions, or security policies.

### 9. Separation of Responsibilities
The agent handles flexible reasoning, while deterministic application code remains responsible for security-critical decisions and execution.

---

## Day 1 — Completion Summary

By completing this document, the initial design foundations of OpsPilot have been established.

The project will focus on building a controlled, multi-step AI agent capable of investigating different IT incidents using knowledge retrieval, diagnostic tools, and adaptive troubleshooting strategies.

Its architecture will combine React, ASP.NET Core, Python, LangGraph, ChromaDB, PostgreSQL, MCP, and Docker.

The next development phase will focus on understanding ReAct, reasoning loops, and tool calling before implementing the agent's orchestration logic.
