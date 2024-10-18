# 1.72

- [You can extract](https://code.visualstudio.com/updates/v1_72#_extract-to-link-definition-for-markdown) markdown link url values to a common abstraction name where they can be reused in multiple locations
- code action support for organizing link actions at the bottom of a markdown file.

# 1.73
- audio cues for task events:
  - ```audioCues.taskEnded```
  - ```audioCues.taskFailed```

- ```markdown.updateLinksOnFileMove.enabled``` = auto update markdown links

- ```markdown.validate.enabled``` = can alert for unused or duplicated link definitions



# 1.74
```json
{
  "explorer.autoRevealExclude": {
    "**/node_modules": true
  }
}

```
- Exclude files from being auto revealed in the side panel explorer
- You can install an extension from a local ```.vsix``` file

- ```editor.indentSize``` can be used to separate tabSize from indentSize


# 1.76
- Command to link to all markdown headers in current code workspace
- sort json documents by key command


# 1.79
- can copy image/audio file directly from the keyboard into a markdown file
- dev containers extensions allows you to develop locally in a container

# 1.80
- ```Help: Troubleshoot Issue``` allows you to determine whether a bug is with vscode or an extension
- ```preLaunchTask``` key in ```.vscode/launch.json``` enables you to run a task befor debugging
- ```envFile``` key in ```.vscode/launch.json``` enables you to [set environement variables for debugging](https://code.visualstudio.com/docs/python/environments#_environment-variables)
- images in terminal supported for ```.six``` files

# 1.82
- ```json.sortOnSave.enable``` = auto sort json files

# 1.84
- ```SHIFT + ENTER``` = run line of python program in terminal

# 1.85
- An editor can be split into a new window
- A terminal can be turned into an editor and then split into a new window
- Can paste from operating system file explorer into VSCode file explorer

# 1.86
- [VS Code Speech extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-speech) enables you to interact with copilot chat using speech to text software
- You can configure autosave by file extension

```bash
# stdout of process directly into a vscode editor
ls -l | code -
```

- ```#file:``` context variable allows you to ask about a specific file

# 1.87
- vscode speech can be used to enter text in an editor
- vscode speech supports 26 languages including japanese
- inline copilot completion for multi-cursors!!!

# 1.90
- github enterprise license enables copilot chat to enrich results with information provided by a web search using the ```@github``` context

# 1.92
- Vscode extension that enables you to open [Edge Developer tools](https://marketplace.visualstudio.com/items?itemName=ms-edgedevtools.vscode-edge-devtools)
- ```/runCommand``` in copilot chat, search for and execute a vscode command
- ```/new``` create new files in copilot chat
- vscode chat now uses GPT-4o model
- Can add attachments to vscode chat


# 1.93
- ```Option+CMD+F``` for searching in the debug console
  
# 1.94
- ```@vscode``` ```/startDebugging``` for setting up launch.json
- copilot ```/setupTests``` slash command for setting up testing environment
- ```"problemMatcher": "$python"``` in ```task.json``` default problem matcher