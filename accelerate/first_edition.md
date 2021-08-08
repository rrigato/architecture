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


# architecture_ch5
- Developers should be able to complete their work without needing to communicate or coordinate with people outside of their team
- Testing and deployment should be on-demand without needing to integrate with a third party
- Security teams need to have the same focus on usability and customer satisfaction for internal 'developer customers' as for building products for external customers
  - enabling developers to choose their own tools will allow them to not use internal tools that are not helpful


# security_ch6
- security team members should be built into the software development life cycle starting with requirements gathering and ensuring automated test features are built into the pipeline instead of acting as a review gate post deployment
- Enable developers to consider security a top tier concern by providing the needed tools, training, and support during the development process instead of retrofitting security after improves security performance


# management_practices_ch7
- Have work in progress limits with a demoable link that shows visual progress of small, batch sized features
- approvals by a body external to your team does not increase the stability of production systems but does slow down release velocity
- Having no changes to production that do not also go through an automated deployment process also provides excellent auditing of historical changes
- external teams reviewing code they have no context for does nothing to improve software quality