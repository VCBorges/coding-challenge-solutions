Hi, thanks for the opportunity.

**I’m Vinícius Costa Borges, a Python-focused software engineer who loves turning data into reliable products.**

I started my career at a company called **Seven Systems**. I came in as an intern with only basic Django knowledge and quickly became proficient developer working on a system that automates Google Ads keyword optimization. That meant calling the Google Ads API, processing large CSVs with **pandas**, and off-loading heavy analysis to background queues that i implemented myself using Django-Q. Next I built a social-media posting automation tool that later as also able merges images with TTS audio from **AWS Polly, ElevenLabs, Azure Cognitive** and others. I used **FFmpeg** for video creation and even added AI text-correction and review using the **ChatGPT API**. This was my first taste of a product using GenAI in production and it sparked my interest in the space.

Today I’m finishing an internship at **Ericsson,** i work on a product called **Ericsson Network Intelligence**. A platform thats ingests 4 G/5 G radio telemetry at scale. My main contribution was designing an **asynchronous data-collection backend** that fans out SSH connections to dozens servers, fetches XML counters every 15 minutes, writes into PostgreSQL, all orchestrated with **Celery**. Delivering that  saved the project about **R$ 50 000** in external licensing fees.

On the side I’m building my first side-project that i plan to release some day, a **flash-cards study web-app powered by GenAI with** FastAPI on the back end, **React + Typescript** on the front end, using React Router, React Query, React Hook Form and Zod. The project is teaching me a lot from react and tools of its ecosystem, skills I’m eager to apply professionally.

Technically I’m comfortable with **Python**, REST, async IO, SQLAlchemy, testing (Pytest), **Docker/Podman** and basic Kubernetes ops. I’ve used AWS only for TTS services so far, but I’ve been hands-on with containers and I’m studying core AWS services like EC2, S3 and EKS.

**What motivates me** is shipping clean, observable code that solves real business problems—and learning whatever is necessary along the way. I enjoy remote collaboration, at Ericsson I participated in nightly deployments with engineers in China and morning stand-ups with the US, documenting decisions to bridge the time-zone gap.

I’m excited about EPAM’s focus on GenAI and full-stack work. My mix of Python backend strengths, growing React experience and curiosity around LangChain and cloud services makes me confident I can contribute quickly while continuing to grow.

Thank you—I’m happy to dive deeper into any area.

# Questions to the interviewer

- “What’s your current approach to prompt versioning and rollback when an LLM output degrades?”
- “How do code reviews work here—pair sessions, GitHub PRs, or both—and what’s the SLA for review turnaround?”
- “Which metrics do you monitor in production for GenAI features beyond the typical latency and error rates? (e.g., hallucination frequency, user satisfaction scores).”
- “How is the team distributed across time zones, and which collaboration rituals have proven most effective so far?”
- “What does onboarding look like for new engineers—do you assign a buddy, run architecture walkthroughs, or start with a small production bug?”
- “What skills or achievements typically distinguish engineers who move from mid-level to senior on this project?”
- “How often do you run formal feedback cycles, and do you encourage informal feedback between those cycles?”
- “Which GenAI capability has delivered the most business value so far?”


## Code review

“In my last two roles we followed a fairly rigorous pull-request model, but the mechanics differed slightly.

At Ericsson

Every change—feature, bug-fix, or config—went through a GitLab Merge Request.

We had two mandatory reviewers: one from my own squad and one from a neighbouring squad to catch cross-domain issues.

We used a clean-commit rule, so reviewers focused on the final, squashed diff rather than WIP noise.

I made a habit of adding a short design note and local test results so reviewers could reproduce quickly.

Once approved, the MR triggered a pipeline that ran linters, unit tests, and a small integration test set in a staging namespace; only a green pipeline allowed the merge.

The SLA for review turnaround was 24 h on business days. If the pipeline was blocking a release, we pinged in a #reviews Slack channel and paired synchronously.

At Seven Systems

It was a smaller team, so we used branch-protection rules in GitHub: one reviewer + all tests passing.

We combined code review with lightweight pair-programming sessions, especially for tricky FFmpeg and TTS integrations.

I introduced a checklist covering security, performance, and data-privacy concerns—simple things like “no secrets in code” and “SQL queries parameterised”—which reduced post-merge defects.

Things I learned

Context is king—supplying clear commit messages and a design rationale cuts review time dramatically.

Automated gates (lint, test, container scan) free reviewers to focus on architecture, not style issues.

