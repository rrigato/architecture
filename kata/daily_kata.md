
# bash_commands

- ```detect-secrets scan | python3 -c "import sys; import json; print(json.load(sys.stdin)['results'])"```
<details>
<code>
d_s
</code>
</details>

- git add
<details>
<code>
g_a
</code>
</details>

- git branch
<details>
<code>
g_b
</code>
</details>

- git checkout
<details>
<code>
g_c
</code>
</details>

- git diff
<details>
<code>
g_d
</code>
</details>

- git fetch origin
<details>
<code>
g_f
</code>
</details>

- git init
<details>
<code>
g_i
</code>
</details>

- git branch | grep
-v master | grep
-v dev | xargs git branch
-d
<details>
<code>
g_g
</code>
</details>

- git fetch origin dev:dev
<details>
<code>
g_j
</code>
</details>

- git fetch origin master:master
<details>
<code>
g_k
</code>
</details>

- git log
<details>
<code>
g_l
</code>
</details>

- git add --all; git commit -m
<details>
<code>
g_m
</code>
</details>

- git pull origin
<details>
<code>
g_p
</code>
</details>

- git remote add origin
<details>
<code>
g_r
</code>
</details>

- git status
<details>
<code>
g_s
</code>
</details>

- git tag
<details>
<code>
g_t
</code>
</details>

- git push origin
<details>
<code>
g_u
</code>
</details>

- git remote
<details>
<code>
g_v
</code>
</details>

- git fetch origin; git merge origin/dev --no-edit

<details>
<code>
g_w
</code>
</details>

- node --inspect-brk node_modules/.bin/jest --runInBand
<details>
<code>
j_d
</code>
</details>

- node_modules/.bin/jest
<details>
<code>
j_t
</code>
</details>

- npm run build
<details>
<code>
npm_b
</code>
</details>

- npm install --save-dev
<details>
<code>
npm_d
</code>
</details>

- npm install
<details>
<code>
npm_i
</code>
</details>

- npm run local
<details>
<code>
npm_l
</code>
</details>

- rm -r node_modules
<details>
<code>
npm_r
</code>
</details>

- rm -r node_modules; npm install
<details>
<code>
npm_s
</code>
</details>

- npm run test
<details>
<code>
npm_t
</code>
</details>

- npm update --dev
<details>
<code>
npm_u
</code>
</details>

- npm list --depth 0
<details>
<code>
npm_v
</code>
</details>

- nvm install
<details>
<code>
nvm_i
</code>
</details>

- nvm use
<details>
<code>
nvm_u
</code>
</details>

- list installed node versions
<details>
<code>
nvm_v
</code>
</details>

- activate virtualenv by name
<details>
<code>
py_a
</code>
</details>

- create virtualenv by name
<details>
<code>
py_c
</code>
</details>

- deactivate virtualenv
<details>
<code>
py_d
</code>
</details>

- pip install -r requirements/requirements-dev.txt
<details>
<code>
py_i
</code>
</details>

- list virtualenv
<details>
<code>
py_l
</code>
</details>

- python -m
<details>
<code>
py_m
</code>
</details>

- install python version
<details>
<code>
py_n
</code>
</details>

- remove a virtualenv by name
<details>
<code>
py_r
</code>
</details>

- deactivate; rm -r avenv; python3 -m venv avenv && source avenv/bin/activate && pip install -r requirements/requirements-dev.txt
<details>
<code>
py_s
</code>
</details>

- python -m unittest
<details>
<code>
py_t
</code>
</details>

- use a python version globally
<details>
<code>
py_u
</code>
</details>

- pip list; python --version; which python
<details>
<code>
py_v
</code>
</details>

- right shift for left side of keyboard

