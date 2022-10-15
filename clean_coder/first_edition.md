# responsibility_ch1
- take responsibility to ensure no bugs make it to QA testers or your customers while also realizing that unexpected bugs occur and have the humility to apologize when they slip past your test suites

- merciless refactoring = always check code into your repo in better shape than you checked it out
- never modify software in a way that makes the software more difficult to change in the future
- professionals spend time outside of work caring for their profession

- doing your daily job is performance, you need to practice outside of your job to become a master performer
- professionals never demean fellow engineers for making a mistake and will always be willing to acknowledge when they make a mistake


# saying_no_ch2
- focus on providing ```just the facts``` of the timeline estimate not explaining the ```technical why``` unless prompted
- being a team player who says yes to trying to meet an impossible feature release timeline is worse than being professional and saying no from the beginning
- clean code is extendable, maintainable and lends itself to modification
- the stakeholders/users of an application will never care as much about the feature deadline as you do
- saying yes to dropping software quality in order to try to meet an unrealistic timeline ultimately slows down release velocity since you will no longer have an extendable code base


# saying_yes_ch3
- alert stakeholders as soon as you realize a commitment cannot be met
- If your feature release depends on an exterior team or technical unknowns, commit to actions that will unambiguously move you closer to releasing the feature that are in your control
- When working weekends, be honest about how (in)efficient your work will be, how much recovery time you will need to avoid burnout, and maintaining code quality standards to make sure you do not impact release velocity 


# coding_ch4
- do not code if you are feeling tired or distracted from aniexty, resolve the source of aniexty before resuming development
- professionalism involves having the discipline to show to work fully rested and healthy so you will be at peak performance throughout the work day
- professional developers arrange their personal lives to ensure their time working is as productive as possible
- be polite when someone interrupts your programming context as you might be the person interrupting someone else in the future
- clearly define what done is from a business usecase perspective before beginning development and comunicate back to stakeholders as soon as you realize a deadline is not realistic
- professionals are honor bound to not sequester themselves adn provide help whenever it is needed


# test_driven_development_ch5
> I don't think surgons should have to defend hand washing and I don't think software engineers should have to defend test driven development
- trust your unit test suite enough to where if is passing your product ships
- TDD gives engineers confidence to refactor their code without fear of breaking anything
- View each test case as self generating documentation on how to invoke an object

3 laws of TDD:
1) No prod code until you have a failing unit test
2) Do not write more a unit test than what is sufficient to fail the test
3) You are not allowed to write more prod code than what is needed to pass the currently failing test


# practing_ch6
- kata = writing the implementation of a practice problem that you already know the answer to in order to strengthen your keystrokes and mouse movements
- wasa = one programmer writes the test case for a problem the other programmer needs to implement
- practicing yor development skills is what you do when you are not gettting paid so that you are paid well and when you show up to work you are ready to perform


# testing_strategy_ch8
- UI tests should confirm the system construction since business rules have already been validated with lower level unit tests


# time_management_ch9
> Any technical disagreement that cannot be solved in 5 minutes of discussion will not be solved by arguing

- prioritize coding when in your total concentration mode, take 30 minutes of unfocused physical activity to regain total concentration mode if you have lost it
- breakup short bursts of focused development with time blocks reserved for adhoc/less cognitive intensive tasks
- priority inversion = pickup a lower priority task because it is easier/quicker/more interesting than the higher priority task


# estimation_ch10
- break large tasks into a series of small estimates that you can forecast independently


# high_pressure_situations_ch11
- if you do not follow your disciplines in a crisis, you do not believe in those disciplines
- when you are in a high intensity situation double down on your software engineering disciplines/values


# collaboration_ch12
- it is good to be passionate about what you do, but it is more important to keep an eye of the goals of the people who pay you
- professionals avoid creating knowledge silos by learning the different parts of the system and business
- when issue trackers have more than 1000 issues, they lose all meaning as issue trackers
- any ci/cd build failures should be treated as a prod down
- Unittests should not be dependent on shared instance state or test run order