Psychological safety matters: framing feedback around the code, not the person, keeps reviews productive.

I’m comfortable adapting to whichever review culture you use—whether that’s GitHub PRs, Gerrit, or pair-review—and I always try to leave the codebase a bit clearer than I found it.”


## Situation based questions

1 “Tell me about a time you had to learn a new technology quickly.”
S When I joined Seven Systems I had only touched Django once, yet my first ticket was to build an internal Google-Ads automation service.
T Deliver a working MVP in four weeks.
A I spent evenings on the official tutorial, read two open-source projects’ code, and pair-programmed twice a week with a senior. Within ten days I had CRUD endpoints and background tasks running with Django-Q; by week four I connected to the Google Ads API and released to staging.
R The tool went live on schedule, saving the marketing team ~2 hours/day of manual keyword work. More importantly, that rapid ramp-up became my personal template for learning FastAPI, Pandas and Kubernetes later on.

2 “Describe a time you disagreed with a teammate or stakeholder.”
S In Ericsson’s ENI project, the data-science lead wanted to keep the new EBS-Counters collector synchronous “for simplicity.”
T Convince him that async was worth the complexity.
A I ran a 30-minute benchmark: sync vs asyncssh fan-out over 128 servers. The async prototype cut crawl time from 35 min to 4 min. I presented the numbers and proposed hiding async details behind a simple interface so the team wouldn’t feel the complexity.
R He agreed; we shipped the async version. Result: p99 latency < 5 min and zero missed intervals over 60 days— exactly the SLA the analysts needed.

3 “Tell me about a failure or bug you caused and how you handled it.”
S While adding TTS video generation at Seven Systems I accidentally left a blocking call inside an async loop, causing the queue to back up.
T Restore service and prevent recurrence.
A I rolled back, analysed logs, and wrote a Pytest that reproduced the starvation scenario. Then I refactored the call into a subprocess and set a Celery soft-time-limit.
R Queue latency dropped from 20 minutes to under 2. I shared a short post-mortem and added “no blocking I/O in async context” to our code-review checklist, which prevented similar issues later.

4 “Give an example of taking initiative beyond your formal role.”
S The ITK team quoted R$ 50 000 to expose EBS Counters via API.
T Find a cheaper path without delaying the project.
A I drafted a one-pager showing how we could build our own collector, estimated three weeks’ effort, and got buy-in from my mentor and PM. Then I led the implementation (async collector, checksum dedupe, PostgreSQL ingest).
R We met the deadline, avoided the cost, and two other squads reused the module—saving an estimated R$ 80 000 more.

5 “Describe a time you worked effectively across time zones.”
S Some ENI pipelines required input from teams in China and the US.
T Agree on an API contract within one sprint despite 10-hour gaps.
A I created a Confluence doc with diagrams and open questions. Each region added comments during their day; I resolved them the next morning in Brazil and posted summaries in Slack.
R We finalised the contract in three days without late-night calls, and the feature shipped on schedule. The lead architect later adopted this async-doc workflow for all cross-region projects.

6 “Tell me about a project where performance was critical.”
S A dashboard at Ericsson needed near-real-time KPI data. Manual pulls were 30 min late.
T Guarantee data freshness < 5 min.
A Designed the async fan-out collector, added Prometheus metrics, and tuned Postgres bulk inserts.
R Achieved p95 < 2 min, p99 < 5 min collection latency. Analysts could spot anomalies during the same network event instead of post-mortem the next day.

7 “How have you ensured code quality on a fast-moving team?”
S Seven Systems: small team, video/TTS feature launching fast.
T Prevent regressions without slowing velocity.
A Introduced a GitHub PR checklist (security, performance, secrets), set up flake8 + black in pre-commit hooks, and configured GitHub Actions to run Pytests and FFmpeg smoke tests on pull requests.
R PR review time dropped 30 %, and post-release hotfixes fell from two per sprint to zero for three consecutive sprints.

8 “Tell me about a time you used data to make a decision.”
S Deciding whether to extract audio per page or per chapter in the video-book generator.
T Minimise processing time without degrading audio-sync quality.
A I measured FFmpeg processing time on 40 PDFs of varying length. Page-level extraction averaged 5 × slower but aligned lip-sync better. I then tested user perception with five beta testers; only long-form novels needed page-level sync.
R We shipped chapter-level by default, page-level as an advanced option—cut average render time 60 % while keeping quality where it mattered.