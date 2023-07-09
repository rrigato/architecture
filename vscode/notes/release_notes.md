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