- iterate over keys:
- ```0-9```
- ```()```
- ```[]```
- ```\```
- ```=+-```
- ```+```
- ```-```


# mac_commands
- delete an unsaved file
 <details><code>CMD + W</code></details>
 <details><code>CMD + DELETE</code></details>

- finder search by path
 <details><code>CMD + SHIFT + G</code></details>

- open screenshot
 <details><code>CMD + SHIFT + 5</code></details>

- switch focus on split screen
 <details><code>CMD + TAB</code></details>

# outlook
- archive email
 <details><code>CTRL + E</code></details>

- Create hyperlink
 <details><code>CMD + K</code></details>

- Switch between calendar and inbox
 <details><code>CMD + 1</code></details>
 <details><code>CMD + 2</code></details>

# slack
- hyperlink selected text
 <details><code> CMD + SHIFT + U</code></details>

- mark message as unread
 <details><code> CMD + SHIFT + U</code></details>

# vscode

- change language mode
 <details><code>CMD + K + M</code></details>

- open copilot chat in editor
 <details><code>CMD + K CMD + O</code></details>

- ask copilot chat about vscode
 <details><code>@vscode</code></details>


- ask copilot chat about a specific file
 <details><code>#file</code></details>

- pass selection as context to copilot chat
 <details><code>#selection</code></details>

- ask copilot about last terminal command
 <details><code>#terminalLastCommand</code></details>

- ask copilot about your workspace
 <details><code>@workspace</code></details>

- accept only next word of copilot suggestion
 <details><code>CMD + right arrow</code></details>

- copilot inline terminal close chat
 <details><code>ESCAPE</code></details>

- copilot inline terminal insert suggestion at shell prompt
 <details><code>OPTION + ENTER</code></details>

- copilot inline terminal run suggestion
 <details><code>CMD + ENTER</code></details>

- copilot inline terminal edit suggestion
 <details><code>CMD + down arrow + TAB + TAB</code></details>

- copilot inline terminal initialize chat
 <details><code>CMD + I</code></details>

- paste stdout of shell command into new editor
 <details><code>echo "output that will be in editor" | code -</code></details>

- inline breakpoint
 <details><code>no keyboard shortcut</code></details>

- remove all debug breakpoints
 <details><code>no keyboard shortcut</code></details>

- add a cursor
 <details><code>CMD + OPTION + up or down arrow </code></details>

- copy line up/down
 <details><code>SHIFT + OPTION + up or down arrow </code></details>

- increment by .1, 1, 10
 <details><code>CMD + SHIFT + P + increment by x </code></details>

- decrement .1, 1, 10
 <details><code>CMD + SHIFT + P + decrement by x </code></details>

- hide the sidebar
 <details><code>CMD + B </code></details>

- increase/decrease selection to brackets
 <details><code>CTRL + SHIFT + plus left or right arrow </code></details>

- select line
 <details><code>CMD + L</code></details>

- undo cursor position
 <details><code>CMD + U</code></details>

- redo cursor position
 <details><code>SHIFT + CMD + U</code></details>

- move up page without scrolling
 <details><code>CMD + page up</code></details>

- move down page without scrolling
 <details><code>CMD + page down</code></details>

- collapse all code
 <details><code>CMD + K + CMD + 0 </code></details>

- collapse/expand code section
 <details><code>CMD + OPTION + [ or ] </code></details>

- expand code recursively
 <details><code>CMD + K + CMD + ] </code></details>

- show hover
 <details><code>CMD + K + CMD + I </code></details>

- reveal command pallette
 <details><code>CMD + SHIFT + P </code></details>

- go to symbol in workspace
 <details><code>CMD + T </code></details>

- focus debug console terminal
 <details><code>CMD + SHIFT + Y </code></details>

- search previous terminal commands
 <details><code>CTRL + R </code></details>

- Focus and Toggle panel
 <details><code>CMD + J</code></details>

- switch between active terminals
 <details><code>CMD + SHIFT + [ or ] </code></details>

- jump between previous command results
 <details><code>CMD + up or down arrow </code></details>

- open link in terminal
 <details><code>CMD + SHIFT + O </code></details>

- Go up one line in the terminal
 <details><code>CMD + OPTION + page up</code></details>

- Go down one line in the terminal
 <details><code>CMD + OPTION + page down</code></details>

- increase terminal/panel size
 <details><code>SHIFT + OPTION + M</code></details>

- decrease terminal/panel size
 <details><code>SHIFT + OPTION + N</code></details>

- kill terminal
 <details><code>CMD + CTRL + K</code></details>

- open an editor to the side
 <details><code>CMD + return </code></details>

- toggle left/right/center editor groups
 <details><code>CMD + 1 OR 2 OR 3 </code></details>

- Move editor to different editor group
 <details><code>CMD + CTRL + plus left or right arrow </code></details>

- Toggle maximize editor group
 <details><code>CMD + K + CMD + M</code></details>

- close editor
 <details><code>CMD + W </code></details>

- place cursor at matching/closest parentheses/brackets
 <details><code>CMD + SHIFT + \ </code></details>

- toggle case sensitive search
 <details><code>CMD + OPTION + C </code></details>

- find and replace across workspace
 <details><code>CMD + SHIFT + H </code></details>

- move to replace input box or file match section
 <details><code>CMD + down arrow </code></details>

- collapse files with matches
 <details><code>CMD + left arrow </code></details>

- replace next file/match within file
 <details><code>CMD + SHIFT + ! </code></details>

- replace all matches across all files
 <details><code>CMD + OPTION + return </code></details>

- find all reference
 <details><code>CMD+K CMD+A</code></details>

- go to defintion
 <details><code>CMD+k CMD+g</code></details>

- change keyboard input source
 <details><code>CTRL + SPACE</code></details>

- copy python path
 <details><code>CMD+k CMD+p</code></details>

- copy relative path to file
 <details><code>CMD + OPTION + SHIFT + C</code></details>

- Add cursor at next match
 <details><code>CMD + D</code></details>

- Add cursor to previous match
 <details><code>CMD + SHIFT + D</code></details>

- Skip Add cursor to previous match
 <details><code>CMD+K CMD+D</code></details>

- revert selected range
 <details><code>CMD+K CMD+R</code></details>

- view available code actions for selected code
 <details><code>CTRL+SHIFT+R</code></details>

- quick fix import
 <details><code>CMD+.</code></details>

- focus breadcrumbs
 <details><code>CMD+SHIFT+.</code></details>

- wrap selection in jsx
 <details><code>CMD+K CMD+H</code></details>
