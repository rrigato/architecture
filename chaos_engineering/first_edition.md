- engineers should be empowered to use any solution architecture they think works best, along with the responsibilities that come with the design decisions they make
- teams should be **highly aligned, loosely coupled** with the same goal but freedom to implement how they see fit

- complex systems = any system where one person is unable is incapable of having a complete understanding 
- It is crucial to understand the HTTP level (4xx/5xx) codes a system will return in a fault scenario to handle errors gracefully
- client induced retry storm = user clicking refresh 50 times causes 50 api calls flooding the downstream service

- All software is embedded with the assumptions and priorities of the software engineer at the time the software was developed


# chaos_engineering_principles_ch3
- testing involves making assertions about expected system behavior while chaos engineering is needed to create new knowledge about a systems interactions

principles of chaos engineering:
1) Define system steady-state
2) Hypothesis of what will happen in control and experimental group
3) Introduce variables that reflect real world events like hardware crashes, network connectivity, database backup recovery
4) Prove or disprove the hypothesis

- antifragility = systems that become stronger when exposed to outside stress

- Example chaos engineering hypothesis
  > under <list_adversity_being_introduced_to_system> circumstances, customers will still have a good time

- chaos engineering experiments should uncover new knowledge about a system
  - If you know an experiment will break prod, do not run it as that provides no new knowledge

- Focus chaos engineering experiments on the user experience/Key KPI's of a system, not on creating a mental model of the system
  

# slack_ch4
- design systems that are decoupled from their initial hardware runtime environment
- test your system resiliency to faults by validating automated retries occur with exponential backoff when upstream services fail
- Chaos engineering is not exploratory, you should always have a hypothesis in place before inciting failure
- Dev matching prod is not only crucial for testing new features but also for exposing previously unknown fault tolerance vulnerabilities vai chaos experiments
- Be honest about your confidence levels of any action occurring in a dev environment being replicated in prod
