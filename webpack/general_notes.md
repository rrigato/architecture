- [overview](#overview)
- [browser_parsing](#browser_parsing)
- [loaders](#loaders)
- [plugins](#plugins)
- [webpack_config](#webpack_config)
  
## overview
webpack starts at your main js file and bundles all dependencies referenced there

## browser_parsing
- By default the html parsing stops when it hits a script tag, waits for the script tag to download and execute, then resumes parsing

- Defer is run in order but downloads script tags in parallel


## loaders
loaders enable you to bundle non javascript file types, you provide a regex for which file extensions each loader applies to

- css-loader = takes css and injects it into js
- style-loader = takes compiled css and places into the dom

## plugins
transform js modules to do bundle optimization and asset management 

## webpack_config 
- webpack.config.js (can also be .json or .yaml) = define entry, loaders and output for webpack
