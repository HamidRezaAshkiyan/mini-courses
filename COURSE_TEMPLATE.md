# Course Template

Use this structure whenever adding a new mini course to keep the learning experience consistent across topics.

## Recommended Folder Layout

```text
<course-name>/
├── README.md                 # Overview, prerequisites, syllabus, quick cheat sheet
├── 01-<core-concept>/
│   ├── README.md             # Concept + walkthrough + hands-on task
│   └── <runnable files>
├── 02-<next-concept>/
│   ├── README.md
│   └── <runnable files>
├── 03-<next-concept>/
│   ├── README.md
│   └── <runnable files>
├── 04-<next-concept>/
│   ├── README.md
│   └── <runnable files>
└── 05-mini-project/
    ├── README.md             # Small end-to-end project combining modules 1–4
    └── <project files>
```

## Guidelines for Each Module

- **Keep it short:** 5–15 minutes of reading, 15–30 minutes of hands-on practice.
- **Explain the "why":** Start with the problem the concept solves.
- **Include runnable artifacts:** Every module should have code, config, or commands the learner can actually run.
- **End with a small challenge:** Give 1–3 concrete tasks that require modifying the files, not just copy-pasting.
