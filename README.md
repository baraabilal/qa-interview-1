# ChalkTalk • QA Interview • Score Calculator

_Version 1.0.0_

## This is a coding challenge for applicants interested in joining ChalkTalk as QA Engineers.

We ask you to _read this file carefully_ **before** you begin writing a solution.

There is a Q&A and an example section at the end of the file, which may help you to complete this challenge faster.

We sincerely thank you for your interest and your time.

Best,  
Eddie


## Submit the minimum possible

- You should **not implement features not required explicitely**.
- Coding more than required will waste your time, and waste our time. Please, don't.

## Challenge: Test an API server/application

There is an API for submitting exam questions and calculating scores. The application is running, but has some issues. Your job is to identify them and fix them.

- Write an integration that tests the happy path: submit 3 answers and check if they are correct.
- Write unit tests where appropriate. At least test loading the data and reponses.
- You can use any standard python libraries or standards for testing. If you need help with this, let us know and we will share a quick-starter project promptly.
- This project must be done in Python. Feel free to use your favorite libraries, we don't have a preference.

### Rules of the exam

- Only math questions are on the exam
- The only valid answer is an integer or a float 
- When scoring, all submitted responses should be scored

### Implementing your code

- Your tests should be runnable with something standard like py.test or nosetests
- Your tests should be documented (including parameters), implicitely (in code) or explicitely. 
- You can use any type of persistance (app memory, in-memory database, database engine, etc).

## Stretch goals

These are **not required**, but would make your submission stand out. You can implement none, one or all of these. If you do, let us know your decision so we evaluate them.

- Create additional endpoints or functions that help with testing
- Add a timestamp to the responses and if there are duplicates use the latest one
- Add logging where it would be helpful for debugging

#### Example

Your initial question bank looks like so:


| index | question | answer |
|-------|----------|--------|
| 1     | 1+1      | 2      |
| 2     | 7/2      | 3.5    |
| 3     | 8*3      | 24     |


Then a user submits one or more responses via the endpoint:

```
    {2: 3}
```

The server should record the response and when calling the score calculation endpoint shoould match the index to the answer. In this case, it would be incorrect.

---

## Submitting your work

Your deliverable should satisfy all these requirements:

- Describe what tests you've implemented, included optional stretch goals.

- It should include _instructions on how to test_ (installing dependencies, starting it, etc) and it shouldn't have any obscure environment requirements.

- Describe your tests and why you chose them.

- It should be submitted using one of the following alternatives:
  1. bitbucket.org or github.com repo (_Note: Do NOT clone our repo because other candidates can find it_).
  2. Upload a compressed file somewhere and send us the URL.
  3. Email us your code.
  - _Note: Do NOT include `.pyc` files or any other files that will be auto-generated_.

---

## Frequently asked question

- Q: Can I use external libraries?
  - Of course you can!
  - However, if some functionality is very easy to implement, try to implement it yourself (i.e. Don't install a library to figure out if a number is odd/even).
  - Choosing *when* to use libraries and *what libraries* you imported will speak about your judgement.
- Q: This coding challenge is too long. Is it OK if I implement it partially?
  - Although we recognize this exercise may take some time, it does measure if you have the skills we need to work at ChalkTalk.
  - *Submitting an incomplete solution is acceptable*, specially if you explain the reasons.
  - However, a complete solution will increase the likelihood of being selected to continue our process, and it will save time during our in-person interview.

## Thanks for your time!

Eddie
