- fixed time variable scope = do not ask the time it takes to develop a feature, set how much development time the idea is worth 
- circuit breakers = if you do not deliver a feature within an iteration it does not get an extension
- Start each iteration cycle by building one demoable e2e piece starting with the biggest technical unknowns


# shaping_projects_ch2

- fat marker sketch = rough idea that solves the business problem without the fine details worked out
- Address potiential risks and rabbit holes in your project pitch document


# setting_project_boundaries
- The default response for any new issue should be to not immediately put it in a backlog but to gather the context of whether it is really important and what developer resources it might entail

- define how refactors/redesigns affect a specific business problem statement, because otherwise you will never know when a refactor/v2 of a product is truly done

- Each new feature should have a raw idea, business problem statement, risks, and proposed scope that fits within your time appetite


# project_risks_ch5
- you want to bet on projects with independent, well understood parts that assemble together in known ways
- potential risks:
  - new technical work never done before
  - assuming a design solution exists that you havent come up with yourself

# pitching_projects_ch6
- Anybody can suggest expensive and complicated solutions, it takes discipline and reflection to shape a simple idea that fits within a time appetite
- elements of a pitch: business requirements, time appetite, solution, risk, out of scope


# pitch_backlog_ch7
- Do not have a backlog, evaluate what you are doing before each iteration with a pitch
- Important ideas do not get lost, they will come up again in a future pitch meeting

# choosing_pitches_ch8
- iterations need to be long enough to complete a project e2e, but short enough so the pressure of a deadline does not can be used to enforce tradeoffs

- Only pick up a feature/pitch if you agree:
  - it can be completed e2e in 1 iteration
  - the development team will be given uninterrupted development time for the whole iteration
  - a circuit breaker will be invoked if the iterations time limit is hit

- There is nothing special about bugs that makes them automatically more important than everything else if your core business requirements are being met by the application
- All software has bugs, few are critical enough to where you should drop everything to fix a bug instead of prioritizing a fix in a future iteration

- bugs should be prioritized for pickup in an iteration like any feature release
- Never commit to work more than 1 cycle iteration at a time, because the work in the current iteration always informs prioritazation in the next one.
- Do not carry any technical debt over from a previous iteration, otherwise you are not honoring your circuit breakers
