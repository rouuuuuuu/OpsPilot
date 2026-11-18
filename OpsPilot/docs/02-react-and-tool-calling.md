
# OpsPilot — ReAct and Tool Calling

## 1. ReAct Pattern

ReAct stands for Reasoning + Acting.

It is an agent design pattern in which an LLM alternates between reasoning about a task, taking actions through tools, and observing their results.

The cycle consists of:

- Reason: Determine the next appropriate action.
- Act: Request execution of a selected tool.
- Observe: Analyze the returned result.
- Repeat: Continue, ask for clarification, escalate, or finish.

## 2. Tool Calling

Tool calling allows an LLM to request the execution of predefined application functions through structured arguments.

The application remains responsible for validating and executing those requests.

The tool-calling lifecycle is:

1. Provide the LLM with available tool definitions.
2. Receive a structured tool request.
3. Validate the requested tool and arguments.
4. Check authorization and execution limits.
5. Execute the tool.
6. Return its result to the LLM.
7. Continue the agent's investigation.

## 3. Initial Diagnostic Tools

### Tool 1: check_vpn_status

Purpose:
Check whether the VPN service is running on a specified device.

Input:
- device_id: string

Expected output:
- device_id
- service_status
- diagnostic_message

### Tool 2: check_network_connectivity

Purpose:
Check the network connectivity of a specified device.

Input:
- device_id: string

Expected output:
- device_id
- connectivity_status
- diagnostic_message

### Tool 3: get_device_information

Purpose:
Retrieve basic information about a specified device.

Input:
- device_id: string

Expected output:
- device_id
- operating_system
- network_adapter_status

## 4. Tool Execution Rules

- Only registered tools can be executed.
- Tool arguments must be validated.
- Only approved non-destructive diagnostics can execute automatically.
- Execution must have timeouts and retry limits.
- Tool outputs must be validated before being used.
- Diagnostic tools must not perform corrective actions.

## 5. ReAct Example

Incident:
"I cannot connect to the company VPN."

Investigation:

1. Classify the incident as VPN connectivity.
2. Call check_vpn_status.
3. Observe the service status.
4. Decide whether network diagnostics are necessary.
5. Call check_network_connectivity if appropriate.
6. Observe the connectivity result.
7. Retrieve relevant troubleshooting documentation.
8. Recommend the next step or escalate.

## 6. Key Takeaway

The LLM proposes actions through structured tool calls, while the application validates and executes them.

Tool results inform the next agent decision.
