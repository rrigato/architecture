- Measure software delivery performance by the feature request lead time, deployment frequency, time to restore service and change failure percentage
- Deliver work in small batches because it allows you to gather user feedback quickly and take an experimental approach to product development
- use measurement of software delivery performance to improve your processes not as a form of control
- Production incidents rarely have a single root cause but are often a combination of contributing factors

# technical_practices
- TDD and ci/cd technical practices are enablers of more frequent and lower risk deployments
- Split work into small chunks that deliver measureable business outcomes for a small part of your target market so you can get essential feedback and easily course correct
- The goal of working in small batches is to avoid work that delivers zero or negative value and make the cost of pushing an individual feature request to production very low
- Invest in automating regression testing/software delivery to free up individuals to focus on higer value problem solving work
- The most important characteristic of high-performing teams is that they relentlessly pursue continuous improvement and make the strive to get better part of everybody's daily work
- All configuration management to provision environments, build/test/deploy software should be maintained in your version control system
- Keep feature branches at less than one days work and merge them into master frequently



- developers should be able to run all automated testing in the pipeline on their local machine
- continuous testing = developers iterate in small steps and run unit tests with each code change
- loosely coupled, encapsulated architectures with well defined interfaces enables continuous delivery
- Continuous delivery shortens development lead time and increases deployment frequency while also driving a strong identification for the team you work for
- Application configuration management in version control should be a tier 1 concern just like application code
- unit tests need to give developers confidence their application will work when passing and have no false positives when they fail
- Having long lived feature branches discourages refactoring and intra-team communication
- Info security teams should be involved in all stages of the ci/cd process the moment you have a demoable link in a way that does not slow down the development process