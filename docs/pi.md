### Quick Start Example

Source: https://pi.dev/docs/latest/sdk

A basic example demonstrating how to set up credentials, create an agent session, subscribe to events, and send a prompt.

```APIDOC
## Quick Start
```javascript
import { AuthStorage, createAgentSession, ModelRegistry, SessionManager } from "@mariozechner/pi-coding-agent";

// Set up credential storage and model registry
const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("What files are in the current directory?");
```
```

--------------------------------

### Install Pi Packages from Git Repositories

Source: https://pi.dev/docs/latest/packages

Examples of installing Pi packages directly from git repositories using different URL formats and SSH shorthand.

```bash
# git@host:path shorthand (requires git: prefix)
pi install git:git@github.com:user/repo

# ssh:// protocol format
pi install ssh://git@github.com/user/repo

# With version ref
pi install git:git@github.com:user/repo@v1.0.0
```

--------------------------------

### Complete Agent Session Setup and Execution

Source: https://pi.dev/docs/latest/sdk

A comprehensive example demonstrating the setup of authentication, model registry, tools, settings, resource loader, and initiating an agent session with a prompt. Includes custom tool definition and session subscription for real-time output.

```typescript
import { getModel } from "@mariozech/pi-ai";
import { Type } from "typebox";
import {
  AuthStorage,
  bashTool,
  createAgentSession,
  DefaultResourceLoader,
  defineTool,
  ModelRegistry,
  readTool,
  SessionManager,
  SettingsManager,
} from "@mariozechner/pi-coding-agent";

// Set up auth storage (custom location)
const authStorage = AuthStorage.create("/custom/agent/auth.json");

// Runtime API key override (not persisted)
if (process.env.MY_KEY) {
  authStorage.setRuntimeApiKey("anthropic", process.env.MY_KEY);
}

// Model registry (no custom models.json)
const modelRegistry = ModelRegistry.create(authStorage);

// Inline tool
const statusTool = defineTool({
  name: "status",
  label: "Status",
  description: "Get system status",
  parameters: Type.Object({}),
  execute: async () => ({
    content: [{ type: "text", text: `Uptime: ${process.uptime()}s` }],
    details: {},
  }),
});

const model = getModel("anthropic", "claude-opus-4-5");
if (!model) throw new Error("Model not found");

// In-memory settings with overrides
const settingsManager = SettingsManager.inMemory({
  compaction: { enabled: false },
  retry: { enabled: true, maxRetries: 2 },
});

const loader = new DefaultResourceLoader({
  cwd: process.cwd(),
  agentDir: "/custom/agent",
  settingsManager,
  systemPromptOverride: () => "You are a minimal assistant. Be concise.",
});
await loader.reload();

const { session } = await createAgentSession({
  cwd: process.cwd(),
  agentDir: "/custom/agent",

  model,
  thinkingLevel: "off",
  authStorage,
  modelRegistry,

  tools: [readTool, bashTool],
  customTools: [statusTool],
  resourceLoader: loader,

  sessionManager: SessionManager.inMemory(),
  settingsManager,
});

session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("Get status and list files.");

```

--------------------------------

### Brave Search Skill Setup

Source: https://pi.dev/docs/latest/skills

Install dependencies for the Brave Search skill by running this command in the skill's directory.

```bash
cd /path/to/brave-search && npm install
```

--------------------------------

### Create and Load a Basic Extension

Source: https://pi.dev/docs/latest/extensions

This example demonstrates how to create a basic extension that reacts to session start and tool call events, registers a custom 'greet' tool, and a '/hello' command. Place this file in `~/.pi/agent/extensions/my-extension.ts` for auto-discovery.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  // React to events
  pi.on("session_start", async (_event, ctx) => {
    ctx.ui.notify("Extension loaded!", "info");
  });

  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName === "bash" && event.input.command?.includes("rm -rf")) {
      const ok = await ctx.ui.confirm("Dangerous!", "Allow rm -rf?");
      if (!ok) return { block: true, reason: "Blocked by user" };
    }
  });

  // Register a custom tool
  pi.registerTool({
    name: "greet",
    label: "Greet",
    description: "Greet someone by name",
    parameters: Type.Object({
      name: Type.String({ description: "Name to greet" }),
    }),
    async execute(toolCallId, params, signal, onUpdate, ctx) {
      return {
        content: [{ type: "text", text: `Hello, ${params.name}!` }],
        details: {},
      };
    },
  });

  // Register a command
  pi.registerCommand("hello", {
    description: "Say hello",
    handler: async (args, ctx) => {
      ctx.ui.notify(`Hello ${args || "world"}!`, "info");
    },
  });
}

```

--------------------------------

### SKILL.md Frontmatter and Usage Example

Source: https://pi.dev/docs/latest/skills

Defines the skill's metadata and provides setup and usage instructions. Relative paths are used for referencing assets within the skill directory.

```markdown
---
name: my-skill
description: What this skill does and when to use it. Be specific.
---

# My Skill

## Setup

Run once before first use:
```bash
cd /path/to/skill && npm install
```

## Usage

```bash
./scripts/process.sh <input>
```

See [the reference guide](references/REFERENCE.md) for details.

```

--------------------------------

### Run Pi

Source: https://pi.dev/docs/latest

Starts the Pi terminal coding harness. After installation, you can run Pi from your terminal.

```bash
pi
```

--------------------------------

### Prompt Template Usage Examples

Source: https://pi.dev/docs/latest/prompt-templates

Demonstrates how to invoke prompt templates from the editor using a slash command, with examples of direct invocation and invocation with arguments.

```shell
/review                           # Expands review.md
/component Button                 # Expands with argument
/component Button "click handler" # Multiple arguments

```

--------------------------------

### Branch Summarization Path Example

Source: https://pi.dev/docs/latest/tree

Visualizes the path that gets summarized when switching branches, starting from the old leaf and going back to the common ancestor with the target branch. Summarization stops at the common ancestor or a compaction node.

```text
A → B → C → D → E → F  ← old leaf
        ↘ G → H        ← target

Abandoned path: D → E → F (summarized)
```

--------------------------------

### Vim Keybinding Example

Source: https://pi.dev/docs/latest/keybindings

Example configuration for Vim-style keybindings. This enables users to leverage their familiarity with Vim commands within the application.

```json
{
  "tui.editor.cursorUp": ["up", "alt+k"],
  "tui.editor.cursorDown": ["down", "alt+j"],
  "tui.editor.cursorLeft": ["left", "alt+h"],
  "tui.editor.cursorRight": ["right", "alt+l"],
  "tui.editor.cursorWordLeft": ["alt+left", "alt+b"],
  "tui.editor.cursorWordRight": ["alt+right", "alt+w"]
}
```

--------------------------------

### Install Pi with npm

Source: https://pi.dev/docs/latest

Installs the Pi coding agent globally using npm. Ensure you have Node.js and npm installed.

```bash
npm install -g @mariozechner/pi-coding-agent
```

--------------------------------

### Example Agent Settings Configuration

Source: https://pi.dev/docs/latest/settings

A comprehensive example of agent settings, including default provider, model, theme, compaction, retry logic, enabled models, warnings, and package loading.

```json
{
  "defaultProvider": "anthropic",
  "defaultModel": "claude-sonnet-4-20250514",
  "defaultThinkingLevel": "medium",
  "theme": "dark",
  "compaction": {
    "enabled": true,
    "reserveTokens": 16384,
    "keepRecentTokens": 20000
  },
  "retry": {
    "enabled": true,
    "maxRetries": 3
  },
  "enabledModels": ["claude-*", "gpt-4o"],
  "warnings": {
    "anthropicExtraUsage": true
  },
  "packages": ["pi-skills"]
}
```

--------------------------------

### Clone and Install Pi Project

Source: https://pi.dev/docs/latest/development

Clone the Pi monorepo, navigate into the directory, install dependencies, and build the project.

```bash
git clone https://github.com/badlogic/pi-mono
cd pi-mono
npm install
npm run build

```

--------------------------------

### Emacs Keybinding Example

Source: https://pi.dev/docs/latest/keybindings

Example configuration for Emacs-style keybindings. This allows users to map common Emacs commands to application actions.

```json
{
  "tui.editor.cursorUp": ["up", "ctrl+p"],
  "tui.editor.cursorDown": ["down", "ctrl+n"],
  "tui.editor.cursorLeft": ["left", "ctrl+b"],
  "tui.editor.cursorRight": ["right", "ctrl+f"],
  "tui.editor.cursorWordLeft": ["alt+left", "alt+b"],
  "tui.editor.cursorWordRight": ["alt+right", "alt+f"],
  "tui.editor.deleteCharForward": ["delete", "ctrl+d"],
  "tui.editor.deleteCharBackward": ["backspace", "ctrl+h"],
  "tui.input.newLine": ["shift+enter", "ctrl+j"]
}
```

--------------------------------

### createAgentSession() - Minimal Example

Source: https://pi.dev/docs/latest/sdk

Demonstrates the minimal usage of `createAgentSession` with default resource loading.

```APIDOC
## createAgentSession()
### Minimal: defaults with DefaultResourceLoader
```javascript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

const { session } = await createAgentSession();
```
```

--------------------------------

### Argument Preparation Example

Source: https://pi.dev/docs/latest/extensions

Demonstrates the `prepareArguments` function to handle backward compatibility for tool arguments.

```APIDOC
## pi.registerTool("edit") with prepareArguments

### Description
This tool allows editing a single file using exact text replacement. The `prepareArguments` function ensures compatibility with older argument structures.

### Parameters
- **path** (string) - Required - The path to the file to edit.
- **edits** (array of objects) - Required - An array of edit operations.
  - **oldText** (string) - Required - The exact text to be replaced.
  - **newText** (string) - Required - The text to replace `oldText` with.

### prepareArguments
Transforms older argument formats (e.g., `oldText`, `newText`) into the current `edits` array format.

### execute
Applies the specified edits to the file.

#### Arguments
- **toolCallId** (string): Unique identifier for the tool call.
- **params** (object): The parameters for the tool, including `path` and `edits`.

#### Response Example
```json
{
  "content": [
    {
      "type": "text",
      "text": "Applying 2 edit block(s)"
    }
  ],
  "details": {}
}
```
```

--------------------------------

### Install and Manage Pi Packages

Source: https://pi.dev/docs/latest/packages

Commands for installing, removing, listing, and updating Pi packages. Use `-l` for project settings instead of global. Use `-e` to try a package without installing.

```bash
pi install npm:@foo/bar@1.0.0
pi install git:github.com/user/repo@v1
pi install https://github.com/user/repo  # raw URLs work too
pi install /absolute/path/to/package
pi install ./relative/path/to/package

pi remove npm:@foo/bar
pi list                     # show installed packages from settings
pi update                   # update pi and all non-pinned packages
pi update --extensions      # update all non-pinned packages only
pi update --self            # update pi only
pi update npm:@foo/bar      # update one package
pi update --extension npm:@foo/bar
```

```bash
pi -e npm:@foo/bar
pi -e git:github.com/user/repo
```

--------------------------------

### Install Pi Coding Agent SDK

Source: https://pi.dev/docs/latest/sdk

Installs the Pi Coding Agent SDK using npm. The SDK is included in the main package and requires no separate installation.

```bash
npm install @mariozechner/pi-coding-agent

```

--------------------------------

### Session File Location Example

Source: https://pi.dev/docs/latest/session

Illustrates the typical file path for storing session data.

```bash
~/.pi/agent/sessions/--<path>--/<timestamp>_<uuid>.jsonl

```

--------------------------------

### Install Pi and Dependencies in Termux

Source: https://pi.dev/docs/latest/termux

Update packages, install necessary dependencies like Node.js and Termux-API, and then install the Pi agent globally. Finally, create a configuration directory and run Pi.

```bash
pkg update && pkg upgrade

pkg install nodejs termux-api git

npm install -g @mariozechner/pi-coding-agent

mkdir -p ~/.pi/agent

pi
```

--------------------------------

### Start Pi in RPC Mode

Source: https://pi.dev/docs/latest/rpc

Use this command to start the Pi agent in RPC mode. Common options include specifying the LLM provider, model, and session persistence.

```bash
pi --mode rpc [options]

```

--------------------------------

### Install Pi Coding Agent

Source: https://pi.dev

Install the Pi coding agent globally using npm, pnpm, or bun. This command is used to set up the agent for use in your terminal.

```bash
curl -fsSL https://pi.dev/install.sh | bash
```

```bash
npm install -g @mariozechner/pi-coding-agent
```

```bash
pnpm add -g @mariozechner/pi-coding-agent
```

```bash
bun add -g @mariozechner/pi-coding-agent
```

--------------------------------

### createAgentSession() - Custom Example

Source: https://pi.dev/docs/latest/sdk

Shows how to customize `createAgentSession` by providing specific options like model, tools, and session manager.

```APIDOC
## createAgentSession()
### Custom: override specific options
```javascript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

const { session } = await createAgentSession({
  model: myModel,
  tools: [readTool, bashTool],
  sessionManager: SessionManager.inMemory(),
});
```
```

--------------------------------

### Install Termux API CLI Tools

Source: https://pi.dev/docs/latest/termux

If clipboard or other Termux:API functionalities are not working, ensure the CLI tools are installed.

```bash
pkg install termux-api
```

--------------------------------

### Project Overrides Example

Source: https://pi.dev/docs/latest/settings

Demonstrates how project-specific settings in `.pi/settings.json` override global settings in `~/.pi/agent/settings.json`. Nested objects are merged.

```json
// ~/.pi/agent/settings.json (global)
{
  "theme": "dark",
  "compaction": { "enabled": true, "reserveTokens": 16384 }
}

// .pi/settings.json (project)
{
  "compaction": { "reserveTokens": 8192 }
}

// Result
{
  "theme": "dark",
  "compaction": { "enabled": true, "reserveTokens": 8192 }
}
```

--------------------------------

### Skill Structure Example

Source: https://pi.dev/docs/latest/skills

A typical skill directory structure includes a `SKILL.md` file for frontmatter and instructions, along with optional directories for scripts, references, and assets.

```tree
my-skill/
├── SKILL.md              # Required: frontmatter + instructions
├── scripts/              # Helper scripts
│   └── process.sh
├── references/           # Detailed docs loaded on-demand
│   └── api-reference.md
└── assets/
    └── template.json

```

--------------------------------

### Install Pi Packages

Source: https://pi.dev

Install Pi packages from npm or git. This allows for extending Pi's functionality with custom tools, themes, and more.

```bash
$ pi install npm:@foo/pi-tools
```

```bash
$ pi install git:github.com/badlogic/pi-doom
```

--------------------------------

### Start a new session with parent tracking

Source: https://pi.dev/docs/latest/rpc

Starts a new session while optionally tracking its parent session for context.

```json
{"type": "new_session", "parentSession": "/path/to/parent-session.jsonl"}
```

--------------------------------

### Prompt Template Argument Usage

Source: https://pi.dev/docs/latest/prompt-templates

Example of how to use a prompt template that accepts multiple arguments, demonstrating the invocation with positional arguments.

```shell
/component Button "onClick handler" "disabled support"

```

--------------------------------

### Quick Start: Create and Use Agent Session

Source: https://pi.dev/docs/latest/sdk

Initializes an agent session with default configurations for authentication and model registry, then subscribes to message updates and sends an initial prompt.

```typescript
import { AuthStorage, createAgentSession, ModelRegistry, SessionManager } from "@mariozechner/pi-coding-agent";

// Set up credential storage and model registry
const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

session.subscribe((event) => {
  if (event.type === "message_update" && event.assistantMessageEvent.type === "text_delta") {
    process.stdout.write(event.assistantMessageEvent.delta);
  }
});

await session.prompt("What files are in the current directory?");

```

--------------------------------

### Create a Pi Package Manifest

Source: https://pi.dev/docs/latest/packages

Example `package.json` for a Pi package, defining extensions, skills, prompts, and themes using conventional directories. Include `pi-package` keyword for discoverability.

```json
{
  "name": "my-package",
  "keywords": ["pi-package"],
  "pi": {
    "extensions": ["./extensions"],
    "skills": ["./skills"],
    "prompts": ["./prompts"],
    "themes": ["./themes"]
  }
}
```

--------------------------------

### Streaming Text Response Example

Source: https://pi.dev/docs/latest/rpc

Illustrates the sequence of events when streaming a text response, from start to end, including text deltas.

```json
{"type":"message_update","message":{...},"assistantMessageEvent":{"type":"text_start","contentIndex":0,"partial":{...}}}
```

```json
{"type":"message_update","message":{...},"assistantMessageEvent":{"type":"text_delta","contentIndex":0,"delta":"Hello","partial":{...}}}
```

```json
{"type":"message_update","message":{...},"assistantMessageEvent":{"type":"text_delta","contentIndex":0,"delta":" world","partial":{...}}}
```

```json
{"type":"message_update","message":{...},"assistantMessageEvent":{"type":"text_end","contentIndex":0,"content":"Hello world","partial":{...}}}
```

--------------------------------

### Start a new session

Source: https://pi.dev/docs/latest/rpc

Initiates a new session. This can be overridden by a `session_before_switch` extension event handler.

```json
{"type": "new_session"}
```

--------------------------------

### Tool Execution Start Event

Source: https://pi.dev/docs/latest/rpc

Emitted when a tool begins execution. Includes the tool's name and arguments.

```json
{
  "type": "tool_execution_start",
  "toolCallId": "call_abc123",
  "toolName": "bash",
  "args": {"command": "ls -la"}
}
```

--------------------------------

### ctx.newSession(options?)

Source: https://pi.dev/docs/latest/extensions

Creates a new session, optionally with a parent session and setup logic. The `withSession` callback executes within the context of the new session.

```APIDOC
## ctx.newSession(options?)

### Description
Create a new session. This method is only available in commands.

### Method
await ctx.newSession(options)

### Parameters
#### Options
- **parentSession** (object) - Optional - The parent session file to record in the new session header.
- **setup** (function) - Optional - A function to mutate the new session's `SessionManager` before `withSession` runs.
- **withSession** (function) - Optional - A function that runs post-switch work against a fresh replacement-session context.

### Request Example
```javascript
const parentSession = ctx.sessionManager.getSessionFile();
const kickoff = "Continue in the replacement session";

const result = await ctx.newSession({
  parentSession,
  setup: async (sm) => {
    sm.appendMessage({
      role: "user",
      content: [{ type: "text", text: "Context from previous session..." }],
      timestamp: Date.now(),
    });
  },
  withSession: async (ctx) => {
    // Use only the replacement-session ctx here.
    await ctx.sendUserMessage(kickoff);
  },
});

if (result.cancelled) {
  // An extension cancelled the new session
}
```
```

--------------------------------

### Custom Summarizer Hook Example

Source: https://pi.dev/docs/latest/tree

An example of how to implement a custom summarizer by listening to the `session_before_tree` event. This handler can provide a custom summary or cancel the navigation.

```typescript
export default function(pi: HookAPI) {
  pi.on("session_before_tree", async (event, ctx) => {
    if (!event.preparation.userWantsSummary) return;
    if (event.preparation.entriesToSummarize.length === 0) return;
    
    const summary = await myCustomSummarizer(event.preparation.entriesToSummarize);
    return { summary: { summary, details: { custom: true } } };
  });
}
```

--------------------------------

### Agent start event

Source: https://pi.dev/docs/latest/rpc

Emitted when the agent begins processing a prompt.

```json
{"type": "agent_start"}
```

--------------------------------

### Autocomplete Dropdown Example

Source: https://pi.dev/docs/latest/prompt-templates

Illustrates how prompt templates with argument hints appear in the autocomplete dropdown, showing command names, argument placeholders, and descriptions.

```text
→ pr   <PR-URL>       — Review PRs from URLs with structured issue and code analysis
  is   <issue>        — Analyze GitHub issues (bugs or feature requests)
  wr   [instructions] — Finish the current task end-to-end
  cl   — Audit changelog entries before release

```

--------------------------------

### Register Command to Switch Sessions

Source: https://pi.dev/docs/latest/extensions

Register a command to allow users to switch sessions. This example uses `SessionManager.list()` to discover available sessions and `ctx.ui.select()` for user interaction.

```javascript
import { SessionManager } from "@mariozechner/pi-coding-agent";

pi.registerCommand("switch", {
  description: "Switch to another session",
  handler: async (args, ctx) => {
    const sessions = await SessionManager.list(ctx.cwd);
    if (sessions.length === 0) return;
    const choice = await ctx.ui.select(
      "Pick session:",
      sessions.map(s => s.file),
    );
    if (choice) {
      await ctx.switchSession(choice, {
        withSession: async (ctx) => {
          ctx.ui.notify("Switched session", "info");
        },
      });
    }
  },
});
```

--------------------------------

### new_session

Source: https://pi.dev/docs/latest/rpc

Start a fresh session. Can be cancelled by a `session_before_switch` extension event handler.

```APIDOC
## new_session

### Description
Start a fresh session. Can be cancelled by a `session_before_switch` extension event handler.

### Method
new_session

### Request Body
- **type** (string) - Required - Must be "new_session"
- **parentSession** (string) - Optional - Path to the parent session for tracking.

### Request Example
```json
{"type": "new_session"}
```

### Request Example with Parent Session
```json
{"type": "new_session", "parentSession": "/path/to/parent-session.jsonl"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "new_session"
- **success** (boolean) - true
- **data** (object) - Contains session cancellation status.
  - **cancelled** (boolean) - true if the session was cancelled by an extension.
```

--------------------------------

### Start with Only Extension Tools

Source: https://pi.dev/docs/latest/extensions

Use `--no-builtin-tools` to disable all built-in tools, enabling only the extensions specified with `-e`. This is useful for a clean environment focused solely on custom logic.

```bash
# No built-in tools, only extension tools
pi --no-builtin-tools -e ./my-extension.ts
```

--------------------------------

### Pi Package Source Types: npm

Source: https://pi.dev/docs/latest/packages

Specifies npm package sources for Pi. Versioned specs are pinned and skipped by updates. Global installs use `npm install -g`, project installs go under `.pi/npm/`.

```bash
npm:@scope/pkg@1.2.3
npm:pkg
```

--------------------------------

### Compaction Start Event

Source: https://pi.dev/docs/latest/rpc

Indicates the beginning of a compaction process, triggered manually or automatically due to thresholds or overflow.

```json
{"type": "compaction_start", "reason": "threshold"}
```

--------------------------------

### Handle agent_start / agent_end

Source: https://pi.dev/docs/latest/extensions

React to the start and end of an agent's processing for a user prompt.

```javascript
pi.on("agent_start", async (_event, ctx) => {});

pi.on("agent_end", async (event, ctx) => {
  // event.messages - messages from this prompt
});
```

--------------------------------

### Get available commands

Source: https://pi.dev/docs/latest/rpc

Retrieves a list of available commands, including extension commands, prompt templates, and skills. Commands can be invoked via the `prompt` command by prefixing with `/`.

```json
{"type": "get_commands"}
```

```json
{
  "type": "response",
  "command": "get_commands",
  "success": true,
  "data": {
    "commands": [
      {"name": "session-name", "description": "Set or clear session name", "source": "extension", "path": "/home/user/.pi/agent/extensions/session.ts"},
      {"name": "fix-tests", "description": "Fix failing tests", "source": "prompt", "location": "project", "path": "/home/user/myproject/.pi/agent/prompts/fix-tests.md"},
      {"name": "skill:brave-search", "description": "Web search via Brave API", "source": "skill", "location": "user", "path": "/home/user/.pi/agent/skills/brave-search/SKILL.md"}
    ]
  }
}
```

--------------------------------

### Register a Custom Tool with Parameters and Execution Logic

Source: https://pi.dev/docs/latest/extensions

Register a custom tool callable by the LLM. This example demonstrates defining tool parameters using TypeBox, including optional fields and string enums. It also shows how to implement the `execute` function for tool logic, including streaming updates and returning results. The `prepareArguments` function can be used for argument compatibility.

```typescript
import { Type } from "typebox";
import { StringEnum } from "@mariozechner/pi-ai";

pi.registerTool({
  name: "my_tool",
  label: "My Tool",
  description: "What this tool does",
  promptSnippet: "Summarize or transform text according to action",
  promptGuidelines: ["Use my_tool when the user asks to summarize previously generated text."],
  parameters: Type.Object({
    action: StringEnum(["list", "add"] as const),
    text: Type.Optional(Type.String()),
  }),
  prepareArguments(args) {
    // Optional compatibility shim. Runs before schema validation.
    // Return the current schema shape, for example to fold legacy fields
    // into the modern parameter object.
    return args;
  },

  async execute(toolCallId, params, signal, onUpdate, ctx) {
    // Stream progress
    onUpdate?.({ content: [{ type: "text", text: "Working..." }] });

    return {
      content: [{ type: "text", text: "Done" }],
      details: { result: "..." },
    };
  },

  // Optional: Custom rendering
  renderCall(args, theme, context) { ... },
  renderResult(result, options, theme, context) { ... },
});
```

--------------------------------

### Tree UI Example

Source: https://pi.dev/docs/latest/tree

Illustrates the hierarchical structure of session history as displayed in the tree UI. The active leaf is marked with '← active'.

```text
├─ user: "Hello, can you help..."
│  └─ assistant: "Of course! I can..."
│     ├─ user: "Let's try approach A..."
│     │  └─ assistant: "For approach A..."
│     │     └─ [compaction: 12k tokens]
│     │        └─ user: "That worked..."  ← active
│     └─ user: "Actually, approach B..."
│        └─ assistant: "For approach B..."

```

--------------------------------

### Handle Session Start Events

Source: https://pi.dev/docs/latest/extensions

Implement a listener for the 'session_start' event to perform actions when a session begins, loads, or reloads. Access event details like the reason and context for UI notifications.

```javascript
pi.on("session_start", async (event, ctx) => {
  // event.reason - "startup" | "reload" | "new" | "resume" | "fork"
  // event.previousSessionFile - present for "new", "resume", and "fork"
  ctx.ui.notify(`Session: ${ctx.sessionManager.getSessionFile() ?? "ephemeral"}`, "info");
});
```

--------------------------------

### Register Command and Tool for Runtime Reload

Source: https://pi.dev/docs/latest/extensions

This example registers a command to reload the runtime and a tool that triggers this command via a user message. This pattern allows LLMs to initiate extension reloads. The tool queues the `/reload-runtime` command as a follow-up.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  pi.registerCommand("reload-runtime", {
    description: "Reload extensions, skills, prompts, and themes",
    handler: async (_args, ctx) => {
      await ctx.reload();
      return;
    },
  });

  pi.registerTool({
    name: "reload_runtime",
    label: "Reload Runtime",
    description: "Reload extensions, skills, prompts, and themes",
    parameters: Type.Object({}),
    async execute() {
      pi.sendUserMessage("/reload-runtime", { deliverAs: "followUp" });
      return {
        content: [{ type: "text", text: "Queued /reload-runtime as a follow-up command." }],
      };
    },
  });
}
```

--------------------------------

### Custom UI Dialogs

Source: https://pi.dev/docs/latest/extensions

Provides examples of using `ctx.ui` methods for common dialogs like selection, confirmation, text input, and multi-line editing. Notifications can be shown non-blockingly.

```javascript
// Select from options
const choice = await ctx.ui.select("Pick one:", ["A", "B", "C"]);

// Confirm dialog
const ok = await ctx.ui.confirm("Delete?", "This cannot be undone");

// Text input
const name = await ctx.ui.input("Name:", "placeholder");

// Multi-line editor
const text = await ctx.ui.editor("Edit:", "prefilled text");

// Notification (non-blocking)
ctx.ui.notify("Done!", "info");  // "info" | "warning" | "error"
```

--------------------------------

### Turn Start Event

Source: https://pi.dev/docs/latest/rpc

Indicates the beginning of a turn, which comprises an assistant response and any associated tool calls and results.

```json
{"type": "turn_start"}
```

--------------------------------

### get_state

Source: https://pi.dev/docs/latest/rpc

Get current session state.

```APIDOC
## get_state

### Description
Get current session state.

### Method
get_state

### Request Body
- **type** (string) - Required - Must be "get_state"

### Request Example
```json
{"type": "get_state"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "get_state"
- **success** (boolean) - true
- **data** (object) - The current session state.
  - **model** (object or null) - The current model configuration.
  - **thinkingLevel** (string) - The current thinking level (e.g., "medium").
  - **isStreaming** (boolean) - Indicates if streaming is enabled.
  - **isCompacting** (boolean) - Indicates if compaction is enabled.
  - **steeringMode** (string) - The current steering mode (e.g., "all").
  - **followUpMode** (string) - The current follow-up mode (e.g., "one-at-a-time").
  - **sessionFile** (string) - Path to the session file.
  - **sessionId** (string) - The unique identifier for the session.
  - **sessionName** (string) - The display name of the session.
  - **autoCompactionEnabled** (boolean) - Indicates if auto-compaction is enabled.
  - **messageCount** (integer) - The number of messages in the session.
  - **pendingMessageCount** (integer) - The number of pending messages.
```

--------------------------------

### Clear npm Cache

Source: https://pi.dev/docs/latest/termux

If npm installation or other npm-related commands fail, try clearing the npm cache.

```bash
npm cache clean --force
```

--------------------------------

### SessionMessageEntry Examples

Source: https://pi.dev/docs/latest/session

Represents messages exchanged within a session. Includes user, assistant, and tool result messages with their respective content and metadata.

```json
{"type":"message","id":"a1b2c3d4","parentId":"prev1234","timestamp":"2024-12-03T14:00:01.000Z","message":{"role":"user","content":"Hello"}}
```

```json
{"type":"message","id":"b2c3d4e5","parentId":"a1b2c3d4","timestamp":"2024-12-03T14:00:02.000Z","message":{"role":"assistant","content":[{"type":"text","text":"Hi!"}],"provider":"anthropic","model":"claude-sonnet-4-5","usage":{...},"stopReason":"stop"}}
```

```json
{"type":"message","id":"c3d4e5f6","parentId":"b2c3d4e5","timestamp":"2024-12-03T14:00:03.000Z","message":{"role":"toolResult","toolCallId":"call_123","toolName":"bash","content":[{"type":"text","text":"output"}],"isError":false}}
```

--------------------------------

### get_messages

Source: https://pi.dev/docs/latest/rpc

Get all messages in the conversation.

```APIDOC
## get_messages

### Description
Get all messages in the conversation.

### Method
get_messages

### Request Body
- **type** (string) - Required - Must be "get_messages"

### Request Example
```json
{"type": "get_messages"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "get_messages"
- **success** (boolean) - true
- **data** (object)
  - **messages** (array) - An array of `AgentMessage` objects representing the conversation history.
```

--------------------------------

### Get forkable messages

Source: https://pi.dev/docs/latest/rpc

Retrieves a list of user messages that are available for forking.

```json
{"type": "get_fork_messages"}
```

```json
{
  "type": "response",
  "command": "get_fork_messages",
  "success": true,
  "data": {
    "messages": [
      {"entryId": "abc123", "text": "First prompt..."},
      {"entryId": "def456", "text": "Second prompt..."}
    ]
  }
}
```

--------------------------------

### Modify agent prompt with before_agent_start

Source: https://pi.dev/docs/latest/extensions

Intercept the agent's start to inject messages or modify the system prompt using structured options.

```javascript
pi.on("before_agent_start", async (event, ctx) => {
  // event.prompt - user's prompt text
  // event.images - attached images (if any)
  // event.systemPrompt - current chained system prompt for this handler
  //   (includes changes from earlier before_agent_start handlers)
  // event.systemPromptOptions - structured options used to build the system prompt
  //   .customPrompt - any custom system prompt (from --system-prompt, SYSTEM.md, or custom templates)
  //   .selectedTools - tools currently active in the prompt
  //   .toolSnippets - one-line descriptions for each tool
  //   .promptGuidelines - custom guideline bullets
  //   .appendSystemPrompt - text from --append-system-prompt flags
  //   .cwd - working directory
  //   .contextFiles - AGENTS.md files and other loaded context files
  //   .skills - loaded skills

  return {
    // Inject a persistent message (stored in session, sent to LLM)
    message: {
      customType: "my-extension",
      content: "Additional context for the LLM",
      display: true,
    },
    // Replace the system prompt for this turn (chained across extensions)
    systemPrompt: event.systemPrompt + "\n\nExtra instructions for this turn...",
  };
});
```

--------------------------------

### pi.getSessionName

Source: https://pi.dev/docs/latest/extensions

Get the current session name, if it has been set.

```APIDOC
## pi.getSessionName()

### Description
Get the current session name, if set.

### Returns
- (string | undefined) - The session name if set, otherwise undefined.
```

--------------------------------

### Example Session Events JSON Format

Source: https://pi.dev/docs/latest/json

Subsequent lines in the JSON event stream represent events as they occur during the session.

```json
{"type":"agent_start"}

```

```json
{"type":"turn_start"}

```

```json
{"type":"message_start","message":{"role":"assistant","content":[],...}}

```

```json
{"type":"message_update","message":{...},"assistantMessageEvent":{"type":"text_delta","delta":"Hello",...}}

```

```json
{"type":"message_end","message":{...}}

```

```json
{"type":"turn_end","message":{...},"toolResults":[]}

```

```json
{"type":"agent_end","messages":[...]}

```

--------------------------------

### Registering a Custom Provider

Source: https://pi.dev/docs/latest/custom-provider

Provides an example of how to register a custom stream function with the AI framework. Ensure all required fields like `baseUrl`, `apiKey`, and `api` are correctly set.

```javascript
pi.registerProvider("my-provider", {
  baseUrl: "https://api.example.com",
  apiKey: "MY_API_KEY",
  api: "my-custom-api",
  models: [...],
  streamSimple: streamMyProvider
});

```

--------------------------------

### Message Start and End Events

Source: https://pi.dev/docs/latest/rpc

These events mark the beginning and completion of a message. The `message` field contains an `AgentMessage` object.

```json
{"type": "message_start", "message": {...}}
```

```json
{"type": "message_end", "message": {...}}
```

--------------------------------

### Configure Package Loading (String Form)

Source: https://pi.dev/docs/latest/settings

Load all resources from specified npm or git packages.

```json
{
  "packages": ["pi-skills", "@org/my-extension"]
}
```

--------------------------------

### Get Session Statistics

Source: https://pi.dev/docs/latest/rpc

Retrieve token usage, cost statistics, and current context window usage for the session. Provides insights into resource consumption.

```json
{"type": "get_session_stats"}
```

--------------------------------

### Static Creation Methods

Source: https://pi.dev/docs/latest/session

Methods for creating or opening session instances.

```APIDOC
## SessionManager.create
### Description
Creates a new session.
### Method
`SessionManager.create(cwd, sessionDir?)
### Parameters
#### Path Parameters
- **cwd** (string) - Required - The current working directory.
- **sessionDir** (string) - Optional - The directory to store session files.

## SessionManager.open
### Description
Opens an existing session file.
### Method
`SessionManager.open(path, sessionDir?)
### Parameters
#### Path Parameters
- **path** (string) - Required - The path to the session file.
- **sessionDir** (string) - Optional - The directory to store session files.

## SessionManager.continueRecent
### Description
Continues the most recent session or creates a new one if none exists.
### Method
`SessionManager.continueRecent(cwd, sessionDir?)
### Parameters
#### Path Parameters
- **cwd** (string) - Required - The current working directory.
- **sessionDir** (string) - Optional - The directory to store session files.

## SessionManager.inMemory
### Description
Creates a session with no file persistence.
### Method
`SessionManager.inMemory(cwd?)
### Parameters
#### Path Parameters
- **cwd** (string) - Optional - The current working directory.

## SessionManager.forkFrom
### Description
Forks a session from another project.
### Method
`SessionManager.forkFrom(sourcePath, targetCwd, sessionDir?)
### Parameters
#### Path Parameters
- **sourcePath** (string) - Required - The path to the source session.
- **targetCwd** (string) - Required - The target current working directory.
- **sessionDir** (string) - Optional - The directory to store session files.
```

--------------------------------

### Run Print Mode with Pi SDK

Source: https://pi.dev/docs/latest/sdk

This mode is for single-shot interactions: send prompts, get a result, and exit. It's useful for scripting and automated tasks.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  runPrintMode,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};
const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

await runPrintMode(runtime, {
  mode: "text",
  initialMessage: "Hello",
  initialImages: [],
  messages: ["Follow up"],
});


```

--------------------------------

### Get all conversation messages

Source: https://pi.dev/docs/latest/rpc

Fetches all messages exchanged within the current conversation. Messages are returned as `AgentMessage` objects.

```json
{"type": "get_messages"}
```

--------------------------------

### Create and Manage Agent Sessions

Source: https://pi.dev/docs/latest/sdk

Demonstrates various ways to create and manage agent sessions, including in-memory, persistent, continuing recent, and opening specific sessions. Also shows how to list sessions and use the session replacement API.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSession,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

// In-memory (no persistence)
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
});

// New persistent session
const { session: persisted } = await createAgentSession({
  sessionManager: SessionManager.create(process.cwd()),
});

// Continue most recent
const { session: continued, modelFallbackMessage } = await createAgentSession({
  sessionManager: SessionManager.continueRecent(process.cwd()),
});
if (modelFallbackMessage) {
  console.log("Note:", modelFallbackMessage);
}

// Open specific file
const { session: opened } = await createAgentSession({
  sessionManager: SessionManager.open("/path/to/session.jsonl"),
});

// List sessions
const currentProjectSessions = await SessionManager.list(process.cwd());
const allSessions = await SessionManager.listAll(process.cwd());

// Session replacement API for /new, /resume, /fork, and import flows.
const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({
      services,
      sessionManager,
      sessionStartEvent,
    })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

// Replace the active session with a fresh one
await runtime.newSession();

// Replace the active session with another saved session
await runtime.switchSession("/path/to/session.jsonl");

// Replace the active session with a fork from a specific user entry
await runtime.fork("entry-id");

// Clone the active path through a specific entry
await runtime.fork("entry-id", { position: "at" });

```

--------------------------------

### Custom Streaming API Implementation Pattern

Source: https://pi.dev/docs/latest/custom-provider

Provides a template for implementing a custom streaming API for AI providers. It outlines the necessary imports, the structure of the stream function, and how to handle start, content, and done events.

```typescript
import {
  type AssistantMessage,
  type AssistantMessageEventStream,
  type Context,
  type Model,
  type SimpleStreamOptions,
  calculateCost,
  createAssistantMessageEventStream,
} from "@mariozechner/pi-ai";

function streamMyProvider(
  model: Model<any>,
  context: Context,
  options?: SimpleStreamOptions
): AssistantMessageEventStream {
  const stream = createAssistantMessageEventStream();

  (async () => {
    // Initialize output message
    const output: AssistantMessage = {
      role: "assistant",
      content: [],
      api: model.api,
      provider: model.provider,
      model: model.id,
      usage: {
        input: 0,
        output: 0,
        cacheRead: 0,
        cacheWrite: 0,
        totalTokens: 0,
        cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, total: 0 },
      },
      stopReason: "stop",
      timestamp: Date.now(),
    };

    try {
      // Push start event
      stream.push({ type: "start", partial: output });

      // Make API request and process response...
      // Push content events as they arrive...

      // Push done event
      stream.push({
        type: "done",
        reason: output.stopReason as "stop" | "length" | "toolUse",
        message: output
      });
      stream.end();
    } catch (error) {
      output.stopReason = options?.signal?.aborted ? "aborted" : "error";
      output.errorMessage = error instanceof Error ? error.message : String(error);
      stream.push({ type: "error", reason: output.stopReason, error: output });
      stream.end();
    }
  })();

  return stream;
}

```

--------------------------------

### Prompt Template with Argument Hint

Source: https://pi.dev/docs/latest/prompt-templates

Includes an 'argument-hint' in the frontmatter to guide users on expected arguments in the autocomplete dropdown. Use angle brackets for required arguments and square brackets for optional ones.

```markdown
---
description: Review PRs from URLs with structured issue and code analysis
argument-hint: "<PR-URL>"
---


```

--------------------------------

### Register Custom Command with Selector

Source: https://pi.dev/docs/latest/tui

Register a command that utilizes the `MySelector` component to allow users to pick an item. This example shows how to integrate a custom component with the pi-tui context.

```typescript
pi.registerCommand("pick", {
  description: "Pick an item",
  handler: async (args, ctx) => {
    const items = ["Option A", "Option B", "Option C"];
    const selector = new MySelector(items);
    
    let handle: { close: () => void; requestRender: () => void };
    
    await new Promise<void>((resolve) => {
      selector.onSelect = (item) => {
        ctx.ui.notify(`Selected: ${item}`, "info");
        handle.close();
        resolve();
      };
      selector.onCancel = () => {
        handle.close();
        resolve();
      };
      handle = ctx.ui.custom(selector);
    });
  }
});
```

--------------------------------

### Filter JSON Events with jq

Source: https://pi.dev/docs/latest/json

Example of piping the JSON event stream output to jq to filter for specific event types, such as 'message_end'.

```bash
pi --mode json "List files" 2>/dev/null | jq -c 'select(.type == "message_end")'
```

--------------------------------

### Get Current Session Name

Source: https://pi.dev/docs/latest/extensions

Retrieve the current session's display name if it has been set. Logs the name if it exists.

```javascript
const name = pi.getSessionName();
if (name) {
  console.log(`Session: ${name}`);
}

```

--------------------------------

### Get Available Commands

Source: https://pi.dev/docs/latest/extensions

Retrieves all available slash commands, including those from extensions, prompt templates, and skills. Filters can be applied to select commands based on their source or scope.

```javascript
const commands = pi.getCommands();
const bySource = commands.filter((command) => command.source === "extension");
const userScoped = commands.filter((command) => command.sourceInfo.scope === "user");
```

--------------------------------

### Configure Vercel AI Gateway OpenAI Compatibility

Source: https://pi.dev/docs/latest/models

Set up OpenAI compatibility for Vercel AI Gateway, specifying routing preferences for model selection. This example uses a specific model with custom routing.

```json
{
  "providers": {
    "vercel-ai-gateway": {
      "baseUrl": "https://ai-gateway.vercel.sh/v1",
      "apiKey": "AI_GATEWAY_API_KEY",
      "api": "openai-completions",
      "models": [
        {
          "id": "moonshotai/kimi-k2.5",
          "name": "Kimi K2.5 (Fireworks via Vercel)",
          "reasoning": true,
          "input": ["text", "image"],
          "cost": { "input": 0.6, "output": 3, "cacheRead": 0, "cacheWrite": 0 },
          "contextWindow": 262144,
          "maxTokens": 262144,
          "compat": {
            "vercelGatewayRouting": {
              "only": ["fireworks", "novita"],
              "order": ["fireworks", "novita"]
            }
          }
        }
      ]
    }
  }
}
```

--------------------------------

### Compact Conversation Context

Source: https://pi.dev/docs/latest/rpc

Manually compact conversation context to reduce token usage. Can include custom instructions to guide the compaction process.

```json
{"type": "compact"}
```

```json
{"type": "compact", "customInstructions": "Focus on code changes"}
```

--------------------------------

### Creating Agent Sessions

Source: https://pi.dev/docs/latest/sdk

Demonstrates various ways to create agent sessions, from in-memory sessions to persistent ones and resuming recent sessions.

```APIDOC
## Creating Agent Sessions

### Description
Examples of creating agent sessions, including in-memory, persistent, and resuming recent sessions.

### Usage
```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSession,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

// In-memory (no persistence)
const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
});

// New persistent session
const { session: persisted } = await createAgentSession({
  sessionManager: SessionManager.create(process.cwd()),
});

// Continue most recent
const { session: continued, modelFallbackMessage } = await createAgentSession({
  sessionManager: SessionManager.continueRecent(process.cwd()),
});
if (modelFallbackMessage) {
  console.log("Note:", modelFallbackMessage);
}

// Open specific file
const { session: opened } = await createAgentSession({
  sessionManager: SessionManager.open("/path/to/session.jsonl"),
});
```
```

--------------------------------

### SessionManager Methods

Source: https://pi.dev/docs/latest/tree

Provides an overview of the `SessionManager` methods for interacting with the session tree, including getting the current leaf, resetting it, retrieving the full tree, and branching.

```typescript
  * `getLeafUuid(): string | null` - Current leaf (null if empty)
  * `resetLeaf(): void` - Set leaf to null (for root user message navigation)
  * `getTree(): SessionTreeNode[]` - Full tree with children sorted by timestamp
  * `branch(id)` - Change leaf pointer
  * `branchWithSummary(id, summary)` - Change leaf and create summary entry
```

--------------------------------

### Instance Methods - Tree Navigation

Source: https://pi.dev/docs/latest/session

Methods for navigating and querying the session's entry tree.

```APIDOC
## getLeafId
### Description
Gets the ID of the current leaf entry.
### Method
`getLeafId()
### Returns
(string) - The ID of the current leaf entry.
```

```APIDOC
## getLeafEntry
### Description
Gets the current leaf entry.
### Method
`getLeafEntry()
### Returns
(object) - The current leaf entry.
```

```APIDOC
## getEntry
### Description
Gets an entry by its ID.
### Method
`getEntry(id)
### Parameters
#### Path Parameters
- **id** (string) - Required - The ID of the entry to retrieve.
### Returns
(object) - The entry object.
```

```APIDOC
## getBranch
### Description
Walks from a given entry ID to the root of the session tree.
### Method
`getBranch(fromId?)
### Parameters
#### Path Parameters
- **fromId** (string) - Optional - The ID of the entry to start from. Defaults to the current leaf.
### Returns
(array) - An array of entries representing the branch from the specified entry to the root.
```

```APIDOC
## getTree
### Description
Gets the full structure of the session tree.
### Method
`getTree()
### Returns
(object) - The root of the session tree structure.
```

```APIDOC
## getChildren
### Description
Gets the direct children of a given parent entry.
### Method
`getChildren(parentId)
### Parameters
#### Path Parameters
- **parentId** (string) - Required - The ID of the parent entry.
### Returns
(array) - An array of the direct children entries.
```

```APIDOC
## getLabel
### Description
Gets the label associated with a specific entry.
### Method
`getLabel(id)
### Parameters
#### Path Parameters
- **id** (string) - Required - The ID of the entry.
### Returns
(string | undefined) - The label of the entry, or undefined if no label is set.
```

```APIDOC
## branch
### Description
Moves the current leaf to an earlier entry in the session history.
### Method
`branch(entryId)
### Parameters
#### Path Parameters
- **entryId** (string) - Required - The ID of the entry to branch to.
```

```APIDOC
## resetLeaf
### Description
Resets the current leaf to null, effectively before any entries have been added.
### Method
`resetLeaf()
```

```APIDOC
## branchWithSummary
### Description
Branches to a specified entry and includes a context summary.
### Method
`branchWithSummary(entryId, summary, details?, fromHook?)
### Parameters
#### Path Parameters
- **entryId** (string) - Required - The ID of the entry to branch to.
- **summary** (string) - Required - The summary to include with the branch.
- **details** (any) - Optional - Additional details for the branch.
- **fromHook** (boolean) - Optional - Indicates if the branch was triggered by a hook.
```

--------------------------------

### Restart tmux Server

Source: https://pi.dev/docs/latest/tmux

After modifying your `~/.tmux.conf`, you need to restart the tmux server for the changes to take effect. This command kills the server and then starts a new session.

```bash
tmux kill-server
tmux
```

--------------------------------

### Handle Message Lifecycle Events

Source: https://pi.dev/docs/latest/extensions

Listen for message lifecycle events like start, update (streaming), and end. Access message details and assistant streaming events.

```javascript
pi.on("message_start", async (event, ctx) => {
  // event.message
});
```

```javascript
pi.on("message_update", async (event, ctx) => {
  // event.message
  // event.assistantMessageEvent (token-by-token stream event)
});
```

```javascript
pi.on("message_end", async (event, ctx) => {
  // event.message
});
```

--------------------------------

### Configure npm Command

Source: https://pi.dev/docs/latest/settings

Specify a custom command for npm package operations. This is used for operations like global installs and dependency management within git packages.

```json
{
  "npmCommand": ["mise", "exec", "node@20", "--", "npm"]
}
```

--------------------------------

### Create Agent Session with Default Settings

Source: https://pi.dev/docs/latest/sdk

Loads settings from global and project files by default. Use this for standard configurations.

```typescript
import { createAgentSession, SettingsManager } from "@mariozechner/pi-coding-agent";

// Default: loads from files (global + project merged)
const { session } = await createAgentSession({
  settingsManager: SettingsManager.create(),
});
```

--------------------------------

### Get last assistant text

Source: https://pi.dev/docs/latest/rpc

Fetches the text content of the most recent assistant message. Returns `{"text": null}` if no assistant messages exist.

```json
{"type": "get_last_assistant_text"}
```

```json
{
  "type": "response",
  "command": "get_last_assistant_text",
  "success": true,
  "data": {"text": "The assistant's response..."}
}
```

--------------------------------

### Get current session state

Source: https://pi.dev/docs/latest/rpc

Retrieves the current state of the session, including model information, thinking level, streaming status, and message counts.

```json
{"type": "get_state"}
```

--------------------------------

### Get System Prompt in Event Handler

Source: https://pi.dev/docs/latest/extensions

Retrieves the current system prompt string during the `before_agent_start` event. This reflects chained prompt changes for the current turn but not later mutations or rewrites.

```javascript
pi.on("before_agent_start", (event, ctx) => {
  const prompt = ctx.getSystemPrompt();
  console.log(`System prompt length: ${prompt.length}`);
});

```

--------------------------------

### Create Custom Theme Directory

Source: https://pi.dev/docs/latest/themes

Create a directory for custom themes in the user's Pi configuration folder. This is where custom theme JSON files should be placed.

```bash
mkdir -p ~/.pi/agent/themes

```

--------------------------------

### Create Bash Tool with Spawn Hook

Source: https://pi.dev/docs/latest/extensions

Illustrates customizing the `bash` tool's execution environment. The `spawnHook` allows modification of the command, current working directory, and environment variables before the shell process starts.

```typescript
import { createBashTool } from "@mariozechner/pi-coding-agent";

const bashTool = createBashTool(cwd, {
  spawnHook: ({ command, cwd, env }) => ({
    command: `source ~/.profile\n${command}`,
    cwd: `/mnt/sandbox${cwd}`,
    env: { ...env, CI: "1" },
  }),
});
```

--------------------------------

### Auto Retry Start Event

Source: https://pi.dev/docs/latest/rpc

Emitted when automatic retry is initiated due to a transient error. It specifies the current attempt number, maximum attempts, delay, and the error message.

```json
{
  "type": "auto_retry_start",
  "attempt": 1,
  "maxAttempts": 3,
  "delayMs": 2000,
  "errorMessage": "529 {\"type\":\"error\",\"error\":{\"type\":\"overloaded_error\",\"message\":\"Overloaded\"}}"
}
```

--------------------------------

### Handle Tool Execution Lifecycle Events

Source: https://pi.dev/docs/latest/extensions

Monitor the lifecycle of tool executions, including start, updates, and end. Useful for tracking tool calls, arguments, and results, especially in parallel mode.

```javascript
pi.on("tool_execution_start", async (event, ctx) => {
  // event.toolCallId, event.toolName, event.args
});
```

```javascript
pi.on("tool_execution_update", async (event, ctx) => {
  // event.toolCallId, event.toolName, event.args, event.partialResult
});
```

```javascript
pi.on("tool_execution_end", async (event, ctx) => {
  // event.toolCallId, event.toolName, event.result, event.isError
});
```

--------------------------------

### Override Built-in Read Tool

Source: https://pi.dev/docs/latest/extensions

Use the `-e` flag to specify a TypeScript file that overrides built-in tools. This example shows how to replace the default `read` tool.

```bash
# Extension's read tool replaces built-in read
pi -e ./tool-override.ts
```

--------------------------------

### Configure Anthropic Messages Compatibility

Source: https://pi.dev/docs/latest/models

Adjust compatibility settings for providers using the 'anthropic-messages' API. This example disables eager tool input streaming and enables long cache retention.

```json
{
  "providers": {
    "anthropic-proxy": {
      "baseUrl": "https://proxy.example.com",
      "api": "anthropic-messages",
      "apiKey": "ANTHROPIC_PROXY_KEY",
      "compat": {
        "supportsEagerToolInputStreaming": false,
        "supportsLongCacheRetention": true
      },
      "models": [
        {
          "id": "claude-opus-4-7",
          "reasoning": true,
          "input": ["text", "image"]
        }
      ]
    }
  }
}

```

--------------------------------

### agent_start

Source: https://pi.dev/docs/latest/rpc

Emitted when the agent begins processing a prompt.

```APIDOC
## agent_start

### Description
Emitted when the agent begins processing a prompt.

### Event Data
```json
{
  "type": "agent_start"
}
```
```

--------------------------------

### Basic Prompt Template Format

Source: https://pi.dev/docs/latest/prompt-templates

Defines a prompt template with a description. The filename becomes the command name. The 'description' field is optional and defaults to the first non-empty line if missing.

```markdown
---
description: Review staged git changes
---
Review the staged changes (`git diff --cached`). Focus on:
- Bugs and logic errors
- Security issues
- Error handling gaps

```

--------------------------------

### Configure Per-Model Overrides for OpenRouter

Source: https://pi.dev/docs/latest/models

Customize specific built-in models within a provider using `modelOverrides`. This example shows how to change the name and compatibility settings for a specific Anthropic model routed through OpenRouter.

```json
{
  "providers": {
    "openrouter": {
      "modelOverrides": {
        "anthropic/claude-sonnet-4": {
          "name": "Claude Sonnet 4 (Bedrock Route)",
          "compat": {
            "openRouterRouting": {
              "only": ["amazon-bedrock"]
            }
          }
        }
      }
    }
  }
}

```

--------------------------------

### Container Component with Focus Propagation

Source: https://pi.dev/docs/latest/tui

Example of a container component implementing Focusable to propagate focus state to its child input, ensuring correct IME cursor positioning. This is crucial for dialogs or selectors containing inputs.

```typescript
import { Container, type Focusable, Input } from "@mariozechner/pi-tui";

class SearchDialog extends Container implements Focusable {
  private searchInput: Input;

  // Focusable implementation - propagate to child input for IME cursor positioning
  private _focused = false;
  get focused(): boolean {
    return this._focused;
  }
  set focused(value: boolean) {
    this._focused = value;
    this.searchInput.focused = value;
  }

  constructor() {
    super();
    this.searchInput = new Input();
    this.addChild(this.searchInput);
  }
}

```

--------------------------------

### Custom Keybinding Configuration

Source: https://pi.dev/docs/latest/keybindings

Configure custom keybindings by creating a `keybindings.json` file. Each action can have a single key or an array of keys. User configuration overrides defaults.

```json
{
  "tui.editor.cursorUp": ["up", "ctrl+p"],
  "tui.editor.cursorDown": ["down", "ctrl+n"],
  "tui.editor.deleteWordBackward": ["ctrl+w", "alt+backspace"]
}
```

--------------------------------

### Using Components in Extensions

Source: https://pi.dev/docs/latest/tui

Demonstrates how to use custom TUI components within Pi extensions.

```APIDOC
## Using Components

**In extensions** via `ctx.ui.custom()`:

```typescript
pi.on("session_start", async (_event, ctx) => {
  const handle = ctx.ui.custom(myComponent);
  // handle.requestRender() - trigger re-render
  // handle.close() - restore normal UI
});
```
```

--------------------------------

### Get Markdown Theme for Markdown Rendering

Source: https://pi.dev/docs/latest/tui

Import and use `getMarkdownTheme()` to obtain a theme object specifically for rendering Markdown content within the TUI. This theme can then be passed to the `Markdown` component.

```typescript
import { getMarkdownTheme } from "@mariozechner/pi-coding-agent";
import { Markdown } from "@mariozechner/pi-tui";

renderResult(result, options, theme, context) {
  const mdTheme = getMarkdownTheme();
  return new Markdown(result.details.markdown, 0, 0, mdTheme);
}
```

--------------------------------

### Configure Extension Paths in settings.json

Source: https://pi.dev/docs/latest/extensions

This JSON configuration shows how to specify additional paths for extensions, including npm packages and git repositories, as well as local file paths.

```json
{
  "packages": [
    "npm:@foo/bar@1.0.0",
    "git:github.com/user/repo@v1"
  ],
  "extensions": [
    "/path/to/local/extension.ts",
    "/path/to/local/extension/dir"
  ]
}

```

--------------------------------

### Queue a Prompt During Streaming (Steer)

Source: https://pi.dev/docs/latest/rpc

When the agent is already streaming, use 'steer' to queue a new message. It will be delivered after the current turn's tool calls.

```json
{"type": "prompt", "message": "New instruction", "streamingBehavior": "steer"}

```

--------------------------------

### Create Agent Session with Custom Settings Directories

Source: https://pi.dev/docs/latest/sdk

Specifies custom directories for loading settings. Useful when project structure deviates from the default.

```typescript
import { createAgentSession, SettingsManager } from "@mariozechner/pi-coding-agent";

// Custom directories
const { session } = await createAgentSession({
  settingsManager: SettingsManager.create("/custom/cwd", "/custom/agent"),
});
```

--------------------------------

### Type Custom Tool Input with pi

Source: https://pi.dev/docs/latest/extensions

Define and use custom input types for your tools. Export the input type from your extension and use `isToolCallEventType` with explicit type parameters to get typed access to `event.input`.

```typescript
// my-extension.ts
export type MyToolInput = Static<typeof myToolSchema>;

```

```typescript
import { isToolCallEventType } from "@mariozechner/pi-coding-agent";
import type { MyToolInput } from "my-extension";

pi.on("tool_call", (event) => {
  if (isToolCallEventType<"my_tool", MyToolInput>("my_tool", event)) {
    event.input.action;  // typed
  }
});

```

--------------------------------

### Listen for Resource Discovery Events

Source: https://pi.dev/docs/latest/extensions

Register a listener for the 'resources_discover' event to provide custom paths for skills, prompts, and themes. This event fires after 'session_start' during startup or reload.

```javascript
pi.on("resources_discover", async (event, _ctx) => {
  // event.cwd - current working directory
  // event.reason - "startup" | "reload"
  return {
    skillPaths: ["/path/to/skills"],
    promptPaths: ["/path/to/prompts"],
    themePaths: ["/path/to/themes"],
  };
});
```

--------------------------------

### Get and Set Thinking Level

Source: https://pi.dev/docs/latest/extensions

Retrieves the current thinking level or sets a new one. The level is automatically clamped to the model's capabilities; non-reasoning models will always use 'off'.

```javascript
const current = pi.getThinkingLevel();  // "off" | "minimal" | "low" | "medium" | "high" | "xhigh"
pi.setThinkingLevel("high");
```

--------------------------------

### Instance Methods - Context & Info

Source: https://pi.dev/docs/latest/session

Methods for retrieving context and information about the session.

```APIDOC
## buildSessionContext
### Description
Builds the session context for the LLM by walking from the current leaf to the root. It collects entries, extracts settings, and formats messages, including summaries for `CompactionEntry`.
### Method
`buildSessionContext()
### Returns
(object) - An object containing messages, thinkingLevel, and model settings for the LLM.
```

```APIDOC
## getEntries
### Description
Retrieves all entries in the session, excluding the header.
### Method
`getEntries()
### Returns
(array) - An array of all session entries.
```

```APIDOC
## getHeader
### Description
Retrieves the session header metadata.
### Method
`getHeader()
### Returns
(object) - The session header metadata.
```

```APIDOC
## getSessionName
### Description
Gets the display name of the session from the latest session info entry.
### Method
`getSessionName()
### Returns
(string | undefined) - The session display name, or undefined if not set.
```

```APIDOC
## getCwd
### Description
Gets the current working directory of the session.
### Method
`getCwd()
### Returns
(string) - The current working directory.
```

```APIDOC
## getSessionDir
### Description
Gets the directory where the session is stored.
### Method
`getSessionDir()
### Returns
(string | undefined) - The session storage directory, or undefined if not persisted.
```

```APIDOC
## getSessionId
### Description
Gets the unique identifier (UUID) of the session.
### Method
`getSessionId()
### Returns
(string) - The session UUID.
```

```APIDOC
## getSessionFile
### Description
Gets the file path of the session.
### Method
`getSessionFile()
### Returns
(string | undefined) - The session file path, or undefined if the session is in-memory.
```

```APIDOC
## isPersisted
### Description
Checks if the session is saved to disk.
### Method
`isPersisted()
### Returns
(boolean) - True if the session is persisted, false otherwise.
```

--------------------------------

### ctx.getSystemPrompt()

Source: https://pi.dev/docs/latest/extensions

Retrieves Pi's current system prompt string. This reflects chained system prompt changes made so far for the current turn, but not later mutations or rewrites.

```APIDOC
## ctx.getSystemPrompt()

### Description
Returns Pi's current system prompt string. This reflects chained system-prompt changes made so far for the current turn. It does not include later `context` message mutations or `before_provider_request` payload rewrites. If later-loaded extensions run after yours, they can still change what is ultimately sent.

### Method
ctx.getSystemPrompt()

### Response
- **string** - The current system prompt.

### Request Example
```javascript
pi.on("before_agent_start", (event, ctx) => {
  const prompt = ctx.getSystemPrompt();
  console.log(`System prompt length: ${prompt.length}`);
});
```
```

--------------------------------

### Configure Package Loading (Object Form)

Source: https://pi.dev/docs/latest/settings

Filter which specific resources (skills, extensions) to load from a package.

```json
{
  "packages": [
    {
      "source": "pi-skills",
      "skills": ["brave-search", "transcribe"],
      "extensions": []
    }
  ]
}
```

--------------------------------

### Configure Built-in Tool Sets

Source: https://pi.dev/docs/latest/sdk

Demonstrates how to use pre-defined sets of tools like `codingTools` or `readOnlyTools` when creating an agent session. This simplifies tool configuration for common use cases.

```typescript
import {
  codingTools,   // read, bash, edit, write (default)
  readOnlyTools, // read, grep, find, ls
  readTool, bashTool, editTool, writeTool,
  grepTool, findTool, lsTool,
} from "@mariozechner/pi-coding-agent";

// Use built-in tool set
const { session } = await createAgentSession({
  tools: readOnlyTools,
});

// Pick specific tools
const { session } = await createAgentSession({
  tools: [readTool, bashTool, grepTool],
});
```

--------------------------------

### Queue a Prompt During Streaming (Follow Up)

Source: https://pi.dev/docs/latest/rpc

Use 'followUp' to queue a message that will only be delivered after the agent has completely finished its current task.

```json
{"type": "prompt", "message": "New instruction", "streamingBehavior": "followUp"}

```

--------------------------------

### before_agent_start

Source: https://pi.dev/docs/latest/extensions

Fired after user submits a prompt and before the agent loop begins. Allows modification of the system prompt and injection of messages.

```APIDOC
## before_agent_start

### Description
Fired after user submits a prompt and before the agent loop begins. Allows modification of the system prompt and injection of messages.

### Event Parameters
- **event**: Object
  - **prompt** (string) - The user's prompt text.
  - **images** (Array) - Attached images, if any.
  - **systemPrompt** (string) - The current chained system prompt for this handler.
  - **systemPromptOptions**: Object - Structured options used to build the system prompt.
    - **customPrompt** (string) - Any custom system prompt (from --system-prompt, SYSTEM.md, or custom templates).
    - **selectedTools** (Array) - Tools currently active in the prompt.
    - **toolSnippets** (Array) - One-line descriptions for each tool.
    - **promptGuidelines** (Array) - Custom guideline bullets.
    - **appendSystemPrompt** (string) - Text from --append-system-prompt flags.
    - **cwd** (string) - Working directory.
    - **contextFiles** (Array) - AGENTS.md files and other loaded context files.
    - **skills** (Array) - Loaded skills.

### Context Parameters
- **ctx**: Object

### Return Value
- **{ message: { customType: string, content: string, display: boolean } }**: To inject a persistent message.
- **{ systemPrompt: string }**: To replace the system prompt for this turn.

### Example
```javascript
pi.on("before_agent_start", async (event, ctx) => {
  // event.prompt - user's prompt text
  // event.images - attached images (if any)
  // event.systemPrompt - current chained system prompt for this handler
  //   (includes changes from earlier before_agent_start handlers)
  // event.systemPromptOptions - structured options used to build the system prompt
  //   .customPrompt - any custom system prompt (from --system-prompt, SYSTEM.md, or custom templates)
  //   .selectedTools - tools currently active in the prompt
  //   .toolSnippets - one-line descriptions for each tool
  //   .promptGuidelines - custom guideline bullets
  //   .appendSystemPrompt - text from --append-system-prompt flags
  //   .cwd - working directory
  //   .contextFiles - AGENTS.md files and other loaded context files
  //   .skills - loaded skills

  return {
    // Inject a persistent message (stored in session, sent to LLM)
    message: {
      customType: "my-extension",
      content: "Additional context for the LLM",
      display: true,
    },
    // Replace the system prompt for this turn (chained across extensions)
    systemPrompt: event.systemPrompt + "\n\nExtra instructions for this turn...",
  };
});
```
```

--------------------------------

### Run Pi from Source

Source: https://pi.dev/docs/latest/development

Execute the Pi test script from any directory. Pi respects the caller's current working directory.

```bash
/path/to/pi-mono/pi-test.sh

```

--------------------------------

### Enable Skill Commands in Settings

Source: https://pi.dev/docs/latest/skills

Toggle the ability to use skills directly via slash commands in interactive mode or by configuring the `settings.json` file.

```json
{
  "enableSkillCommands": true
}
```

--------------------------------

### Package Gallery Metadata

Source: https://pi.dev/docs/latest/packages

Add 'video' or 'image' fields to package metadata to display previews in the gallery. MP4 is supported for video, and PNG, JPEG, GIF, or WebP for images. Video takes precedence if both are provided.

```json
{
  "name": "my-package",
  "keywords": ["pi-package"],
  "pi": {
    "extensions": ["./extensions"],
    "video": "https://example.com/demo.mp4",
    "image": "https://example.com/screenshot.png"
  }
}

```

--------------------------------

### Register Basic Command

Source: https://pi.dev/docs/latest/extensions

Register a new command with a description and a handler function. If multiple extensions register the same command, they receive numeric suffixes.

```javascript
pi.registerCommand("stats", {
  description: "Show session statistics",
  handler: async (args, ctx) => {
    const count = ctx.sessionManager.getEntries().length;
    ctx.ui.notify(`${count} entries`, "info");
  }
});

```

--------------------------------

### List all configured models

Source: https://pi.dev/docs/latest/rpc

Retrieves a list of all models that are configured for use. The response contains an array of full `Model` objects.

```json
{"type": "get_available_models"}
```

--------------------------------

### Using Components in Custom Tools

Source: https://pi.dev/docs/latest/tui

Demonstrates how to use custom TUI components within Pi custom tools.

```APIDOC
**In custom tools** via `pi.ui.custom()`:

```typescript
async execute(toolCallId, params, onUpdate, ctx, signal) {
  const handle = pi.ui.custom(myComponent);
  // ...
  handle.close();
}
```
```

--------------------------------

### session.steer() and session.followUp()

Source: https://pi.dev/docs/latest/sdk

Explicitly queue messages during streaming for specific delivery behaviors.

```APIDOC
## session.steer() and session.followUp()

### Description
These methods allow explicit queueing of messages during streaming for specific delivery behaviors: `steer` for immediate interruption/replacement, and `followUp` for delivery after the current turn.

### Usage
- **Queue a steering message:**
  ```javascript
  // For delivery after the current assistant turn finishes its tool calls
  await session.steer("New instruction");
  ```
- **Queue a follow-up message:**
  ```javascript
  // Wait for agent to finish (delivered only when agent stops)
  await session.followUp("After you're done, also do this");
  ```

### Behavior
- Both `steer()` and `followUp()` expand file-based prompt templates.
- They error on extension commands, as extension commands cannot be queued.
```

--------------------------------

### ctx.navigateTree(targetId, options?)

Source: https://pi.dev/docs/latest/extensions

Navigates to a different point in the session tree, with options to summarize the abandoned branch and customize instructions.

```APIDOC
## ctx.navigateTree(targetId, options?)

### Description
Navigate to a different point in the session tree. This method is only available in commands.

### Method
await ctx.navigateTree(targetId, options)

### Parameters
#### Path Parameters
- **targetId** (string) - Required - The ID of the target entry to navigate to.

#### Options
- **summarize** (boolean) - Optional - Whether to generate a summary of the abandoned branch. Defaults to `false`.
- **customInstructions** (string) - Optional - Custom instructions for the summarizer if `summarize` is true.
- **replaceInstructions** (boolean) - Optional - If true, `customInstructions` replaces the default prompt instead of being appended. Defaults to `false`.
- **label** (string) - Optional - Label to attach to the branch summary entry (or target entry if not summarizing).

### Request Example
```javascript
const result = await ctx.navigateTree("entry-id-456", {
  summarize: true,
  customInstructions: "Focus on error handling changes",
  replaceInstructions: false, // true = replace default prompt entirely
  label: "review-checkpoint",
});
```
```

--------------------------------

### Basic Python Client for RPC

Source: https://pi.dev/docs/latest/rpc

Demonstrates how to interact with the 'pi' CLI in RPC mode using Python's subprocess. Handles sending commands and reading asynchronous events.

```python
import subprocess
import json

proc = subprocess.Popen(
    ["pi", "--mode", "rpc", "--no-session"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

def send(cmd):
    proc.stdin.write(json.dumps(cmd) + "\n")
    proc.stdin.flush()

def read_events():
    for line in proc.stdout:
        yield json.loads(line)

# Send prompt
send({"type": "prompt", "message": "Hello!"})

# Process events
for event in read_events():
    if event.get("type") == "message_update":
        delta = event.get("assistantMessageEvent", {})
        if delta.get("type") == "text_delta":
            print(delta["delta"], end="", flush=True)
    
    if event.get("type") == "agent_end":
        print()
        break

```

--------------------------------

### Listing Sessions

Source: https://pi.dev/docs/latest/sdk

Shows how to list available sessions for the current project or all sessions.

```APIDOC
## Listing Sessions

### Description
Methods to list sessions associated with the current project or all available sessions.

### Usage
```typescript
// List sessions
const currentProjectSessions = await SessionManager.list(process.cwd());
const allSessions = await SessionManager.listAll(process.cwd());
```
```

--------------------------------

### Pi Project Structure Overview

Source: https://pi.dev/docs/latest/development

Overview of the Pi project's monorepo structure, detailing the purpose of key packages.

```text
packages/
  ai/           # LLM provider abstraction
  agent/        # Agent loop and message types  
  tui/          # Terminal UI components
  coding-agent/ # CLI and interactive mode


```

--------------------------------

### Configure thinkingBudgets in Pi Settings

Source: https://pi.dev/docs/latest/settings

Set custom token budgets for different thinking levels. This allows fine-tuning resource allocation for agent thought processes.

```json
{
  "thinkingBudgets": {
    "minimal": 1024,
    "low": 4096,
    "medium": 10240,
    "high": 32768
  }
}
```

--------------------------------

### Configure WezTerm for Pi

Source: https://pi.dev/docs/latest/terminal-setup

Create or modify '~/.wezterm.lua' to enable the Kitty keyboard protocol for WezTerm. This is essential for Pi's modifier key detection.

```lua
local wezterm = require 'wezterm'
local config = wezterm.config_builder()
config.enable_kitty_keyboard = true
return config
```

--------------------------------

### Configure Auth File for API Keys

Source: https://pi.dev/docs/latest/providers

Store API keys in the `~/.pi/agent/auth.json` file for various providers. This file has `0600` permissions and its credentials take priority over environment variables.

```json
{
  "anthropic": { "type": "api_key", "key": "sk-ant-..." },
  "openai": { "type": "api_key", "key": "sk-..." },
  "deepseek": { "type": "api_key", "key": "sk-..." },
  "google": { "type": "api_key", "key": "..." },
  "opencode": { "type": "api_key", "key": "..." },
  "opencode-go": { "type": "api_key", "key": "..." }
}

```

--------------------------------

### Handling Tool Calls

Source: https://pi.dev/docs/latest/custom-provider

Illustrates the process of managing tool calls, including accumulating JSON arguments and signaling completion. Use `contentIndex` to track tool call blocks.

```javascript
// Start tool call
output.content.push({
  type: "toolCall",
  id: toolCallId,
  name: toolName,
  arguments: {}
});
stream.push({ type: "toolcall_start", contentIndex: output.content.length - 1, partial: output });

// Accumulate JSON
let partialJson = "";
partialJson += jsonDelta;
try {
  block.arguments = JSON.parse(partialJson);
} catch {}
stream.push({ type: "toolcall_delta", contentIndex, delta: jsonDelta, partial: output });

// Complete
stream.push({
  type: "toolcall_end",
  contentIndex,
  toolCall: { type: "toolCall", id, name, arguments: block.arguments },
  partial: output
});

```

--------------------------------

### Defining and Loading Custom Slash Commands (Prompt Templates)

Source: https://pi.dev/docs/latest/sdk

Shows how to define a custom prompt template for a slash command and override the default prompts using `DefaultResourceLoader`. The `promptsOverride` function enables adding new commands like 'deploy'.

```typescript
import {
  createAgentSession,
  DefaultResourceLoader,
  type PromptTemplate,
} from "@mariozechner/pi-coding-agent";

const customCommand: PromptTemplate = {
  name: "deploy",
  description: "Deploy the application",
  source: "(custom)",
  content: "# Deploy\n\n1. Build\n2. Test\n3. Deploy",
};

const loader = new DefaultResourceLoader({
  promptsOverride: (current) => ({
    prompts: [...current.prompts, customCommand],
    diagnostics: current.diagnostics,
  }),
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });

```

--------------------------------

### Configure AuthStorage and ModelRegistry

Source: https://pi.dev/docs/latest/sdk

Demonstrates creating AuthStorage and ModelRegistry instances with default and custom locations. Use this to manage API keys and model configurations.

```typescript
import { AuthStorage, ModelRegistry } from "@mariozechner/pi-coding-agent";

// Default: uses ~/.pi/agent/auth.json and ~/.pi/agent/models.json
const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage,
  modelRegistry,
});

// Runtime API key override (not persisted to disk)
authStorage.setRuntimeApiKey("anthropic", "sk-my-temp-key");

// Custom auth storage location
const customAuth = AuthStorage.create("/my/app/auth.json");
const customRegistry = ModelRegistry.create(customAuth, "/my/app/models.json");

const { session } = await createAgentSession({
  sessionManager: SessionManager.inMemory(),
  authStorage: customAuth,
  modelRegistry: customRegistry,
});

// No custom models.json (built-in models only)
const simpleRegistry = ModelRegistry.inMemory(authStorage);
```

--------------------------------

### session.prompt()

Source: https://pi.dev/docs/latest/sdk

Sends a prompt to the agent session, handling templates, extension commands, and message sending.

```APIDOC
## session.prompt()

### Description
Handles prompt templates, extension commands, and message sending to the agent session.

### Usage
- **Basic prompt (not streaming):**
  ```javascript
  await session.prompt("What files are here?");
  ```
- **With images:**
  ```javascript
  await session.prompt("What's in this image?", {
    images: [{ type: "image", source: { type: "base64", mediaType: "image/png", data: "..." } }]
  });
  ```
- **During streaming (specify queueing behavior):**
  ```javascript
  await session.prompt("Stop and do this instead", { streamingBehavior: "steer" });
  await session.prompt("After you're done, also check X", { streamingBehavior: "followUp" });
  ```

### Behavior
- **Extension commands** (e.g., `/mycommand`): Execute immediately, even during streaming. They manage their own LLM interaction via `pi.sendMessage()`.
- **File-based prompt templates** (from `.md` files): Expanded to their content before sending or queueing.
- **During streaming without `streamingBehavior`**: Throws an error. Use `steer()` or `followUp()` directly, or specify the option.
- **`preflightResult(true)`**: Means the prompt was accepted, queued, or handled immediately.
- **`preflightResult(false)`**: Means preflight rejected before acceptance.
```

--------------------------------

### Static Listing Methods

Source: https://pi.dev/docs/latest/session

Methods for listing sessions.

```APIDOC
## SessionManager.list
### Description
Lists sessions for a given directory.
### Method
`SessionManager.list(cwd, sessionDir?, onProgress?)
### Parameters
#### Path Parameters
- **cwd** (string) - Required - The current working directory.
- **sessionDir** (string) - Optional - The directory to store session files.
- **onProgress** (function) - Optional - A callback function for progress updates.

## SessionManager.listAll
### Description
Lists all sessions across all projects.
### Method
`SessionManager.listAll(onProgress?)
### Parameters
#### Path Parameters
- **onProgress** (function) - Optional - A callback function for progress updates.
```

--------------------------------

### Display Keybinding Hints

Source: https://pi.dev/docs/latest/extensions

Displays keybinding hints that respect the active keybinding configuration using `keyHint()`. Available functions include `keyHint`, `keyText`, and `rawKeyHint`. Use namespaced keybinding IDs like `app.*` or `tui.*`.

```javascript
import { keyHint } from "@mariozechner/pi-coding-agent";

renderResult(result, { expanded }, theme, context) {
  let text = theme.fg("success", "✓ Done");
  if (!expanded) {
    text += ` (${keyHint("app.tools.expand", "to expand")})`;
  }
  return new Text(text, 0, 0);
}
```

--------------------------------

### tmux Extended Keys Format Comparison

Source: https://pi.dev/docs/latest/tmux

Illustrates the difference in key reporting format between the default `xterm` and the recommended `csi-u` for tmux extended keys. The `csi-u` format is more reliable for applications like Pi.

```text
With only:
```
set -g extended-keys on

```

tmux defaults to `extended-keys-format xterm`. When an application requests extended key reporting, modified keys are forwarded in xterm `modifyOtherKeys` format such as:
  * `Ctrl+C` → `\x1b[27;5;99~`
  * `Ctrl+D` → `\x1b[27;5;100~`
  * `Ctrl+Enter` → `\x1b[27;5;13~`


With `extended-keys-format csi-u`, the same keys are forwarded as:
  * `Ctrl+C` → `\x1b[99;5u`
  * `Ctrl+D` → `\x1b[100;5u`
  * `Ctrl+Enter` → `\x1b[13;5u`
```

--------------------------------

### pi.exec(command, args, options?)

Source: https://pi.dev/docs/latest/extensions

Executes a shell command with specified arguments and optional configuration.

```APIDOC
## pi.exec(command, args, options?)

### Description
Execute a shell command.

### Usage
```javascript
const result = await pi.exec("git", ["status"], { signal, timeout: 5000 });
// result.stdout, result.stderr, result.code, result.killed
```

### Parameters
- **command** (string) - The command to execute (e.g., "git").
- **args** (array) - An array of string arguments for the command (e.g., `["status"]`).
- **options** (object, optional) - Additional options for execution.
  - **signal** (AbortSignal) - An AbortSignal to cancel the execution.
  - **timeout** (number) - The timeout in milliseconds for the command execution.

### Response
- **stdout** (string) - The standard output of the command.
- **stderr** (string) - The standard error of the command.
- **code** (number) - The exit code of the command.
- **killed** (boolean) - Indicates if the process was killed.
```

--------------------------------

### Loading Extensions with DefaultResourceLoader

Source: https://pi.dev/docs/latest/sdk

Demonstrates how to load custom extensions using `DefaultResourceLoader`. Extensions can be specified via `additionalExtensionPaths` or `extensionFactories`. The loader can be reloaded to apply changes.

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  additionalExtensionPaths: ["/path/to/my-extension.ts"],
  extensionFactories: [
    (pi) => {
      pi.on("agent_start", () => {
        console.log("[Inline Extension] Agent starting");
      });
    },
  ],
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });

```

--------------------------------

### Create Agent Session with Defaults

Source: https://pi.dev/docs/latest/sdk

Creates a minimal agent session using default resource loading.

```typescript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

// Minimal: defaults with DefaultResourceLoader
const { session } = await createAgentSession();

```

--------------------------------

### Navigate Session Tree

Source: https://pi.dev/docs/latest/extensions

Navigates to a different point in the session tree. Options allow for summarizing the abandoned branch, providing custom instructions for summarization, and controlling prompt replacement.

```javascript
const result = await ctx.navigateTree("entry-id-456", {
  summarize: true,
  customInstructions: "Focus on error handling changes",
  replaceInstructions: false, // true = replace default prompt entirely
  label: "review-checkpoint",
});

```

--------------------------------

### PromptOptions Interface

Source: https://pi.dev/docs/latest/sdk

Defines options for controlling prompt expansion, queueing behavior, and preflight notifications.

```APIDOC
## PromptOptions Interface

### Description
The `PromptOptions` interface controls prompt expansion, queueing behavior during streaming, and preflight notifications for prompts.

### Interface Definition
```typescript
interface PromptOptions {
  expandPromptTemplates?: boolean;
  images?: ImageContent[];
  streamingBehavior?: "steer" | "followUp";
  source?: InputSource;
  preflightResult?: (success: boolean) => void;
}
```

### `preflightResult` Callback
- Called once per `prompt()` invocation.
- `true`: The prompt was accepted, queued, or handled immediately.
- `false`: The prompt preflight rejected before acceptance.
- Fires before `prompt()` resolves. `prompt()` resolves only after the full accepted run finishes, including retries.
- Failures after acceptance are reported through the normal event and message stream, not `preflightResult(false)`.
```

--------------------------------

### pi.registerShortcut(shortcut, options)

Source: https://pi.dev/docs/latest/extensions

Registers a keyboard shortcut with a specified handler and description.

```APIDOC
## pi.registerShortcut(shortcut, options)

### Description
Register a keyboard shortcut. See keybindings.md for the shortcut format and built-in keybindings.

### Usage
```javascript
pi.registerShortcut("ctrl+shift+p", {
  description: "Toggle plan mode",
  handler: async (ctx) => {
    ctx.ui.notify("Toggled!");
  },
});
```

### Parameters
- **shortcut** (string) - The key combination for the shortcut (e.g., "ctrl+shift+p").
- **options** (object) - Configuration for the shortcut.
  - **description** (string) - A brief description of the shortcut's action.
  - **handler** (function) - An async function that is called when the shortcut is triggered. It receives a context object `ctx`.
```

--------------------------------

### Trigger Compaction with Callbacks

Source: https://pi.dev/docs/latest/extensions

Initiates a compaction process without waiting for it to finish. Use `onComplete` and `onError` to handle the outcome.

```javascript
ctx.compact({
  customInstructions: "Focus on recent changes",
  onComplete: (result) => {
    ctx.ui.notify("Compaction completed", "info");
  },
  onError: (error) => {
    ctx.ui.notify(`Compaction failed: ${error.message}`, "error");
  },
});

```

--------------------------------

### Prompt Options Interface

Source: https://pi.dev/docs/latest/sdk

Defines options for prompt expansion, streaming behavior, and preflight notifications.

```typescript
interface PromptOptions {
  expandPromptTemplates?: boolean;
  images?: ImageContent[];
  streamingBehavior?: "steer" | "followUp";
  source?: InputSource;
  preflightResult?: (success: boolean) => void;
}

```

--------------------------------

### Create a New Session

Source: https://pi.dev/docs/latest/extensions

Creates a new session, optionally linking it to a parent session and setting up initial messages. The `withSession` callback executes within the context of the new session.

```javascript
const parentSession = ctx.sessionManager.getSessionFile();
const kickoff = "Continue in the replacement session";

const result = await ctx.newSession({
  parentSession,
  setup: async (sm) => {
    sm.appendMessage({
      role: "user",
      content: [{ type: "text", text: "Context from previous session..." }],
      timestamp: Date.now(),
    });
  },
  withSession: async (ctx) => {
    // Use only the replacement-session ctx here.
    await ctx.sendUserMessage(kickoff);
  },
});

if (result.cancelled) {
  // An extension cancelled the new session
}

```

--------------------------------

### Instance Methods - Session Management

Source: https://pi.dev/docs/latest/session

Methods for managing the current session instance.

```APIDOC
## newSession
### Description
Starts a new session.
### Method
`newSession(options?)
### Parameters
#### Path Parameters
- **options** (object) - Optional - Options for the new session.
  - **parentSession** (string) - Optional - The ID of the parent session.
```

```APIDOC
## setSessionFile
### Description
Switches to a different session file.
### Method
`setSessionFile(path)
### Parameters
#### Path Parameters
- **path** (string) - Required - The path to the new session file.
```

```APIDOC
## createBranchedSession
### Description
Extracts a branch to a new session file.
### Method
`createBranchedSession(leafId)
### Parameters
#### Path Parameters
- **leafId** (string) - Required - The ID of the leaf entry to branch from.
```

--------------------------------

### Run Pi Tests

Source: https://pi.dev/docs/latest/development

Execute tests for the Pi project. Use `./test.sh` for non-LLM tests (no API keys required), `npm test` for all tests, or `npm test -- test/specific.test.ts` to run a specific test file.

```bash
./test.sh                         # Run non-LLM tests (no API keys needed)
npm test                          # Run all tests
npm test -- test/specific.test.ts # Run specific test

```

--------------------------------

### get_available_models

Source: https://pi.dev/docs/latest/rpc

List all configured models.

```APIDOC
## get_available_models

### Description
List all configured models.

### Method
get_available_models

### Request Body
- **type** (string) - Required - Must be "get_available_models"

### Request Example
```json
{"type": "get_available_models"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "get_available_models"
- **success** (boolean) - true
- **data** (object)
  - **models** (array) - An array of full Model objects.
```

--------------------------------

### API Key Resolution via Environment Variable

Source: https://pi.dev/docs/latest/models

Shows how to use an environment variable to provide the API key. This is a common method for managing sensitive credentials.

```json
"apiKey": "MY_API_KEY"
```

--------------------------------

### Registering a Custom Tool

Source: https://pi.dev/docs/latest/extensions

Defines a new tool named 'my_tool' with specific parameters and an execution function. It includes argument preparation and error signaling.

```APIDOC
## pi.registerTool("my_tool")

### Description
Registers a new tool that can be used by the LLM. This example defines a tool for managing a project todo list.

### Parameters
- **action** (stringEnum: ["list", "add"]) - Required - The action to perform (list or add items).
- **text** (string) - Optional - The text content for adding an item.

### prepareArguments
Optional function to transform incoming arguments to match the current schema, useful for resuming older sessions.

### execute
Asynchronous function that performs the tool's action. It can stream progress updates and return results or throw an error to signal failure.

#### Arguments
- **toolCallId** (string): Unique identifier for the tool call.
- **params** (object): The parameters for the tool, validated against the schema.
- **signal** (AbortSignal): Signal for cancellation.
- **onUpdate** (function): Callback to stream progress updates.
- **ctx** (object): Context object.

#### Return Value
- **content** (array): Content to be displayed to the user.
- **details** (object): Additional data, e.g., for rendering.
- **terminate** (boolean): Optional flag to indicate early termination.

#### Error Handling
Throw an error from `execute` to signal a failed tool execution.

### Request Example
```json
{
  "action": "add",
  "text": "Buy groceries"
}
```

### Response Example
```json
{
  "content": [
    {
      "type": "text",
      "text": "Done"
    }
  ],
  "details": {
    "data": "some-command-result"
  },
  "terminate": true
}
```
```

--------------------------------

### Define and Use Inline Custom Tools

Source: https://pi.dev/docs/latest/sdk

Shows how to define a custom tool using `defineTool` and pass it directly to `createAgentSession` via the `customTools` option. This allows for custom functionality within the agent.

```typescript
import { Type } from "typebox";
import { createAgentSession, defineTool } from "@mariozechner/pi-coding-agent";

// Inline custom tool
const myTool = defineTool({
  name: "my_tool",
  label: "My Tool",
  description: "Does something useful",
  parameters: Type.Object({
    input: Type.String({ description: "Input value" }),
  }),
  execute: async (_toolCallId, params) => ({
    content: [{ type: "text", text: `Result: ${params.input}` }],
    details: {},
  }),
});

// Pass custom tools directly
const { session } = await createAgentSession({
  customTools: [myTool],
});
```

--------------------------------

### Configure Ghostty for Pi

Source: https://pi.dev/docs/latest/terminal-setup

Add this to your Ghostty config file to enable Kitty keyboard protocol support. This ensures reliable modifier key detection.

```shell
keybind = alt+backspace=text:\x1b\x7f
```

--------------------------------

### Register a Custom Tool

Source: https://pi.dev/docs/latest/extensions

Define a new tool with its name, label, description, prompt guidelines, parameters, and execution logic. Use `StringEnum` for parameters compatible with Google's API. The `prepareArguments` function can be used to adapt older argument shapes to the current schema.

```typescript
import { Type } from "typebox";
import { StringEnum } from "@mariozechner/pi-ai";
import { Text } from "@mariozechner/pi-tui";

pi.registerTool({
  name: "my_tool",
  label: "My Tool",
  description: "What this tool does (shown to LLM)",
  promptSnippet: "List or add items in the project todo list",
  promptGuidelines: [
    "Use my_tool for todo planning instead of direct file edits when the user asks for a task list."
  ],
  parameters: Type.Object({
    action: StringEnum(["list", "add"] as const),  // Use StringEnum for Google compatibility
    text: Type.Optional(Type.String()),
  }),
  prepareArguments(args) {
    if (!args || typeof args !== "object") return args;
    const input = args as { action?: string; oldAction?: string };
    if (typeof input.oldAction === "string" && input.action === undefined) {
      return { ...input, action: input.oldAction };
    }
    return args;
  },

  async execute(toolCallId, params, signal, onUpdate, ctx) {
    // Check for cancellation
    if (signal?.aborted) {
      return { content: [{ type: "text", text: "Cancelled" }] };
    }

    // Stream progress updates
    onUpdate?.({
      content: [{ type: "text", text: "Working..." }],
      details: { progress: 50 },
    });

    // Run commands via pi.exec (captured from extension closure)
    const result = await pi.exec("some-command", [], { signal });

    // Return result
    return {
      content: [{ type: "text", text: "Done" }],  // Sent to LLM
      details: { data: result },                   // For rendering & state
      // Optional: stop after this tool batch when every finalized tool result
      // in the batch also returns terminate: true.
      terminate: true,
    };
  },

  // Optional: Custom rendering
  renderCall(args, theme, context) { ... },
  renderResult(result, options, theme, context) { ... },
});

```

--------------------------------

### follow_up

Source: https://pi.dev/docs/latest/rpc

Queue a follow-up message to be processed after the agent finishes. Delivered only when the agent has no more tool calls or steering messages. Skill commands and prompt templates are expanded. Extension commands are not allowed (use `prompt` instead).

```APIDOC
## follow_up

### Description
Queue a follow-up message to be processed after the agent finishes. Delivered only when agent has no more tool calls or steering messages. Skill commands and prompt templates are expanded. Extension commands are not allowed (use `prompt` instead).

### Method
follow_up

### Request Body
- **type** (string) - Required - Must be "follow_up"
- **message** (string) - Required - The message content.
- **images** (array) - Optional - An array of images to include with the message.
  - **type** (string) - Required - Must be "image"
  - **data** (string) - Required - Base64-encoded image data.
  - **mimeType** (string) - Required - The MIME type of the image (e.g., "image/png").

### Request Example
```json
{"type": "follow_up", "message": "After you're done, also do this"}
```

### Request Example with Images
```json
{"type": "follow_up", "message": "Also check this image", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "follow_up"
- **success** (boolean) - true
```

--------------------------------

### Handle turn_start / turn_end

Source: https://pi.dev/docs/latest/extensions

React to the beginning and end of each turn, which includes an LLM response and potential tool calls.

```javascript
pi.on("turn_start", async (event, ctx) => {
  // event.turnIndex, event.timestamp
});

pi.on("turn_end", async (event, ctx) => {
  // event.turnIndex, event.message, event.toolResults
});
```

--------------------------------

### Manage Active Tools

Source: https://pi.dev/docs/latest/extensions

Retrieves all available tools, filters them by source (e.g., built-in, extension), and sets the active tools for the current session. Note that `pi.getAllTools()` returns detailed information including `sourceInfo`.

```javascript
const active = pi.getActiveTools();
const all = pi.getAllTools();
// [{
//   name: "read",
//   description: "Read file contents...",
//   parameters: ..., 
//   sourceInfo: { path: "<builtin:read>", source: "builtin", scope: "temporary", origin: "top-level" }
// }, ...]
const names = all.map(t => t.name);
const builtinTools = all.filter((t) => t.sourceInfo.source === "builtin");
const extensionTools = all.filter((t) => t.sourceInfo.source !== "builtin" && t.sourceInfo.source !== "sdk");
pi.setActiveTools(["read", "bash"]); // Switch to read-only
```

--------------------------------

### agent_start / agent_end

Source: https://pi.dev/docs/latest/extensions

Fired once per user prompt. `agent_start` is called at the beginning, and `agent_end` is called after the agent has finished processing the prompt.

```APIDOC
## agent_start / agent_end

### Description
Fired once per user prompt. `agent_start` is called at the beginning, and `agent_end` is called after the agent has finished processing the prompt.

### `agent_start` Event Parameters
- **_event**: Object (unused in the example)

### `agent_start` Context Parameters
- **ctx**: Object

### `agent_end` Event Parameters
- **event**: Object
  - **messages** (Array) - Messages generated during the agent's processing of the prompt.

### `agent_end` Context Parameters
- **ctx**: Object

### Examples
```javascript
pi.on("agent_start", async (_event, ctx) => {});

pi.on("agent_end", async (event, ctx) => {
  // event.messages - messages from this prompt
});
```
```

--------------------------------

### Handling Text Content Blocks

Source: https://pi.dev/docs/latest/custom-provider

Demonstrates how to push text content blocks and their deltas to the stream. Ensure `contentIndex` is correctly managed for each block.

```javascript
// Text block
output.content.push({ type: "text", text: "" });
stream.push({ type: "text_start", contentIndex: output.content.length - 1, partial: output });

// As text arrives
const block = output.content[contentIndex];
if (block.type === "text") {
  block.text += delta;
  stream.push({ type: "text_delta", contentIndex, delta, partial: output });
}

// When block completes
stream.push({ type: "text_end", contentIndex, content: block.text, partial: output });

```

--------------------------------

### Test an Extension with the CLI

Source: https://pi.dev/docs/latest/extensions

Use the `--extension` (or `-e`) flag to test a local extension file directly without needing to place it in the auto-discovery directories.

```bash
pi -e ./my-extension.ts

```

--------------------------------

### Send Custom Message with Options

Source: https://pi.dev/docs/latest/extensions

Inject a custom message into the session with optional delivery and triggering behavior. Use 'steer' for immediate queuing during streaming or 'followUp' to wait for tool calls.

```javascript
pi.sendMessage({
  customType: "my-extension",
  content: "Message text",
  display: true,
  details: { ... },
}, {
  triggerTurn: true,
  deliverAs: "steer",
});

```

--------------------------------

### pi.getCommands()

Source: https://pi.dev/docs/latest/extensions

Retrieves a list of all available slash commands for the current session, including those from extensions, prompt templates, and skills. The commands are ordered by source: extensions first, then templates, then skills.

```APIDOC
## pi.getCommands()

### Description
Get the slash commands available for invocation via `prompt` in the current session. Includes extension commands, prompt templates, and skill commands. The list matches the RPC `get_commands` ordering: extensions first, then templates, then skills.

### Usage
```javascript
const commands = pi.getCommands();
const bySource = commands.filter((command) => command.source === "extension");
const userScoped = commands.filter((command) => command.sourceInfo.scope === "user");
```

### Response Shape
Each entry has this shape:
```json
{
  name: string; // Invokable command name without the leading slash. May be suffixed like "review:1"
  description?: string;
  source: "extension" | "prompt" | "skill";
  sourceInfo: {
    path: string;
    source: string;
    scope: "user" | "project" | "temporary";
    origin: "package" | "top-level";
    baseDir?: string;
  };
}
```

### Notes
Use `sourceInfo` as the canonical provenance field. Do not infer ownership from command names or from ad hoc path parsing. Built-in interactive commands (like `/model` and `/settings`) are not included here. They are handled only in interactive mode and would not execute if sent via `prompt`.
```

--------------------------------

### ctx.fork(entryId, options?)

Source: https://pi.dev/docs/latest/extensions

Forks from a specific entry, creating a new session file. The `withSession` callback executes within the context of the new forked session.

```APIDOC
## ctx.fork(entryId, options?)

### Description
Fork from a specific entry, creating a new session file. This method is only available in commands.

### Method
await ctx.fork(entryId, options)

### Parameters
#### Path Parameters
- **entryId** (string) - Required - The ID of the entry to fork from.

#### Options
- **position** (string) - Optional - Determines the position of the fork. Defaults to `"before"`. Can be `"before"` (forks before the selected user message, restoring that prompt into the editor) or `"at"` (duplicates the active path through the selected entry without restoring editor text).
- **withSession** (function) - Optional - A function that runs post-switch work against a fresh replacement-session context.

### Request Example
```javascript
const result = await ctx.fork("entry-id-123", {
  withSession: async (ctx) => {
    // Use only the replacement-session ctx here.
    ctx.ui.notify("Now in the forked session", "info");
  },
});
if (result.cancelled) {
  // An extension cancelled the fork
}

const cloneResult = await ctx.fork("entry-id-456", { position: "at" });
if (cloneResult.cancelled) {
  // An extension cancelled the clone
}
```
```

--------------------------------

### Queue a follow-up message with images

Source: https://pi.dev/docs/latest/rpc

Queue a follow-up message that includes images. The `images` field is optional and each image should follow the `ImageContent` format.

```json
{"type": "follow_up", "message": "Also check this image", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

--------------------------------

### Handle User Input with pi.on("input")

Source: https://pi.dev/docs/latest/extensions

Intercept and process raw user input before skill or template expansion. Can transform input, handle it directly, or route it.

```javascript
pi.on("input", async (event, ctx) => {
  // event.text - raw input (before skill/template expansion)
  // event.images - attached images, if any
  // event.source - "interactive" (typed), "rpc" (API), or "extension" (via sendUserMessage)

  // Transform: rewrite input before expansion
  if (event.text.startsWith("?quick "))
    return { action: "transform", text: `Respond briefly: ${event.text.slice(7)}` };

  // Handle: respond without LLM (extension shows its own feedback)
  if (event.text === "ping") {
    ctx.ui.notify("pong", "info");
    return { action: "handled" };
  }

  // Route by source: skip processing for extension-injected messages
  if (event.source === "extension") return { action: "continue" };

  // Intercept skill commands before expansion
  if (event.text.startsWith("/skill:")) {
    // Could transform, block, or let pass through
  }

  return { action: "continue" };  // Default: pass through to expansion
});
```

--------------------------------

### Prompt Template with Positional Arguments

Source: https://pi.dev/docs/latest/prompt-templates

Shows how to use positional arguments like $1, $@, and sliced arguments like ${@:N} or ${@:N:L} within a prompt template to dynamically insert user-provided values.

```markdown
---
description: Create a component
---
Create a React component named $1 with features: $@


```

--------------------------------

### Create Agent Session with In-Memory Settings and Session

Source: https://pi.dev/docs/latest/sdk

Uses in-memory storage for settings and session management, avoiding file I/O. Ideal for testing scenarios.

```typescript
import { createAgentSession, SettingsManager, SessionManager } from "@mariozechner/pi-coding-agent";

// In-memory (no file I/O, for testing)
const { session } = await createAgentSession({
  settingsManager: SettingsManager.inMemory({ compaction: { enabled: false } }),
  sessionManager: SessionManager.inMemory(),
});
```

--------------------------------

### Pi Package Source Types: Local Paths

Source: https://pi.dev/docs/latest/packages

Specifies local file or directory paths as Pi package sources. Relative paths are resolved against the settings file. Directories are loaded using package rules.

```bash
/absolute/path/to/package
./relative/path/to/package
```

--------------------------------

### API Key Resolution via Shell Command

Source: https://pi.dev/docs/latest/models

Demonstrates resolving API keys using shell commands, which are executed at request time. Pi does not apply built-in caching or TTL logic for these commands.

```json
"apiKey": "!security find-generic-password -ws 'anthropic'"
```

```json
"apiKey": "!op read 'op://vault/item/credential'"
```

--------------------------------

### Instance Methods - Appending

Source: https://pi.dev/docs/latest/session

Methods for appending various types of entries to the session. All return the entry ID.

```APIDOC
## appendMessage
### Description
Adds a message to the session.
### Method
`appendMessage(message)
### Parameters
#### Path Parameters
- **message** (object) - Required - The message object to append.
```

```APIDOC
## appendThinkingLevelChange
### Description
Records a change in the thinking level.
### Method
`appendThinkingLevelChange(level)
### Parameters
#### Path Parameters
- **level** (string) - Required - The new thinking level.
```

```APIDOC
## appendModelChange
### Description
Records a change in the model.
### Method
`appendModelChange(provider, modelId)
### Parameters
#### Path Parameters
- **provider** (string) - Required - The model provider.
- **modelId** (string) - Required - The model ID.
```

```APIDOC
## appendCompaction
### Description
Adds a compaction entry to the session.
### Method
`appendCompaction(summary, firstKeptEntryId, tokensBefore, details?, fromHook?)
### Parameters
#### Path Parameters
- **summary** (string) - Required - The summary of the compacted entries.
- **firstKeptEntryId** (string) - Required - The ID of the first entry kept after compaction.
- **tokensBefore** (number) - Required - The number of tokens before compaction.
- **details** (any) - Optional - Additional details about the compaction.
- **fromHook** (boolean) - Optional - Indicates if the compaction was triggered by a hook.
```

```APIDOC
## appendCustomEntry
### Description
Adds a custom entry to the session (not included in context).
### Method
`appendCustomEntry(customType, data?)
### Parameters
#### Path Parameters
- **customType** (string) - Required - The type of the custom entry.
- **data** (any) - Optional - The data associated with the custom entry.
```

```APIDOC
## appendSessionInfo
### Description
Sets the display name for the session.
### Method
`appendSessionInfo(name)
### Parameters
#### Path Parameters
- **name** (string) - Required - The display name for the session.
```

```APIDOC
## appendCustomMessageEntry
### Description
Adds a custom message entry to the session (included in context).
### Method
`appendCustomMessageEntry(customType, content, display, details?)
### Parameters
#### Path Parameters
- **customType** (string) - Required - The type of the custom message.
- **content** (any) - Required - The content of the message.
- **display** (string) - Required - How the message should be displayed.
- **details** (any) - Optional - Additional details about the message.
```

```APIDOC
## appendLabelChange
### Description
Sets or clears a label for an entry.
### Method
`appendLabelChange(targetId, label)
### Parameters
#### Path Parameters
- **targetId** (string) - Required - The ID of the entry to label.
- **label** (string) - Required - The label to set. Use an empty string to clear.
```

--------------------------------

### OpenAI Compatibility Settings

Source: https://pi.dev/docs/latest/custom-provider

Details on OpenAI compatibility settings for custom models, including support for reasoning, thinking formats, and cache control.

```text
`deepseek` sends `thinking: { type: "enabled" | "disabled" }` and `reasoning_effort` when enabled. `qwen` is for DashScope-style top-level `enable_thinking`. Use `qwen-chat-template` for local Qwen-compatible servers that read `chat_template_kwargs.enable_thinking`. `cacheControlFormat: "anthropic"` applies Anthropic-style `cache_control` markers to the system prompt, last tool definition, and last user/assistant text content.
```

--------------------------------

### ctx.reload()

Source: https://pi.dev/docs/latest/extensions

Triggers a reload of extensions, skills, prompts, and themes, similar to the `/reload` endpoint. It emits `session_shutdown` and then `session_start` with a reload reason. Code after `await ctx.reload()` in the same handler will run from the pre-reload version, but should not assume old in-memory state is valid. For predictable behavior, it's recommended to return immediately after calling `await ctx.reload()`.

```APIDOC
## ctx.reload()

### Description
Run the same reload flow as `/reload`.

### Method
`await ctx.reload()`

### Behavior
- Emits `session_shutdown` for the current extension runtime.
- Reloads resources and emits `session_start` with `reason: "reload"` and `resources_discover` with reason `"reload"`.
- The currently running command handler still continues in the old call frame.
- Code after `await ctx.reload()` still runs from the pre-reload version.
- Code after `await ctx.reload()` must not assume old in-memory extension state is still valid.
- After the handler returns, future commands/events/tool calls use the new extension version.

### Important Note
For predictable behavior, treat reload as terminal for that handler (`await ctx.reload(); return;`). Tools run with `ExtensionContext`, so they cannot call `ctx.reload()` directly. Use a command as the reload entrypoint, then expose a tool that queues that command as a follow-up user message.
```

--------------------------------

### Configure Skill Locations in Settings

Source: https://pi.dev/docs/latest/skills

Specify directories for skills from other harnesses like Claude Code or OpenAI Codex. This can be done globally or per project.

```json
{
  "skills": [
    "~/.claude/skills",
    "~/.codex/skills"
  ]

}
```

```json
{
  "skills": ["../.claude/skills"]
}
```

--------------------------------

### Minimal Ollama Provider Configuration

Source: https://pi.dev/docs/latest/models

For local models like Ollama, LM Studio, or vLLM, only the model `id` is required. The `apiKey` is mandatory but ignored by Ollama.

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        { "id": "llama3.1:8b" },
        { "id": "qwen2.5-coder:7b" }
      ]
    }
  }
}
```

--------------------------------

### Queue a follow-up message

Source: https://pi.dev/docs/latest/rpc

Use this command to queue a message that will be processed after the agent finishes its current tasks. It's suitable for post-completion actions but does not support extension commands.

```json
{"type": "follow_up", "message": "After you're done, also do this"}
```

--------------------------------

### select

Source: https://pi.dev/docs/latest/rpc

Prompt the user to choose from a list. Dialog methods with a `timeout` field include the timeout in milliseconds; the agent auto-resolves with `undefined` if the client doesn't respond in time.

```APIDOC
## select

Prompt the user to choose from a list. Dialog methods with a `timeout` field include the timeout in milliseconds; the agent auto-resolves with `undefined` if the client doesn't respond in time.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-1",
  "method": "select",
  "title": "Allow dangerous command?",
  "options": ["Allow", "Block"],
  "timeout": 10000
}
```

Expected response: `extension_ui_response` with `value` (the selected option string) or `cancelled: true`.
```

--------------------------------

### session_before_compact / session_compact

Source: https://pi.dev/docs/latest/extensions

Fired on compaction. Allows extensions to influence or provide custom summaries for the compaction process.

```APIDOC
## session_before_compact / session_compact

### Description
Fired on compaction. Allows extensions to influence or provide custom summaries for the compaction process.

### `session_before_compact` Event Parameters
- **event**: Object
  - **preparation**: Object
    - **firstKeptEntryId** (string) - The ID of the first entry kept during compaction.
    - **tokensBefore** (number) - The number of tokens before compaction.
  - **branchEntries**: Array - Entries belonging to branches.
  - **customInstructions**: Object - Custom instructions for compaction.
  - **signal**: Object - Abort signal for the operation.

### `session_before_compact` Context Parameters
- **ctx**: Object

### `session_before_compact` Return Value
- **{ cancel: true }**: To cancel the compaction.
- **{ compaction: { summary: string, firstKeptEntryId: string, tokensBefore: number } }**: To provide a custom summary for the compaction.

### `session_compact` Event Parameters
- **event**: Object
  - **compactionEntry**: Object - The saved compaction data.
  - **fromExtension** (boolean) - Whether the compaction data was provided by an extension.

### `session_compact` Context Parameters
- **ctx**: Object

### Examples
```javascript
pi.on("session_before_compact", async (event, ctx) => {
  const { preparation, branchEntries, customInstructions, signal } = event;

  // Cancel:
  return { cancel: true };

  // Custom summary:
  return {
    compaction: {
      summary: "...",
      firstKeptEntryId: preparation.firstKeptEntryId,
      tokensBefore: preparation.tokensBefore,
    }
  };
});

pi.on("session_compact", async (event, ctx) => {
  // event.compactionEntry - the saved compaction
  // event.fromExtension - whether extension provided it
});
```
```

--------------------------------

### get_commands

Source: https://pi.dev/docs/latest/rpc

Retrieves a list of available commands, including extension commands, prompt templates, and skills. These commands can be invoked via the `prompt` command by prefixing with `/`.

```APIDOC
## get_commands

### Description
Get available commands (extension commands, prompt templates, and skills). These can be invoked via the `prompt` command by prefixing with `/`.

### Request Body
- **type** (string) - Required - Must be "get_commands"

### Request Example
```json
{
  "type": "get_commands"
}
```

### Response
#### Success Response (200)
- **type** (string) - The type of the response, should be "response"
- **command** (string) - The command that was executed, should be "get_commands"
- **success** (boolean) - Indicates if the command was successful
- **data** (object) - Contains the result of the command
  - **commands** (array) - A list of available commands
    - **name** (string) - Command name (invoke with `/name`)
    - **description** (string) - Human-readable description (optional for extension commands)
    - **source** (string) - What kind of command: "extension", "prompt", or "skill"
    - **location** (string, optional) - Where it was loaded from: "user", "project", or "path"
    - **path** (string, optional) - Absolute file path to the command source

#### Response Example
```json
{
  "type": "response",
  "command": "get_commands",
  "success": true,
  "data": {
    "commands": [
      {"name": "session-name", "description": "Set or clear session name", "source": "extension", "path": "/home/user/.pi/agent/extensions/session.ts"},
      {"name": "fix-tests", "description": "Fix failing tests", "source": "prompt", "location": "project", "path": "/home/user/myproject/.pi/agent/prompts/fix-tests.md"},
      {"name": "skill:brave-search", "description": "Web search via Brave API", "source": "skill", "location": "user", "path": "/home/user/.pi/agent/skills/brave-search/SKILL.md"}
    ]
  }
}
```

**Note**: Built-in TUI commands (`/settings`, `/hotkeys`, etc.) are not included. They are handled only in interactive mode and would not execute if sent via `prompt`.
```

--------------------------------

### Apply Theming to Rendered Output

Source: https://pi.dev/docs/latest/tui

Use theme objects to style rendered output. `theme.fg()` is for foreground colors and `theme.bg()` is for background colors. The `theme` parameter is available in `renderCall` and `renderResult`.

```typescript
renderResult(result, options, theme, context) {
  // Use theme.fg() for foreground colors
  return new Text(theme.fg("success", "Done!"), 0, 0);
  
  // Use theme.bg() for background colors
  const styled = theme.bg("toolPendingBg", theme.fg("accent", "text"));
}
```

--------------------------------

### Register New Provider with Static Model Definition

Source: https://pi.dev/docs/latest/custom-provider

Define and register a new provider with a static list of models, including details like cost, context window, and reasoning support. When `models` is provided, it replaces any existing models for that provider.

```typescript
pi.registerProvider("my-llm", {
  baseUrl: "https://api.my-llm.com/v1",
  apiKey: "MY_LLM_API_KEY",  // env var name or literal value
  api: "openai-completions",  // which streaming API to use
  models: [
    {
      id: "my-llm-large",
      name: "My LLM Large",
      reasoning: true,        // supports extended thinking
      input: ["text", "image"],
      cost: {
        input: 3.0,           // $/million tokens
        output: 15.0,
        cacheRead: 0.3,
        cacheWrite: 3.75
      },
      contextWindow: 200000,
      maxTokens: 16384
    }
  ]
});

```

--------------------------------

### Override System Prompt with ResourceLoader

Source: https://pi.dev/docs/latest/sdk

Shows how to use a ResourceLoader to set a custom system prompt for the agent session. Ensure to call loader.reload() after configuration.

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  systemPromptOverride: () => "You are a helpful assistant.",
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });
```

--------------------------------

### Configure Compaction Settings in Pi

Source: https://pi.dev/docs/latest/settings

Enable or disable auto-compaction and specify token reserves for LLM responses and recent token retention. This helps manage context window usage.

```json
{
  "compaction": {
    "enabled": true,
    "reserveTokens": 16384,
    "keepRecentTokens": 20000
  }
}
```

--------------------------------

### AgentSession Interface

Source: https://pi.dev/docs/latest/sdk

Provides an overview of the `AgentSession` interface, detailing methods for interaction, state management, and lifecycle control.

```APIDOC
## AgentSession
```typescript
interface AgentSession {
  // Send a prompt and wait for completion
  prompt(text: string, options?: PromptOptions): Promise<void>;

  // Queue messages during streaming
  steer(text: string): Promise<void>;
  followUp(text: string): Promise<void>;

  // Subscribe to events (returns unsubscribe function)
  subscribe(listener: (event: AgentSessionEvent) => void): () => void;

  // Session info
  sessionFile: string | undefined;
  sessionId: string;

  // Model control
  setModel(model: Model): Promise<void>;
  setThinkingLevel(level: ThinkingLevel): void;
  cycleModel(): Promise<ModelCycleResult | undefined>;
  cycleThinkingLevel(): ThinkingLevel | undefined;

  // State access
  agent: Agent;
  model: Model | undefined;
  thinkingLevel: ThinkingLevel;
  messages: AgentMessage[];
  isStreaming: boolean;

  // In-place tree navigation within the current session file
  navigateTree(targetId: string, options?: { summarize?: boolean; customInstructions?: string; replaceInstructions?: boolean; label?: string }): Promise<{ editorText?: string; cancelled: boolean }>;

  // Compaction
  compact(customInstructions?: string): Promise<CompactionResult>;
  abortCompaction(): void;

  // Abort current operation
  abort(): Promise<void>;

  // Cleanup
  dispose(): void;
}
```
```

--------------------------------

### Edit Custom Theme File

Source: https://pi.dev/docs/latest/themes

Open a new or existing theme JSON file using a text editor like vim. This file will contain the theme's color definitions.

```bash
vim ~/.pi/agent/themes/my-theme.json

```

--------------------------------

### Ollama Provider with Compatibility Settings

Source: https://pi.dev/docs/latest/models

Configure compatibility settings for OpenAI-compatible servers that may not support the `developer` role or `reasoning_effort`. These settings can be applied at the provider or model level.

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "compat": {
        "supportsDeveloperRole": false,
        "supportsReasoningEffort": false
      },
      "models": [
        {
          "id": "gpt-oss:20b",
          "reasoning": true
        }
      ]
    }
  }
}
```

--------------------------------

### Configure tmux Extended Keys

Source: https://pi.dev/docs/latest/tmux

Add these settings to your `~/.tmux.conf` file to enable extended key reporting in the recommended `csi-u` format. This ensures modified keys are sent correctly.

```tmux
set -g extended-keys on
set -g extended-keys-format csi-u
```

--------------------------------

### Create Settings/Toggles with SettingsList

Source: https://pi.dev/docs/latest/tui

Utilize `SettingsList` for managing multiple application settings or toggles. It supports search and provides a callback for handling value changes. Ensure `getSettingsListTheme` is imported.

```typescript
import { getSettingsListTheme } from "@mariozechner/pi-coding-agent";
import { Container, type SettingItem, SettingsList, Text } from "@mariozechner/pi-tui";

pi.registerCommand("settings", {
  handler: async (_args, ctx) => {
    const items: SettingItem[] = [
      { id: "verbose", label: "Verbose mode", currentValue: "off", values: ["on", "off"] },
      { id: "color", label: "Color output", currentValue: "on", values: ["on", "off"] },
    ];

    await ctx.ui.custom((_tui, theme, _kb, done) => {
      const container = new Container();
      container.addChild(new Text(theme.fg("accent", theme.bold("Settings")), 1, 1));

      const settingsList = new SettingsList(
        items,
        Math.min(items.length + 2, 15),
        getSettingsListTheme(),
        (id, newValue) => {
          // Handle value change
          ctx.ui.notify(`${id} = ${newValue}`, "info");
        },
        () => done(undefined),  // On close
        { enableSearch: true }, // Optional: enable fuzzy search by label
      );
      container.addChild(settingsList);

      return {
        render: (w) => container.render(w),
        invalidate: () => container.invalidate(),
        handleInput: (data) => settingsList.handleInput?.(data),
      };
    });
  },
});

```

--------------------------------

### Safe Session Handoff Pattern

Source: https://pi.dev/docs/latest/extensions

Demonstrates a safe pattern for handing off to a new session using `ctx.newSession`. The `withSession` callback receives a fresh context, and only plain data should be captured before replacement.

```javascript
pi.registerCommand("handoff", {
  handler: async (_args, ctx) => {
    const kickoff = "Continue from the replacement session";
    await ctx.newSession({
      withSession: async (ctx) => {
        await ctx.sendUserMessage(kickoff);
      },
    });
  },
});
```

--------------------------------

### ctx.compact()

Source: https://pi.dev/docs/latest/extensions

Triggers a compaction process without awaiting its completion. Use `onComplete` and `onError` callbacks for handling the outcome.

```APIDOC
## ctx.compact()

### Description
Trigger compaction without awaiting completion. Use `onComplete` and `onError` for follow-up actions.

### Method
ctx.compact(options)

### Parameters
#### Options
- **customInstructions** (string) - Optional - Custom instructions for the compaction process.
- **onComplete** (function) - Optional - Callback function executed upon successful completion.
- **onError** (function) - Optional - Callback function executed if an error occurs during compaction.

### Request Example
```javascript
ctx.compact({
  customInstructions: "Focus on recent changes",
  onComplete: (result) => {
    ctx.ui.notify("Compaction completed", "info");
  },
  onError: (error) => {
    ctx.ui.notify(`Compaction failed: ${error.message}`, "error");
  },
});
```
```

--------------------------------

### Create Remote Read Tool with Custom Operations

Source: https://pi.dev/docs/latest/extensions

Demonstrates creating a `read` tool that delegates file operations to a remote system via SSH. It defines custom `readFile` and `access` operations using `sshExec`.

```typescript
import { createReadTool, createBashTool, type ReadOperations } from "@mariozechner/pi-coding-agent";

// Create tool with custom operations
const remoteRead = createReadTool(cwd, {
  operations: {
    readFile: (path) => sshExec(remote, `cat ${path}`),
    access: (path) => sshExec(remote, `test -r ${path}`).then(() => {}),
  }
});

// Register, checking flag at execution time
pi.registerTool({
  ...remoteRead,
  async execute(id, params, signal, onUpdate, _ctx) {
    const ssh = getSshConfig();
    if (ssh) {
      const tool = createReadTool(cwd, { operations: createRemoteOps(ssh) });
      return tool.execute(id, params, signal, onUpdate);
    }
    return localRead.execute(id, params, signal, onUpdate);
  },
});
```

--------------------------------

### AgentSession.navigateTree()

Source: https://pi.dev/docs/latest/tree

Navigates the session tree to a specified target ID, with options for summarization and custom instructions.

```APIDOC
## AgentSession.navigateTree()

### Description
Navigates the session tree to a specified target ID. This method can optionally summarize branches and allows for custom instructions during summarization.

### Method
`async navigateTree(targetId: string, options?: { summarize?: boolean; customInstructions?: string; replaceInstructions?: boolean; label?: string; }): Promise<{ editorText?: string; cancelled: boolean }>`

### Parameters
#### Path Parameters
- **targetId** (string) - Required - The ID of the target node in the tree.

#### Options
- **summarize** (boolean) - Optional - Whether to generate a summary of the abandoned branch.
- **customInstructions** (string) - Optional - Custom instructions for the summarizer.
- **replaceInstructions** (boolean) - Optional - If true, `customInstructions` replaces the default prompt instead of being appended.
- **label** (string) - Optional - Label to attach to the branch summary entry (or target entry if not summarizing).

### Returns
- **editorText** (string) - Optional - Text to be displayed in the editor.
- **cancelled** (boolean) - Indicates if the navigation was cancelled.
```

--------------------------------

### Import Package Directories

Source: https://pi.dev/docs/latest/development

Use `src/config.ts` to import package assets like directories. Avoid using `__dirname` directly for package assets.

```typescript
import { getPackageDir, getThemeDir } from "./config.js";

```

--------------------------------

### Extension UI Request: Select

Source: https://pi.dev/docs/latest/rpc

A request to prompt the user for selection from a list. This is a dialog method that expects a response. Includes a timeout in milliseconds.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-1",
  "method": "select",
  "title": "Allow dangerous command?",
  "options": ["Allow", "Block"],
  "timeout": 10000
}
```

--------------------------------

### Skill Description Best Practices

Source: https://pi.dev/docs/latest/skills

Provides guidance on writing effective skill descriptions. A good description is specific and clearly states the skill's purpose and use cases.

```markdown
description: Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents.

```

```markdown
description: Helps with PDFs.

```

--------------------------------

### SessionHeader - Basic

Source: https://pi.dev/docs/latest/session

Represents the initial metadata for a session. It includes type, version, ID, timestamp, and current working directory. This entry is not part of the main tree structure.

```json
{"type":"session","version":3,"id":"uuid","timestamp":"2024-12-03T14:00:00.000Z","cwd":"/path/to/project"}
```

--------------------------------

### Send a Prompt with Images via RPC

Source: https://pi.dev/docs/latest/rpc

Include images in your prompt by encoding them in base64. Ensure the correct mime type is specified.

```json
{"type": "prompt", "message": "What's in this image?", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}

```

--------------------------------

### pi.getActiveTools() / pi.getAllTools() / pi.setActiveTools(names)

Source: https://pi.dev/docs/latest/extensions

Manages the set of active tools, allowing retrieval of all available tools, currently active tools, and setting a specific list of active tools.

```APIDOC
## pi.getActiveTools() / pi.getAllTools() / pi.setActiveTools(names)

### Description
Manage active tools. This works for both built-in tools and dynamically registered tools.

### Usage
```javascript
const active = pi.getActiveTools();
const all = pi.getAllTools();
// Example tool structure:
// {
//   name: "read",
//   description: "Read file contents...",
//   parameters: ..., 
//   sourceInfo: { path: "<builtin:read>", source: "builtin", scope: "temporary", origin: "top-level" }
// }
const names = all.map(t => t.name);
const builtinTools = all.filter((t) => t.sourceInfo.source === "builtin");
const extensionTools = all.filter((t) => t.sourceInfo.source !== "builtin" && t.sourceInfo.source !== "sdk");
pi.setActiveTools(["read", "bash"]); // Switch to read-only
```

### `pi.getAllTools()` Response
Returns an array of tool objects, each containing:
- **name** (string) - The name of the tool.
- **description** (string) - A description of the tool's functionality.
- **parameters** (object) - The parameters the tool accepts.
- **sourceInfo** (object) - Metadata about the tool's origin.
  - **path** (string) - The path or identifier of the tool's source.
  - **source** (string) - The source of the tool (e.g., `builtin`, `sdk`, extension metadata).
  - **scope** (`user` | `project` | `temporary`) - The scope of the tool.
  - **origin** (`package` | `top-level`) - Where the tool originates from.

### `pi.setActiveTools(names)`
- **names** (array of strings) - An array of tool names to set as active.
```

--------------------------------

### RPC Mode CLI Alternative

Source: https://pi.dev/docs/latest/sdk

For subprocess integration without the SDK, use the CLI directly with the '--mode rpc' and '--no-session' flags.

```bash
pi --mode rpc --no-session

```

--------------------------------

### Show Overlay Component

Source: https://pi.dev/docs/latest/tui

Use ctx.ui.custom with { overlay: true } to render a component on top of existing content without clearing the screen. Pass a function that returns a new component instance.

```typescript
const result = await ctx.ui.custom<string | null>(
  (tui, theme, keybindings, done) => new MyDialog({ onClose: done }),
  { overlay: true }
);

```

--------------------------------

### turn_start / turn_end

Source: https://pi.dev/docs/latest/extensions

Fired for each turn, which consists of one LLM response and any associated tool calls. `turn_start` is called at the beginning of a turn, and `turn_end` is called after the turn is completed.

```APIDOC
## turn_start / turn_end

### Description
Fired for each turn, which consists of one LLM response and any associated tool calls. `turn_start` is called at the beginning of a turn, and `turn_end` is called after the turn is completed.

### `turn_start` Event Parameters
- **event**: Object
  - **turnIndex** (number) - The index of the current turn.
  - **timestamp** (number) - The timestamp when the turn started.

### `turn_start` Context Parameters
- **ctx**: Object

### `turn_end` Event Parameters
- **event**: Object
  - **turnIndex** (number) - The index of the completed turn.
  - **message** (Object) - The message generated by the LLM for this turn.
  - **toolResults** (Array) - The results of any tool calls made during this turn.

### `turn_end` Context Parameters
- **ctx**: Object

### Examples
```javascript
pi.on("turn_start", async (event, ctx) => {
  // event.turnIndex, event.timestamp
});

pi.on("turn_end", async (event, ctx) => {
  // event.turnIndex, event.message, event.toolResults
});
```
```

--------------------------------

### Theme Management

Source: https://pi.dev/docs/latest/extensions

Retrieve all available themes, load a theme without switching, or switch the active theme by name or object. Access the current theme for styling.

```javascript
// Theme management (see themes.md for creating themes)
const themes = ctx.ui.getAllThemes();  // [{ name: "dark", path: "/..." | undefined }, ...]
const lightTheme = ctx.ui.getTheme("light");  // Load without switching
const result = ctx.ui.setTheme("light");  // Switch by name
if (!result.success) {
  ctx.ui.notify(`Failed: ${result.error}`, "error");
}
ctx.ui.setTheme(lightTheme!);  // Or switch by Theme object
ctx.ui.theme.fg("accent", "styled text");  // Access current theme

```

--------------------------------

### Send a Basic Prompt via RPC

Source: https://pi.dev/docs/latest/rpc

Send a simple text prompt to the agent. The response indicates if the prompt was accepted, queued, or handled.

```json
{"id": "req-1", "type": "prompt", "message": "Hello, world!"}

```

--------------------------------

### Configure Tools with Custom CWD using Factories

Source: https://pi.dev/docs/latest/sdk

Illustrates using tool factory functions (e.g., `createCodingTools`) when specifying a custom `cwd` and explicit tools. This ensures correct path resolution relative to the custom working directory.

```typescript
import {
  createCodingTools,    // Creates [read, bash, edit, write] for specific cwd
  createReadOnlyTools,  // Creates [read, grep, find, ls] for specific cwd
  createReadTool,
  createBashTool,
  createEditTool,
  createWriteTool,
  createGrepTool,
  createFindTool,
  createLsTool,
} from "@mariozechner/pi-coding-agent";

const cwd = "/path/to/project";

// Use factory for tool sets
const { session } = await createAgentSession({
  cwd,
  tools: createCodingTools(cwd),  // Tools resolve paths relative to cwd
});

// Or pick specific tools
const { session } = await createAgentSession({
  cwd,
  tools: [createReadTool(cwd), createBashTool(cwd), createGrepTool(cwd)],
});
```

--------------------------------

### Configure Agent Session Directories

Source: https://pi.dev/docs/latest/sdk

Set the working directory (cwd) and agent directory (agentDir) when creating an agent session. These directories influence resource discovery for extensions, skills, prompts, and context files.

```typescript
const { session } = await createAgentSession({
  // Working directory for DefaultResourceLoader discovery
  cwd: process.cwd(), // default
  
  // Global config directory
  agentDir: "~/.pi/agent", // default (expands ~)
});
```

--------------------------------

### Register New Provider with Dynamic Model Discovery

Source: https://pi.dev/docs/latest/custom-provider

Register a new provider by fetching models dynamically from a remote endpoint using an async extension factory. This ensures models are available during startup.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";

export default async function (pi: ExtensionAPI) {
  const response = await fetch("http://localhost:1234/v1/models");
  const payload = (await response.json()) as {
    data: Array<{ 
      id: string;
      name?: string;
      context_window?: number;
      max_tokens?: number;
    }>;
  };

  pi.registerProvider("local-openai", {
    baseUrl: "http://localhost:1234/v1",
    apiKey: "LOCAL_OPENAI_API_KEY",
    api: "openai-completions",
    models: payload.data.map((model) => ({
      id: model.id,
      name: model.name ?? model.id,
      reasoning: false,
      input: ["text"],
      cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
      contextWindow: model.context_window ?? 128000,
      maxTokens: model.max_tokens ?? 4096,
    })),
  });
}
```

--------------------------------

### set_model

Source: https://pi.dev/docs/latest/rpc

Switch to a specific model.

```APIDOC
## set_model

### Description
Switch to a specific model.

### Method
set_model

### Request Body
- **type** (string) - Required - Must be "set_model"
- **provider** (string) - Required - The model provider (e.g., "anthropic").
- **modelId** (string) - Required - The identifier of the model to switch to (e.g., "claude-sonnet-4-20250514").

### Request Example
```json
{"type": "set_model", "provider": "anthropic", "modelId": "claude-sonnet-4-20250514"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "set_model"
- **success** (boolean) - true
- **data** (object) - The full Model object configuration.
```

--------------------------------

### Select Theme in Settings

Source: https://pi.dev/docs/latest/themes

Set the active theme by specifying its name in the 'theme' field of your settings.json file. Pi automatically detects terminal background on first run to default to 'dark' or 'light'.

```json
{
  "theme": "my-theme"
}

```

--------------------------------

### Prompt Command

Source: https://pi.dev/docs/latest/rpc

Send a user prompt to the agent. The command response indicates acceptance, queuing, or immediate handling. Events stream asynchronously after acceptance. Supports optional 'id' for correlation and 'images' for image input. 'streamingBehavior' can be used to queue messages during streaming.

```APIDOC
## Prompt Command

### Description
Send a user prompt to the agent. The command response is emitted after the prompt is accepted, queued, or handled. Events continue streaming asynchronously after acceptance.

### Method
`prompt`

### Request Body
- **id** (string) - Optional - For request/response correlation.
- **type** (string) - Required - Must be "prompt".
- **message** (string) - Required - The user's prompt.
- **images** (array) - Optional - An array of image objects for image input.
  - **type** (string) - Required - Must be "image".
  - **data** (string) - Required - Base64-encoded image data.
  - **mimeType** (string) - Required - The MIME type of the image (e.g., "image/png").
- **streamingBehavior** (string) - Optional - Specifies how to handle the message during streaming. Can be "steer" or "followUp".

### Request Example
```json
{"id": "req-1", "type": "prompt", "message": "Hello, world!"}
```

With images:
```json
{"type": "prompt", "message": "What's in this image?", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

During streaming:
```json
{"type": "prompt", "message": "New instruction", "streamingBehavior": "steer"}
```

### Response
#### Success Response
- **id** (string) - The ID of the request, if provided.
- **type** (string) - Must be "response".
- **command** (string) - The command that was processed (e.g., "prompt").
- **success** (boolean) - `true` if the prompt was accepted, queued, or handled; `false` otherwise.

#### Response Example
```json
{"id": "req-1", "type": "response", "command": "prompt", "success": true}
```
```

--------------------------------

### Switch to a Different Session

Source: https://pi.dev/docs/latest/extensions

Use `ctx.switchSession` to switch to a different session file. The `withSession` option allows running post-switch work against a fresh replacement-session context.

```javascript
const result = await ctx.switchSession("/path/to/session.jsonl", {
  withSession: async (ctx) => {
    await ctx.sendUserMessage("Resume work in the replacement session");
  },
});
if (result.cancelled) {
  // An extension cancelled the switch via session_before_switch
}
```

--------------------------------

### pi.on(event, handler)

Source: https://pi.dev/docs/latest/extensions

Subscribe to events. See Events for event types and return values.

```APIDOC
## pi.on(event, handler)

### Description
Subscribe to events. See Events for event types and return values.

### Parameters
- **event** (string) - The name of the event to subscribe to.
- **handler** (function) - The callback function to execute when the event is triggered.
```

--------------------------------

### Switch Session

Source: https://pi.dev/docs/latest/rpc

Load a different session file. This action can be cancelled by a `session_before_switch` extension event handler.

```json
{"type": "switch_session", "sessionPath": "/path/to/session.jsonl"}
```

--------------------------------

### Enable Shell Aliases in Pi Settings

Source: https://pi.dev/docs/latest/shell-aliases

Add this JSON configuration to `~/.pi/agent/settings.json` to enable shell alias expansion. Adjust the path to your shell's configuration file (e.g., `~/.zshrc`, `~/.bashrc`) as needed.

```json
{
  "shellCommandPrefix": "shopt -s expand_aliases\neval \"$(grep \'^alias \' ~/.zshrc)\""
}
```

--------------------------------

### Configure Pi Keybindings for tmux with Shift+Enter

Source: https://pi.dev/docs/latest/terminal-setup

If you are using the legacy Ghostty mapping for Shift+Enter and want it to work in tmux, add 'ctrl+j' to your Pi 'newLine' keybinding in '~/.pi/agent/keybindings.json'.

```json
{
  "newLine": ["shift+enter", "ctrl+j"]
}
```

--------------------------------

### Google AI Studio Provider Configuration

Source: https://pi.dev/docs/latest/models

Add models from Google AI Studio, including custom Gemma models, by specifying the `baseUrl` for the `google-generative-ai` API type.

```json
{
  "providers": {
    "my-google": {
      "baseUrl": "https://generativelanguage.googleapis.com/v1beta",
      "api": "google-generative-ai",
      "apiKey": "GEMINI_API_KEY",
      "models": [
        {
          "id": "gemma-4-31b-it",
          "name": "Gemma 4 31B",
          "input": ["text", "image"],
          "contextWindow": 262144,
          "reasoning": true
        }
      ]
    }
  }
}
```

--------------------------------

### Create Selection Dialog with SelectList

Source: https://pi.dev/docs/latest/tui

Use `SelectList` for user option selection. It supports custom themes and provides callbacks for selection and cancellation. Ensure all necessary imports are included.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { DynamicBorder } from "@mariozechner/pi-coding-agent";
import { Container, type SelectItem, SelectList, Text } from "@mariozechner/pi-tui";

pi.registerCommand("pick", {
  handler: async (_args, ctx) => {
    const items: SelectItem[] = [
      { value: "opt1", label: "Option 1", description: "First option" },
      { value: "opt2", label: "Option 2", description: "Second option" },
      { value: "opt3", label: "Option 3" },  // description is optional
    ];

    const result = await ctx.ui.custom<string | null>((tui, theme, _kb, done) => {
      const container = new Container();

      // Top border
      container.addChild(new DynamicBorder((s: string) => theme.fg("accent", s)));

      // Title
      container.addChild(new Text(theme.fg("accent", theme.bold("Pick an Option")), 1, 0));

      // SelectList with theme
      const selectList = new SelectList(items, Math.min(items.length, 10), {
        selectedPrefix: (t) => theme.fg("accent", t),
        selectedText: (t) => theme.fg("accent", t),
        description: (t) => theme.fg("muted", t),
        scrollInfo: (t) => theme.fg("dim", t),
        noMatch: (t) => theme.fg("warning", t),
      });
      selectList.onSelect = (item) => done(item.value);
      selectList.onCancel = () => done(null);
      container.addChild(selectList);

      // Help text
      container.addChild(new Text(theme.fg("dim", "↑↓ navigate • enter select • esc cancel"), 1, 0));

      // Bottom border
      container.addChild(new DynamicBorder((s: string) => theme.fg("accent", s)));

      return {
        render: (w) => container.render(w),
        invalidate: () => container.invalidate(),
        handleInput: (data) => { selectList.handleInput(data); tui.requestRender(); },
      };
    });

    if (result) {
      ctx.ui.notify(`Selected: ${result}`, "info");
    }
  },
});

```

--------------------------------

### Enable Prompt Caching for Bedrock

Source: https://pi.dev/docs/latest/providers

Enable prompt caching for Bedrock models, especially for application inference profiles. Set AWS_BEDROCK_FORCE_CACHE=1 to enable cache points.

```bash
export AWS_BEDROCK_FORCE_CACHE=1
pi --provider amazon-bedrock --model arn:aws:bedrock:us-east-1:123456789012:application-inference-profile/abc123
```

--------------------------------

### Configure Forking and Rebranding

Source: https://pi.dev/docs/latest/development

Customize Pi's name, configuration directory, and binary field within the package.json file for your fork. This affects the CLI banner, config paths, and environment variable names.

```json
{
  "piConfig": {
    "name": "pi",
    "configDir": ".pi"
  }
}

```

--------------------------------

### Graceful Shutdown with ctx.shutdown()

Source: https://pi.dev/docs/latest/extensions

Initiate a graceful shutdown of pi, which defers until the agent is idle in interactive or RPC modes.

```javascript
pi.on("tool_call", (event, ctx) => {
  if (isFatal(event.input)) {
    ctx.shutdown();
  }
});
```

--------------------------------

### Using Event Bus with DefaultResourceLoader

Source: https://pi.dev/docs/latest/sdk

Shows how to integrate a shared `eventBus` with `DefaultResourceLoader` for inter-extension communication. This allows emitting and listening to events from outside the loader.

```typescript
import { createEventBus, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const eventBus = createEventBus();
const loader = new DefaultResourceLoader({
  eventBus,
});
await loader.reload();

eventBus.on("my-extension:status", (data) => console.log(data));

```

--------------------------------

### pi.registerCommand

Source: https://pi.dev/docs/latest/extensions

Register a command that can be invoked by users. If multiple extensions register the same command name, they will be suffixed with numeric identifiers.

```APIDOC
## pi.registerCommand(name, options)

### Description
Register a command.

### Parameters
- **name** (string) - Required - The name of the command.
- **options** (object) - Required - Configuration for the command.
  - **description** (string) - Required - A description of the command.
  - **handler** (function) - Required - The function to execute when the command is invoked.
  - **getArgumentCompletions** (function) - Optional - A function to provide auto-completion suggestions for command arguments.
```

--------------------------------

### Use Amazon Bedrock Provider

Source: https://pi.dev/docs/latest/providers

Invoke a model using the Amazon Bedrock provider. Supports ECS task roles and IRSA.

```bash
pi --provider amazon-bedrock --model us.anthropic.claude-sonnet-4-20250514-v1:0
```

--------------------------------

### session_before_tree / session_tree

Source: https://pi.dev/docs/latest/extensions

Fired on `/tree` navigation. Allows extensions to cancel or provide custom summaries for tree navigation.

```APIDOC
## session_before_tree / session_tree

### Description
Fired on `/tree` navigation. Allows extensions to cancel or provide custom summaries for tree navigation.

### `session_before_tree` Event Parameters
- **event**: Object
  - **preparation**: Object - Preparation details for tree navigation.
  - **signal**: Object - Abort signal for the operation.

### `session_before_tree` Context Parameters
- **ctx**: Object

### `session_before_tree` Return Value
- **{ cancel: true }**: To cancel the tree navigation.
- **{ summary: { summary: string, details: object } }**: To provide a custom summary for the tree navigation.

### `session_tree` Event Parameters
- **event**: Object
  - **newLeafId**: string - The ID of the new leaf node.
  - **oldLeafId**: string - The ID of the previous leaf node.
  - **summaryEntry**: Object - The entry containing the summary.
  - **fromExtension** (boolean) - Whether the summary was provided by an extension.

### `session_tree` Context Parameters
- **ctx**: Object

### Examples
```javascript
pi.on("session_before_tree", async (event, ctx) => {
  const { preparation, signal } = event;
  return { cancel: true };
  // OR provide custom summary:
  return { summary: { summary: "...", details: {} } };
});

pi.on("session_tree", async (event, ctx) => {
  // event.newLeafId, oldLeafId, summaryEntry, fromExtension
});
```
```

--------------------------------

### Customizing Working Indicators

Source: https://pi.dev/docs/latest/extensions

Configure custom working indicators with frames and intervals, or hide them entirely. Frames can include styling via `ctx.ui.theme.fg`.

```javascript
// Working indicator (shown during streaming)
ctx.ui.setWorkingIndicator({ frames: [ctx.ui.theme.fg("accent", "●")] });  // Static dot
ctx.ui.setWorkingIndicator({
  frames: [
    ctx.ui.theme.fg("dim", "·"),
    ctx.ui.theme.fg("muted", "•"),
    ctx.ui.theme.fg("accent", "●"),
    ctx.ui.theme.fg("muted", "•"),
  ],
  intervalMs: 120,
});
ctx.ui.setWorkingIndicator({ frames: [] });  // Hide indicator
ctx.ui.setWorkingIndicator();  // Restore default spinner

```

--------------------------------

### Configure Retry Settings in Pi

Source: https://pi.dev/docs/latest/settings

Enable agent-level retries for transient errors, set maximum retries, and configure base delay. Also includes provider-specific timeout and retry settings, with an option to cap server-requested delays.

```json
{
  "retry": {
    "enabled": true,
    "maxRetries": 3,
    "baseDelayMs": 2000,
    "provider": {
      "timeoutMs": 3600000,
      "maxRetries": 0,
      "maxRetryDelayMs": 60000
    }
  }
}
```

--------------------------------

### setTitle

Source: https://pi.dev/docs/latest/rpc

Set the terminal window/tab title. Fire-and-forget.

```APIDOC
## setTitle

Set the terminal window/tab title. Fire-and-forget.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-8",
  "method": "setTitle",
  "title": "pi - my project"
}
```
```

--------------------------------

### Create Agent Session with Overridden Settings

Source: https://pi.dev/docs/latest/sdk

Applies specific overrides to the default settings. Useful for temporary adjustments or testing specific configurations.

```typescript
import { createAgentSession, SettingsManager } from "@mariozechner/pi-coding-agent";

// With overrides
const settingsManager = SettingsManager.create();
settingsManager.applyOverrides({
  compaction: { enabled: false },
  retry: { enabled: true, maxRetries: 5 },
});
const { session } = await createAgentSession({ settingsManager });
```

--------------------------------

### AgentSession.navigateTree() Method Signature

Source: https://pi.dev/docs/latest/tree

Defines the signature for the `navigateTree` method, including its parameters and return type. Options allow for summarizing abandoned branches and custom instructions.

```typescript
async navigateTree(
  targetId: string,
  options?: {
    summarize?: boolean;
    customInstructions?: string;
    replaceInstructions?: boolean;
    label?: string;
  }
): Promise<{ editorText?: string; cancelled: boolean }>
```

--------------------------------

### Compaction process visualization

Source: https://pi.dev/docs/latest/compaction

Illustrates the state of messages before and after compaction, and what the LLM perceives. Compaction summarizes older messages while keeping recent ones, appending a new summary entry.

```plaintext
Before compaction:

  entry:  0     1     2     3      4     5     6      7      8     9
        ┌─────┬─────┬─────┬─────┬──────┬─────┬─────┬──────┬──────┬─────┐
        │ hdr │ usr │ ass │ tool │ usr │ ass │ tool │ tool │ ass │ tool│
        └─────┴─────┴─────┴──────┴─────┴─────┴──────┴──────┴─────┴─────┘
                └────────┬───────┘ └──────────────┬──────────────┘
               messagesToSummarize            kept messages
                                   ↑
                          firstKeptEntryId (entry 4)

After compaction (new entry appended):

  entry:  0     1     2     3      4     5     6      7      8     9     10
        ┌─────┬─────┬─────┬─────┬──────┬─────┬─────┬──────┬──────┬─────┬─────┐
        │ hdr │ usr │ ass │ tool │ usr │ ass │ tool │ tool │ ass │ tool│ cmp │
        └─────┴─────┴─────┴──────┴─────┴─────┴──────┴──────┴─────┴─────┴─────┘
               └──────────┬──────┘ └──────────────────────┬───────────────────┘
                 not sent to LLM                    sent to LLM
                                                         ↑
                                              starts from firstKeptEntryId

What the LLM sees:

  ┌────────┬─────────┬─────┬─────┬──────┬──────┬─────┬──────┐
  │ system │ summary │ usr │ ass │ tool │ tool │ ass │ tool │
  └────────┴─────────┴─────┴─────┴──────┴──────┴─────┴──────┘
       ↑         ↑      └─────────────────┬────────────────┘
    prompt   from cmp          messages from firstKeptEntryId

```

--------------------------------

### Interactive Mode with Pi SDK

Source: https://pi.dev/docs/latest/sdk

Use this mode for a full TUI interactive experience with editor, chat history, and built-in commands. It requires setting up the agent session runtime.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  InteractiveMode,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};
const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

const mode = new InteractiveMode(runtime, {
  migratedProviders: [],
  modelFallbackMessage: undefined,
  initialMessage: "Hello",
  initialImages: [],
  initialMessages: [],
});

await mode.run();

```

--------------------------------

### Configure Google Vertex AI

Source: https://pi.dev/docs/latest/providers

Configure Google Cloud project and location for Vertex AI. Uses Application Default Credentials, which can be set via `gcloud auth application-default login` or by setting GOOGLE_APPLICATION_CREDENTIALS.

```bash
gcloud auth application-default login
export GOOGLE_CLOUD_PROJECT=your-project
export GOOGLE_CLOUD_LOCATION=us-central1
```

--------------------------------

### Initialize DefaultResourceLoader

Source: https://pi.dev/docs/latest/sdk

Initializes the resource loader to discover extensions, skills, prompts, and themes. Requires specifying the current working directory and agent directory.

```typescript
import {
  DefaultResourceLoader,
  getAgentDir,
} from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  cwd,
  agentDir: getAgentDir(),
});
await loader.reload();

const extensions = loader.getExtensions();
const skills = loader.getSkills();
const prompts = loader.getPrompts();
const themes = loader.getThemes();
const contextFiles = loader.getAgentsFiles().agentsFiles;
```

--------------------------------

### Configure Amazon Bedrock Credentials

Source: https://pi.dev/docs/latest/providers

Set environment variables for Amazon Bedrock authentication. Options include using an AWS profile, IAM keys, or a bearer token.

```bash
# Option 1: AWS Profile
export AWS_PROFILE=your-profile

# Option 2: IAM Keys
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...

# Option 3: Bearer Token
export AWS_BEARER_TOKEN_BEDROCK=...

```

--------------------------------

### Use Shell Command for API Key

Source: https://pi.dev/docs/latest/providers

Specify an API key using a shell command, which will be executed and its stdout used. The result is cached for the process lifetime.

```json
{ "type": "api_key", "key": "!security find-generic-password -ws 'anthropic'" }
```

```json
{ "type": "api_key", "key": "!op read 'op://vault/item/credential'" }
```

--------------------------------

### Create Agent Session Runtime

Source: https://pi.dev/docs/latest/sdk

Use this factory to create a new agent session runtime. It recreates cwd-bound services and resolves session options.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({
      services,
      sessionManager,
      sessionStartEvent,
    })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

```

--------------------------------

### Container Components with Embedded Inputs

Source: https://pi.dev/docs/latest/tui

Guidance for container components to correctly propagate focus to child inputs for proper IME cursor positioning.

```APIDOC
### Container Components with Embedded Inputs

When a container component (dialog, selector, etc.) contains an `Input` or `Editor` child, the container must implement `Focusable` and propagate the focus state to the child. Otherwise, the hardware cursor won't be positioned correctly for IME input.

```typescript
import { Container, type Focusable, Input } from "@mariozechner/pi-tui";

class SearchDialog extends Container implements Focusable {
  private searchInput: Input;

  // Focusable implementation - propagate to child input for IME cursor positioning
  private _focused = false;
  get focused(): boolean {
    return this._focused;
  }
  set focused(value: boolean) {
    this._focused = value;
    this.searchInput.focused = value;
  }

  constructor() {
    super();
    this.searchInput = new Input();
    this.addChild(this.searchInput);
  }
}
```

Without this propagation, typing with an IME (Chinese, Japanese, Korean, etc.) will show the candidate window in the wrong position on screen.
```

--------------------------------

### Configure Provider Compatibility Settings

Source: https://pi.dev/docs/latest/custom-provider

Customize provider behavior for specific APIs using the `compat` object. This is useful for handling differences in role naming, token limits, or reasoning effort mapping.

```javascript
models: [{
  id: "custom-model",
  // ...
  compat: {
    supportsDeveloperRole: false,      // use "system" instead of "developer"
    supportsReasoningEffort: true,
    reasoningEffortMap: {
      minimal: "default",
      low: "default",
      medium: "default",
      high: "default",
      xhigh: "default"
    },
      maxTokensField: "max_tokens",      // instead of "max_completion_tokens"
      requiresToolResultName: true,      // tool results need name field
      thinkingFormat: "qwen",           // top-level enable_thinking: true
      cacheControlFormat: "anthropic"   // Anthropic-style cache_control markers
    }
  }]


```

--------------------------------

### Structured Summary Format

Source: https://pi.dev/docs/latest/compaction

The standardized format used for both compaction and branch summarization, including sections for goal, constraints, progress, decisions, next steps, critical context, and file tracking.

```markdown
## Goal
[What the user is trying to accomplish]

## Constraints & Preferences
- [Requirements mentioned by user]

## Progress
### Done
- [x] [Completed tasks]

### In Progress
- [ ] [Current work]

### Blocked
- [Issues, if any]

## Key Decisions
- **[Decision]**: [Rationale]

## Next Steps
1. [What should happen next]

## Critical Context
- [Data needed to continue]

<read-files>
path/to/file1.ts
path/to/file2.ts
</read-files>

<modified-files>
path/to/changed.ts
</modified-files>
```

--------------------------------

### Configure Session Directory

Source: https://pi.dev/docs/latest/settings

Set the directory where session files are stored. This can be an absolute or relative path, or use '~' for the home directory.

```json
{ "sessionDir": ".pi/sessions" }
```

--------------------------------

### Configure Local LLM OpenAI Compatibility

Source: https://pi.dev/docs/latest/models

Set provider-level compatibility settings for local LLM providers. This applies defaults to all models under the provider.

```json
{
  "providers": {
    "local-llm": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "compat": {
        "supportsUsageInStreaming": false,
        "maxTokensField": "max_tokens"
      },
      "models": [...] 
    }
  }
}
```

--------------------------------

### Configure Bedrock API Proxy

Source: https://pi.dev/docs/latest/providers

Configure environment variables for connecting to a Bedrock API proxy. Supports setting the endpoint URL, skipping authentication, and forcing HTTP/1.1.

```bash
# Set the URL for the Bedrock proxy (standard AWS SDK env var)
export AWS_ENDPOINT_URL_BEDROCK_RUNTIME=https://my.corp.proxy/bedrock

# Set if your proxy does not require authentication
export AWS_BEDROCK_SKIP_AUTH=1

# Set if your proxy only supports HTTP/1.1
export AWS_BEDROCK_FORCE_HTTP1=1
```

--------------------------------

### Prompt with Images

Source: https://pi.dev/docs/latest/sdk

Send a prompt that includes image content. Ensure the image data is correctly formatted.

```typescript
// With images
await session.prompt("What's in this image?", {
  images: [{ type: "image", source: { type: "base64", mediaType: "image/png", data: "..." } }]
});

```

--------------------------------

### pi.registerCommand(name, definition)

Source: https://pi.dev/docs/latest/extensions

Registers a command that can be invoked by the user or other parts of the system. The handler function receives arguments and the extension context.

```APIDOC
## pi.registerCommand(name, definition)

### Description
Registers a command that can be invoked by the user or other parts of the system.

### Parameters
- **name** (string) - The name of the command.
- **definition** (object) - An object containing the command's description and handler.
  - **description** (string) - A description of what the command does.
  - **handler** (function) - An async function that executes when the command is called. It receives `_args` (any) and `ctx` (ExtensionContext).
```

--------------------------------

### Steer Command

Source: https://pi.dev/docs/latest/rpc

Queue a steering message while the agent is running. This message is delivered after the current assistant turn finishes its tool calls, before the next LLM call. Skill commands and prompt templates are expanded. Extension commands are not allowed.

```APIDOC
## Steer Command

### Description
Queue a steering message while the agent is running. It is delivered after the current assistant turn finishes executing its tool calls, before the next LLM call. Skill commands and prompt templates are expanded. Extension commands are not allowed (use `prompt` instead).

### Method
`steer`

### Request Body
- **type** (string) - Required - Must be "steer".
- **message** (string) - Required - The steering message.
- **images** (array) - Optional - An array of image objects for image input.
  - **type** (string) - Required - Must be "image".
  - **data** (string) - Required - Base64-encoded image data.
  - **mimeType** (string) - Required - The MIME type of the image (e.g., "image/png").

### Request Example
```json
{"type": "steer", "message": "Stop and do this instead"}
```

With images:
```json
{"type": "steer", "message": "Look at this instead", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}
```

### Response
#### Success Response
- **type** (string) - Must be "response".
- **command** (string) - The command that was processed (e.g., "steer").
- **success** (boolean) - `true` if the steering message was accepted; `false` otherwise.

#### Response Example
```json
{"type": "response", "command": "steer", "success": true}
```
```

--------------------------------

### Manual Dismissal with AbortSignal

Source: https://pi.dev/docs/latest/extensions

Demonstrates how to use AbortSignal for manual dismissal of dialogs, allowing differentiation between user cancellation and timeouts.

```APIDOC
## Manual Dismissal with AbortSignal

For more control (e.g., to distinguish timeout from user cancel), use `AbortSignal`:

```javascript
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 5000);

const confirmed = await ctx.ui.confirm(
  "Timed Confirmation",
  "This dialog will auto-cancel in 5 seconds. Confirm?",
  { signal: controller.signal }
);

clearTimeout(timeoutId);

if (confirmed) {
  // User confirmed
} else if (controller.signal.aborted) {
  // Dialog timed out
} else {
  // User cancelled (pressed Escape or selected "No")
}
```
```

--------------------------------

### Unsafe Session Handoff Pattern

Source: https://pi.dev/docs/latest/extensions

Illustrates an unsafe pattern for session handoff. Avoid reusing old session-bound objects like `ctx.sessionManager` or `pi` after replacement, as they become stale and will throw errors.

```javascript
pi.registerCommand("handoff", {
  handler: async (_args, ctx) => {
    const oldSessionManager = ctx.sessionManager;
    await ctx.newSession({
      withSession: async (_ctx) => {
        // stale old objects: do not do this
        oldSessionManager.getSessionFile();
        pi.sendUserMessage("wrong");
      },
    });
  },
});
```

--------------------------------

### Handle session_shutdown

Source: https://pi.dev/docs/latest/extensions

Perform cleanup or save state before an extension runtime is torn down.

```javascript
pi.on("session_shutdown", async (event, ctx) => {
  // event.reason - "quit" | "reload" | "new" | "resume" | "fork"
  // event.targetSessionFile - destination session for session replacement flows
  // Cleanup, save state, etc.
});
```

--------------------------------

### Package Resource Filtering

Source: https://pi.dev/docs/latest/packages

Filter which resources (extensions, skills, prompts, themes) a package loads using an object configuration within the 'packages' setting. Use glob patterns and exclusion/inclusion prefixes like '!', '+', and '-' for precise control.

```json
{
  "packages": [
    "npm:simple-pkg",
    {
      "source": "npm:my-package",
      "extensions": ["extensions/*.ts", "!extensions/legacy.ts"],
      "skills": [],
      "prompts": ["prompts/review.md"],
      "themes": ["+themes/legacy.json"]
    }
  ]
}

```

--------------------------------

### Termux Environment Configuration for Pi Agent

Source: https://pi.dev/docs/latest/termux

This configuration file helps the Pi agent understand the Termux environment on Android, including OS details, file paths, and how to interact with device features.

```markdown
# Agent Environment: Termux on Android

## Location
- **OS**: Android (Termux terminal emulator)
- **Home**: `/data/data/com.termux/files/home`
- **Prefix**: `/data/data/com.termux/files/usr`
- **Shared storage**: `/storage/emulated/0` (Downloads, Documents, etc.)

## Opening URLs
```bash
termux-open-url "https://example.com"

```

## Opening Files
```
termux-open file.pdf          # Opens with default app
termux-open -c image.jpg      # Choose app

```

## Clipboard
```
termux-clipboard-set "text"   # Copy
termux-clipboard-get          # Paste

```

## Notifications
```
termux-notification -t "Title" -c "Content"

```

## Device Info
```
termux-battery-status         # Battery info
termux-wifi-connectioninfo    # WiFi info
termux-telephony-deviceinfo   # Device info

```

## Sharing
```
termux-share -a send file.txt # Share file

```

## Other Useful Commands
```
termux-toast "message"        # Quick toast popup
termux-vibrate                # Vibrate device
termux-tts-speak "hello"      # Text to speech
termux-camera-photo out.jpg   # Take photo

```

## Notes
  * Termux:API app must be installed for `termux-*` commands
  * Use `pkg install termux-api` for the command-line tools
  * Storage permission needed for `/storage/emulated/0` access

```

--------------------------------

### State Management with Tool Results

Source: https://pi.dev/docs/latest/extensions

Extensions with state should store it in tool result `details` for proper branching support. This allows state to be reconstructed from session history.

```APIDOC
## State Management

Extensions with state should store it in tool result `details` for proper branching support:

```javascript
export default function (pi: ExtensionAPI) {
  let items: string[] = [];

  // Reconstruct state from session
  pi.on("session_start", async (_event, ctx) => {
    items = [];
    for (const entry of ctx.sessionManager.getBranch()) {
      if (entry.type === "message" && entry.message.role === "toolResult") {
        if (entry.message.toolName === "my_tool") {
          items = entry.message.details?.items ?? [];
        }
      }
    }
  });

  pi.registerTool({
    name: "my_tool",
    // ...
    async execute(toolCallId, params, signal, onUpdate, ctx) {
      items.push("new item");
      return {
        content: [{ type: "text", text: "Added" }],
        details: { items: [...items] },  // Store for reconstruction
      };
    },
  });
}
```
```

--------------------------------

### Create Agent Session with Custom Options

Source: https://pi.dev/docs/latest/sdk

Creates an agent session, overriding default options such as the model, tools, and session manager.

```typescript
import { createAgentSession } from "@mariozechner/pi-coding-agent";

// Custom: override specific options
const { session } = await createAgentSession({
  model: myModel,
  tools: [readTool, bashTool],
  sessionManager: SessionManager.inMemory(),
});

```

--------------------------------

### Configure Enabled Models for Cycling

Source: https://pi.dev/docs/latest/settings

Define patterns for models that will be included in Ctrl+P cycling. Supports glob patterns.

```json
{
  "enabledModels": ["claude-*", "gpt-4o", "gemini-2*"]
}
```

--------------------------------

### BranchSummaryEntry

Source: https://pi.dev/docs/latest/session

Created when switching branches, this entry summarizes the context of the abandoned branch up to the common ancestor. It includes IDs, timestamp, and a summary string. Optional 'details' and 'fromHook' fields can provide further context.

```json
{"type":"branch_summary","id":"g7h8i9j0","parentId":"a1b2c3d4","timestamp":"2024-12-03T14:15:00.000Z","fromId":"f6g7h8i9","summary":"Branch explored approach A..."}
```

--------------------------------

### Configure Custom Shell Path in settings.json

Source: https://pi.dev/docs/latest/windows

Specify a custom bash shell path in `~/.pi/agent/settings.json` to ensure Pi uses your preferred shell.

```json
{
  "shellPath": "C:\\cygwin64\\bin\\bash.exe"
}

```

--------------------------------

### Implement File Mutation Queue for Custom Tools

Source: https://pi.dev/docs/latest/extensions

Use `withFileMutationQueue` to ensure tools that mutate files participate in a per-file queue, preventing race conditions with other tools. Pass the absolute target file path to the function. The queue includes the entire read-modify-write logic.

```typescript
import { withFileMutationQueue } from "@mariozechner/pi-coding-agent";
import { mkdir, readFile, writeFile } from "node:fs/promises";
import { dirname, resolve } from "node:path";

async execute(_toolCallId, params, _signal, _onUpdate, ctx) {
  const absolutePath = resolve(ctx.cwd, params.path);

  return withFileMutationQueue(absolutePath, async () => {
    await mkdir(dirname(absolutePath), { recursive: true });
    const current = await readFile(absolutePath, "utf8");
    const next = current.replace(params.oldText, params.newText);
    await writeFile(absolutePath, next, "utf8");

    return {
      content: [{ type: "text", text: `Updated ${params.path}` }],
      details: {},
    };
  });
}

```

--------------------------------

### Fork Session from Specific Entry

Source: https://pi.dev/docs/latest/extensions

Creates a new session by forking from a specified entry ID. The `withSession` callback runs in the new session context. Options control positioning and editor text restoration.

```javascript
const result = await ctx.fork("entry-id-123", {
  withSession: async (ctx) => {
    // Use only the replacement-session ctx here.
    ctx.ui.notify("Now in the forked session", "info");
  },
});
if (result.cancelled) {
  // An extension cancelled the fork
}

const cloneResult = await ctx.fork("entry-id-456", { position: "at" });
if (cloneResult.cancelled) {
  // An extension cancelled the clone
}

```

--------------------------------

### Prompt with Streaming Behavior

Source: https://pi.dev/docs/latest/sdk

Specify streaming behavior for prompts. Use 'steer' to interrupt the current turn or 'followUp' to queue after the current turn.

```typescript
// During streaming: must specify how to queue the message
await session.prompt("Stop and do this instead", { streamingBehavior: "steer" });
await session.prompt("After you're done, also check X", { streamingBehavior: "followUp" });

```

--------------------------------

### Register Command to Trigger Runtime Reload

Source: https://pi.dev/docs/latest/extensions

Register a command that calls `ctx.reload()` to restart the extension runtime. This emits `session_shutdown` and `session_start` events. Code after `ctx.reload()` runs from the pre-reload version and should not assume old state is valid. For predictable behavior, treat reload as terminal for the handler.

```typescript
pi.registerCommand("reload-runtime", {
  description: "Reload extensions, skills, prompts, and themes",
  handler: async (_args, ctx) => {
    await ctx.reload();
    return;
  },
});
```

--------------------------------

### pi.registerProvider(name, config)

Source: https://pi.dev/docs/latest/extensions

Dynamically registers or overrides a model provider. Calls made during the extension factory function are queued and applied on runner initialization. Calls made after initialization take effect immediately.

```APIDOC
## pi.registerProvider(name, config)

### Description
Register or override a model provider dynamically. Useful for proxies, custom endpoints, or team-wide model configurations.
Calls made during the extension factory function are queued and applied once the runner initialises. Calls made after that — for example from a command handler following a user setup flow — take effect immediately without requiring a `/reload`.
If you need to discover models from a remote endpoint, prefer an async extension factory over deferring the fetch to `session_start`. pi waits for the factory before startup continues, so the registered models are available immediately, including to `pi --list-models`.

### Parameters
* `name` (string) - The name of the provider to register or override.
* `config` (object) - Configuration options for the provider.
  * `baseUrl` (string) - API endpoint URL. Required when defining models.
  * `apiKey` (string) - API key or environment variable name. Required when defining models (unless `oauth` provided).
  * `api` (string) - API type: e.g., `"anthropic-messages"`, `"openai-completions"`, `"openai-responses"`.
  * `headers` (object) - Custom headers to include in requests.
  * `authHeader` (boolean) - If true, adds `Authorization: Bearer` header automatically.
  * `models` (array) - Array of model definitions. If provided, replaces all existing models for this provider.
  * `oauth` (object) - OAuth provider config for `/login` support. When provided, the provider appears in the login menu.
    * `name` (string) - Display name for the OAuth provider.
    * `login` (function) - Custom OAuth login flow.
    * `refreshToken` (function) - Logic to refresh OAuth tokens.
    * `getApiKey` (function) - Function to retrieve the API key from credentials.
  * `streamSimple` (function) - Custom streaming implementation for non-standard APIs.

### Request Example
```javascript
// Register a new provider with custom models
pi.registerProvider("my-proxy", {
  baseUrl: "https://proxy.example.com",
  apiKey: "PROXY_API_KEY",  // env var name or literal
  api: "anthropic-messages",
  models: [
    {
      id: "claude-sonnet-4-20250514",
      name: "Claude 4 Sonnet (proxy)",
      reasoning: false,
      input: ["text", "image"],
      cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
      contextWindow: 200000,
      maxTokens: 16384
    }
  ]
});

// Override baseUrl for an existing provider (keeps all models)
pi.registerProvider("anthropic", {
  baseUrl: "https://proxy.example.com"
});

// Register provider with OAuth support for /login
pi.registerProvider("corporate-ai", {
  baseUrl: "https://ai.corp.com",
  api: "openai-responses",
  models: [...],
  oauth: {
    name: "Corporate AI (SSO)",
    async login(callbacks) {
      // Custom OAuth flow
      callbacks.onAuth({ url: "https://sso.corp.com/..." });
      const code = await callbacks.onPrompt({ message: "Enter code:" });
      return { refresh: code, access: code, expires: Date.now() + 3600000 };
    },
    async refreshToken(credentials) {
      // Refresh logic
      return credentials;
    },
    getApiKey(credentials) {
      return credentials.access;
    }
  }
});
```
```

--------------------------------

### Implement Custom Editor (Vim Mode)

Source: https://pi.dev/docs/latest/tui

Replace the main input editor with a custom implementation by extending `CustomEditor`. This allows for custom keybindings and input handling. Remember to call `super.handleInput(data)` for unhandled keys. Use `undefined` to restore the default editor.

```typescript
import { CustomEditor, type ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { matchesKey, truncateToWidth } from "@mariozechner/pi-tui";

type Mode = "normal" | "insert";

class VimEditor extends CustomEditor {
  private mode: Mode = "insert";

  handleInput(data: string): void {
    // Escape: switch to normal mode, or pass through for app handling
    if (matchesKey(data, "escape")) {
      if (this.mode === "insert") {
        this.mode = "normal";
        return;
      }
      // In normal mode, escape aborts agent (handled by CustomEditor)
      super.handleInput(data);
      return;
    }

    // Insert mode: pass everything to CustomEditor
    if (this.mode === "insert") {
      super.handleInput(data);
      return;
    }

    // Normal mode: vim-style navigation
    switch (data) {
      case "i": this.mode = "insert"; return;
      case "h": super.handleInput("\x1b[D"); return; // Left
      case "j": super.handleInput("\x1b[B"); return; // Down
      case "k": super.handleInput("\x1b[A"); return; // Up
      case "l": super.handleInput("\x1b[C"); return; // Right
    }
    // Pass unhandled keys to super (ctrl+c, etc.), but filter printable chars
    if (data.length === 1 && data.charCodeAt(0) >= 32) return;
    super.handleInput(data);
  }

  render(width: number): string[] {
    const lines = super.render(width);
    // Add mode indicator to bottom border (use truncateToWidth for ANSI-safe truncation)
    if (lines.length > 0) {
      const label = this.mode === "normal" ? " NORMAL " : " INSERT ";
      const lastLine = lines[lines.length - 1]!;
      // Pass "" as ellipsis to avoid adding "..." when truncating
      lines[lines.length - 1] = truncateToWidth(lastLine, width - label.length, "") + label;
    }
    return lines;
  }
}

export default function (pi: ExtensionAPI) {
  pi.on("session_start", (_event, ctx) => {
    // Factory receives theme and keybindings from the app
    ctx.ui.setEditorComponent((tui, theme, keybindings) =>
      new VimEditor(theme, keybindings)
    );
  });
}
```

--------------------------------

### Configure Azure OpenAI Credentials

Source: https://pi.dev/docs/latest/providers

Set environment variables for Azure OpenAI, including the API key, base URL, and optional resource name and API version. A deployment name map can also be specified.

```bash
export AZURE_OPENAI_API_KEY=...
export AZURE_OPENAI_BASE_URL=https://your-resource.openai.azure.com
# also supported: https://your-resource.cognitiveservices.azure.com
# root endpoints are auto-normalized to /openai/v1
# or use resource name instead of base URL
export AZURE_OPENAI_RESOURCE_NAME=your-resource

# Optional
export AZURE_OPENAI_API_VERSION=2024-02-01
export AZURE_OPENAI_DEPLOYMENT_NAME_MAP=gpt-4=my-gpt4,gpt-4o=my-gpt4o

```

--------------------------------

### Set follow-up message mode

Source: https://pi.dev/docs/latest/rpc

Configures the delivery of follow-up messages. 'all' delivers them when the agent finishes, and 'one-at-a-time' delivers one per agent completion.

```json
{"type": "set_follow_up_mode", "mode": "one-at-a-time"}
```

--------------------------------

### Using Custom TUI Components in Custom Tools

Source: https://pi.dev/docs/latest/tui

Shows how to integrate a custom TUI component within a Pi custom tool via `pi.ui.custom()`. The component can be managed using the returned handle.

```typescript
async execute(toolCallId, params, onUpdate, ctx, signal) {
  const handle = pi.ui.custom(myComponent);
  // ...
  handle.close();
}

```

--------------------------------

### HTML Export Theme Configuration

Source: https://pi.dev/docs/latest/themes

Configure colors for HTML export. If omitted, colors are derived from userMessageBg.

```json
{
  "export": {
    "pageBg": "#18181e",
    "cardBg": "#1e1e24",
    "infoBg": "#3c3728"
  }
}
```

--------------------------------

### Extension UI Request: Editor

Source: https://pi.dev/docs/latest/rpc

A request to open a multi-line text editor, potentially with pre-filled content. This is a dialog method that expects a response.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-4",
  "method": "editor",
  "title": "Edit some text",
  "prefill": "Line 1\nLine 2\nLine 3"
}
```

--------------------------------

### Focusable Interface

Source: https://pi.dev/docs/latest/tui

Enables components to support IME (Input Method Editor) by managing focus and cursor positioning.

```APIDOC
## Focusable Interface (IME Support)

Components that display a text cursor and need IME (Input Method Editor) support should implement the `Focusable` interface:

```typescript
import { CURSOR_MARKER, type Component, type Focusable } from "@mariozechner/pi-tui";

class MyInput implements Component, Focusable {
  focused: boolean = false;  // Set by TUI when focus changes
  
  render(width: number): string[] {
    const marker = this.focused ? CURSOR_MARKER : "";
    // Emit marker right before the fake cursor
    return [`> ${beforeCursor}${marker}\x1b[7m${atCursor}\x1b[27m${afterCursor}`];
  }
}
```

When a `Focusable` component has focus, TUI:
  1. Sets `focused = true` on the component
  2. Scans rendered output for `CURSOR_MARKER` (a zero-width APC escape sequence)
  3. Positions the hardware terminal cursor at that location
  4. Shows the hardware cursor

This enables IME candidate windows to appear at the correct position for CJK input methods. The `Editor` and `Input` built-in components already implement this interface.
```

--------------------------------

### Configure Overlay Size and Position

Source: https://pi.dev/docs/latest/tui

Customize overlay appearance using overlayOptions for width, height, positioning, and margins. The 'visible' option allows for responsive behavior based on terminal dimensions.

```typescript
const result = await ctx.ui.custom<string | null>(
  (tui, theme, keybindings, done) => new SidePanel({ onClose: done }),
  {
    overlay: true,
    overlayOptions: {
      // Size: number or percentage string
      width: "50%",          // 50% of terminal width
      minWidth: 40,          // minimum 40 columns
      maxHeight: "80%",      // max 80% of terminal height

      // Position: anchor-based (default: "center")
      anchor: "right-center", // 9 positions: center, top-left, top-center, etc.
      offsetX: -2,            // offset from anchor
      offsetY: 0,

      // Or percentage/absolute positioning
      row: "25%",            // 25% from top
      col: 10,               // column 10

      // Margins
      margin: 2,             // all sides, or { top, right, bottom, left }

      // Responsive: hide on narrow terminals
      visible: (termWidth, termHeight) => termWidth >= 80,
    },
    // Get handle for programmatic visibility control
    onHandle: (handle) => {
      // handle.setHidden(true/false) - toggle visibility
      // handle.hide() - permanently remove
    },
  }
);

```

--------------------------------

### Configure Custom Proxy Provider with Headers

Source: https://pi.dev/docs/latest/models

Define a custom proxy provider with specific headers, including API keys and secrets. This is useful for routing requests through a proxy that requires custom authentication.

```json
{
  "providers": {
    "custom-proxy": {
      "baseUrl": "https://proxy.example.com/v1",
      "apiKey": "MY_API_KEY",
      "api": "anthropic-messages",
      "headers": {
        "x-portkey-api-key": "PORTKEY_API_KEY",
        "x-secret": "!op read 'op://vault/item/secret'"
      },
      "models": [...] 
    }
  }
}

```

--------------------------------

### Timed Dialogs with Countdown

Source: https://pi.dev/docs/latest/extensions

Demonstrates how to use the `timeout` option for dialogs, which auto-dismisses with a live countdown display. Return values on timeout are `undefined` for `select` and `input`, and `false` for `confirm`.

```javascript
// Dialog shows "Title (5s)" → "Title (4s)" → ... → auto-dismisses at 0
const confirmed = await ctx.ui.confirm(
  "Timed Confirmation",
  "This dialog will auto-cancel in 5 seconds. Confirm?",
  { timeout: 5000 }
);

if (confirmed) {
  // User confirmed
} else {
  // User cancelled or timed out
}
```

--------------------------------

### Basic Prompt

Source: https://pi.dev/docs/latest/sdk

Send a simple text prompt to the session when not streaming.

```typescript
// Basic prompt (when not streaming)
await session.prompt("What files are here?");

```

--------------------------------

### Overriding Built-in Tools

Source: https://pi.dev/docs/latest/extensions

Explains how extensions can replace default tools like 'read', 'bash', or 'edit' by registering a tool with the same name.

```APIDOC
## Overriding Built-in Tools

### Description
Extensions can override default tools provided by the pi.ai framework. To do this, simply register a new tool with the same name as a built-in tool (e.g., `read`, `bash`, `edit`, `write`, `grep`, `find`, `ls`).

### Behavior
When a tool with a name that already exists is registered, the new tool definition replaces the original one. The interactive mode will display a warning when a built-in tool is overridden.
```

--------------------------------

### Export Session to HTML

Source: https://pi.dev/docs/latest/rpc

Export the current session to an HTML file. An optional output path can be specified.

```json
{"type": "export_html"}
```

```json
{"type": "export_html", "outputPath": "/tmp/session.html"}
```

--------------------------------

### Interactive RPC Client with Node.js

Source: https://pi.dev/docs/latest/rpc

This Node.js script spawns a child process for an RPC agent, attaches a reader for JSON lines output, and sends prompts. It handles message updates and provides a way to abort the process.

```javascript
const { spawn } = require("child_process");
const { StringDecoder } = require("string_decoder");

const agent = spawn("pi", ["--mode", "rpc", "--no-session"]);

function attachJsonlReader(stream, onLine) {
    const decoder = new StringDecoder("utf8");
    let buffer = "";

    stream.on("data", (chunk) => {
        buffer += typeof chunk === "string" ? chunk : decoder.write(chunk);

        while (true) {
            const newlineIndex = buffer.indexOf("\n");
            if (newlineIndex === -1) break;

            let line = buffer.slice(0, newlineIndex);
            buffer = buffer.slice(newlineIndex + 1);
            if (line.endsWith("\r")) line = line.slice(0, -1);
            onLine(line);
        }
    });

    stream.on("end", () => {
        buffer += decoder.end();
        if (buffer.length > 0) {
            onLine(buffer.endsWith("\r") ? buffer.slice(0, -1) : buffer);
        }
    });
}

attachJsonlReader(agent.stdout, (line) => {
    const event = JSON.parse(line);

    if (event.type === "message_update") {
        const { assistantMessageEvent } = event;
        if (assistantMessageEvent.type === "text_delta") {
            process.stdout.write(assistantMessageEvent.delta);
        }
    }
});

// Send prompt
agent.stdin.write(JSON.stringify({ type: "prompt", message: "Hello" }) + "\n");

// Abort on Ctrl+C
process.on("SIGINT", () => {
    agent.stdin.write(JSON.stringify({ type: "abort" }) + "\n");
});

```

--------------------------------

### input

Source: https://pi.dev/docs/latest/rpc

Prompt the user for free-form text.

```APIDOC
## input

Prompt the user for free-form text.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-3",
  "method": "input",
  "title": "Enter a value",
  "placeholder": "type something..."
}
```

Expected response: `extension_ui_response` with `value` (the entered text) or `cancelled: true`.
```

--------------------------------

### Response for new session command

Source: https://pi.dev/docs/latest/rpc

Indicates the success or cancellation status of a `new_session` command.

```json
{"type": "response", "command": "new_session", "success": true, "data": {"cancelled": false}}
```

```json
{"type": "response", "command": "new_session", "success": true, "data": {"cancelled": true}}
```

--------------------------------

### Bundled and Peer Dependencies

Source: https://pi.dev/docs/latest/packages

Configure 'dependencies', 'bundledDependencies', and 'peerDependencies' in package.json for managing third-party and core pi packages. Bundled dependencies are included in the tarball, while peer dependencies are expected to be provided by the pi environment.

```json
{
  "dependencies": {
    "shitty-extensions": "^1.0.1"
  },
  "bundledDependencies": ["shitty-extensions"],
  "pi": {
    "extensions": ["extensions", "node_modules/shitty-extensions/extensions"],
    "skills": ["skills", "node_modules/shitty-extensions/skills"]
  }
}

```

--------------------------------

### Configure Windows Terminal for Pi

Source: https://pi.dev/docs/latest/terminal-setup

Add these actions to your Windows Terminal 'settings.json' to forward modified Enter key chords that Pi uses. This ensures Shift+Enter inserts a new line and Alt+Enter is not intercepted by fullscreen.

```json
{
  "actions": [
    {
      "command": { "action": "sendInput", "input": "\u001b[13;2u" },
      "keys": "shift+enter"
    },
    {
      "command": { "action": "sendInput", "input": "\u001b[13;3u" },
      "keys": "alt+enter"
    }
  ]
}
```

--------------------------------

### Extension Package JSON Configuration

Source: https://pi.dev/docs/latest/extensions

This package.json configuration is used for extensions that require npm packages. It declares dependencies and specifies the entry point for the extension.

```json
{
  "name": "my-extension",
  "dependencies": {
    "zod": "^3.0.0",
    "chalk": "^5.0.0"
  },
  "pi": {
    "extensions": ["./src/index.ts"]
  }
}
```

--------------------------------

### Register and Override Providers

Source: https://pi.dev/docs/latest/custom-provider

Use `pi.registerProvider()` to override an existing provider's base URL or register a new provider with custom models and API configurations.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  // Override baseUrl for existing provider
  pi.registerProvider("anthropic", {
    baseUrl: "https://proxy.example.com"
  });

  // Register new provider with models
  pi.registerProvider("my-provider", {
    baseUrl: "https://api.example.com",
    apiKey: "MY_API_KEY",
    api: "openai-completions",
    models: [
      {
        id: "my-model",
        name: "My Model",
        reasoning: false,
        input: ["text", "image"],
        cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
        contextWindow: 128000,
        maxTokens: 4096
      }
    ]
  });
}
```

--------------------------------

### Send a response command

Source: https://pi.dev/docs/latest/rpc

This is a standard response command, often used to acknowledge the successful completion of another command.

```json
{"type": "response", "command": "follow_up", "success": true}
```

--------------------------------

### Import TUI Built-in Components

Source: https://pi.dev/docs/latest/tui

Import essential TUI components like Text, Box, Container, Spacer, and Markdown from the '@mariozechner/pi-tui' package.

```typescript
import { Text, Box, Container, Spacer, Markdown } from "@mariozechner/pi-tui";

```

--------------------------------

### Using Custom TUI Components in Extensions

Source: https://pi.dev/docs/latest/tui

Demonstrates how to use a custom TUI component within a Pi extension using `ctx.ui.custom()`. The returned handle allows for re-rendering or closing the component.

```typescript
pi.on("session_start", async (_event, ctx) => {
  const handle = ctx.ui.custom(myComponent);
  // handle.requestRender() - trigger re-render
  // handle.close() - restore normal UI
});

```

--------------------------------

### SessionHeader - With Parent

Source: https://pi.dev/docs/latest/session

Represents session metadata for sessions created from a parent session. Includes all fields from the basic SessionHeader plus the parentSession identifier.

```json
{"type":"session","version":3,"id":"uuid","timestamp":"2024-12-03T14:00:00.000Z","cwd":"/path/to/project","parentSession":"/path/to/original/session.jsonl"}
```

--------------------------------

### Run RPC Mode with Pi SDK

Source: https://pi.dev/docs/latest/sdk

Utilize JSON-RPC mode for seamless integration with subprocesses. This is ideal for inter-process communication.

```typescript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  runRpcMode,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({ services, sessionManager, sessionStartEvent })),
    services,
    diagnostics: services.diagnostics,
  };
};
const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

await runRpcMode(runtime);


```

--------------------------------

### API Key Resolution via Literal Value

Source: https://pi.dev/docs/latest/models

Illustrates using a literal string value for the API key. This is suitable for keys that are not sensitive or are hardcoded for specific testing scenarios.

```json
"apiKey": "sk-..."
```

--------------------------------

### Model Select Event

Source: https://pi.dev/docs/latest/extensions

Fired when the model changes via `/model` command, model cycling, or session restore. Useful for updating UI or performing model-specific initialization.

```APIDOC
#### model_select

Fired when the model changes via `/model` command, model cycling (`Ctrl+P`), or session restore.
```javascript
pi.on("model_select", async (event, ctx) => {
  // event.model - newly selected model
  // event.previousModel - previous model (undefined if first selection)
  // event.source - "set" | "cycle" | "restore"

  const prev = event.previousModel
    ? `${event.previousModel.provider}/${event.previousModel.id}`
    : "none";
  const next = `${event.model.provider}/${event.model.id}`;

  ctx.ui.notify(`Model changed (${event.source}): ${prev} -> ${next}`, "info");
});

```

Use this to update UI elements (status bars, footers) or perform model-specific initialization when the active model changes.
```

--------------------------------

### State Management with Tool Results

Source: https://pi.dev/docs/latest/extensions

Store extension state in tool result `details` for proper branching support. The state is reconstructed from session data during `session_start`.

```typescript
export default function (pi: ExtensionAPI) {
  let items: string[] = [];

  // Reconstruct state from session
  pi.on("session_start", async (_event, ctx) => {
    items = [];
    for (const entry of ctx.sessionManager.getBranch()) {
      if (entry.type === "message" && entry.message.role === "toolResult") {
        if (entry.message.toolName === "my_tool") {
          items = entry.message.details?.items ?? [];
        }
      }
    }
  });

  pi.registerTool({
    name: "my_tool",
    // ...
    async execute(toolCallId, params, signal, onUpdate, ctx) {
      items.push("new item");
      return {
        content: [{ type: "text", text: "Added" }],
        details: { items: [...items] },  // Store for reconstruction
      };
    },
  });
}
```

--------------------------------

### pi.events

Source: https://pi.dev/docs/latest/extensions

Provides an event bus for communication between different extensions.

```APIDOC
## pi.events

### Description
Shared event bus for communication between extensions:

### Usage
```javascript
pi.events.on("my:event", (data) => { ... });
pi.events.emit("my:event", { ... });
```

### Methods
- **on(eventName, listener)**: Registers a listener function for a specific event.
  - **eventName** (string) - The name of the event to listen for.
  - **listener** (function) - The callback function to execute when the event is emitted.
- **emit(eventName, data)**: Emits an event with optional data.
  - **eventName** (string) - The name of the event to emit.
  - **data** (any) - The data to pass along with the event.
```

--------------------------------

### Updating Usage and Calculating Cost

Source: https://pi.dev/docs/latest/custom-provider

Shows how to update token usage from an API response and calculate the total cost. Ensure `calculateCost` is defined and accessible.

```javascript
output.usage.input = response.usage.input_tokens;
output.usage.output = response.usage.output_tokens;
output.usage.cacheRead = response.usage.cache_read_tokens ?? 0;
output.usage.cacheWrite = response.usage.cache_write_tokens ?? 0;
output.usage.totalTokens = output.usage.input + output.usage.output +
                           output.usage.cacheRead + output.usage.cacheWrite;
calculateCost(model, output.usage);

```

--------------------------------

### Create and Update Text Component

Source: https://pi.dev/docs/latest/tui

Instantiate a Text component for multi-line text with word wrapping. Padding and an optional background function can be provided. The text content can be updated using setText.

```typescript
const text = new Text(
  "Hello World",    // content
  1,                // paddingX (default: 1)
  1,                // paddingY (default: 1)
  (s) => bgGray(s)  // optional background function
);
text.setText("Updated");

```

--------------------------------

### pi.registerFlag(name, options)

Source: https://pi.dev/docs/latest/extensions

Registers a command-line interface (CLI) flag with a name, description, type, and default value.

```APIDOC
## pi.registerFlag(name, options)

### Description
Register a CLI flag.

### Usage
```javascript
pi.registerFlag("plan", {
  description: "Start in plan mode",
  type: "boolean",
  default: false,
});

// Check value
if (pi.getFlag("plan")) {
  // Plan mode enabled
}
```

### Parameters
- **name** (string) - The name of the flag.
- **options** (object) - Configuration for the flag.
  - **description** (string) - A description of the flag's purpose.
  - **type** (string) - The data type of the flag (e.g., "boolean", "string", "number").
  - **default** (any) - The default value of the flag.
```

--------------------------------

### pi.registerTool(definition)

Source: https://pi.dev/docs/latest/extensions

Register a custom tool callable by the LLM. Tools can be registered during extension load or after startup. Newly registered tools are refreshed immediately and available without a reload.

```APIDOC
## pi.registerTool(definition)

### Description
Register a custom tool callable by the LLM. See Custom Tools for full details.
`pi.registerTool()` works both during extension load and after startup. You can call it inside `session_start`, command handlers, or other event handlers. New tools are refreshed immediately in the same session, so they appear in `pi.getAllTools()` and are callable by the LLM without `/reload`.

### Parameters
- **definition** (object) - The definition of the tool.
  - **name** (string) - The unique name of the tool.
  - **label** (string) - A user-friendly label for the tool.
  - **description** (string) - A description of what the tool does.
  - **promptSnippet** (string, optional) - A short snippet for listing the tool.
  - **promptGuidelines** (array of strings, optional) - Guidelines for using the tool.
  - **parameters** (object) - A TypeBox object defining the tool's parameters.
  - **prepareArguments** (function, optional) - A function to prepare arguments before schema validation.
  - **execute** (function) - An async function that executes the tool's logic. It receives `toolCallId`, `params`, `signal`, `onUpdate` (optional), and `ctx`.
  - **renderCall** (function, optional) - Custom rendering for the tool call.
  - **renderResult** (function, optional) - Custom rendering for the tool result.
```

--------------------------------

### Add Custom Autocomplete Provider

Source: https://pi.dev/docs/latest/extensions

Register a custom autocomplete provider to add extension-specific syntax suggestions. Delegate to the current provider if the syntax does not match.

```typescript
pi.on("session_start", (_event, ctx) => {
  ctx.ui.addAutocompleteProvider((current) => ({
    async getSuggestions(lines, cursorLine, cursorCol, options) {
      const line = lines[cursorLine] ?? "";
      const beforeCursor = line.slice(0, cursorCol);
      const match = beforeCursor.match(/(?:^|[ \t])#([^\s#]*)$/);
      if (!match) {
        return current.getSuggestions(lines, cursorLine, cursorCol, options);
      }

      return {
        prefix: `#${match[1] ?? ""}`,
        items: [
          { value: "#2983", label: "#2983", description: "Extension API for registering custom @ autocomplete providers" },
          { value: "#2753", label: "#2753", description: "Reload stale resource settings" },
        ],
      };
    },

    applyCompletion(lines, cursorLine, cursorCol, item, prefix) {
      return current.applyCompletion(lines, cursorLine, cursorCol, item, prefix);
    },

    shouldTriggerFileCompletion(lines, cursorLine, cursorCol) {
      return current.shouldTriggerFileCompletion?.(lines, cursorLine, cursorCol) ?? true;
    },
  }));
});

```

--------------------------------

### Execute Shell Command

Source: https://pi.dev/docs/latest/rpc

Execute a shell command and add its output to the conversation context. The output is available on the next prompt.

```json
{"type": "bash", "command": "ls -la"}
```

--------------------------------

### Handle session_before_fork/clone

Source: https://pi.dev/docs/latest/extensions

Intercept session forking or cloning to cancel the operation or prepare for future state restoration.

```javascript
pi.on("session_before_fork", async (event, ctx) => {
  // event.entryId - ID of the selected entry
  // event.position - "before" for /fork, "at" for /clone
  return { cancel: true }; // Cancel fork/clone
  // OR
  return { skipConversationRestore: true }; // Reserved for future conversation restore control
});
```

--------------------------------

### createAgentSessionRuntime

Source: https://pi.dev/docs/latest/sdk

Creates a new agent session runtime. This is used to replace the active session and rebuild runtime state. It takes a runtime factory and initial session parameters.

```APIDOC
## createAgentSessionRuntime()

### Description
Creates a new agent session runtime, which is the same layer used by built-in interactive, print, and RPC modes. It replaces the active session and rebuilds cwd-bound runtime state.

### Parameters
- `createRuntime` (CreateAgentSessionRuntimeFactory): A factory function that creates the runtime.
- `options` (object): Options for creating the runtime.
  - `cwd` (string): The current working directory.
  - `agentDir` (string): The agent directory.
  - `sessionManager` (SessionManager): The session manager instance.

### Request Example
```javascript
import {
  type CreateAgentSessionRuntimeFactory,
  createAgentSessionFromServices,
  createAgentSessionRuntime,
  createAgentSessionServices,
  getAgentDir,
  SessionManager,
} from "@mariozechner/pi-coding-agent";

const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({
      services,
      sessionManager,
      sessionStartEvent,
    })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});
```
```

--------------------------------

### Check Truecolor Terminal Support

Source: https://pi.dev/docs/latest/themes

Verify if your terminal supports truecolor (24-bit RGB colors). Expected output is 'truecolor' or '24bit'.

```bash
echo $COLORTERM  # Should output "truecolor" or "24bit"
```

--------------------------------

### Configure Agent Session Model

Source: https://pi.dev/docs/latest/sdk

Specify the LLM model to use for the agent session, including built-in and custom models. Options include setting a primary model, thinking level, and scoped models for cycling.

```typescript
import { getModel } from "@mariozechner/pi-ai";
import { AuthStorage, ModelRegistry } from "@mariozechner/pi-coding-agent";

const authStorage = AuthStorage.create();
const modelRegistry = ModelRegistry.create(authStorage);

// Find specific built-in model (doesn't check if API key exists)
const opus = getModel("anthropic", "claude-opus-4-5");
if (!opus) throw new Error("Model not found");

// Find any model by provider/id, including custom models from models.json
// (doesn't check if API key exists)
const customModel = modelRegistry.find("my-provider", "my-model");

// Get only models that have valid API keys configured
const available = await modelRegistry.getAvailable();

const { session } = await createAgentSession({
  model: opus,
  thinkingLevel: "medium", // off, minimal, low, medium, high, xhigh
  
  // Models for cycling (Ctrl+P in interactive mode)
  scopedModels: [
    { model: opus, thinkingLevel: "high" },
    { model: haiku, thinkingLevel: "off" },
  ],
  
  authStorage,
  modelRegistry,
});
```

--------------------------------

### CustomEntry

Source: https://pi.dev/docs/latest/session

Used for extension state persistence and does not participate in LLM context. It requires a 'customType' to identify the extension and can store arbitrary 'data'.

```json
{"type":"custom","id":"h8i9j0k1","parentId":"g7h8i9j0","timestamp":"2024-12-03T14:20:00.000Z","customType":"my-extension","data":{"count":42}}
```

--------------------------------

### Widgets, Status, and Footer

Source: https://pi.dev/docs/latest/extensions

Provides methods for managing UI elements such as status messages in the footer, working indicators, custom widgets, and the terminal title.

```APIDOC
## Widgets, Status, and Footer

```javascript
// Status in footer (persistent until cleared)
ctx.ui.setStatus("my-ext", "Processing...");
ctx.ui.setStatus("my-ext", undefined);  // Clear

// Working loader (shown during streaming)
ctx.ui.setWorkingMessage("Thinking deeply...");
ctx.ui.setWorkingMessage();  // Restore default
ctx.ui.setWorkingVisible(false);  // Hide the built-in working loader row entirely
ctx.ui.setWorkingVisible(true);   // Show the built-in working loader row

// Working indicator (shown during streaming)
ctx.ui.setWorkingIndicator({ frames: [ctx.ui.theme.fg("accent", "●")] });  // Static dot
ctx.ui.setWorkingIndicator({
  frames: [
    ctx.ui.theme.fg("dim", "·"),
    ctx.ui.theme.fg("muted", "•"),
    ctx.ui.theme.fg("accent", "●"),
    ctx.ui.theme.fg("muted", "•"),
  ],
  intervalMs: 120,
});
ctx.ui.setWorkingIndicator({ frames: [] });  // Hide indicator
ctx.ui.setWorkingIndicator();  // Restore default spinner

// Widget above editor (default)
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"]);
// Widget below editor
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"], { placement: "belowEditor" });
ctx.ui.setWidget("my-widget", (tui, theme) => new Text(theme.fg("accent", "Custom"), 0, 0));
ctx.ui.setWidget("my-widget", undefined);  // Clear

// Custom footer (replaces built-in footer entirely)
ctx.ui.setFooter((tui, theme) => ({
  render(width) { return [theme.fg("dim", "Custom footer")]; },
  invalidate() {},
}));
ctx.ui.setFooter(undefined);  // Restore built-in footer

// Terminal title
ctx.ui.setTitle("pi - my-project");

// Editor text
ctx.ui.setEditorText("Prefill text");
const current = ctx.ui.getEditorText();

// Paste into editor (triggers paste handling, including collapse for large content)
ctx.ui.pasteToEditor("pasted content");

// Stack custom autocomplete behavior on top of the built-in provider
ctx.ui.addAutocompleteProvider((current) => ({
  async getSuggestions(lines, line, col, options) {
    const beforeCursor = (lines[line] ?? "").slice(0, col);
    const match = beforeCursor.match(/(?:^|[ \t])#([^\s#]*)$/);
    if (!match) {
      return current.getSuggestions(lines, line, col, options);
    }

    return {
      prefix: `#${match[1] ?? ""}`,
      items: [{ value: "#2983", label: "#2983", description: "Extension API for autocomplete" }],
    };
  },
  applyCompletion(lines, line, col, item, prefix) {
    return current.applyCompletion(lines, line, col, item, prefix);
  },
  shouldTriggerFileCompletion(lines, line, col) {
    return current.shouldTriggerFileCompletion?.(lines, line, col) ?? true;
  },
}));

// Tool output expansion
const wasExpanded = ctx.ui.getToolsExpanded();
ctx.ui.setToolsExpanded(true);
ctx.ui.setToolsExpanded(wasExpanded);

// Custom editor (vim mode, emacs mode, etc.)
ctx.ui.setEditorComponent((tui, theme, keybindings) => new VimEditor(tui, theme, keybindings));
ctx.ui.setEditorComponent(undefined);  // Restore default editor

// Theme management (see themes.md for creating themes)
const themes = ctx.ui.getAllThemes();  // [{ name: "dark", path: "/..." | undefined }, ...]
const lightTheme = ctx.ui.getTheme("light");  // Load without switching
const result = ctx.ui.setTheme("light");  // Switch by name
if (!result.success) {
  ctx.ui.notify(`Failed: ${result.error}`, "error");
}
ctx.ui.setTheme(lightTheme!);  // Or switch by Theme object
ctx.ui.theme.fg("accent", "styled text");  // Access current theme
```

Custom working-indicator frames are rendered verbatim. If you want colors, add them to the frame strings yourself, for example with `ctx.ui.theme.fg(...)`.
```

--------------------------------

### Extension UI Request: Input

Source: https://pi.dev/docs/latest/rpc

A request to prompt the user for free-form text input. This is a dialog method that expects a response.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-3",
  "method": "input",
  "title": "Enter a value",
  "placeholder": "type something..."
}
```

--------------------------------

### editor

Source: https://pi.dev/docs/latest/rpc

Open a multi-line text editor with optional prefilled content.

```APIDOC
## editor

Open a multi-line text editor with optional prefilled content.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-4",
  "method": "editor",
  "title": "Edit some text",
  "prefill": "Line 1\nLine 2\nLine 3"
}
```

Expected response: `extension_ui_response` with `value` (the edited text) or `cancelled: true`.
```

--------------------------------

### Model Type Definition

Source: https://pi.dev/docs/latest/rpc

Defines the structure for model configuration, including API details, capabilities, and cost.

```json
{
  "id": "claude-sonnet-4-20250514",
  "name": "Claude Sonnet 4",
  "api": "anthropic-messages",
  "provider": "anthropic",
  "baseUrl": "https://api.anthropic.com",
  "reasoning": true,
  "input": ["text", "image"],
  "contextWindow": 200000,
  "maxTokens": 16384,
  "cost": {
    "input": 3.0,
    "output": 15.0,
    "cacheRead": 0.3,
    "cacheWrite": 3.75
  }
}

```

--------------------------------

### Cycle to the next available model

Source: https://pi.dev/docs/latest/rpc

Advances the active model to the next one in the configured list. Returns `null` data if only one model is available.

```json
{"type": "cycle_model"}
```

--------------------------------

### Render Tool Result

Source: https://pi.dev/docs/latest/extensions

Renders the tool result or output, handling partial results, errors, and expanded views with detailed items. Use `Text` with padding (0, 0) and `\n` for multi-line content.

```javascript
renderResult(result, { expanded, isPartial }, theme, context) {
  if (isPartial) {
    return new Text(theme.fg("warning", "Processing..."), 0, 0);
  }

  if (result.details?.error) {
    return new Text(theme.fg("error", `Error: ${result.details.error}`), 0, 0);
  }

  let text = theme.fg("success", "✓ Done");
  if (expanded && result.details?.items) {
    for (const item of result.details.items) {
      text += "\n  " + theme.fg("dim", item);
    }
  }
  return new Text(text, 0, 0);
}
```

--------------------------------

### Adding Custom Autocomplete Providers

Source: https://pi.dev/docs/latest/extensions

Stack custom autocomplete logic on top of the existing provider. The custom provider can intercept suggestions and return its own or delegate to the default.

```javascript
// Stack custom autocomplete behavior on top of the built-in provider
ctx.ui.addAutocompleteProvider((current) => ({
  async getSuggestions(lines, line, col, options) {
    const beforeCursor = (lines[line] ?? "").slice(0, col);
    const match = beforeCursor.match(/(?:^|[ \t])#([^\s#]*)$/);
    if (!match) {
      return current.getSuggestions(lines, line, col, options);
    }

    return {
      prefix: `#${match[1] ?? ""}`,
      items: [{ value: "#2983", label: "#2983", description: "Extension API for autocomplete" }],
    };
  },
  applyCompletion(lines, line, col, item, prefix) {
    return current.applyCompletion(lines, line, col, item, prefix);
  },
  shouldTriggerFileCompletion(lines, line, col) {
    return current.shouldTriggerFileCompletion?.(lines, line, col) ?? true;
  },
}));

```

--------------------------------

### Add Custom Providers via models.json

Source: https://pi.dev/docs/latest/providers

Add custom providers like Ollama, LM Studio, or vLLM by defining them in models.json. This supports providers that speak supported API formats (OpenAI, Anthropic, Google).

```json
{
  "providers": [
    {
      "name": "ollama",
      "api_type": "ollama",
      "base_url": "http://localhost:11434"
    }
  ]
}
```

--------------------------------

### Brave Search Skill Usage

Source: https://pi.dev/docs/latest/skills

Perform a basic web search or include page content using the Brave Search skill. The `--content` flag retrieves the full page content.

```bash
./search.js "query"              # Basic search
```

```bash
./search.js "query" --content    # Include page content
```

--------------------------------

### Send a Steering Message with Images via RPC

Source: https://pi.dev/docs/latest/rpc

Similar to a regular steering message, but includes images for context. The images are base64 encoded.

```json
{"type": "steer", "message": "Look at this instead", "images": [{"type": "image", "data": "base64-encoded-data", "mimeType": "image/png"}]}

```

--------------------------------

### Handling Tool Calls

Source: https://pi.dev/docs/latest/extensions

Listen for the `tool_call` event to intercept and modify tool arguments before execution. This allows for pre-processing, validation, or blocking dangerous commands.

```APIDOC
## tool_call

### Description
Fired after `tool_execution_start`, before the tool executes. **Can block.** Use `isToolCallEventType` to narrow and get typed inputs.

### Method
`pi.on("tool_call", async (event, ctx) => { ... });`

### Parameters
- **event**: An object containing event details.
  - **event.toolName** (string): The name of the tool being called.
  - **event.toolCallId** (string): The unique identifier for the tool call.
  - **event.input** (object): The mutable tool parameters. Mutations to this object affect the actual tool execution.
- **ctx**: The context object.

### Behavior Guarantees
- Mutations to `event.input` affect the actual tool execution.
- Later `tool_call` handlers see mutations made by earlier handlers.
- No re-validation is performed after your mutation.
- Return values from `tool_call` only control blocking via `{ block: true, reason?: string }`.

### Example
```javascript
import { isToolCallEventType } from "@mariozechner/pi-coding-agent";

pi.on("tool_call", async (event, ctx) => {
  // event.toolName - "bash", "read", "write", "edit", etc.
  // event.toolCallId
  // event.input - tool parameters (mutable)

  // Built-in tools: no type params needed
  if (isToolCallEventType("bash", event)) {
    // event.input is { command: string; timeout?: number }
    event.input.command = `source ~/.profile\n${event.input.command}`;

    if (event.input.command.includes("rm -rf")) {
      return { block: true, reason: "Dangerous command" };
    }
  }

  if (isToolCallEventType("read", event)) {
    // event.input is { path: string; offset?: number; limit?: number }
    console.log(`Reading: ${event.input.path}`);
  }
});
```

### Typing Custom Tool Input
Custom tools should export their input type:
```typescript
// my-extension.ts
export type MyToolInput = Static<typeof myToolSchema>;
```

Use `isToolCallEventType` with explicit type parameters:
```javascript
import { isToolCallEventType } from "@mariozechner/pi-coding-agent";
import type { MyToolInput } from "my-extension";

pi.on("tool_call", (event) => {
  if (isToolCallEventType<"my_tool", MyToolInput>("my_tool", event)) {
    event.input.action;  // typed
  }
});
```
```

--------------------------------

### Pi Package Source Types: git

Source: https://pi.dev/docs/latest/packages

Specifies git repository sources for Pi packages. Supports various URL formats and SSH keys. Refs pin packages and skip updates. Cloned to `~/.pi/agent/git/` (global) or `.pi/git/` (project).

```bash
git:github.com/user/repo@v1
git:git@github.com:user/repo@v1
https://github.com/user/repo@v1
ssh://git@github.com/user/repo@v1
```

--------------------------------

### SessionManager Methods

Source: https://pi.dev/docs/latest/tree

Utilities for managing the current session tree state.

```APIDOC
## SessionManager

### Description
Provides methods to interact with the session tree, such as retrieving the current leaf, resetting it, or accessing the full tree.

### Methods
- `getLeafUuid(): string | null` - Returns the UUID of the current leaf node, or null if the session is empty.
- `resetLeaf(): void` - Resets the current leaf to null, typically used for root user message navigation.
- `getTree(): SessionTreeNode[]` - Returns the entire session tree with children sorted by timestamp.
- `branch(id)` - Changes the current leaf pointer to the node with the specified ID.
- `branchWithSummary(id, summary)` - Changes the current leaf pointer and creates a summary entry for the specified ID.
```

--------------------------------

### Runtime Session Management

Source: https://pi.dev/docs/latest/sdk

API for replacing the active session with new, saved, forked, or cloned sessions.

```APIDOC
## Runtime Session Management

### Description
Provides an API for replacing the active session, supporting flows like new, resume, fork, clone, and import.

### Usage
```typescript
const createRuntime: CreateAgentSessionRuntimeFactory = async ({ cwd, sessionManager, sessionStartEvent }) => {
  const services = await createAgentSessionServices({ cwd });
  return {
    ...(await createAgentSessionFromServices({
      services,
      sessionManager,
      sessionStartEvent,
    })),
    services,
    diagnostics: services.diagnostics,
  };
};

const runtime = await createAgentSessionRuntime(createRuntime, {
  cwd: process.cwd(),
  agentDir: getAgentDir(),
  sessionManager: SessionManager.create(process.cwd()),
});

// Replace the active session with a fresh one
await runtime.newSession();

// Replace the active session with another saved session
await runtime.switchSession("/path/to/session.jsonl");

// Replace the active session with a fork from a specific user entry
await runtime.fork("entry-id");

// Clone the active path through a specific entry
await runtime.fork("entry-id", { position: "at" });
```
```

--------------------------------

### Register CLI Flag

Source: https://pi.dev/docs/latest/extensions

Registers a command-line interface flag with a description, type, and default value. Use `pi.getFlag()` to check the value of a registered flag.

```javascript
pi.registerFlag("plan", {
  description: "Start in plan mode",
  type: "boolean",
  default: false,
});

// Check value
if (pi.getFlag("plan")) {
  // Plan mode enabled
}
```

--------------------------------

### Prepare Arguments for Backward Compatibility

Source: https://pi.dev/docs/latest/extensions

The `prepareArguments` function runs before schema validation and `execute`. Use it to adapt older argument shapes to the current schema, ensuring compatibility when resuming older sessions. Return the object that should be validated against the `parameters` schema.

```typescript
pi.registerTool({
  name: "edit",
  label: "Edit",
  description: "Edit a single file using exact text replacement",
  parameters: Type.Object({
    path: Type.String(),
    edits: Type.Array(
      Type.Object({
        oldText: Type.String(),
        newText: Type.String(),
      }),
    ),
  }),
  prepareArguments(args) {
    if (!args || typeof args !== "object") return args;

    const input = args as {
      path?: string;
      edits?: Array<{ oldText: string; newText: string }>;
      oldText?: unknown;
      newText?: unknown;
    };

    if (typeof input.oldText !== "string" || typeof input.newText !== "string") {
      return args;
    }

    return {
      ...input,
      edits: [...(input.edits ?? []), { oldText: input.oldText, newText: input.newText }],
    };
  },
  async execute(toolCallId, params, signal, onUpdate, ctx) {
    // params now matches the current schema
    return {
      content: [{ type: "text", text: `Applying ${params.edits.length} edit block(s)` }],
      details: {},
    };
  },
});

```

--------------------------------

### Switch to a specific model

Source: https://pi.dev/docs/latest/rpc

Changes the active model to a specified one, identified by its provider and model ID. The response includes the full `Model` object.

```json
{"type": "set_model", "provider": "anthropic", "modelId": "claude-sonnet-4-20250514"}
```

--------------------------------

### Send User Message During Streaming

Source: https://pi.dev/docs/latest/extensions

When the agent is streaming, user messages require a `deliverAs` option. Use 'steer' to queue after tool calls or 'followUp' to wait for all tool calls to complete.

```javascript
// During streaming - must specify delivery mode
pi.sendUserMessage("Focus on error handling", { deliverAs: "steer" });
pi.sendUserMessage("And then summarize", { deliverAs: "followUp" });

```

--------------------------------

### Intercept session_before_compact Event

Source: https://pi.dev/docs/latest/compaction

Fired before auto-compaction or `/compact`. Allows cancellation or provision of a custom summary. Provides access to messages to summarize, turn prefixes, previous summary, file operations, token counts, and compaction settings.

```typescript
pi.on("session_before_compact", async (event, ctx) => {
  const { preparation, branchEntries, customInstructions, signal } = event;

  // preparation.messagesToSummarize - messages to summarize
  // preparation.turnPrefixMessages - split turn prefix (if isSplitTurn)
  // preparation.previousSummary - previous compaction summary
  // preparation.fileOps - extracted file operations
  // preparation.tokensBefore - context tokens before compaction
  // preparation.firstKeptEntryId - where kept messages start
  // preparation.settings - compaction settings

  // branchEntries - all entries on current branch (for custom state)
  // signal - AbortSignal (pass to LLM calls)

  // Cancel:
  return { cancel: true };

  // Custom summary:
  return {
    compaction: {
      summary: "Your summary...",
      firstKeptEntryId: preparation.firstKeptEntryId,
      tokensBefore: preparation.tokensBefore,
      details: { /* custom data */ },
    }
  };
});

```

--------------------------------

### ctx.waitForIdle()

Source: https://pi.dev/docs/latest/extensions

Waits for the agent to finish streaming, ensuring it is idle before proceeding. This is safe to call from command handlers.

```APIDOC
## ctx.waitForIdle()

### Description
Wait for the agent to finish streaming.

### Method
await ctx.waitForIdle()

### Usage
This method is available in command handlers to ensure the agent is idle before modifying the session.

### Request Example
```javascript
pi.registerCommand("my-cmd", {
  handler: async (args, ctx) => {
    await ctx.waitForIdle();
    // Agent is now idle, safe to modify session
  },
});
```
```

--------------------------------

### Customizing the Footer and Terminal Title

Source: https://pi.dev/docs/latest/extensions

Replace the built-in footer with custom renderable content or restore it. Also, set the terminal window title.

```javascript
// Custom footer (replaces built-in footer entirely)
ctx.ui.setFooter((tui, theme) => ({
  render(width) { return [theme.fg("dim", "Custom footer")]; },
  invalidate() {},
}));
ctx.ui.setFooter(undefined);  // Restore built-in footer

// Terminal title
ctx.ui.setTitle("pi - my-project");

```

--------------------------------

### Run Pi in JSON Event Stream Mode

Source: https://pi.dev/docs/latest/json

Outputs all session events as JSON lines to stdout. Useful for integrating pi into other tools or custom UIs.

```bash
pi --mode json "Your prompt"
```

--------------------------------

### cycle_model

Source: https://pi.dev/docs/latest/rpc

Cycle to the next available model. Returns `null` data if only one model available.

```APIDOC
## cycle_model

### Description
Cycle to the next available model. Returns `null` data if only one model available.

### Method
cycle_model

### Request Body
- **type** (string) - Required - Must be "cycle_model"

### Request Example
```json
{"type": "cycle_model"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "cycle_model"
- **success** (boolean) - true
- **data** (object or null) - Contains information about the new model if cycling occurred.
  - **model** (object) - The newly selected Model object.
  - **thinkingLevel** (string) - The thinking level associated with the model.
  - **isScoped** (boolean) - Indicates if the model selection is scoped.
```

--------------------------------

### Create and Configure Box Component

Source: https://pi.dev/docs/latest/tui

Use the Box component for a container with padding and background color. It can hold child components and its background function can be changed.

```typescript
const box = new Box(
  1,                // paddingX
  1,                // paddingY
  (s) => bgGray(s)  // background function
);
box.addChild(new Text("Content", 0, 0));
box.setBgFn((s) => bgBlue(s));

```

--------------------------------

### Provider Model Configuration Interface

Source: https://pi.dev/docs/latest/custom-provider

Defines the structure for configuring individual models within a custom provider, including ID, display name, API type, cost, context window, and compatibility settings.

```typescript
interface ProviderModelConfig {
  /** Model ID (e.g., "claude-sonnet-4-20250514"). */
  id: string;

  /** Display name (e.g., "Claude 4 Sonnet"). */
  name: string;

  /** API type override for this specific model. */
  api?: Api;

  /** Whether the model supports extended thinking. */
  reasoning: boolean;

  /** Supported input types. */
  input: ("text" | "image")[];

  /** Cost per million tokens (for usage tracking). */
  cost: {
    input: number;
    output: number;
    cacheRead: number;
    cacheWrite: number;
  };

  /** Maximum context window size in tokens. */
  contextWindow: number;

  /** Maximum output tokens. */
  maxTokens: number;

  /** Custom headers for this specific model. */
  headers?: Record<string, string>;

  /** OpenAI compatibility settings for openai-completions API. */
  compat?: {
    supportsStore?: boolean;
    supportsDeveloperRole?: boolean;
    supportsReasoningEffort?: boolean;
    reasoningEffortMap?: Partial<Record<"minimal" | "low" | "medium" | "high" | "xhigh", string>>;
    supportsUsageInStreaming?: boolean;
    maxTokensField?: "max_completion_tokens" | "max_tokens";
    requiresToolResultName?: boolean;
    requiresAssistantAfterToolResult?: boolean;
    requiresThinkingAsText?: boolean;
    requiresReasoningContentOnAssistantMessages?: boolean;
    thinkingFormat?: "openai" | "deepseek" | "zai" | "qwen" | "qwen-chat-template";
    cacheControlFormat?: "anthropic";
  };
}
```

--------------------------------

### Create Image Component

Source: https://pi.dev/docs/latest/tui

Display images in supported terminals using the Image component. Provide base64 data, MIME type, theme, and optional size constraints.

```typescript
const image = new Image(
  base64Data,   // base64-encoded image
  "image/png",  // MIME type
  theme,        // ImageTheme
  { maxWidthCells: 80, maxHeightCells: 24 }
);

```

--------------------------------

### Usage Type

Source: https://pi.dev/docs/latest/session

Defines the structure for tracking token usage and associated costs.

```typescript
interface Usage {
  input: number;
  output: number;
  cacheRead: number;
  cacheWrite: number;
  totalTokens: number;
  cost: {
    input: number;
    output: number;
    cacheRead: number;
    cacheWrite: number;
    total: number;
  };
}

```

--------------------------------

### Create Custom Footer

Source: https://pi.dev/docs/latest/tui

Replace the default footer with custom content. The `footerData` object provides access to Git branch and extension statuses. Use `undefined` to restore the default footer.

```typescript
ctx.ui.setFooter((tui, theme, footerData) => ({
  invalidate() {}
  render(width: number): string[] {
    // footerData.getGitBranch(): string | null
    // footerData.getExtensionStatuses(): ReadonlyMap<string, string>
    return [`${ctx.model?.id} (${footerData.getGitBranch() || "no git"})`];
  },
  dispose: footerData.onBranchChange(() => tui.requestRender()), // reactive
}));
```

```typescript
ctx.ui.setFooter(undefined); // restore default
```

--------------------------------

### Before Provider Request Event

Source: https://pi.dev/docs/latest/extensions

Fired after the provider-specific payload is built, right before the request is sent. Allows modification of the payload.

```APIDOC
## before_provider_request

Fired after the provider-specific payload is built, right before the request is sent. Handlers run in extension load order. Returning `undefined` keeps the payload unchanged. Returning any other value replaces the payload for later handlers and for the actual request.
This hook can rewrite provider-level system instructions or remove them entirely. Those payload-level changes are not reflected by `ctx.getSystemPrompt()`, which reports Pi's system prompt string rather than the final serialized provider payload.
```javascript
pi.on("before_provider_request", (event, ctx) => {
  console.log(JSON.stringify(event.payload, null, 2));

  // Optional: replace payload
  // return { ...event.payload, temperature: 0 };
});

```

This is mainly useful for debugging provider serialization and cache behavior.
```

--------------------------------

### Create and Update Markdown Component

Source: https://pi.dev/docs/latest/tui

Render markdown content with syntax highlighting using the Markdown component. It accepts content, padding, and a theme. The displayed markdown can be updated with setText.

```typescript
const md = new Markdown(
  "# Title\n\nSome **bold** text",
  1,        // paddingX
  1,        // paddingY
  theme     // MarkdownTheme (see below)
);
md.setText("Updated markdown");

```

--------------------------------

### Extension UI Confirmation Response

Source: https://pi.dev/docs/latest/rpc

Sent for confirm dialogs. The 'id' must match the request.

```json
{"type": "extension_ui_response", "id": "uuid-2", "confirmed": true}

```

--------------------------------

### Focusable Interface for IME Support

Source: https://pi.dev/docs/latest/tui

Implements the Focusable interface for components needing IME support and a text cursor. TUI manages focus and cursor positioning based on the CURSOR_MARKER.

```typescript
import { CURSOR_MARKER, type Component, type Focusable } from "@mariozechner/pi-tui";

class MyInput implements Component, Focusable {
  focused: boolean = false;  // Set by TUI when focus changes
  
  render(width: number): string[] {
    const marker = this.focused ? CURSOR_MARKER : "";
    // Emit marker right before the fake cursor
    return [`> ${beforeCursor}${marker}\x1b[7m${atCursor}\x1b[27m${afterCursor}`];
  }
}

```

--------------------------------

### Component Interface

Source: https://pi.dev/docs/latest/tui

Defines the core interface for all TUI components, including rendering and input handling.

```APIDOC
## Component Interface

All components implement:
```typescript
interface Component {
  render(width: number): string[];
  handleInput?(data: string): void;
  wantsKeyRelease?: boolean;
  invalidate(): void;
}
```

### Methods

- `render(width)`: Return array of strings (one per line). Each line **must not exceed `width`**.
- `handleInput?(data)`: Receive keyboard input when component has focus.
- `wantsKeyRelease?`: If true, component receives key release events (Kitty protocol). Default: false.
- `invalidate()`: Clear cached render state. Called on theme changes.

The TUI appends a full SGR reset and OSC 8 reset at the end of each rendered line. Styles do not carry across lines. If you emit multi-line text with styling, reapply styles per line or use `wrapTextWithAnsi()` so styles are preserved for each wrapped line.
```

--------------------------------

### Tool Execution Update Event (Streaming)

Source: https://pi.dev/docs/latest/rpc

Streams partial results during tool execution, such as bash output as it arrives. The `partialResult` contains accumulated output.

```json
{
  "type": "tool_execution_update",
  "toolCallId": "call_abc123",
  "toolName": "bash",
  "args": {"command": "ls -la"},
  "partialResult": {
    "content": [{"type": "text", "text": "partial output so far..."}],
    "details": {"truncation": null, "fullOutputPath": null}
  }
}
```

--------------------------------

### Truncate Command Output

Source: https://pi.dev/docs/latest/extensions

Use truncation utilities to limit output size and inform the LLM when truncation occurs. Inform the LLM where to find the full output if truncated.

```typescript
import {
  truncateHead,
  truncateTail,
  truncateLine,
  formatSize,
  DEFAULT_MAX_BYTES,
  DEFAULT_MAX_LINES,
} from "@mariozechner/pi-coding-agent";

async execute(toolCallId, params, signal, onUpdate, ctx) {
  const output = await runCommand();

  const truncation = truncateHead(output, {
    maxLines: DEFAULT_MAX_LINES,
    maxBytes: DEFAULT_MAX_BYTES,
  });

  let result = truncation.content;

  if (truncation.truncated) {
    const tempFile = writeTempFile(output);

    result += `\n\n[Output truncated: ${truncation.outputLines} of ${truncation.totalLines} lines`;
    result += ` (${formatSize(truncation.outputBytes)} of ${formatSize(truncation.totalBytes)}).`;
    result += ` Full output saved to: ${tempFile}]`;
  }

  return { content: [{ type: "text", text: result }] };
}
```

--------------------------------

### Set Anthropic API Key via Environment Variable

Source: https://pi.dev/docs/latest/providers

Set the ANTHROPIC_API_KEY environment variable to authenticate with Anthropic services. This is one method for API key providers.

```bash
export ANTHROPIC_API_KEY=sk-ant-...
pi

```

--------------------------------

### Controlling Tool Expansion and Editor Components

Source: https://pi.dev/docs/latest/extensions

Toggle the expansion state of tools and switch between different editor components like Vim or Emacs modes, or restore the default.

```javascript
// Tool output expansion
const wasExpanded = ctx.ui.getToolsExpanded();
ctx.ui.setToolsExpanded(true);
ctx.ui.setToolsExpanded(wasExpanded);

// Custom editor (vim mode, emacs mode, etc.)
ctx.ui.setEditorComponent((tui, theme, keybindings) => new VimEditor(tui, theme, keybindings));
ctx.ui.setEditorComponent(undefined);  // Restore default editor

```

--------------------------------

### pi.setModel(model)

Source: https://pi.dev/docs/latest/extensions

Sets the current language model to be used for operations. Returns false if no API key is available for the specified model.

```APIDOC
## pi.setModel(model)

### Description
Set the current model. Returns `false` if no API key is available for the model. See models.md for configuring custom models.

### Usage
```javascript
const model = ctx.modelRegistry.find("anthropic", "claude-sonnet-4-5");
if (model) {
  const success = await pi.setModel(model);
  if (!success) {
    ctx.ui.notify("No API key for this model", "error");
  }
}
```

### Parameters
- **model** (object) - The model object to set as current. This object should be obtained from `ctx.modelRegistry` or a similar source.
```

--------------------------------

### Bash Command Response (Standard)

Source: https://pi.dev/docs/latest/rpc

Standard response for a successful bash command execution, including output, exit code, and cancellation status.

```json
{
  "type": "response",
  "command": "bash",
  "success": true,
  "data": {
    "output": "total 48\ndrwxr-xr-x ...",
    "exitCode": 0,
    "cancelled": false,
    "truncated": false
  }
}
```

--------------------------------

### Defining and Loading Custom Skills

Source: https://pi.dev/docs/latest/sdk

Illustrates how to define a custom `Skill` object and override the default skills loaded by `DefaultResourceLoader`. The `skillsOverride` function allows merging custom skills with existing ones.

```typescript
import {
  createAgentSession,
  DefaultResourceLoader,
  type Skill,
} from "@mariozechner/pi-coding-agent";

const customSkill: Skill = {
  name: "my-skill",
  description: "Custom instructions",
  filePath: "/path/to/SKILL.md",
  baseDir: "/path/to",
  source: "custom",
};

const loader = new DefaultResourceLoader({
  skillsOverride: (current) => ({
    skills: [...current.skills, customSkill],
    diagnostics: current.diagnostics,
  }),
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });

```

--------------------------------

### Handling User Bash Events

Source: https://pi.dev/docs/latest/extensions

Intercept user-initiated bash commands triggered by `!` or `!!` prefixes. This allows for custom command execution logic, such as routing to remote shells or providing alternative implementations.

```APIDOC
## user_bash

### Description
Fired when user executes `!` or `!!` commands. **Can intercept.**

### Method
`pi.on("user_bash", (event, ctx) => { ... });`

### Parameters
- **event**: An object containing event details.
  - **event.command** (string): The bash command executed by the user.
  - **event.excludeFromContext** (boolean): True if the `!!` prefix was used, indicating the command should not be included in context history.
  - **event.cwd** (string): The current working directory for the command.
- **ctx**: The context object.

### Return Value
- **operations**: An object defining custom bash operations.
  - **exec**: A function to execute a command.
- **result**: An object containing the direct result of the command execution.
  - **output** (string): The command's output.
  - **exitCode** (number): The command's exit code.
  - **cancelled** (boolean): Whether the command was cancelled.
  - **truncated** (boolean): Whether the output was truncated.

### Example
```javascript
import { createLocalBashOperations } from "@mariozechner/pi-coding-agent";

pi.on("user_bash", (event, ctx) => {
  // event.command - the bash command
  // event.excludeFromContext - true if !! prefix
  // event.cwd - working directory

  // Option 1: Provide custom operations (e.g., SSH)
  // return { operations: remoteBashOps };

  // Option 2: Wrap pi's built-in local bash backend
  const local = createLocalBashOperations();
  return {
    operations: {
      exec(command, cwd, options) {
        return local.exec(`source ~/.profile\n${command}`, cwd, options);
      }
    }
  };

  // Option 3: Full replacement - return result directly
  // return { result: { output: "...", exitCode: 0, cancelled: false, truncated: false } };
});
```
```

--------------------------------

### Configure OpenRouter OpenAI Compatibility with Routing

Source: https://pi.dev/docs/latest/models

Define OpenAI compatibility for the OpenRouter provider, including advanced routing preferences. Model-level compat overrides provider-level values.

```json
{
  "providers": {
    "openrouter": {
      "baseUrl": "https://openrouter.ai/api/v1",
      "apiKey": "OPENROUTER_API_KEY",
      "api": "openai-completions",
      "models": [
        {
          "id": "openrouter/anthropic/claude-3.5-sonnet",
          "name": "OpenRouter Claude 3.5 Sonnet",
          "compat": {
            "openRouterRouting": {
              "allow_fallbacks": true,
              "require_parameters": false,
              "data_collection": "deny",
              "zdr": true,
              "enforce_distillable_text": false,
              "order": ["anthropic", "amazon-bedrock", "google-vertex"],
              "only": ["anthropic", "amazon-bedrock"],
              "ignore": ["gmicloud", "friendli"],
              "quantizations": ["fp16", "bf16"],
              "sort": {
                "by": "price",
                "partition": "model"
              },
              "max_price": {
                "prompt": 10,
                "completion": 20
              },
              "preferred_min_throughput": {
                "p50": 100,
                "p90": 50
              },
              "preferred_max_latency": {
                "p50": 1,
                "p90": 3,
                "p99": 5
              }
            }
          }
        }
      ]
    }
  }
}
```

--------------------------------

### Overriding Agent Context Files

Source: https://pi.dev/docs/latest/sdk

Demonstrates how to override the default agent files using `DefaultResourceLoader`. The `agentsFilesOverride` function allows adding custom files, such as guidelines, to the agent's context.

```typescript
import { createAgentSession, DefaultResourceLoader } from "@mariozechner/pi-coding-agent";

const loader = new DefaultResourceLoader({
  agentsFilesOverride: (current) => ({
    agentsFiles: [
      ...current.agentsFiles,
      { path: "/virtual/AGENTS.md", content: "# Guidelines\n\n- Be concise" },
    ],
  }),
});
await loader.reload();

const { session } = await createAgentSession({ resourceLoader: loader });

```

--------------------------------

### Handle Tool Results with Abort Signal

Source: https://pi.dev/docs/latest/extensions

Process tool results while respecting the agent's abort signal for cancellable operations like network requests.

```javascript
pi.on("tool_result", async (event, ctx) => {
  const response = await fetch("https://example.com/api", {
    method: "POST",
    body: JSON.stringify(event),
    signal: ctx.signal,
  });

  const data = await response.json();
  return { details: data };
});
```

--------------------------------

### Use Environment Variable for API Key

Source: https://pi.dev/docs/latest/providers

Reference an environment variable directly for the API key value.

```json
{ "type": "api_key", "key": "MY_ANTHROPIC_KEY" }
```

--------------------------------

### Handle session_before_compact / session_compact

Source: https://pi.dev/docs/latest/extensions

Intercept or react to session compaction events. Can be used to cancel compaction or provide a custom summary.

```javascript
pi.on("session_before_compact", async (event, ctx) => {
  const { preparation, branchEntries, customInstructions, signal } = event;

  // Cancel:
  return { cancel: true };

  // Custom summary:
  return {
    compaction: {
      summary: "...",
      firstKeptEntryId: preparation.firstKeptEntryId,
      tokensBefore: preparation.tokensBefore,
    }
  };
});

pi.on("session_compact", async (event, ctx) => {
  // event.compactionEntry - the saved compaction
  // event.fromExtension - whether extension provided it
});
```

--------------------------------

### Overlay Component Lifecycle Management

Source: https://pi.dev/docs/latest/tui

Always create fresh instances of overlay components. Reusing disposed references can lead to errors. Call the creation function again to re-show a previously closed overlay.

```typescript
// Wrong - stale reference
let menu: MenuComponent;
await ctx.ui.custom((_, __, ___, done) => {
  menu = new MenuComponent(done);
  return menu;
}, { overlay: true });
setActiveComponent(menu);  // Disposed

// Correct - re-call to re-show
const showMenu = () => ctx.ui.custom((_, __, ___, done) => 
  new MenuComponent(done), { overlay: true });

await showMenu();  // First show
await showMenu();  // "Back" = just call again

```

--------------------------------

### Create Interactive Selector Component

Source: https://pi.dev/docs/latest/tui

Implement a custom interactive selector component with navigation and selection handling. This component uses `matchesKey` for input and `truncateToWidth` for rendering.

```typescript
import {
  matchesKey, Key,
  truncateToWidth, visibleWidth
} from "@mariozechner/pi-tui";

class MySelector {
  private items: string[];
  private selected = 0;
  private cachedWidth?: number;
  private cachedLines?: string[];
  
  public onSelect?: (item: string) => void;
  public onCancel?: () => void;

  constructor(items: string[]) {
    this.items = items;
  }

  handleInput(data: string): void {
    if (matchesKey(data, Key.up) && this.selected > 0) {
      this.selected--;
      this.invalidate();
    } else if (matchesKey(data, Key.down) && this.selected < this.items.length - 1) {
      this.selected++;
      this.invalidate();
    } else if (matchesKey(data, Key.enter)) {
      this.onSelect?.(this.items[this.selected]);
    } else if (matchesKey(data, Key.escape)) {
      this.onCancel?.();
    }
  }

  render(width: number): string[] {
    if (this.cachedLines && this.cachedWidth === width) {
      return this.cachedLines;
    }

    this.cachedLines = this.items.map((item, i) => {
      const prefix = i === this.selected ? "> " : "  ";
      return truncateToWidth(prefix + item, width);
    });
    this.cachedWidth = width;
    return this.cachedLines;
  }

  invalidate(): void {
    this.cachedWidth = undefined;
    this.cachedLines = undefined;
  }
}
```

--------------------------------

### Basic Extension Factory Function

Source: https://pi.dev/docs/latest/extensions

An extension exports a default factory function that receives ExtensionAPI. This function can subscribe to events and register tools, commands, shortcuts, and flags. Use ctx.ui for user interactions like confirmations and notifications.

```typescript
import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";

export default function (pi: ExtensionAPI) {
  // Subscribe to events
  pi.on("event_name", async (event, ctx) => {
    // ctx.ui for user interaction
    const ok = await ctx.ui.confirm("Title", "Are you sure?");
    ctx.ui.notify("Done!", "success");
    ctx.ui.setStatus("my-ext", "Processing...");  // Footer status
    ctx.ui.setWidget("my-ext", ["Line 1", "Line 2"]);  // Widget above editor (default)
  });

  // Register tools, commands, shortcuts, flags
  pi.registerTool({ ... });
  pi.registerCommand("name", { ... });
  pi.registerShortcut("ctrl+x", { ... });
  pi.registerFlag("my-flag", { ... });
}
```

--------------------------------

### Context Event

Source: https://pi.dev/docs/latest/extensions

Fired before each LLM call, allowing modification of messages non-destructively.

```APIDOC
## context

Fired before each LLM call. Modify messages non-destructively. See session.md for message types.
```javascript
pi.on("context", async (event, ctx) => {
  // event.messages - deep copy, safe to modify
  const filtered = event.messages.filter(m => !shouldPrune(m));
  return { messages: filtered };
});
```
```

--------------------------------

### CompactionEntry Interface

Source: https://pi.dev/docs/latest/compaction

Defines the structure for compaction entries, including type, IDs, timestamp, summary, and optional details for custom data.

```typescript
interface CompactionEntry<T = unknown> {
  type: "compaction";
  id: string;
  parentId: string;
  timestamp: number;
  summary: string;
  firstKeptEntryId: string;
  tokensBefore: number;
  fromHook?: boolean;  // true if provided by extension (legacy field name)
  details?: T;         // implementation-specific data
}

// Default compaction uses this for details (from compaction.ts):
interface CompactionDetails {
  readFiles: string[];
  modifiedFiles: string[];
}
```

--------------------------------

### Provider Configuration Interface

Source: https://pi.dev/docs/latest/custom-provider

Defines the structure for configuring a custom AI provider, including API endpoint, authentication, custom streaming, headers, and model registration.

```typescript
interface ProviderConfig {
  /** API endpoint URL. Required when defining models. */
  baseUrl?: string;

  /** API key or environment variable name. Required when defining models (unless oauth). */
  apiKey?: string;

  /** API type for streaming. Required at provider or model level when defining models. */
  api?: Api;

  /** Custom streaming implementation for non-standard APIs. */
  streamSimple?: (
    model: Model<Api>,
    context: Context,
    options?: SimpleStreamOptions
  ) => AssistantMessageEventStream;

  /** Custom headers to include in requests. Values can be env var names. */
  headers?: Record<string, string>;

  /** If true, adds Authorization: Bearer header with the resolved API key. */
  authHeader?: boolean;

  /** Models to register. If provided, replaces all existing models for this provider. */
  models?: ProviderModelConfig[];

  /** OAuth provider for /login support. */
  oauth?: {
    name: string;
    login(callbacks: OAuthLoginCallbacks): Promise<OAuthCredentials>;
    refreshToken(credentials: OAuthCredentials): Promise<OAuthCredentials>;
    getApiKey(credentials: OAuthCredentials): string;
    modifyModels?(models: Model<Api>[], credentials: OAuthCredentials): Model<Api>[];
  };
}
```

--------------------------------

### pi.sendUserMessage

Source: https://pi.dev/docs/latest/extensions

Send a user message to the agent. This function simulates a user typing a message and can include text, images, or a combination. It always triggers a turn and requires specific delivery modes when the agent is streaming.

```APIDOC
## pi.sendUserMessage(content, options?)

### Description
Send a user message to the agent. Unlike `sendMessage()` which sends custom messages, this sends an actual user message that appears as if typed by the user. Always triggers a turn.

### Parameters
#### Content
- **content** (string | Array<{ type: "text", text: string } | { type: "image", source: { type: "base64", mediaType: string, data: string } }>) - Required - The message content, which can be a string or an array of text and image objects.

#### Options Object
- **deliverAs** (string) - Required when agent is streaming - Delivery mode: "steer" or "followUp".

When not streaming, the message is sent immediately and triggers a new turn. When streaming without `deliverAs`, throws an error.
```

--------------------------------

### Extension UI Value Response

Source: https://pi.dev/docs/latest/rpc

Sent for select, input, or editor dialogs. The 'id' must match the request.

```json
{"type": "extension_ui_response", "id": "uuid-1", "value": "Allow"}

```

--------------------------------

### Register Multiple Tools with Shared State

Source: https://pi.dev/docs/latest/extensions

An extension can register multiple tools that share state. Ensure resources are cleaned up on session shutdown.

```typescript
export default function (pi: ExtensionAPI) {
  let connection = null;

  pi.registerTool({ name: "db_connect", ... });
  pi.registerTool({ name: "db_query", ... });
  pi.registerTool({ name: "db_close", ... });

  pi.on("session_shutdown", async () => {
    connection?.close();
  });
}
```

--------------------------------

### Grant Storage Permissions in Termux

Source: https://pi.dev/docs/latest/termux

Run this command once to grant Termux permission to access shared storage (e.g., Downloads, Documents).

```bash
termux-setup-storage
```

--------------------------------

### Send a Steering Message via RPC

Source: https://pi.dev/docs/latest/rpc

Send a steering message to interrupt the current agent task and redirect its focus. This is useful for immediate course correction.

```json
{"type": "steer", "message": "Stop and do this instead"}

```

--------------------------------

### Implement Async Operation with Cancellation

Source: https://pi.dev/docs/latest/tui

Use `BorderedLoader` for long-running async tasks. It displays a spinner and allows cancellation via the escape key. The `fetchData` function should accept a signal for aborting the operation.

```typescript
import { BorderedLoader } from "@mariozechner/pi-coding-agent";

pi.registerCommand("fetch", {
  handler: async (_args, ctx) => {
    const result = await ctx.ui.custom<string | null>((tui, theme, _kb, done) => {
      const loader = new BorderedLoader(tui, theme, "Fetching data...");
      loader.onAbort = () => done(null);

      // Do async work
      fetchData(loader.signal)
        .then((data) => done(data))
        .catch(() => done(null));

      return loader;
    });

    if (result === null) {
      ctx.ui.notify("Cancelled", "info");
    } else {
      ctx.ui.setEditorText(result);
    }
  },
});

```

--------------------------------

### Fork a message

Source: https://pi.dev/docs/latest/rpc

Initiates a new fork from a previous user message. Can be cancelled by a session_before_fork extension event handler. Returns the text of the message being forked from.

```json
{"type": "fork", "entryId": "abc123"}
```

```json
{
  "type": "response",
  "command": "fork",
  "success": true,
  "data": {"text": "The original prompt text...", "cancelled": false}
}
```

```json
{
  "type": "response",
  "command": "fork",
  "success": true,
  "data": {"text": "The original prompt text...", "cancelled": true}
}
```

--------------------------------

### Highlight Code with Auto-detected Language

Source: https://pi.dev/docs/latest/extensions

Auto-detect the language from a file path and then highlight the code using the detected language and theme.

```typescript
import { highlightCode, getLanguageFromPath } from "@mariozechner/pi-coding-agent";

// Auto-detect language from file path
const lang = getLanguageFromPath("/path/to/file.rs");  // "rust"
const highlighted = highlightCode(code, lang, theme);

```

--------------------------------

### Define a Custom Pi Theme

Source: https://pi.dev/docs/latest/themes

Define a custom theme for Pi by specifying its name, optional variables, and all required color tokens. The '$schema' field enables editor auto-completion and validation. Colors can be defined as hex codes or by referencing other defined variables.

```json
{
  "$schema": "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/src/modes/interactive/theme/theme-schema.json",
  "name": "my-theme",
  "vars": {
    "primary": "#00aaff",
    "secondary": 242
  },
  "colors": {
    "accent": "primary",
    "border": "primary",
    "borderAccent": "#00ffff",
    "borderMuted": "secondary",
    "success": "#00ff00",
    "error": "#ff0000",
    "warning": "#ffff00",
    "muted": "secondary",
    "dim": 240,
    "text": "",
    "thinkingText": "secondary",
    "selectedBg": "#2d2d30",
    "userMessageBg": "#2d2d30",
    "userMessageText": "",
    "customMessageBg": "#2d2d30",
    "customMessageText": "",
    "customMessageLabel": "primary",
    "toolPendingBg": "#1e1e2e",
    "toolSuccessBg": "#1e2e1e",
    "toolErrorBg": "#2e1e1e",
    "toolTitle": "primary",
    "toolOutput": "",
    "mdHeading": "#ffaa00",
    "mdLink": "primary",
    "mdLinkUrl": "secondary",
    "mdCode": "#00ffff",
    "mdCodeBlock": "",
    "mdCodeBlockBorder": "secondary",
    "mdQuote": "secondary",
    "mdQuoteBorder": "secondary",
    "mdHr": "secondary",
    "mdListBullet": "#00ffff",
    "toolDiffAdded": "#00ff00",
    "toolDiffRemoved": "#ff0000",
    "toolDiffContext": "secondary",
    "syntaxComment": "secondary",
    "syntaxKeyword": "primary",
    "syntaxFunction": "#00aaff",
    "syntaxVariable": "#ffaa00",
    "syntaxString": "#00ff00",
    "syntaxNumber": "#ff00ff",
    "syntaxType": "#00aaff",
    "syntaxOperator": "primary",
    "syntaxPunctuation": "secondary",
    "thinkingOff": "secondary",
    "thinkingMinimal": "primary",
    "thinkingLow": "#00aaff",
    "thinkingMedium": "#00ffff",
    "thinkingHigh": "#ff00ff",
    "thinkingXhigh": "#ff0000",
    "bashMode": "#ffaa00"
  }
}

```

--------------------------------

### Enable TUI Debug Logging

Source: https://pi.dev/docs/latest/tui

Capture the raw ANSI stream written to stdout by setting the `PI_TUI_WRITE_LOG` environment variable to a file path. This is useful for debugging TUI rendering issues.

```bash
PI_TUI_WRITE_LOG=/tmp/tui-ansi.log npx tsx packages/tui/test/chat-simple.ts
```

--------------------------------

### Theme Text Styles

Source: https://pi.dev/docs/latest/extensions

Apply text styles such as bold, italic, and strikethrough using the theme object.

```typescript
// Text styles
theme.bold(text)
theme.italic(text)
theme.strikethrough(text)

```

--------------------------------

### Handle Model Selection Changes

Source: https://pi.dev/docs/latest/extensions

Respond to changes in the selected LLM model. This event fires when the model is changed via commands, cycling, or session restore, allowing for UI updates or model-specific initialization.

```javascript
pi.on("model_select", async (event, ctx) => {
  // event.model - newly selected model
  // event.previousModel - previous model (undefined if first selection)
  // event.source - "set" | "cycle" | "restore"

  const prev = event.previousModel
    ? `${event.previousModel.provider}/${event.previousModel.id}`
    : "none";
  const next = `${event.model.provider}/${event.model.id}`;

  ctx.ui.notify(`Model changed (${event.source}): ${prev} -> ${next}`, "info");
});
```

--------------------------------

### Extension UI Request: Set Title

Source: https://pi.dev/docs/latest/rpc

A request to set the terminal window or tab title. This is a fire-and-forget method.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-8",
  "method": "setTitle",
  "title": "pi - my project"
}
```

--------------------------------

### Send User Message with Content Array

Source: https://pi.dev/docs/latest/extensions

Send a user message that includes both text and images. The image source can be specified using base64 encoding.

```javascript
// With content array (text + images)
pi.sendUserMessage([
  { type: "text", text: "Describe this image:" },
  { type: "image", source: { type: "base64", mediaType: "image/png", data: "..." } },
]);

```

--------------------------------

### OAuthLoginCallbacks Interface

Source: https://pi.dev/docs/latest/custom-provider

Defines the callback methods available for authenticating a user during the OAuth login process. These include opening a URL, displaying a device code, or prompting the user for input.

```typescript
interface OAuthLoginCallbacks {
  // Open URL in browser (for OAuth redirects)
  onAuth(params: { url: string }): void;

  // Show device code (for device authorization flow)
  onDeviceCode(params: { userCode: string; verificationUri: string }): void;

  // Prompt user for input (for manual token entry)
  onPrompt(params: { message: string }): Promise<string>;
}

```

--------------------------------

### RPC Prompt Response

Source: https://pi.dev/docs/latest/rpc

A successful response to a 'prompt' command indicates the prompt was accepted, queued, or handled. Failures after acceptance are streamed as events.

```json
{"id": "req-1", "type": "response", "command": "prompt", "success": true}

```

--------------------------------

### Bash Command Response (Truncated Output)

Source: https://pi.dev/docs/latest/rpc

Response for a bash command where the output was truncated. Includes a `fullOutputPath` pointing to the complete log file.

```json
{
  "type": "response",
  "command": "bash",
  "success": true,
  "data": {
    "output": "truncated output...",
    "exitCode": 0,
    "cancelled": false,
    "truncated": true,
    "fullOutputPath": "/tmp/pi-bash-abc123.log"
  }
}
```

--------------------------------

### Event Bus for Extension Communication

Source: https://pi.dev/docs/latest/extensions

Utilizes a shared event bus for inter-extension communication. Use `pi.events.on` to subscribe to events and `pi.events.emit` to trigger them with associated data.

```javascript
pi.events.on("my:event", (data) => { ... });
pi.events.emit("my:event", { ... });
```

--------------------------------

### Manage Agent Session Runtime

Source: https://pi.dev/docs/latest/sdk

Handles replacement of the active runtime across various session operations. Remember to re-subscribe to events and re-bind extensions after runtime replacement.

```typescript
let session = runtime.session;
let unsubscribe = session.subscribe(() => {});

await runtime.newSession();

unsubscribe();
session = runtime.session;
unsubscribe = session.subscribe(() => {});

```

--------------------------------

### Custom Tool Call Rendering

Source: https://pi.dev/docs/latest/extensions

Implement `renderCall` to customize how tool calls are displayed in the TUI. Use `context.state` for shared state across renders.

```typescript
import { Text } from "@mariozechner/pi-tui";

renderCall(args, theme, context) {
  const text = (context.lastComponent as Text | undefined) ?? new Text("", 0, 0);
  let content = theme.fg("toolTitle", theme.bold("my_tool "));
  content += theme.fg("muted", args.action);
  if (args.text) {
    content += " " + theme.fg("dim", `"${args.text}"`);
  }
  text.setText(content);
  return text;
}
```

--------------------------------

### Register Provider with Auth Header

Source: https://pi.dev/docs/latest/custom-provider

Register a custom provider that requires an `Authorization: Bearer <key>` header by setting `authHeader: true`. This is for non-standard API key implementations.

```javascript
pi.registerProvider("custom-api", {
  baseUrl: "https://api.example.com",
  apiKey: "MY_API_KEY",
  authHeader: true,  // adds Authorization: Bearer header
  api: "openai-completions",
  models: [...] 
});


```

--------------------------------

### SessionManager Tree API Operations

Source: https://pi.dev/docs/latest/sdk

Illustrates how to interact with the SessionManager's tree structure for session traversal, label management, and branching operations.

```typescript
const sm = SessionManager.open("/path/to/session.jsonl");

// Session listing
const currentProjectSessions = await SessionManager.list(process.cwd());
const allSessions = await SessionManager.listAll(process.cwd());

// Tree traversal
const entries = sm.getEntries();        // All entries (excludes header)
const tree = sm.getTree();              // Full tree structure
const path = sm.getPath();              // Path from root to current leaf
const leaf = sm.getLeafEntry();         // Current leaf entry
const entry = sm.getEntry(id);          // Get entry by ID
const children = sm.getChildren(id);    // Direct children of entry

// Labels
const label = sm.getLabel(id);          // Get label for entry
sm.appendLabelChange(id, "checkpoint"); // Set label

// Branching
sm.branch(entryId);                     // Move leaf to earlier entry
sm.branchWithSummary(id, "Summary...");  // Branch with context summary
sm.createBranchedSession(leafId);       // Extract path to new file

```

--------------------------------

### Configure Code Block Indentation

Source: https://pi.dev/docs/latest/settings

Set the indentation string used for code blocks within markdown.

```json
{
  "markdown.codeBlockIndent": "  "
}
```

--------------------------------

### Register Command with Argument Autocompletion

Source: https://pi.dev/docs/latest/extensions

Register a command that provides argument autocompletion suggestions. The `getArgumentCompletions` function filters potential values based on user input.

```javascript
import type { AutocompleteItem } from "@mariozechner/pi-tui";

pi.registerCommand("deploy", {
  description: "Deploy to an environment",
  getArgumentCompletions: (prefix: string): AutocompleteItem[] | null => {
    const envs = ["dev", "staging", "prod"];
    const items = envs.map((e) => ({ value: e, label: e }));
    const filtered = items.filter((i) => i.value.startsWith(prefix));
    return filtered.length > 0 ? filtered : null;
  },
  handler: async (args, ctx) => {
    ctx.ui.notify(`Deploying: ${args}`, "info");
  },
});

```

--------------------------------

### Command Failure Response

Source: https://pi.dev/docs/latest/rpc

Indicates a failed command with 'success: false' and an error message.

```json
{
  "type": "response",
  "command": "set_model",
  "success": false,
  "error": "Model not found: invalid/model"
}

```

--------------------------------

### session_shutdown

Source: https://pi.dev/docs/latest/extensions

Fired before an extension runtime is torn down. Useful for cleanup and state saving.

```APIDOC
## session_shutdown

### Description
Fired before an extension runtime is torn down. Useful for cleanup and state saving.

### Event Parameters
- **event**: Object
  - **reason** (string) - The reason for shutdown: "quit" | "reload" | "new" | "resume" | "fork".
  - **targetSessionFile** (string) - The destination session file for session replacement flows.

### Context Parameters
- **ctx**: Object

### Example
```javascript
pi.on("session_shutdown", async (event, ctx) => {
  // event.reason - "quit" | "reload" | "new" | "resume" | "fork"
  // event.targetSessionFile - destination session for session replacement flows
  // Cleanup, save state, etc.
});
```
```

--------------------------------

### Custom Tool Rendering with renderShell

Source: https://pi.dev/docs/latest/extensions

Tools can use `renderShell: "self"` for complete control over framing and background behavior. This allows for custom UI elements beyond the default Box.

```typescript
pi.registerTool({
  name: "my_tool",
  label: "My Tool",
  description: "Custom shell example",
  parameters: Type.Object({}),
  renderShell: "self",
  async execute() {
    return { content: [{ type: "text", text: "ok" }], details: undefined };
  },
  renderCall(args, theme, context) {
    return new Text(theme.fg("accent", "my custom shell"), 0, 0);
  },
});
```

--------------------------------

### Register Custom Keyboard Shortcut

Source: https://pi.dev/docs/latest/extensions

Registers a custom keyboard shortcut with a specified handler function. Ensure the shortcut format is valid and the handler is an async function if it performs asynchronous operations.

```javascript
pi.registerShortcut("ctrl+shift+p", {
  description: "Toggle plan mode",
  handler: async (ctx) => {
    ctx.ui.notify("Toggled!");
  },
});
```

--------------------------------

### SessionBeforeTreeEvent Interface

Source: https://pi.dev/docs/latest/tree

Defines the structure of the `session_before_tree` event, including preparation details and the expected result for hook handlers.

```typescript
interface TreePreparation {
  targetId: string;
  oldLeafId: string | null;
  commonAncestorId: string | null;
  entriesToSummarize: SessionEntry[];
  userWantsSummary: boolean;
  customInstructions?: string;
  replaceInstructions?: boolean;
  label?: string;
}

interface SessionBeforeTreeEvent {
  type: "session_before_tree";
  preparation: TreePreparation;
  signal: AbortSignal;
}

interface SessionBeforeTreeResult {
  cancel?: boolean;
  summary?: { summary: string; details?: unknown };
  customInstructions?: string;    // Override custom instructions
  replaceInstructions?: boolean;  // Override replace mode
  label?: string;                 // Override label
}
```

--------------------------------

### RPC Steering Message Response

Source: https://pi.dev/docs/latest/rpc

A successful response to a 'steer' command confirms that the steering message was received and processed.

```json
{"type": "response", "command": "steer", "success": true}

```

--------------------------------

### BranchSummaryEntry Interface

Source: https://pi.dev/docs/latest/compaction

Defines the structure for branch summary entries, similar to CompactionEntry but includes fields for navigation context like 'fromId'.

```typescript
interface BranchSummaryEntry<T = unknown> {
  type: "branch_summary";
  id: string;
  parentId: string;
  timestamp: number;
  summary: string;
  fromId: string;      // Entry we navigated from
  fromHook?: boolean;  // true if provided by extension (legacy field name)
  details?: T;         // implementation-specific data
}

// Default branch summarization uses this for details (from branch-summarization.ts):
interface BranchSummaryDetails {
  readFiles: string[];
  modifiedFiles: string[];
}
```

--------------------------------

### Switch Session Response (Cancelled)

Source: https://pi.dev/docs/latest/rpc

Response indicating that a session switch was attempted but cancelled by an extension event handler.

```json
{"type": "response", "command": "switch_session", "success": true, "data": {"cancelled": true}}
```

--------------------------------

### Extension UI Request: Set Editor Text

Source: https://pi.dev/docs/latest/rpc

A request to set the text content within the input editor. This is a fire-and-forget method.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-9",
  "method": "set_editor_text",
  "text": "prefilled text for the user"
}
```

--------------------------------

### Tool Execution End Event

Source: https://pi.dev/docs/latest/rpc

Indicates the completion of a tool's execution. Includes the final result and a flag indicating if an error occurred.

```json
{
  "type": "tool_execution_end",
  "toolCallId": "call_abc123",
  "toolName": "bash",
  "result": {
    "content": [{"type": "text", "text": "total 48\n..."}],
    "details": {...}
  },
  "isError": false
}
```

--------------------------------

### Extension UI Request: Confirm

Source: https://pi.dev/docs/latest/rpc

A request to prompt the user for a yes/no confirmation. This is a dialog method that expects a response and includes a timeout.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-2",
  "method": "confirm",
  "title": "Clear session?",
  "message": "All messages will be lost.",
  "timeout": 5000
}
```

--------------------------------

### set_follow_up_mode

Source: https://pi.dev/docs/latest/rpc

Control how follow-up messages (from `follow_up`) are delivered.

```APIDOC
## set_follow_up_mode

### Description
Control how follow-up messages (from `follow_up`) are delivered.

### Method
set_follow_up_mode

### Request Body
- **type** (string) - Required - Must be "set_follow_up_mode"
- **mode** (string) - Required - The follow-up mode. Possible values: "all", "one-at-a-time".
  - "all": Deliver all follow-up messages when agent finishes.
  - "one-at-a-time": Deliver one follow-up message per agent completion (default).

### Request Example
```json
{"type": "set_follow_up_mode", "mode": "one-at-a-time"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "set_follow_up_mode"
- **success** (boolean) - true
```

--------------------------------

### Intercept Session Switch Events

Source: https://pi.dev/docs/latest/extensions

Use the 'session_before_switch' event to intercept new session creation or session resume actions. You can prompt the user for confirmation or cancel the action.

```javascript
pi.on("session_before_switch", async (event, ctx) => {
  // event.reason - "new" or "resume"
  // event.targetSessionFile - session we're switching to (only for "resume")

  if (event.reason === "new") {
    const ok = await ctx.ui.confirm("Clear?", "Delete all messages?");
    if (!ok) return { cancel: true };
  }
});
```

--------------------------------

### confirm

Source: https://pi.dev/docs/latest/rpc

Prompt the user for yes/no confirmation.

```APIDOC
## confirm

Prompt the user for yes/no confirmation.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-2",
  "method": "confirm",
  "title": "Clear session?",
  "message": "All messages will be lost.",
  "timeout": 5000
}
```

Expected response: `extension_ui_response` with `confirmed: true/false` or `cancelled: true`.
```

--------------------------------

### Compaction End Event

Source: https://pi.dev/docs/latest/rpc

Signifies the completion of compaction. It includes a summary, token counts, and status flags like `aborted` or `willRetry`.

```json
{
  "type": "compaction_end",
  "reason": "threshold",
  "result": {
    "summary": "Summary of conversation...",
    "firstKeptEntryId": "abc123",
    "tokensBefore": 150000,
    "details": {}
  },
  "aborted": false,
  "willRetry": false
}
```

--------------------------------

### Configure Anthropic Extra Usage Warning in Pi Settings

Source: https://pi.dev/docs/latest/settings

Control whether a warning is displayed when Anthropic subscription authentication might incur paid extra usage. Set to `false` to disable the warning.

```json
{
  "warnings": {
    "anthropicExtraUsage": false
  }
}
```

--------------------------------

### Create Custom UI Component

Source: https://pi.dev/docs/latest/extensions

Temporarily replace the editor with a custom UI component. Call `done(value)` to close the component and return a value.

```typescript
import { Text, Component } from "@mariozechner/pi-tui";

const result = await ctx.ui.custom<boolean>((tui, theme, keybindings, done) => {
  const text = new Text("Press Enter to confirm, Escape to cancel", 1, 1);

  text.onKey = (key) => {
    if (key === "return") done(true);
    if (key === "escape") done(false);
    return true;
  };

  return text;
});

if (result) {
  // User pressed Enter
}

```

--------------------------------

### Full Ollama Model Configuration

Source: https://pi.dev/docs/latest/models

Override default settings for a specific model, including its display name, reasoning capability, input types, context window size, and token limits.

```json
{
  "providers": {
    "ollama": {
      "baseUrl": "http://localhost:11434/v1",
      "api": "openai-completions",
      "apiKey": "ollama",
      "models": [
        {
          "id": "llama3.1:8b",
          "name": "Llama 3.1 8B (Local)",
          "reasoning": false,
          "input": ["text"],
          "contextWindow": 128000,
          "maxTokens": 32000,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
        }
      ]
    }
  }
}
```

--------------------------------

### Configure VS Code Integrated Terminal for Shift+Enter

Source: https://pi.dev/docs/latest/terminal-setup

Add this keybinding to your VS Code 'keybindings.json' to enable Shift+Enter for multi-line input in the integrated terminal. Ensure 'terminalFocus' is active.

```json
{
  "key": "shift+enter",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "\u001b[13;2u" },
  "when": "terminalFocus"
}
```

--------------------------------

### Detect Keyboard Input with matchesKey

Source: https://pi.dev/docs/latest/tui

Use the matchesKey function from '@mariozechner/pi-tui' to detect specific key presses, including basic keys, arrow keys, and keys with modifiers like Ctrl, Shift, and Alt.

```typescript
import { matchesKey, Key } from "@mariozechner/pi-tui";

handleInput(data: string) {
  if (matchesKey(data, Key.up)) {
    this.selectedIndex--;
  } else if (matchesKey(data, Key.enter)) {
    this.onSelect?.(this.selectedIndex);
  } else if (matchesKey(data, Key.escape)) {
    this.onCancel?.();
  } else if (matchesKey(data, Key.ctrl("c"))) {
    // Ctrl+C
  }
}

```

--------------------------------

### session_before_fork / session_clone

Source: https://pi.dev/docs/latest/extensions

Fired when forking via `/fork` or cloning via `/clone`. Allows for cancellation or modification of the fork/clone process.

```APIDOC
## session_before_fork / session_clone

### Description
Fired when forking via `/fork` or cloning via `/clone`. Allows for cancellation or modification of the fork/clone process.

### Event Parameters
- **event**: Object
  - **entryId** (string) - ID of the selected entry.
  - **position** (string) - "before" for `/fork`, "at" for `/clone`.

### Context Parameters
- **ctx**: Object

### Return Value
- **{ cancel: true }**: To cancel fork/clone.
- **{ skipConversationRestore: true }**: Reserved for future conversation restore control.

### Example
```javascript
pi.on("session_before_fork", async (event, ctx) => {
  // event.entryId - ID of the selected entry
  // event.position - "before" for /fork, "at" for /clone
  return { cancel: true }; // Cancel fork/clone
  // OR
  return { skipConversationRestore: true }; // Reserved for future conversation restore control
});
```
```

--------------------------------

### Check Context Usage

Source: https://pi.dev/docs/latest/extensions

Retrieve and check the current context usage, particularly token count, for the active model.

```javascript
const usage = ctx.getContextUsage();
if (usage && usage.tokens > 100_000) {
  // ...
}
```

--------------------------------

### Set AWS Region for Bedrock

Source: https://pi.dev/docs/latest/providers

Set the AWS region for Amazon Bedrock. Defaults to us-east-1 if not specified.

```bash
export AWS_REGION=us-west-2
```

--------------------------------

### Message Serialization Format

Source: https://pi.dev/docs/latest/compaction

Messages are serialized to text using `serializeConversation()` for summarization. Tool results are truncated to 2000 characters, with a marker indicating truncation.

```text
[User]: What they said
[Assistant thinking]: Internal reasoning
[Assistant]: Response text
[Assistant tool calls]: read(path="foo.ts"); edit(path="bar.ts", ...)
[Tool result]: Output from tool

```

--------------------------------

### AgentSessionRuntime Operations

Source: https://pi.dev/docs/latest/sdk

AgentSessionRuntime manages the replacement of the active runtime across various session operations.

```APIDOC
## AgentSessionRuntime Operations

### Description
The `AgentSessionRuntime` object manages the replacement of the active runtime for various session operations, including creating new sessions, switching sessions, forking, cloning flows, and importing from JSON.

### Key Operations
- `newSession()`: Creates a new session.
- `switchSession()`: Switches to a different session.
- `fork()`: Forks the current session.
- `fork(entryId, { position: "at" })`: Clones flows via fork.
- `importFromJsonl()`: Imports session data from a JSONL file.

### Important Behavior
- `runtime.session` is updated after these operations.
- Event subscriptions are tied to a specific `AgentSession`, requiring re-subscription after replacement.
- If using extensions, call `runtime.session.bindExtensions(...)` again for the new session.
- Creation returns diagnostics on `runtime.diagnostics`.
- Failures during creation or replacement will throw an error, requiring caller handling.

### Example Usage
```javascript
let session = runtime.session;
let unsubscribe = session.subscribe(() => {});

await runtime.newSession();

unsubscribe();
session = runtime.session;
unsubscribe = session.subscribe(() => {});
```
```

--------------------------------

### Manipulating Editor Text and Pasting

Source: https://pi.dev/docs/latest/extensions

Set prefill text in the editor, retrieve the current editor content, or paste new content, which triggers paste handling.

```javascript
// Editor text
ctx.ui.setEditorText("Prefill text");
const current = ctx.ui.getEditorText();

// Paste into editor (triggers paste handling, including collapse for large content)
ctx.ui.pasteToEditor("pasted content");

```

--------------------------------

### Extension UI Request: Set Widget

Source: https://pi.dev/docs/latest/rpc

A request to set or clear a widget displayed above or below the editor. This is a fire-and-forget method. To clear a widget, send 'widgetLines: undefined'.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-7",
  "method": "setWidget",
  "widgetKey": "my-ext",
  "widgetLines": ["--- My Widget ---", "Line 1", "Line 2"],
  "widgetPlacement": "aboveEditor"
}
```

--------------------------------

### Handle session_before_tree / session_tree

Source: https://pi.dev/docs/latest/extensions

Intercept or react to tree navigation events. Can be used to cancel navigation or provide a custom summary.

```javascript
pi.on("session_before_tree", async (event, ctx) => {
  const { preparation, signal } = event;
  return { cancel: true };
  // OR provide custom summary:
  return { summary: { summary: "...", details: {} } };
});

pi.on("session_tree", async (event, ctx) => {
  // event.newLeafId, oldLeafId, summaryEntry, fromExtension
});
```

--------------------------------

### fork

Source: https://pi.dev/docs/latest/rpc

Creates a new fork from a previous user message on the active branch. This operation can be cancelled by a `session_before_fork` extension event handler. The command returns the text of the message being forked from.

```APIDOC
## fork

### Description
Create a new fork from a previous user message on the active branch. Can be cancelled by a `session_before_fork` extension event handler. Returns the text of the message being forked from.

### Request Body
- **type** (string) - Required - Must be "fork"
- **entryId** (string) - Required - The ID of the entry to fork from

### Request Example
```json
{
  "type": "fork", 
  "entryId": "abc123"
}
```

### Response
#### Success Response (200)
- **type** (string) - The type of the response, should be "response"
- **command** (string) - The command that was executed, should be "fork"
- **success** (boolean) - Indicates if the command was successful
- **data** (object) - Contains the result of the command
  - **text** (string) - The text of the message being forked from
  - **cancelled** (boolean) - Indicates if the fork was cancelled by an extension

#### Response Example
```json
{
  "type": "response",
  "command": "fork",
  "success": true,
  "data": {"text": "The original prompt text...", "cancelled": false}
}
```

If an extension cancelled the fork:
```json
{
  "type": "response",
  "command": "fork",
  "success": true,
  "data": {"text": "The original prompt text...", "cancelled": true}
}
```
```

--------------------------------

### Cycle through thinking levels

Source: https://pi.dev/docs/latest/rpc

Cycles through the available thinking levels for the current model. Returns `null` data if the model does not support thinking levels.

```json
{"type": "cycle_thinking_level"}
```

--------------------------------

### Switch Session Response (Not Cancelled)

Source: https://pi.dev/docs/latest/rpc

Response indicating a successful session switch that was not cancelled by an extension.

```json
{"type": "response", "command": "switch_session", "success": true, "data": {"cancelled": false}}
```

--------------------------------

### Implement Custom Editor Component

Source: https://pi.dev/docs/latest/extensions

Replace the main input editor with a custom implementation by extending `CustomEditor`. Ensure to call `super.handleInput(data)` for unhandled input.

```typescript
import { CustomEditor, type ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { matchesKey } from "@mariozechner/pi-tui";

class VimEditor extends CustomEditor {
  private mode: "normal" | "insert" = "insert";

  handleInput(data: string): void {
    if (matchesKey(data, "escape") && this.mode === "insert") {
      this.mode = "normal";
      return;
    }
    if (this.mode === "normal" && data === "i") {
      this.mode = "insert";
      return;
    }
    super.handleInput(data);  // App keybindings + text editing
  }
}

export default function (pi: ExtensionAPI) {
  pi.on("session_start", (_event, ctx) => {
    ctx.ui.setEditorComponent((_tui, theme, keybindings) =>
      new VimEditor(theme, keybindings)
    );
  });
}

```

--------------------------------

### Queue Update Event

Source: https://pi.dev/docs/latest/rpc

Emitted when the pending steering or follow-up queue changes, reflecting adjustments in the agent's task prioritization or next steps.

```json
{
  "type": "queue_update",
  "steering": ["Focus on error handling"],
  "followUp": ["After that, summarize the result"]
}
```

--------------------------------

### Register and Unregister a Custom Provider

Source: https://pi.dev/docs/latest/custom-provider

Register a custom LLM provider with its API details and later remove it using `pi.unregisterProvider`. Ensure the provider name matches during unregistration.

```javascript
// Register
pi.registerProvider("my-llm", {
  baseUrl: "https://api.my-llm.com/v1",
  apiKey: "MY_LLM_API_KEY",
  api: "openai-completions",
  models: [
    {
      id: "my-llm-large",
      name: "My LLM Large",
      reasoning: true,
      input: ["text", "image"],
      cost: { input: 3.0, output: 15.0, cacheRead: 0.3, cacheWrite: 3.75 },
      contextWindow: 200000,
      maxTokens: 16384
    }
  ]
});

// Later, remove it
pi.unregisterProvider("my-llm");

```

--------------------------------

### pi.appendEntry

Source: https://pi.dev/docs/latest/extensions

Persist extension state to the session. This state does not participate in the LLM context but can be restored on reload.

```APIDOC
## pi.appendEntry(customType, data?)

### Description
Persist extension state (does NOT participate in LLM context).

### Parameters
- **customType** (string) - Required - A unique type identifier for the state.
- **data** (object) - Optional - The data to persist.
```

--------------------------------

### Define Custom Theme Interface

Source: https://pi.dev/docs/latest/tui

For custom components, define your own theme interface to specify the styling functions available for that component. This allows for component-specific theming.

```typescript
interface MyTheme {
  selected: (s: string) => string;
  normal: (s: string) => string;
}
```

--------------------------------

### Intercept session_before_tree Event

Source: https://pi.dev/docs/latest/compaction

Fired before `/tree` navigation. Can cancel navigation or provide a custom summary if the user wants one. Provides navigation targets, current position, common ancestor, entries to summarize, and user preference for summarization.

```typescript
pi.on("session_before_tree", async (event, ctx) => {
  const { preparation, signal } = event;

  // preparation.targetId - where we're navigating to
  // preparation.oldLeafId - current position (being abandoned)
  // preparation.commonAncestorId - shared ancestor
  // preparation.entriesToSummarize - entries that would be summarized
  // preparation.userWantsSummary - whether user chose to summarize

  // Cancel navigation entirely:
  return { cancel: true };

  // Provide custom summary (only used if userWantsSummary is true):
  if (preparation.userWantsSummary) {
    return {
      summary: {
        summary: "Your summary...",
        details: { /* custom data */ },
      }
    };
  }
});

```

--------------------------------

### Theme Foreground Colors

Source: https://pi.dev/docs/latest/extensions

Apply predefined foreground colors to text using the `theme.fg` function for different UI elements like tool titles, accents, status messages, and muted text.

```typescript
// Foreground colors
theme.fg("toolTitle", text)   // Tool names
theme.fg("accent", text)      // Highlights
theme.fg("success", text)     // Success (green)
theme.fg("error", text)       // Errors (red)
theme.fg("warning", text)     // Warnings (yellow)
theme.fg("muted", text)       // Secondary text
theme.fg("dim", text)         // Tertiary text

```

--------------------------------

### Customize Working Indicator

Source: https://pi.dev/docs/latest/tui

Set custom frames for the working indicator during streaming. Use an empty array to hide it, or call without arguments to restore the default spinner. Custom frames are rendered as-is, so include colors if needed.

```typescript
// Static indicator
ctx.ui.setWorkingIndicator({ frames: [ctx.ui.theme.fg("accent", "●")] });
```

```typescript
// Custom animated indicator
ctx.ui.setWorkingIndicator({
  frames: [
    ctx.ui.theme.fg("dim", "·"),
    ctx.ui.theme.fg("muted", "•"),
    ctx.ui.theme.fg("accent", "●"),
    ctx.ui.theme.fg("muted", "•"),
  ],
  intervalMs: 120,
});
```

```typescript
// Hide the indicator entirely
ctx.ui.setWorkingIndicator({ frames: [] });
```

```typescript
// Restore pi's default spinner
ctx.ui.setWorkingIndicator();
```

--------------------------------

### Access Session State with ctx.sessionManager

Source: https://pi.dev/docs/latest/extensions

Retrieve session entries, the current branch, or the current leaf entry ID using the session manager.

```javascript
ctx.sessionManager.getEntries()       // All entries
ctx.sessionManager.getBranch()        // Current branch
ctx.sessionManager.getLeafId()        // Current leaf entry ID
```

--------------------------------

### Theme Format Structure

Source: https://pi.dev/docs/latest/themes

A Pi theme is defined by a JSON object including a name, optional variables for reuse, and a comprehensive list of color tokens. The '$schema' field is crucial for editor support.

```json
{
  "$schema": "https://raw.githubusercontent.com/badlogic/pi-mono/main/packages/coding-agent/src/modes/interactive/theme/theme-schema.json",
  "name": "my-theme",
  "vars": {
    "blue": "#0066cc",
    "gray": 242
  },
  "colors": {
    "accent": "blue",
    "muted": "gray",
    "text": "",
    ...
  }
}

```

--------------------------------

### Set steering message mode

Source: https://pi.dev/docs/latest/rpc

Controls how steering messages are delivered. 'all' delivers them after tool calls, while 'one-at-a-time' delivers one per turn.

```json
{"type": "set_steering_mode", "mode": "one-at-a-time"}
```

--------------------------------

### CompactionEntry

Source: https://pi.dev/docs/latest/session

Indicates that the session's context has been compacted to save space. Stores a summary of earlier messages, the ID of the first kept entry, and the token count before compaction.

```json
{"type":"compaction","id":"f6g7h8i9","parentId":"e5f6g7h8","timestamp":"2024-12-03T14:10:00.000Z","summary":"User discussed X, Y, Z...","firstKeptEntryId":"c3d4e5f6","tokensBefore":50000}
```

--------------------------------

### Highlight Code with Explicit Language

Source: https://pi.dev/docs/latest/extensions

Highlight a code string using a specified language and theme.

```typescript
import { highlightCode, getLanguageFromPath } from "@mariozechner/pi-coding-agent";

// Highlight code with explicit language
const highlighted = highlightCode("const x = 1;", "typescript", theme);

```

--------------------------------

### Set or Clear Entry Label

Source: https://pi.dev/docs/latest/extensions

Set or clear a user-defined label on a specific entry for bookmarking and navigation. Labels persist across session restarts and can be read via `ctx.sessionManager.getLabel()`.

```javascript
// Set a label
pi.setLabel(entryId, "checkpoint-before-refactor");

// Clear a label
pi.setLabel(entryId, undefined);

// Read labels via sessionManager
const label = ctx.sessionManager.getLabel(entryId);

```

--------------------------------

### Managing Editor Widgets

Source: https://pi.dev/docs/latest/extensions

Display custom content as widgets above or below the editor, or clear them. Widgets can be simple text arrays or custom TUI components.

```javascript
// Widget above editor (default)
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"]);
// Widget below editor
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"], { placement: "belowEditor" });
ctx.ui.setWidget("my-widget", (tui, theme) => new Text(theme.fg("accent", "Custom"), 0, 0));
ctx.ui.setWidget("my-widget", undefined);  // Clear

```

--------------------------------

### clone

Source: https://pi.dev/docs/latest/rpc

Duplicates the current active branch into a new session at the current position. This operation can be cancelled by a `session_before_fork` extension event handler.

```APIDOC
## clone

### Description
Duplicate the current active branch into a new session at the current position. Can be cancelled by a `session_before_fork` extension event handler.

### Request Body
- **type** (string) - Required - Must be "clone"

### Request Example
```json
{
  "type": "clone"
}
```

### Response
#### Success Response (200)
- **type** (string) - The type of the response, should be "response"
- **command** (string) - The command that was executed, should be "clone"
- **success** (boolean) - Indicates if the command was successful
- **data** (object) - Contains the result of the command
  - **cancelled** (boolean) - Indicates if the clone was cancelled by an extension

#### Response Example
```json
{
  "type": "response",
  "command": "clone",
  "success": true,
  "data": {"cancelled": false}
}
```

If an extension cancelled the clone:
```json
{
  "type": "response",
  "command": "clone",
  "success": true,
  "data": {"cancelled": true}
}
```
```

--------------------------------

### Send Simple User Message

Source: https://pi.dev/docs/latest/extensions

Send a basic text message as if typed by the user. This always triggers a new turn.

```javascript
// Simple text message
pi.sendUserMessage("What is 2+2?");

```

--------------------------------

### Merge Custom Models into Built-in Provider

Source: https://pi.dev/docs/latest/models

Extend a built-in provider by adding custom models. This configuration merges custom models with existing ones, allowing for model upserts or additions.

```json
{
  "providers": {
    "anthropic": {
      "baseUrl": "https://my-proxy.example.com/v1",
      "apiKey": "ANTHROPIC_API_KEY",
      "api": "anthropic-messages",
      "models": [...] 
    }
  }
}

```

--------------------------------

### Parse Session JSONL File

Source: https://pi.dev/docs/latest/session

Reads a session file line by line, parses each JSON entry, and logs details based on the entry type. Handles various session entry types including session info, messages, and metadata changes.

```typescript
import { readFileSync } from "fs";

const lines = readFileSync("session.jsonl", "utf8").trim().split("\n");

for (const line of lines) {
  const entry = JSON.parse(line);

  switch (entry.type) {
    case "session":
      console.log(`Session v${entry.version ?? 1}: ${entry.id}`);
      break;
    case "message":
      console.log(`[${entry.id}] ${entry.message.role}: ${JSON.stringify(entry.message.content)}`);
      break;
    case "compaction":
      console.log(`[${entry.id}] Compaction: ${entry.tokensBefore} tokens summarized`);
      break;
    case "branch_summary":
      console.log(`[${entry.id}] Branch from ${entry.fromId}`);
      break;
    case "custom":
      console.log(`[${entry.id}] Custom (${entry.customType}): ${JSON.stringify(entry.data)}`);
      break;
    case "custom_message":
      console.log(`[${entry.id}] Extension message (${entry.customType}): ${entry.content}`);
      break;
    case "label":
      console.log(`[${entry.id}] Label "${entry.label}" on ${entry.targetId}`);
      break;
    case "model_change":
      console.log(`[${entry.id}] Model: ${entry.provider}/${entry.modelId}`);
      break;
    case "thinking_level_change":
      console.log(`[${entry.id}] Thinking: ${entry.thinkingLevel}`);
      break;
  }
}

```

--------------------------------

### setStatus

Source: https://pi.dev/docs/latest/rpc

Set or clear a status entry in the footer/status bar. Fire-and-forget.

```APIDOC
## setStatus

Set or clear a status entry in the footer/status bar. Fire-and-forget.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-6",
  "method": "setStatus",
  "statusKey": "my-ext",
  "statusText": "Turn 3 running..."
}
```

Send `statusText: undefined` (or omit it) to clear the status entry for that key.
```

--------------------------------

### Legacy Ghostty Mapping (Remove if not needed)

Source: https://pi.dev/docs/latest/terminal-setup

Older versions of Pi might have added this mapping. It sends a raw linefeed byte which can interfere with tmux and Pi's interpretation of Shift+Enter. Remove if Claude Code 2.x or newer is the only reason for this mapping, unless using Claude Code in tmux.

```shell
keybind = shift+enter=text:\n
```

--------------------------------

### Create Spacer Component

Source: https://pi.dev/docs/latest/tui

Add empty vertical space using the Spacer component, specifying the number of empty lines required.

```typescript
const spacer = new Spacer(2);  // 2 empty lines

```

--------------------------------

### Auto Retry End Event (Success)

Source: https://pi.dev/docs/latest/rpc

Indicates that an automatic retry attempt was successful. It includes the attempt number that succeeded.

```json
{
  "type": "auto_retry_end",
  "success": true,
  "attempt": 2
}
```

--------------------------------

### Session Statistics Response

Source: https://pi.dev/docs/latest/rpc

Detailed response containing session statistics, including message counts, token usage, cost, and context window utilization.

```json
{
  "type": "response",
  "command": "get_session_stats",
  "success": true,
  "data": {
    "sessionFile": "/path/to/session.jsonl",
    "sessionId": "abc123",
    "userMessages": 5,
    "assistantMessages": 5,
    "toolCalls": 12,
    "toolResults": 12,
    "totalMessages": 22,
    "tokens": {
      "input": 50000,
      "output": 10000,
      "cacheRead": 40000,
      "cacheWrite": 5000,
      "total": 105000
    },
    "cost": 0.45,
    "contextUsage": {
      "tokens": 60000,
      "contextWindow": 200000,
      "percent": 30
    }
  }
}
```

--------------------------------

### Set Automatic Compaction

Source: https://pi.dev/docs/latest/rpc

Enable or disable automatic context compaction when the context is nearly full. This helps manage token usage without manual intervention.

```json
{"type": "set_auto_compaction", "enabled": true}
```

--------------------------------

### pi.unregisterProvider(name)

Source: https://pi.dev/docs/latest/extensions

Removes a previously registered provider and its models. Built-in models that were overridden by the provider are restored. Has no effect if the provider was not registered. Takes effect immediately.

```APIDOC
## pi.unregisterProvider(name)

### Description
Remove a previously registered provider and its models. Built-in models that were overridden by the provider are restored. Has no effect if the provider was not registered.
Like `registerProvider`, this takes effect immediately when called after the initial load phase, so a `/reload` is not required.

### Parameters
* `name` (string) - The name of the provider to unregister.

### Request Example
```javascript
pi.registerCommand("my-setup-teardown", {
  description: "Remove the custom proxy provider",
  handler: async (_args, _ctx) => {
    pi.unregisterProvider("my-proxy");
  },
});
```
```

--------------------------------

### Extract Page Content with Brave Search Skill

Source: https://pi.dev/docs/latest/skills

Extract the content of a given URL using the Brave Search skill's content extraction functionality.

```bash
./content.js https://example.com
```

--------------------------------

### CustomMessageEntry

Source: https://pi.dev/docs/latest/session

Extension-injected messages that participate in LLM context. They have a 'customType', 'content', and a 'display' flag. Optional 'details' can hold extension-specific metadata.

```json
{"type":"custom_message","id":"i9j0k1l2","parentId":"h8i9j0k1","timestamp":"2024-12-03T14:25:00.000Z","customType":"my-extension","content":"Injected context...","display":true}
```

--------------------------------

### Explicit Follow-Up Message

Source: https://pi.dev/docs/latest/sdk

Queue a follow-up message to be delivered only when the agent stops. This expands file-based prompt templates but errors on extension commands.

```typescript
// Wait for agent to finish (delivered only when agent stops)
await session.followUp("After you're done, also do this");

```

--------------------------------

### Hook Events

Source: https://pi.dev/docs/latest/tree

Events that can be hooked into for custom behavior during tree navigation.

```APIDOC
## Hook Events

### `session_before_tree`

#### Description
This event is fired before the tree navigation occurs. Extensions can intercept and modify navigation parameters or provide a custom summary.

#### Interface
```typescript
interface TreePreparation {
  targetId: string;
  oldLeafId: string | null;
  commonAncestorId: string | null;
  entriesToSummarize: SessionEntry[];
  userWantsSummary: boolean;
  customInstructions?: string;
  replaceInstructions?: boolean;
  label?: string;
}

interface SessionBeforeTreeEvent {
  type: "session_before_tree";
  preparation: TreePreparation;
  signal: AbortSignal;
}

interface SessionBeforeTreeResult {
  cancel?: boolean;
  summary?: { summary: string; details?: unknown };
  customInstructions?: string;    // Override custom instructions
  replaceInstructions?: boolean;  // Override replace mode
  label?: string;                 // Override label
}
```

### `session_tree`

#### Description
This event is fired after the tree navigation has completed.

#### Interface
```typescript
interface SessionTreeEvent {
  type: "session_tree";
  newLeafId: string | null;
  oldLeafId: string | null;
  summaryEntry?: BranchSummaryEntry;
  fromHook?: boolean;
}
```

### Example: Custom Summarizer

#### Description
An example demonstrating how to use the `session_before_tree` hook to implement a custom summarizer.

#### Code
```javascript
export default function(pi: HookAPI) {
  pi.on("session_before_tree", async (event, ctx) => {
    if (!event.preparation.userWantsSummary) return;
    if (event.preparation.entriesToSummarize.length === 0) return;
    
    const summary = await myCustomSummarizer(event.preparation.entriesToSummarize);
    return { summary: { summary, details: { custom: true } } };
  });
}
```
```

--------------------------------

### Execute Shell Command

Source: https://pi.dev/docs/latest/extensions

Executes a shell command with specified arguments and optional options like signals or timeouts. The result object contains stdout, stderr, exit code, and a killed status.

```javascript
const result = await pi.exec("git", ["status"], { signal, timeout: 5000 });
// result.stdout, result.stderr, result.code, result.killed
```

--------------------------------

### setWidget

Source: https://pi.dev/docs/latest/rpc

Set or clear a widget (block of text lines) displayed above or below the editor. Fire-and-forget.

```APIDOC
## setWidget

Set or clear a widget (block of text lines) displayed above or below the editor. Fire-and-forget.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-7",
  "method": "setWidget",
  "widgetKey": "my-ext",
  "widgetLines": ["--- My Widget ---", "Line 1", "Line 2"],
  "widgetPlacement": "aboveEditor"
}
```

Send `widgetLines: undefined` (or omit it) to clear the widget. The `widgetPlacement` field is `"aboveEditor"` (default) or `"belowEditor"`. Only string arrays are supported in RPC mode; component factories are ignored.
```

--------------------------------

### Export HTML Response

Source: https://pi.dev/docs/latest/rpc

Response indicating the successful export of the session to an HTML file, including the path to the generated file.

```json
{
  "type": "response",
  "command": "export_html",
  "success": true,
  "data": {"path": "/tmp/session.html"}
}
```

--------------------------------

### notify

Source: https://pi.dev/docs/latest/rpc

Display a notification. Fire-and-forget, no response expected.

```APIDOC
## notify

Display a notification. Fire-and-forget, no response expected.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-5",
  "method": "notify",
  "message": "Command blocked by user",
  "notifyType": "warning"
}
```

The `notifyType` field is `"info"`, `"warning"`, or `"error"`. Defaults to `"info"` if omitted.
```

--------------------------------

### Modified Enter Key Behavior

Source: https://pi.dev/docs/latest/tmux

Compares how different modified Enter keys are represented with and without tmux extended keys enabled, specifically highlighting the `csi-u` format. This table shows why `csi-u` is necessary for distinguishing these keys.

```text
Key | Without extkeys | With `csi-u`  
---|---|---
Enter | `\r` | `\r`  
Shift+Enter | `\r` | `\x1b[13;2u`  
Ctrl+Enter | `\r` | `\x1b[13;5u`  
Alt/Option+Enter | `\x1b\r` | `\x1b[13;3u`
```

--------------------------------

### pi.setLabel

Source: https://pi.dev/docs/latest/extensions

Set or clear a label on a specific entry within the session. Labels are user-defined markers for bookmarking and navigation.

```APIDOC
## pi.setLabel(entryId, label)

### Description
Set or clear a label on an entry. Labels are user-defined markers for bookmarking and navigation (shown in `/tree` selector).

### Parameters
- **entryId** (string) - Required - The ID of the entry to label.
- **label** (string | undefined) - Required - The label text to set, or undefined to clear the label.
```

--------------------------------

### BranchSummaryEntry Interface

Source: https://pi.dev/docs/latest/tree

Defines the structure for storing branch summaries, including type, IDs, timestamp, source, and the generated summary. It also includes an optional 'details' field.

```typescript
interface BranchSummaryEntry {
  type: "branch_summary";
  id: string;
  parentId: string;      // New leaf position
  timestamp: string;
  fromId: string;        // Old leaf we abandoned
  summary: string;       // LLM-generated summary
  details?: unknown;     // Optional hook data
}

```

--------------------------------

### Session Entry Base Interface

Source: https://pi.dev/docs/latest/session

Defines the base interface for all session entries, including type, ID, parent ID, and timestamp.

```typescript
interface SessionEntryBase {
  type: string;
  id: string;           // 8-char hex ID
  parentId: string | null;  // Parent entry ID (null for first entry)
  timestamp: string;    // ISO timestamp
}

```

--------------------------------

### SessionManager Tree API - Labels

Source: https://pi.dev/docs/latest/sdk

APIs for managing labels associated with session entries.

```APIDOC
## SessionManager Tree API - Labels

### Description
Methods for retrieving and setting labels for session entries.

### Usage
```typescript
const sm = SessionManager.open("/path/to/session.jsonl");

// Labels
const label = sm.getLabel(id);          // Get label for entry
sm.appendLabelChange(id, "checkpoint"); // Set label
```
```

--------------------------------

### Handling Tool Results

Source: https://pi.dev/docs/latest/extensions

Use the `tool_result` event to process and potentially modify the output of a tool execution before it's finalized. This is useful for summarizing, reformatting, or error handling.

```APIDOC
## tool_result

### Description
Fired after tool execution finishes and before `tool_execution_end` plus the final tool result message events are emitted. **Can modify result.**

### Method
`pi.on("tool_result", async (event, ctx) => { ... });`

### Parameters
- **event**: An object containing event details.
  - **event.toolName** (string): The name of the tool that executed.
  - **event.toolCallId** (string): The unique identifier for the tool call.
  - **event.input**: The input parameters used for the tool call.
  - **event.content**: The primary output content of the tool.
  - **event.details**: Additional details about the tool execution.
  - **event.isError** (boolean): Indicates if the tool execution resulted in an error.
- **ctx**: The context object, including `ctx.signal` for aborting nested async operations.

### Behavior Guarantees
- Handlers run in extension load order.
- Each handler sees the latest result after previous handler changes.
- Handlers can return partial patches (`content`, `details`, or `isError`); omitted fields keep their current values.

### Example
```javascript
import { isBashToolResult } from "@mariozechner/pi-coding-agent";

pi.on("tool_result", async (event, ctx) => {
  // event.toolName, event.toolCallId, event.input
  // event.content, event.details, event.isError

  if (isBashToolResult(event)) {
    // event.details is typed as BashToolDetails
  }

  const response = await fetch("https://example.com/summarize", {
    method: "POST",
    body: JSON.stringify({ content: event.content }),
    signal: ctx.signal,
  });

  // Modify result:
  return { content: [...], details: {...}, isError: false };
});
```
```

--------------------------------

### LabelEntry

Source: https://pi.dev/docs/latest/session

A user-defined bookmark or marker on a specific session entry. It includes the target entry ID and the label text. Labels can be cleared by setting the label value to undefined.

```json
{"type":"label","id":"j0k1l2m3","parentId":"i9j0k1l2","timestamp":"2024-12-03T14:30:00.000Z","targetId":"a1b2c3d4","label":"checkpoint-1"}
```

--------------------------------

### After Provider Response Event

Source: https://pi.dev/docs/latest/extensions

Fired after an HTTP response is received and before its stream body is consumed. Allows inspection of response status and headers.

```APIDOC
#### after_provider_response

Fired after an HTTP response is received and before its stream body is consumed. Handlers run in extension load order.
```javascript
pi.on("after_provider_response", (event, ctx) => {
  // event.status - HTTP status code
  // event.headers - normalized response headers
  if (event.status === 429) {
    console.log("rate limited", event.headers["retry-after"]);
  }
});

```

Header availability depends on provider and transport. Providers that abstract HTTP responses may not expose headers.
```

--------------------------------

### Bash Execution Message Format for LLM

Source: https://pi.dev/docs/latest/rpc

Format of the BashExecutionMessage when transformed into a UserMessage for the LLM, including the command and its output.

```markdown
Ran `ls -la`
```
total 48
drwxr-xr-x ...
```
```

--------------------------------

### SessionManager Tree API - Traversal

Source: https://pi.dev/docs/latest/sdk

Methods for traversing the session tree structure, retrieving entries, paths, and children.

```APIDOC
## SessionManager Tree API - Traversal

### Description
Functions for navigating and retrieving data from the session tree structure.

### Usage
```typescript
const sm = SessionManager.open("/path/to/session.jsonl");

// Tree traversal
const entries = sm.getEntries();        // All entries (excludes header)
const tree = sm.getTree();              // Full tree structure
const path = sm.getPath();              // Path from root to current leaf
const leaf = sm.getLeafEntry();         // Current leaf entry
const entry = sm.getEntry(id);          // Get entry by ID
const children = sm.getChildren(id);    // Direct children of entry
```
```

--------------------------------

### Custom Summarization with External Model

Source: https://pi.dev/docs/latest/compaction

Converts AgentMessages to LLM-compatible messages and serializes them to text using `serializeConversation`. This text can then be sent to an external model for summarization.

```typescript
import { convertToLlm, serializeConversation } from "@mariozechner/pi-coding-agent";

pi.on("session_before_compact", async (event, ctx) => {
  const { preparation } = event;
  
  // Convert AgentMessage[] to Message[], then serialize to text
  const conversationText = serializeConversation(
    convertToLlm(preparation.messagesToSummarize)
  );
  // Returns:
  // [User]: message text
  // [Assistant thinking]: thinking content
  // [Assistant]: response text
  // [Assistant tool calls]: read(path="..."); bash(command="...")
  // [Tool result]: output text

  // Now send to your model for summarization
  const summary = await myModel.summarize(conversationText);
  
  return {
    compaction: {
      summary,
      firstKeptEntryId: preparation.firstKeptEntryId,
      tokensBefore: preparation.tokensBefore,
    }
  };
});

```

--------------------------------

### Managing UI Status and Working Messages

Source: https://pi.dev/docs/latest/extensions

Set persistent status messages in the footer or temporary working messages during operations. Clear or reset them as needed.

```javascript
// Status in footer (persistent until cleared)
ctx.ui.setStatus("my-ext", "Processing...");
ctx.ui.setStatus("my-ext", undefined);  // Clear

// Working loader (shown during streaming)
ctx.ui.setWorkingMessage("Thinking deeply...");
ctx.ui.setWorkingMessage();  // Restore default
ctx.ui.setWorkingVisible(false);  // Hide the built-in working loader row entirely
ctx.ui.setWorkingVisible(true);   // Show the built-in working loader row

```

--------------------------------

### ThinkingLevelChangeEntry

Source: https://pi.dev/docs/latest/session

Logs a change in the reasoning or thinking level for the session. Includes the entry ID, parent ID, timestamp, and the new thinking level.

```json
{"type":"thinking_level_change","id":"e5f6g7h8","parentId":"d4e5f6g7","timestamp":"2024-12-03T14:06:00.000Z","thinkingLevel":"high"}
```

--------------------------------

### Extension UI Cancellation Response

Source: https://pi.dev/docs/latest/rpc

Used to dismiss any dialog method. The extension receives 'undefined' or 'false'.

```json
{"type": "extension_ui_response", "id": "uuid-3", "cancelled": true}

```

--------------------------------

### Compaction Summary Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for messages summarizing session compaction, including token count before compaction.

```typescript
interface CompactionSummaryMessage {
  role: "compactionSummary";
  summary: string;
  tokensBefore: number;
  timestamp: number;
}

```

--------------------------------

### Clone the current session

Source: https://pi.dev/docs/latest/rpc

Duplicates the current active branch into a new session. Can be cancelled by a session_before_fork extension event handler.

```json
{"type": "clone"}
```

```json
{
  "type": "response",
  "command": "clone",
  "success": true,
  "data": {"cancelled": false}
}
```

```json
{
  "type": "response",
  "command": "clone",
  "success": true,
  "data": {"cancelled": true}
}
```

--------------------------------

### Agent Completion Event

Source: https://pi.dev/docs/latest/rpc

Emitted when the agent finishes its task. It includes all messages generated during the run.

```json
{
  "type": "agent_end",
  "messages": [...] 
}
```

--------------------------------

### Assistant Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for messages from the assistant, including content, API details, model information, usage, and stop reason.

```typescript
interface AssistantMessage {
  role: "assistant";
  content: (TextContent | ThinkingContent | ToolCall)[];
  api: string;
  provider: string;
  model: string;
  usage: Usage;
  stopReason: "stop" | "length" | "toolUse" | "error" | "aborted";
  errorMessage?: string;
  timestamp: number;
}

```

--------------------------------

### SessionManager Tree API - Branching

Source: https://pi.dev/docs/latest/sdk

Functions for branching sessions, including moving the leaf to an earlier entry or creating new branched sessions.

```APIDOC
## SessionManager Tree API - Branching

### Description
Operations related to branching the session tree, allowing for session history manipulation.

### Usage
```typescript
const sm = SessionManager.open("/path/to/session.jsonl");

// Branching
sm.branch(entryId);                     // Move leaf to earlier entry
sm.branchWithSummary(id, "Summary...");  // Branch with context summary
sm.createBranchedSession(leafId);       // Extract path to new file
```
```

--------------------------------

### ModelChangeEntry

Source: https://pi.dev/docs/latest/session

Records a change in the language model used during a session. Includes the entry ID, parent ID, timestamp, and the new provider and model ID.

```json
{"type":"model_change","id":"d4e5f6g7","parentId":"c3d4e5f6","timestamp":"2024-12-03T14:05:00.000Z","provider":"openai","modelId":"gpt-4o"}
```

--------------------------------

### Register Custom Model Provider

Source: https://pi.dev/docs/latest/extensions

Register a new model provider with custom models, including configuration for base URL, API key, API type, and model definitions. Supports custom OAuth flows for authentication.

```javascript
pi.registerProvider("my-proxy", {
  baseUrl: "https://proxy.example.com",
  apiKey: "PROXY_API_KEY",  // env var name or literal
  api: "anthropic-messages",
  models: [
    {
      id: "claude-sonnet-4-20250514",
      name: "Claude 4 Sonnet (proxy)",
      reasoning: false,
      input: ["text", "image"],
      cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
      contextWindow: 200000,
      maxTokens: 16384
    }
  ]
});
```

```javascript
// Override baseUrl for an existing provider (keeps all models)
pi.registerProvider("anthropic", {
  baseUrl: "https://proxy.example.com"
});
```

```javascript
// Register provider with OAuth support for /login
pi.registerProvider("corporate-ai", {
  baseUrl: "https://ai.corp.com",
  api: "openai-responses",
  models: [...],
  oauth: {
    name: "Corporate AI (SSO)",
    async login(callbacks) {
      // Custom OAuth flow
      callbacks.onAuth({ url: "https://sso.corp.com/તાઓ"
      const code = await callbacks.onPrompt({ message: "Enter code:" });
      return { refresh: code, access: code, expires: Date.now() + 3600000 };
    },
    async refreshToken(credentials) {
      // Refresh logic
      return credentials;
    },
    getApiKey(credentials) {
      return credentials.access;
    }
  }
});
```

--------------------------------

### SessionInfoEntry

Source: https://pi.dev/docs/latest/session

Stores session metadata, such as a user-defined display name. This name is shown in the session selector. It can be set via commands or extension APIs.

```json
{"type":"session_info","id":"k1l2m3n4","parentId":"j0k1l2m3","timestamp":"2024-12-03T14:35:00.000Z","name":"Refactor auth module"}
```

--------------------------------

### abort

Source: https://pi.dev/docs/latest/rpc

Abort the current agent operation.

```APIDOC
## abort

### Description
Abort the current agent operation.

### Method
abort

### Request Body
- **type** (string) - Required - Must be "abort"

### Request Example
```json
{"type": "abort"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "abort"
- **success** (boolean) - true
```

--------------------------------

### pi.sendMessage

Source: https://pi.dev/docs/latest/extensions

Inject a custom message into the session. This function allows for sending messages with custom types and detailed content, with options to control delivery and triggering behavior.

```APIDOC
## pi.sendMessage(message, options?)

### Description
Inject a custom message into the session.

### Parameters
#### Message Object
- **customType** (string) - Required - The custom type of the message.
- **content** (string) - Required - The main content of the message.
- **display** (boolean) - Optional - Whether to display the message.
- **details** (object) - Optional - Additional details for the message.

#### Options Object
- **deliverAs** (string) - Optional - Delivery mode: "steer" (default), "followUp", "nextTurn".
- **triggerTurn** (boolean) - Optional - If agent is idle, trigger an LLM response immediately. Only applies to "steer" and "followUp" modes.
```

--------------------------------

### Abort current agent operation

Source: https://pi.dev/docs/latest/rpc

Use this command to immediately stop the agent's current operation. A response command will be sent upon successful abortion.

```json
{"type": "abort"}
```

--------------------------------

### extension_error

Source: https://pi.dev/docs/latest/rpc

Emitted when an extension throws an error.

```APIDOC
## extension_error

Emitted when an extension throws an error.

```json
{
  "type": "extension_error",
  "extensionPath": "/path/to/extension.ts",
  "event": "tool_call",
  "error": "Error message..."
}
```
```

--------------------------------

### Explicit Steering Message

Source: https://pi.dev/docs/latest/sdk

Queue a steering message to be delivered after the current assistant turn finishes its tool calls.

```typescript
// Queue a steering message for delivery after the current assistant turn finishes its tool calls
await session.steer("New instruction");

```

--------------------------------

### get_fork_messages

Source: https://pi.dev/docs/latest/rpc

Retrieves a list of user messages that are available for forking.

```APIDOC
## get_fork_messages

### Description
Get user messages available for forking.

### Request Body
- **type** (string) - Required - Must be "get_fork_messages"

### Request Example
```json
{
  "type": "get_fork_messages"
}
```

### Response
#### Success Response (200)
- **type** (string) - The type of the response, should be "response"
- **command** (string) - The command that was executed, should be "get_fork_messages"
- **success** (boolean) - Indicates if the command was successful
- **data** (object) - Contains the result of the command
  - **messages** (array) - A list of messages available for forking
    - **entryId** (string) - The unique identifier for the message
    - **text** (string) - The content of the message

#### Response Example
```json
{
  "type": "response",
  "command": "get_fork_messages",
  "success": true,
  "data": {
    "messages": [
      {"entryId": "abc123", "text": "First prompt..."},
      {"entryId": "def456", "text": "Second prompt..."}
    ]
  }
}
```
```

--------------------------------

### Tool Execution Lifecycle Events

Source: https://pi.dev/docs/latest/extensions

These events are fired for tool execution lifecycle updates, with specific behavior noted for parallel tool mode.

```APIDOC
## tool_execution_start / tool_execution_update / tool_execution_end

Fired for tool execution lifecycle updates.
In parallel tool mode:
  * `tool_execution_start` is emitted in assistant source order during the preflight phase
  * `tool_execution_update` events may interleave across tools
  * `tool_execution_end` is emitted in tool completion order after each tool is finalized
  * final `toolResult` message events are still emitted later in assistant source order

```javascript
pi.on("tool_execution_start", async (event, ctx) => {
  // event.toolCallId, event.toolName, event.args
});

pi.on("tool_execution_update", async (event, ctx) => {
  // event.toolCallId, event.toolName, event.args, event.partialResult
});

pi.on("tool_execution_end", async (event, ctx) => {
  // event.toolCallId, event.toolName, event.result, event.isError
});
```
```

--------------------------------

### Overlay Mode Custom Component

Source: https://pi.dev/docs/latest/extensions

Render a custom UI component as a floating modal without clearing the screen. Advanced options for positioning and programmatic visibility control are available.

```typescript
const result = await ctx.ui.custom<string | null>(
  (tui, theme, keybindings, done) => new MyOverlayComponent({ onClose: done }),
  { overlay: true }
);

```

```typescript
const result = await ctx.ui.custom<string | null>(
  (tui, theme, keybindings, done) => new MyOverlayComponent({ onClose: done }),
  {
    overlay: true,
    overlayOptions: { anchor: "top-right", width: "50%", margin: 2 },
    onHandle: (handle) => { /* handle.setHidden(true/false) */ }
  }
);

```

--------------------------------

### Message Lifecycle Events

Source: https://pi.dev/docs/latest/extensions

These events are fired for message lifecycle updates, including user, assistant, and toolResult messages, as well as assistant streaming updates.

```APIDOC
## message_start / message_update / message_end

Fired for message lifecycle updates.
  * `message_start` and `message_end` fire for user, assistant, and toolResult messages.
  * `message_update` fires for assistant streaming updates.

```javascript
pi.on("message_start", async (event, ctx) => {
  // event.message
});

pi.on("message_update", async (event, ctx) => {
  // event.message
  // event.assistantMessageEvent (token-by-token stream event)
});

pi.on("message_end", async (event, ctx) => {
  // event.message
});
```
```

--------------------------------

### Parse Error Response

Source: https://pi.dev/docs/latest/rpc

Indicates a failure during command parsing, including the error details.

```json
{
  "type": "response",
  "command": "parse",
  "success": false,
  "error": "Failed to parse command: Unexpected token..."
}

```

--------------------------------

### Attachment Type Definition

Source: https://pi.dev/docs/latest/rpc

Defines the structure for attachments, including image details, base64 content, and optional extracted text or preview.

```json
{
  "id": "img1",
  "type": "image",
  "fileName": "photo.jpg",
  "mimeType": "image/jpeg",
  "size": 102400,
  "content": "base64-encoded-data...",
  "extractedText": null,
  "preview": null
}

```

--------------------------------

### Register Custom Message Renderer

Source: https://pi.dev/docs/latest/extensions

Register a custom renderer for messages with a specific `customType`. The renderer receives the message, options, and theme, and should return a TUI-renderable element.

```typescript
import { Text } from "@mariozechner/pi-tui";

pi.registerMessageRenderer("my-extension", (message, options, theme) => {
  const { expanded } = options;
  let text = theme.fg("accent", `[${message.customType}] `);
  text += message.content;

  if (expanded && message.details) {
    text += "\n" + theme.fg("dim", JSON.stringify(message.details, null, 2));
  }

  return new Text(text, 0, 0);
});

```

--------------------------------

### Register Custom OAuth Provider

Source: https://pi.dev/docs/latest/custom-provider

Register a custom OAuth provider for SSO integration. This involves defining the provider's base URL, API type, and implementing the login, refreshToken, getApiKey, and optional modifyModels methods.

```typescript
import type { OAuthCredentials, OAuthLoginCallbacks } from "@mariozechner/pi-ai";

pi.registerProvider("corporate-ai", {
  baseUrl: "https://ai.corp.com/v1",
  api: "openai-responses",
  models: [...],
  oauth: {
    name: "Corporate AI (SSO)",

    async login(callbacks: OAuthLoginCallbacks): Promise<OAuthCredentials> {
      // Option 1: Browser-based OAuth
      callbacks.onAuth({ url: "https://sso.corp.com/authorize?..." });

      // Option 2: Device code flow
      callbacks.onDeviceCode({
        userCode: "ABCD-1234",
        verificationUri: "https://sso.corp.com/device"
      });

      // Option 3: Prompt for token/code
      const code = await callbacks.onPrompt({ message: "Enter SSO code:" });

      // Exchange for tokens (your implementation)
      const tokens = await exchangeCodeForTokens(code);

      return {
        refresh: tokens.refreshToken,
        access: tokens.accessToken,
        expires: Date.now() + tokens.expiresIn * 1000
      };
    },

    async refreshToken(credentials: OAuthCredentials): Promise<OAuthCredentials> {
      const tokens = await refreshAccessToken(credentials.refresh);
      return {
        refresh: tokens.refreshToken ?? credentials.refresh,
        access: tokens.accessToken,
        expires: Date.now() + tokens.expiresIn * 1000
      };
    },

    getApiKey(credentials: OAuthCredentials): string {
      return credentials.access;
    },

    // Optional: modify models based on user's subscription
    modifyModels(models, credentials) {
      const region = decodeRegionFromToken(credentials.access);
      return models.map(m => ({
        ...m,
        baseUrl: `https://${region}.ai.corp.com/v1`
      }));
    }
  }
});

```

--------------------------------

### Override Built-in Provider Base URL

Source: https://pi.dev/docs/latest/models

Route a built-in provider, such as Anthropic, through a custom proxy by specifying a new `baseUrl`. This allows using existing models with a different endpoint without redefining them.

```json
{
  "providers": {
    "anthropic": {
      "baseUrl": "https://my-proxy.example.com/v1"
    }
  }
}

```

--------------------------------

### AssistantMessage Type Definition

Source: https://pi.dev/docs/latest/rpc

Represents a message from the assistant, including content blocks (text, thinking, tool calls), API details, usage statistics, and stop reason.

```json
{
  "role": "assistant",
  "content": [
    {"type": "text", "text": "Hello! How can I help?"},
    {"type": "thinking", "thinking": "User is greeting me..."},
    {"type": "toolCall", "id": "call_123", "name": "bash", "arguments": {"command": "ls"}}
  ],
  "api": "anthropic-messages",
  "provider": "anthropic",
  "model": "claude-sonnet-4-20250514",
  "usage": {
    "input": 100,
    "output": 50,
    "cacheRead": 0,
    "cacheWrite": 0,
    "cost": {"input": 0.0003, "output": 0.00075, "cacheRead": 0, "cacheWrite": 0, "total": 0.00105}
  },
  "stopReason": "stop",
  "timestamp": 1733234567890
}

```

--------------------------------

### cycle_thinking_level

Source: https://pi.dev/docs/latest/rpc

Cycle through available thinking levels. Returns `null` data if model doesn't support thinking.

```APIDOC
## cycle_thinking_level

### Description
Cycle through available thinking levels. Returns `null` data if model doesn't support thinking.

### Method
cycle_thinking_level

### Request Body
- **type** (string) - Required - Must be "cycle_thinking_level"

### Request Example
```json
{"type": "cycle_thinking_level"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "cycle_thinking_level"
- **success** (boolean) - true
- **data** (object or null) - Contains the new thinking level if supported.
  - **level** (string) - The new thinking level (e.g., "high").
```

--------------------------------

### Set the thinking level

Source: https://pi.dev/docs/latest/rpc

Adjusts the reasoning or thinking level for models that support this feature. Available levels range from 'off' to 'xhigh'.

```json
{"type": "set_thinking_level", "level": "high"}
```

--------------------------------

### Component Interface Definition

Source: https://pi.dev/docs/latest/tui

Defines the core interface for all TUI components, including rendering and input handling methods. Styles do not carry across lines; reapply styles per line or use wrapTextWithAnsi().

```typescript
interface Component {
  render(width: number): string[];
  handleInput?(data: string): void;
  wantsKeyRelease?: boolean;
  invalidate(): void;
}

```

--------------------------------

### set_editor_text

Source: https://pi.dev/docs/latest/rpc

Set the text in the input editor. Fire-and-forget.

```APIDOC
## set_editor_text

Set the text in the input editor. Fire-and-forget.

### Request Example
```json
{
  "type": "extension_ui_request",
  "id": "uuid-9",
  "method": "set_editor_text",
  "text": "prefilled text for the user"
}
```
```

--------------------------------

### Manual Dismissal with AbortSignal

Source: https://pi.dev/docs/latest/extensions

Use AbortSignal for manual control over dialogs, allowing differentiation between user cancellation and timeouts. Ensure to clear the timeout when the dialog is dismissed.

```javascript
const controller = new AbortController();
const timeoutId = setTimeout(() => controller.abort(), 5000);

const confirmed = await ctx.ui.confirm(
  "Timed Confirmation",
  "This dialog will auto-cancel in 5 seconds. Confirm?",
  { signal: controller.signal }
);

clearTimeout(timeoutId);

if (confirmed) {
  // User confirmed
} else if (controller.signal.aborted) {
  // Dialog timed out
} else {
  // User cancelled (pressed Escape or selected "No")
}

```

--------------------------------

### Tool Call Type

Source: https://pi.dev/docs/latest/session

Defines the structure for representing a call to a tool, including its ID, name, and arguments.

```typescript
interface ToolCall {
  type: "toolCall";
  id: string;
  name: string;
  arguments: Record<string, any>;
}

```

--------------------------------

### pi.registerMessageRenderer(customType, renderer)

Source: https://pi.dev/docs/latest/extensions

Registers a custom Text User Interface (TUI) renderer for messages of a specified custom type.

```APIDOC
## pi.registerMessageRenderer(customType, renderer)

### Description
Register a custom TUI renderer for messages with your `customType`. See Custom UI.

### Parameters
- **customType** (string) - The custom type of the message to render.
- **renderer** (function) - The function to use for rendering the message.
```

--------------------------------

### Extension UI Request: Notify

Source: https://pi.dev/docs/latest/rpc

A request to display a notification to the user. This is a fire-and-forget method and does not expect a response. The 'notifyType' can be 'info', 'warning', or 'error'.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-5",
  "method": "notify",
  "message": "Command blocked by user",
  "notifyType": "warning"
}
```

--------------------------------

### Handle User Bash Events with pi

Source: https://pi.dev/docs/latest/extensions

Intercept user-executed bash commands (`!` or `!!`). You can provide custom operations (e.g., SSH), wrap pi's built-in local bash backend with modifications, or completely replace the bash execution by returning a result directly.

```typescript
import { createLocalBashOperations } from "@mariozechner/pi-coding-agent";

pi.on("user_bash", (event, ctx) => {
  // event.command - the bash command
  // event.excludeFromContext - true if !! prefix
  // event.cwd - working directory

  // Option 1: Provide custom operations (e.g., SSH)
  return { operations: remoteBashOps };

  // Option 2: Wrap pi's built-in local bash backend
  const local = createLocalBashOperations();
  return {
    operations: {
      exec(command, cwd, options) {
        return local.exec(`source ~/.profile\n${command}`, cwd, options);
      }
    }
  };

  // Option 3: Full replacement - return result directly
  return { result: { output: "...", exitCode: 0, cancelled: false, truncated: false } };
});

```

--------------------------------

### Override Existing Provider Configurations

Source: https://pi.dev/docs/latest/custom-provider

Modify an existing provider's endpoint or add custom headers without redefining its models. This is useful for proxying requests or adding authentication tokens.

```typescript
// All Anthropic requests now go through your proxy
pi.registerProvider("anthropic", {
  baseUrl: "https://proxy.example.com"
});

// Add custom headers to OpenAI requests
pi.registerProvider("openai", {
  headers: {
    "X-Custom-Header": "value"
  }
});

// Both baseUrl and headers
pi.registerProvider("google", {
  baseUrl: "https://ai-gateway.corp.com/google",
  headers: {
    "X-Corp-Auth": "CORP_AUTH_TOKEN"  // env var or literal
  }
});

```

--------------------------------

### Set Current Model

Source: https://pi.dev/docs/latest/extensions

Sets the active language model for the session. Returns false if no API key is configured for the specified model. Ensure the model object is valid and available in the `modelRegistry`.

```javascript
const model = ctx.modelRegistry.find("anthropic", "claude-sonnet-4-5");
if (model) {
  const success = await pi.setModel(model);
  if (!success) {
    ctx.ui.notify("No API key for this model", "error");
  }
}
```

--------------------------------

### Set session name

Source: https://pi.dev/docs/latest/rpc

Assigns a display name to the current session for easier identification in session listings.

```json
{"type": "set_session_name", "name": "my-feature-work"}
```

```json
{
  "type": "response",
  "command": "set_session_name",
  "success": true
}
```

--------------------------------

### Set Session Display Name

Source: https://pi.dev/docs/latest/extensions

Set a custom display name for the current session, which will be shown in the session selector instead of the first message.

```javascript
pi.setSessionName("Refactor auth module");

```

--------------------------------

### pi.setSessionName

Source: https://pi.dev/docs/latest/extensions

Set the session display name, which will be shown in the session selector instead of the first message.

```APIDOC
## pi.setSessionName(name)

### Description
Set the session display name (shown in session selector instead of first message).

### Parameters
- **name** (string) - Required - The desired session name.
```

--------------------------------

### Set Widgets Above/Below Editor

Source: https://pi.dev/docs/latest/tui

Display persistent content above or below the input editor. Widgets can be simple strings or renderable objects returned by a factory function. Use `undefined` to clear.

```typescript
// Simple string array (above editor by default)
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"]);
```

```typescript
// Render below the editor
ctx.ui.setWidget("my-widget", ["Line 1", "Line 2"], { placement: "belowEditor" });
```

```typescript
// Or with theme
ctx.ui.setWidget("my-widget", (_tui, theme) => {
  const lines = items.map((item, i) =>
    item.done
      ? theme.fg("success", "✓ ") + theme.fg("muted", item.text)
      : theme.fg("dim", "○ ") + item.text
  );
  return {
    render: () => lines,
    invalidate: () => {},
  };
});
```

```typescript
// Clear
ctx.ui.setWidget("my-widget", undefined);
```

--------------------------------

### Auto Retry End Event (Final Failure)

Source: https://pi.dev/docs/latest/rpc

Signifies that all automatic retry attempts have been exhausted without success. It includes the final attempt number and the ultimate error encountered.

```json
{
  "type": "auto_retry_end",
  "success": false,
  "attempt": 3,
  "finalError": "529 overloaded_error: Overloaded"
}
```

--------------------------------

### Set Automatic Retry

Source: https://pi.dev/docs/latest/rpc

Enable or disable automatic retries for transient errors such as overload, rate limiting, or 5xx server errors. This improves resilience to temporary issues.

```json
{"type": "set_auto_retry", "enabled": true}
```

--------------------------------

### Custom Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for custom messages used by extensions, including type, content, and display flag.

```typescript
interface CustomMessage {
  role: "custom";
  customType: string;            // Extension identifier
  content: string | (TextContent | ImageContent)[];
  display: boolean;              // Show in TUI
  details?: any;                 // Extension-specific metadata
  timestamp: number;
}

```

--------------------------------

### Branch Summary Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for messages summarizing a branched session entry.

```typescript
interface BranchSummaryMessage {
  role: "branchSummary";
  summary: string;
  fromId: string;                // Entry we branched from
  timestamp: number;
}

```

--------------------------------

### Send Custom Message

Source: https://pi.dev/docs/latest/extensions

Send a message with a custom type that can be rendered by a registered renderer. Include `details` for additional information available in the renderer.

```typescript
pi.sendMessage({
  customType: "my-extension",  // Matches registerMessageRenderer
  content: "Status update",
  display: true,               // Show in TUI
  details: { ... },            // Available in renderer
});

```

--------------------------------

### Session Header JSON Format

Source: https://pi.dev/docs/latest/json

The first line of the JSON event stream is the session header, containing metadata about the session.

```json
{"type":"session","version":3,"id":"uuid","timestamp":"...","cwd":"/path"}

```

--------------------------------

### Subscribe to Agent Events

Source: https://pi.dev/docs/latest/sdk

Subscribe to various agent events to receive streaming output, lifecycle notifications, and tool execution status. Handles message updates, tool calls, and agent/turn lifecycle events.

```typescript
session.subscribe((event) => {
  switch (event.type) {
    // Streaming text from assistant
    case "message_update":
      if (event.assistantMessageEvent.type === "text_delta") {
        process.stdout.write(event.assistantMessageEvent.delta);
      }
      if (event.assistantMessageEvent.type === "thinking_delta") {
        // Thinking output (if thinking enabled)
      }
      break;
    
    // Tool execution
    case "tool_execution_start":
      console.log(`Tool: ${event.toolName}`);
      break;
    case "tool_execution_update":
      // Streaming tool output
      break;
    case "tool_execution_end":
      console.log(`Result: ${event.isError ? "error" : "success"}`);
      break;
    
    // Message lifecycle
    case "message_start":
      // New message starting
      break;
    case "message_end":
      // Message complete
      break;
    
    // Agent lifecycle
    case "agent_start":
      // Agent started processing prompt
      break;
    case "agent_end":
      // Agent finished (event.messages contains new messages)
      break;
    
    // Turn lifecycle (one LLM response + tool calls)
    case "turn_start":
      break;
    case "turn_end":
      // event.message: assistant response
      // event.toolResults: tool results from this turn
      break;
    
    // Session events (queue, compaction, retry)
    case "queue_update":
      console.log(event.steering, event.followUp);
      break;
    case "compaction_start":
    case "compaction_end":
    case "auto_retry_start":
    case "auto_retry_end":
      break;
  }
});
```

--------------------------------

### SessionTreeEvent Interface

Source: https://pi.dev/docs/latest/tree

Defines the structure of the `session_tree` event, which is fired after the session tree has been updated.

```typescript
interface SessionTreeEvent {
  type: "session_tree";
  newLeafId: string | null;
  oldLeafId: string | null;
  summaryEntry?: BranchSummaryEntry;
  fromHook?: boolean;
}
```

--------------------------------

### Handle Tool Calls with pi

Source: https://pi.dev/docs/latest/extensions

Intercept and modify tool call arguments before execution. Use `isToolCallEventType` to filter by tool name and type. Mutations to `event.input` directly affect the tool execution. Return `{ block: true, reason?: string }` to prevent execution.

```typescript
import { isToolCallEventType } from "@mariozechner/pi-coding-agent";

pi.on("tool_call", async (event, ctx) => {
  // event.toolName - "bash", "read", "write", "edit", etc.
  // event.toolCallId
  // event.input - tool parameters (mutable)

  // Built-in tools: no type params needed
  if (isToolCallEventType("bash", event)) {
    // event.input is { command: string; timeout?: number }
    event.input.command = `source ~/.profile\n${event.input.command}`;

    if (event.input.command.includes("rm -rf")) {
      return { block: true, reason: "Dangerous command" };
    }
  }

  if (isToolCallEventType("read", event)) {
    // event.input is { path: string; offset?: number; limit?: number }
    console.log(`Reading: ${event.input.path}`);
  }
});

```

--------------------------------

### Thinking Content Block Type

Source: https://pi.dev/docs/latest/session

Defines the structure for 'thinking' content, often used to represent intermediate processing steps.

```typescript
interface ThinkingContent {
  type: "thinking";
  thinking: string;
}

```

--------------------------------

### Wait for Agent to Be Idle

Source: https://pi.dev/docs/latest/extensions

Ensures the agent has finished streaming before proceeding. This is safe to use within command handlers to modify the session.

```javascript
pi.registerCommand("my-cmd", {
  handler: async (args, ctx) => {
    await ctx.waitForIdle();
    // Agent is now idle, safe to modify session
  },
});

```

--------------------------------

### Handle Tool Results with pi

Source: https://pi.dev/docs/latest/extensions

Intercept tool execution results to modify them before they are processed further. Handlers chain like middleware, with each handler seeing the result modified by previous ones. Use `ctx.signal` for abort-aware async operations.

```typescript
import { isBashToolResult } from "@mariozechner/pi-coding-agent";

pi.on("tool_result", async (event, ctx) => {
  // event.toolName, event.toolCallId, event.input
  // event.content, event.details, event.isError

  if (isBashToolResult(event)) {
    // event.details is typed as BashToolDetails
  }

  const response = await fetch("https://example.com/summarize", {
    method: "POST",
    body: JSON.stringify({ content: event.content }),
    signal: ctx.signal,
  });

  // Modify result:
  return { content: [...], details: {...}, isError: false };
});

```

--------------------------------

### AgentSession Interface Definition

Source: https://pi.dev/docs/latest/sdk

Defines the interface for an AgentSession, outlining its methods for managing agent lifecycle, message history, model state, and event streaming.

```typescript
interface AgentSession {
  // Send a prompt and wait for completion
  prompt(text: string, options?: PromptOptions): Promise<void>;

  // Queue messages during streaming
  steer(text: string): Promise<void>;
  followUp(text: string): Promise<void>;

  // Subscribe to events (returns unsubscribe function)
  subscribe(listener: (event: AgentSessionEvent) => void): () => void;

  // Session info
  sessionFile: string | undefined;
  sessionId: string;

  // Model control
  setModel(model: Model): Promise<void>;
  setThinkingLevel(level: ThinkingLevel): void;
  cycleModel(): Promise<ModelCycleResult | undefined>;
  cycleThinkingLevel(): ThinkingLevel | undefined;

  // State access
  agent: Agent;
  model: Model | undefined;
  thinkingLevel: ThinkingLevel;
  messages: AgentMessage[];
  isStreaming: boolean;

  // In-place tree navigation within the current session file
  navigateTree(targetId: string, options?: { summarize?: boolean; customInstructions?: string; replaceInstructions?: boolean; label?: string }): Promise<{ editorText?: string; cancelled: boolean }>;

  // Compaction
  compact(customInstructions?: string): Promise<CompactionResult>;
  abortCompaction(): void;

  // Abort current operation
  abort(): Promise<void>;

  // Cleanup
  dispose(): void;
}

```

--------------------------------

### Text Content Block Type

Source: https://pi.dev/docs/latest/session

Defines the structure for text-based content within session messages.

```typescript
interface TextContent {
  type: "text";
  text: string;
}

```

--------------------------------

### set_session_name

Source: https://pi.dev/docs/latest/rpc

Sets a display name for the current session, which aids in identifying sessions in listings.

```APIDOC
## set_session_name

### Description
Set a display name for the current session. The name appears in session listings and helps identify sessions.

### Request Body
- **type** (string) - Required - Must be "set_session_name"
- **name** (string) - Required - The desired name for the session

### Request Example
```json
{
  "type": "set_session_name", 
  "name": "my-feature-work"
}
```

### Response
#### Success Response (200)
- **type** (string) - The type of the response, should be "response"
- **command** (string) - The command that was executed, should be "set_session_name"
- **success** (boolean) - Indicates if the command was successful

#### Response Example
```json
{
  "type": "response",
  "command": "set_session_name",
  "success": true
}
```

The current session name is available via `get_state` in the `sessionName` field.
```

--------------------------------

### Turn End Event

Source: https://pi.dev/docs/latest/rpc

Signifies the completion of a turn. It includes the final message and any tool results.

```json
{
  "type": "turn_end",
  "message": {...},
  "toolResults": [...] 
}
```

--------------------------------

### Base AgentEvent Type Definition

Source: https://pi.dev/docs/latest/json

Defines the base event types for agent lifecycle, turn lifecycle, message lifecycle, and tool execution.

```typescript
type AgentEvent =
  // Agent lifecycle
  | { type: "agent_start" }
  | { type: "agent_end"; messages: AgentMessage[] }
  // Turn lifecycle
  | { type: "turn_start" }
  | { type: "turn_end"; message: AgentMessage; toolResults: ToolResultMessage[] }
  // Message lifecycle
  | { type: "message_start"; message: AgentMessage }
  | { type: "message_update"; message: AgentMessage; assistantMessageEvent: AssistantMessageEvent }
  | { type: "message_end"; message: AgentMessage }
  // Tool execution
  | { type: "tool_execution_start"; toolCallId: string; toolName: string; args: any }
  | { type: "tool_execution_update"; toolCallId: string; toolName: string; args: any; partialResult: any }
  | { type: "tool_execution_end"; toolCallId: string; toolName: string; result: any; isError: boolean };

```

--------------------------------

### Truncate Line to Width

Source: https://pi.dev/docs/latest/tui

Use `truncateToWidth` to ensure lines do not exceed the specified width parameter in `render()`.

```typescript
import { visibleWidth, truncateToWidth } from "@mariozechner/pi-tui";

render(width: number): string[] {
  // Truncate long lines
  return [truncateToWidth(this.text, width)];
}
```

--------------------------------

### OAuthCredentials Interface

Source: https://pi.dev/docs/latest/custom-provider

Defines the structure for storing OAuth credentials, including refresh tokens, access tokens, and their expiration times. These are persisted for future use.

```typescript
interface OAuthCredentials {
  refresh: string;   // Refresh token (for refreshToken())
  access: string;    // Access token (returned by getApiKey())
  expires: number;   // Expiration timestamp in milliseconds
}

```

--------------------------------

### User Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for messages originating from the user, including content and timestamp.

```typescript
interface UserMessage {
  role: "user";
  content: string | (TextContent | ImageContent)[];
  timestamp: number;  // Unix ms
}

```

--------------------------------

### set_steering_mode

Source: https://pi.dev/docs/latest/rpc

Control how steering messages (from `steer`) are delivered.

```APIDOC
## set_steering_mode

### Description
Control how steering messages (from `steer`) are delivered.

### Method
set_steering_mode

### Request Body
- **type** (string) - Required - Must be "set_steering_mode"
- **mode** (string) - Required - The steering mode. Possible values: "all", "one-at-a-time".
  - "all": Deliver all steering messages after the current assistant turn finishes executing its tool calls.
  - "one-at-a-time": Deliver one steering message per completed assistant turn (default).

### Request Example
```json
{"type": "set_steering_mode", "mode": "one-at-a-time"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "set_steering_mode"
- **success** (boolean) - true
```

--------------------------------

### Image Content Block Type

Source: https://pi.dev/docs/latest/session

Defines the structure for image-based content within session messages, including base64 data and MIME type.

```typescript
interface ImageContent {
  type: "image";
  data: string;      // base64 encoded
  mimeType: string;  // e.g., "image/jpeg", "image/png"
}

```

--------------------------------

### set_thinking_level

Source: https://pi.dev/docs/latest/rpc

Set the reasoning/thinking level for models that support it.

```APIDOC
## set_thinking_level

### Description
Set the reasoning/thinking level for models that support it.

### Method
set_thinking_level

### Request Body
- **type** (string) - Required - Must be "set_thinking_level"
- **level** (string) - Required - The desired thinking level. Possible values: "off", "minimal", "low", "medium", "high", "xhigh". Note: "xhigh" is only supported by OpenAI codex-max models.

### Request Example
```json
{"type": "set_thinking_level", "level": "high"}
```

### Response
#### Success Response (200)
- **type** (string) - "response"
- **command** (string) - "set_thinking_level"
- **success** (boolean) - true
```

--------------------------------

### pi.getThinkingLevel() / pi.setThinkingLevel(level)

Source: https://pi.dev/docs/latest/extensions

Retrieves or sets the current thinking level, which influences the model's reasoning depth. The level is clamped to the model's capabilities.

```APIDOC
## pi.getThinkingLevel() / pi.setThinkingLevel(level)

### Description
Get or set the thinking level. Level is clamped to model capabilities (non-reasoning models always use "off").

### Usage
```javascript
const current = pi.getThinkingLevel();  // "off" | "minimal" | "low" | "medium" | "high" | "xhigh"
pi.setThinkingLevel("high");
```

### Parameters
- **level** (string) - The desired thinking level. Possible values include: `"off"`, `"minimal"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`.
```

--------------------------------

### Auto-compaction trigger condition

Source: https://pi.dev/docs/latest/compaction

Auto-compaction triggers when the current context tokens exceed the context window minus reserved tokens. This ensures space for the LLM's response.

```plaintext
contextTokens > contextWindow - reserveTokens
```

--------------------------------

### UserMessage Type Definition

Source: https://pi.dev/docs/latest/rpc

Represents a message from the user, including content and timestamp. Content can be text or attachments.

```json
{
  "role": "user",
  "content": "Hello!",
  "timestamp": 1733234567890,
  "attachments": []
}

```

--------------------------------

### Unregister a Model Provider

Source: https://pi.dev/docs/latest/extensions

Remove a previously registered provider and its models. Built-in models that were overridden by the provider are restored. This takes effect immediately when called after the initial load phase.

```javascript
pi.registerCommand("my-setup-teardown", {
  description: "Remove the custom proxy provider",
  handler: async (_args, _ctx) => {
    pi.unregisterProvider("my-proxy");
  },
});
```

--------------------------------

### BashExecutionMessage Type Definition

Source: https://pi.dev/docs/latest/rpc

Represents the output of a bash command executed via RPC, including command, output, exit code, and truncation status.

```json
{
  "role": "bashExecution",
  "command": "ls -la",
  "output": "total 48\ndrwxr-xr-x ...",
  "exitCode": 0,
  "cancelled": false,
  "truncated": false,
  "fullOutputPath": null,
  "timestamp": 1733234567890
}

```

--------------------------------

### Extension Error Event

Source: https://pi.dev/docs/latest/rpc

This JSON object represents an 'extension_error' event, emitted when an extension encounters an error during its execution. It includes the path to the extension, the event that triggered the error, and the error message.

```json
{
  "type": "extension_error",
  "extensionPath": "/path/to/extension.ts",
  "event": "tool_call",
  "error": "Error message..."
}
```

--------------------------------

### Persist Extension State

Source: https://pi.dev/docs/latest/extensions

Persist extension state using `appendEntry`. This data does not participate in LLM context but can be restored on session reload by iterating through `sessionManager.getEntries()`.

```javascript
pi.appendEntry("my-state", { count: 42 });

// Restore on reload
pi.on("session_start", async (_event, ctx) => {
  for (const entry of ctx.sessionManager.getEntries()) {
    if (entry.type === "custom" && entry.customType === "my-state") {
      // Reconstruct from entry.data
    }
  }
});

```

--------------------------------

### Rebuild Complex UI on Invalidation in TUI

Source: https://pi.dev/docs/latest/tui

This `ComplexComponent` pattern demonstrates how to rebuild a complex UI structure when `invalidate()` is called. It clears existing children and reconstructs the UI, applying theme colors and styles dynamically, ensuring that all themed elements are updated correctly.

```typescript
class ComplexComponent extends Container {
  private data: SomeData;

  constructor(data: SomeData) {
    super();
    this.data = data;
    this.rebuild();
  }

  private rebuild(): void {
    this.clear();  // Remove all children

    // Build UI with current theme
    this.addChild(new Text(theme.fg("accent", theme.bold("Title")), 1, 0));
    this.addChild(new Spacer(1));

    for (const item of this.data.items) {
      const color = item.active ? "success" : "muted";
      this.addChild(new Text(theme.fg(color, item.label), 1, 0));
    }
  }

  override invalidate(): void {
    super.invalidate();
    this.rebuild();
  }
}
```

--------------------------------

### Extension UI Request: Set Status

Source: https://pi.dev/docs/latest/rpc

A request to set or clear a status entry in the footer or status bar. This is a fire-and-forget method. To clear a status, send 'statusText: undefined'.

```json
{
  "type": "extension_ui_request",
  "id": "uuid-6",
  "method": "setStatus",
  "statusKey": "my-ext",
  "statusText": "Turn 3 running..."
}
```

--------------------------------

### Bash Execution Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for messages representing the execution of bash commands, including output and exit code.

```typescript
interface BashExecutionMessage {
  role: "bashExecution";
  command: string;
  output: string;
  exitCode: number | undefined;
  cancelled: boolean;
  truncated: boolean;
  fullOutputPath?: string;
  excludeFromContext?: boolean;  // true for !! prefix commands
  timestamp: number;
}

```

--------------------------------

### Streaming Message Update Event

Source: https://pi.dev/docs/latest/rpc

Used for streaming assistant messages. It provides both the partial message content and a streaming delta event, such as text or tool call updates.

```json
{
  "type": "message_update",
  "message": {...},
  "assistantMessageEvent": {
    "type": "text_delta",
    "contentIndex": 0,
    "delta": "Hello ",
    "partial": {...}
  }
}
```

--------------------------------

### get_last_assistant_text

Source: https://pi.dev/docs/latest/rpc

Retrieves the text content of the most recent assistant message.

```APIDOC
## get_last_assistant_text

### Description
Get the text content of the last assistant message.

### Request Body
- **type** (string) - Required - Must be "get_last_assistant_text"

### Request Example
```json
{
  "type": "get_last_assistant_text"
}
```

### Response
#### Success Response (200)
- **type** (string) - The type of the response, should be "response"
- **command** (string) - The command that was executed, should be "get_last_assistant_text"
- **success** (boolean) - Indicates if the command was successful
- **data** (object) - Contains the result of the command
  - **text** (string or null) - The text of the last assistant message, or null if no assistant messages exist

#### Response Example
```json
{
  "type": "response",
  "command": "get_last_assistant_text",
  "success": true,
  "data": {"text": "The assistant's response..."}
}
```

Returns `{"text": null}` if no assistant messages exist.
```

--------------------------------

### Set and Clear Persistent Status Indicator

Source: https://pi.dev/docs/latest/tui

Use `ctx.ui.setStatus` to display persistent status messages in the footer. Pass `undefined` to clear the status. This is useful for mode indicators or ongoing process notifications.

```typescript
// Set status (shown in footer)
ctx.ui.setStatus("my-ext", ctx.ui.theme.fg("accent", "● active"));

// Clear status
ctx.ui.setStatus("my-ext", undefined);

```

--------------------------------

### AgentSessionEvent Type Definition

Source: https://pi.dev/docs/latest/json

Defines the various event types emitted by the agent session, including queue updates, compaction events, and retry attempts.

```typescript
type AgentSessionEvent =
  | AgentEvent
  | { type: "queue_update"; steering: readonly string[]; followUp: readonly string[] }
  | { type: "compaction_start"; reason: "manual" | "threshold" | "overflow" }
  | { type: "compaction_end"; reason: "manual" | "threshold" | "overflow"; result: CompactionResult | undefined; aborted: boolean; willRetry: boolean; errorMessage?: string }
  | { type: "auto_retry_start"; attempt: number; maxAttempts: number; delayMs: number; errorMessage: string }
  | { type: "auto_retry_end"; success: boolean; attempt: number; finalError?: string };

```

--------------------------------

### Access and Modify Agent State

Source: https://pi.dev/docs/latest/sdk

Access the current state of the agent, including conversation history, model, and system prompt. State properties like messages and tools can be replaced directly.

```typescript
const state = session.agent.state;

// state.messages: AgentMessage[] - conversation history
// state.model: Model - current model
// state.thinkingLevel: ThinkingLevel - current thinking level
// state.systemPrompt: string - system prompt
// state.tools: AgentTool[] - available tools
// state.streamingMessage?: AgentMessage - current partial assistant message
// state.errorMessage?: string - latest assistant error

// Replace messages (useful for branching or restoration)
session.agent.state.messages = messages; // copies the top-level array

// Replace tools
session.agent.state.tools = tools; // copies the top-level array

// Wait for agent to finish processing
await session.agent.waitForIdle();
```

--------------------------------

### Abort Retry

Source: https://pi.dev/docs/latest/rpc

Abort an in-progress automatic retry. This command cancels any pending retry attempts and stops the retry mechanism.

```json
{"type": "abort_retry"}
```

--------------------------------

### Cache Rendered Output in TUI Component

Source: https://pi.dev/docs/latest/tui

Implement a `CachedComponent` to store rendered output and avoid recomputation when dimensions haven't changed. Call `invalidate()` when state changes and `handle.requestRender()` to trigger a re-render.

```typescript
class CachedComponent {
  private cachedWidth?: number;
  private cachedLines?: string[];

  render(width: number): string[] {
    if (this.cachedLines && this.cachedWidth === width) {
      return this.cachedLines;
    }
    // ... compute lines ...
    this.cachedWidth = width;
    this.cachedLines = lines;
    return lines;
  }

  invalidate(): void {
    this.cachedWidth = undefined;
    this.cachedLines = undefined;
  }
}
```

--------------------------------

### Signal Tool Execution Errors

Source: https://pi.dev/docs/latest/extensions

To mark a tool execution as failed, throw an `Error` from the `execute` function. This sets `isError: true` on the result and reports the error to the LLM. Returning a value, even with error-like properties, does not set the error flag.

```typescript
// Correct: throw to signal an error
async execute(toolCallId, params) {
  if (!isValid(params.input)) {
    throw new Error(`Invalid input: ${params.input}`);
  }
  return { content: [{ type: "text", text: "OK" }], details: {} };
}

```

--------------------------------

### Intercept Provider Request

Source: https://pi.dev/docs/latest/extensions

Hook into the request process just before it's sent to the provider. Allows modification of the provider-specific payload, including system instructions.

```javascript
pi.on("before_provider_request", (event, ctx) => {
  console.log(JSON.stringify(event.payload, null, 2));

  // Optional: replace payload
  // return { ...event.payload, temperature: 0 };
});
```

--------------------------------

### Intercept Provider Response

Source: https://pi.dev/docs/latest/extensions

Execute code after receiving an HTTP response from the provider and before consuming the stream body. Useful for checking status codes and headers, like handling rate limiting.

```javascript
pi.on("after_provider_response", (event, ctx) => {
  // event.status - HTTP status code
  // event.headers - normalized response headers
  if (event.status === 429) {
    console.log("rate limited", event.headers["retry-after"]);
  }
});
```

--------------------------------

### ToolResultMessage Type Definition

Source: https://pi.dev/docs/latest/rpc

Represents the result of a tool call, including the tool's output and whether it was an error.

```json
{
  "role": "toolResult",
  "toolCallId": "call_123",
  "toolName": "bash",
  "content": [{"type": "text", "text": "total 48\ndrwxr-xr-x ..."}],
  "isError": false,
  "timestamp": 1733234567890
}

```

--------------------------------

### Manage Child Components in Container

Source: https://pi.dev/docs/latest/tui

The Container component groups child components vertically. Use addChild to add components and removeChild to remove them.

```typescript
const container = new Container();
container.addChild(component1);
container.addChild(component2);
container.removeChild(component1);

```

--------------------------------

### Abort Bash Command

Source: https://pi.dev/docs/latest/rpc

Abort a running bash command. This command cancels the execution of any currently running shell command.

```json
{"type": "abort_bash"}
```

--------------------------------

### Correct Theme Invalidation in TUI Component

Source: https://pi.dev/docs/latest/tui

The `GoodComponent` correctly handles theme changes by overriding `invalidate()`. It calls `super.invalidate()` to clear child caches and then calls `updateDisplay()` to rebuild its content using the current theme, ensuring theme colors are always up-to-date.

```typescript
class GoodComponent extends Container {
  private message: string;
  private content: Text;

  constructor(message: string) {
    super();
    this.message = message;
    this.content = new Text("", 1, 0);
    this.addChild(this.content);
    this.updateDisplay();
  }

  private updateDisplay(): void {
    // Rebuild content with current theme
    this.content.setText(theme.fg("accent", this.message));
  }

  override invalidate(): void {
    super.invalidate();  // Clear child caches
    this.updateDisplay(); // Rebuild with new theme
  }
}
```

--------------------------------

### Tool Result Message Type

Source: https://pi.dev/docs/latest/session

Defines the structure for messages reporting the result of a tool execution, including call ID, content, and error status.

```typescript
interface ToolResultMessage {
  role: "toolResult";
  toolCallId: string;
  toolName: string;
  content: (TextContent | ImageContent)[];
  details?: any;      // Tool-specific metadata
  isError: boolean;
  timestamp: number;
}

```

--------------------------------

### Incorrect Theme Invalidation in TUI Component

Source: https://pi.dev/docs/latest/tui

This `BadComponent` demonstrates an incorrect approach to theme changes. It pre-bakes theme colors into a `Text` component, and its `invalidate()` method (inherited from `Container`) only clears render caches, not the pre-baked content, leading to outdated theme colors.

```typescript
class BadComponent extends Container {
  private content: Text;

  constructor(message: string, theme: Theme) {
    super();
    // Pre-baked theme colors stored in Text component
    this.content = new Text(theme.fg("accent", message), 1, 0);
    this.addChild(this.content);
  }
  // No invalidate override - parent's invalidate only clears
  // child render caches, not the pre-baked content
}
```

--------------------------------

### AgentMessage Union Type

Source: https://pi.dev/docs/latest/session

Defines the union type for all possible AgentMessage variants.

```typescript
type AgentMessage =
  | UserMessage
  | AssistantMessage
  | ToolResultMessage
  | BashExecutionMessage
  | CustomMessage
  | BranchSummaryMessage
  | CompactionSummaryMessage;

```

--------------------------------

### Modify LLM Context Before Call

Source: https://pi.dev/docs/latest/extensions

Intercept and modify the messages passed to the LLM before each call. This allows for non-destructive filtering or augmentation of the conversation history.

```javascript
pi.on("context", async (event, ctx) => {
  // event.messages - deep copy, safe to modify
  const filtered = event.messages.filter(m => !shouldPrune(m));
  return { messages: filtered };
});
```

=== COMPLETE CONTENT === This response contains all available snippets from this library. No additional content exists. Do not make further requests.