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


# product_development_ch8
- perform user research frequently, work in small batches, build/validate prototypes from the start of the iteration, evolve/pivot product and business models early and often


Lean product development practices:
1) work in small batches
   - Release an end-to-end tracer with just enough features to validate the business usecase is met
  
2) Software engineers understand how a feature release impacts business and customer flows
3) Actively seek customer feedback
4) Software engineers have the ability to change requirements/specifications based on what they discover in an iteration without requiring the approval of people outside their team


# sustainable_work_ch9
- continuous delivery practices that automate deployments decrease engineer anixety and improve work/life balance
- The probability of failed deployments increases when manual changes must be made to deploy to prod or maintain configuration between environments
- ensure that the state of production systems can be reproduced in an automated fashion via version control

## preventing_engineer_burnout
- foster a work environment of learning from failures rather than blaming
- invest time, space and resources during normal working hours for employee upskilling
- ask engineers what is preventing them from achieving their objectives
- ensure engineers are given the authority to make decisions that affect their work when they are responsible for the outcomes
- blame free environment where human error is never the root cause of system failures

# employee_statisfaction_ch10
- a misalignment of organizational and individual values can also contribute to burnout
- increasing software delivery velocity increases the speed at which teams can validate their ideas
- proactive monitoring, testing and deployment automation enable employees to focus on decision making instead of routine, menial tasks


# leadership_principles_ch11
- trust between teams is built on kept promises, open communication and behaving predictably even in stressful situations
- use disaster recovery gamedays to build relationships between teams
- treat failures as opportunities to learn by holding blameless postmorteums
- encourage sharing via demos
- ensure that a team can choose their tools, engineers who choose their infrastructure are much more invested in their work