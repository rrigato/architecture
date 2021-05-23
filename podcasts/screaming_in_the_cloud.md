- [introduction](#introduction)
- [podcast_takeaways](#podcast_takeaways)
  - [Nora Jones](#nora-jones)
  - [Regis Wilson](#regis-wilson)
  - [james_urquhart](#james_urquhart)
  - [eric brandwine](#eric-brandwine)
# introduction
Podcasts about general cloud related innovations
https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/

# podcast_takeaways

# [Nora Jones](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/a-chaos-engineering-jeli-sandwich-with-nora-jones/)

> the most important issue in incident analysis is determing who should be on the call


> you need to have a clear understanding of what is worth waking an engineer up at 6 am for


# [Regis Wilson](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/reconnecting-with-an-old-boss-with-regis-wilson/)
- think about infrastructure in terms of cost per tenet 
  - How much you pay for each user, each analysis, each customer acquisition
  
- the power of infrastructure as code is the ability to store configuration in version control and having a consistent deployment approach without having to rdp/ssh into a server


# james_urquhart
[podcast link](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/flow-architectures-the-future-of-streaming-data-with-james-urquhart/)

- the end unit of work for a developer is a function, not an executable or server

# [eric brandwine](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/the-darth-vader-of-aws-with-eric-brandwine/)

- their is no security incident that has crashed a business

- the most important thing in security is not that you have a particular security setting, but that you have a feedback loop so when something happens that you do not like you are able to write that back into your automated deployment processes




# [randall hunt](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/making-machine-learning-invisible-with-randall-hunt/)

- dry is great for software design but not for infrastructure as code

- machine learning models are mostly automated at this point, the majority of the work is now in cleaning/gathering data



[laura thomson](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/minimum-viable-bureaucracy-with-laura-thomson/)
- approach corporate processes with the same rigor and continual improvement evaluations with which you approach software engineering


[heidi](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/personalization-the-non-creepy-way-with-heidi-waterhouse/)


- decouple pushing code to a server from when a user sees the new feature with a feature flag


- permanent feature flags = everything is live in your local environment, just hidden using feature flags in dev/prod


- building instead of buying results is like gifting puppies, they are free except for all the responsibility 





[talia Nassi](https://www.lastweekinaws.com/podcast/screaming-in-the-cloud/splitballing-on-devrel-with-talia-nassi/) 
- Use a feature flag where you have a subset of internal users who always get the new features enabled in prod, so every local feature development is live behind a feature flag in prod

- Have a dedicated synthetic account in your prod feature flag group

