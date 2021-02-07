Collection of architecture notes I have from books, news feeds, online tech talks.

The goal is to slim down the source material into the smallest amount of actionable information

# table_of_contents
- [table_of_contents](#table_of_contents)
- [aws_news](#aws_news)
  - [builders_library](#builders_library)
  - [whats_new](#whats_new)
  - [summary](#summary)
  - [recommendation](#recommendation)
- [architecture_patterns_with_python](#architecture_patterns_with_python)
  - [summary](#summary-1)
  - [recommendation](#recommendation-1)
- [clean_architectures_in_python](#clean_architectures_in_python)
  - [summary](#summary-2)
  - [recommendation](#recommendation-2)
- [datastores](#datastores)
- [eloquent_javascript](#eloquent_javascript)
  - [summary](#summary-3)
  - [recommendation](#recommendation-3)
- [npm](#npm)
- [refactoring](#refactoring)
  - [summary](#summary-4)
  - [recommendation](#recommendation-4)
- [the_mythical_man_month](#the_mythical_man_month)
  - [summary](#summary-5)
  - [recommendation](#recommendation-5)
- [webpack](#webpack)

# aws_news


## builders_library
Notes on white papers [published by AWS architects](https://aws.amazon.com/builders-library/) describing best practices learned when building aws.

## whats_new
Folder that contains notes from the [whats new on aws news feed](https://aws.amazon.com/new/) for service announcements/upgrades.

## summary
aws has an rss style feed that describes
https://aws.amazon.com/new/

## recommendation
Yes, but do not read every post, skip the "AWS is expanding this service to region X in order to increase our number of service announcements on next year's reinvent presentation".

I personally skip stuff that is not applicable to me (Game tech, IoT, etc.)

The biggest benefit is I can find a new service or feature I was unaware of previously.


# architecture_patterns_with_python
authors:
- Harry Percival
- Bob Gregory

## summary 
Mostly focuses on domain driven design, event based architecture.

## recommendation
Skip, examples are way too specific to the retail use case. Some general material, but not enough to justify the time investment


# clean_architectures_in_python
authors:
- Leonardo Giordani

## summary 
Overview of the Clean Architecture with test driven examples with python

## recommendation
Yes, the second edition. The first edition tries to do too much with the test driven development.
One criticism I do have with this book is far too many external dependencies in my opinion.

# datastores
Notes on fancy distributed data storage systems I will probably never use

# eloquent_javascript
author:
- Marijn Haverbeke

## summary
Overview of programming and javascript language

## recommendation
Yes, skip chapters on topics you are familiar with and any of the game design chapters. Skip any sections that focus on building an interpreter for javascript

# npm
general npm notes


# refactoring
author:
- Martin Fowler
- Kent Beck

## summary
Applying refactoring as a proactive part of the development process

## recommendation
Yes, an interesting take on how to continually improve your code base. Not every refactoring pattern will hit home, but some certainly will

# the_mythical_man_month
author:
- Frederick Brooks

## summary

## recommendation




# webpack
General webpack notes from the docs