# 1.72

- [You can extract](https://code.visualstudio.com/updates/v1_72#_extract-to-link-definition-for-markdown) markdown link url values to a common abstraction name where they can be reused in multiple locations
- code action support for organizing link actions at the bottom of a markdown file.

# 1.73
- audio cues for task events:
  - ```audioCues.taskEnded``` 
  - ```audioCues.taskFailed```

- ```list.collapseAllToFocus``` = new command for folding code recursively, effectiveness tbd

- ```markdown.updateLinksOnFileMove.enabled``` = auto update markdown links

- ```markdown.validate.enabled``` = can alert for unused or duplicated link definitions

- command palette has support for an insert link to file in workspace command 

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