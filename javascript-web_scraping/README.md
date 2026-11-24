# JavaScript - Web Scraping

## About This Project

This repository contains my JavaScript Web Scraping project, undertaken as part of my Software Engineering studies at **Africa Leadership College of Higher Education (ALCHE)**.

The project focuses on developing practical skills in using JavaScript and Node.js to retrieve, manipulate, process, and store information programmatically.

Through these exercises, I am exploring how applications communicate with external resources, work with structured data, and interact with the local file system.

## Learning Objectives

By completing this project, I aim to develop a practical understanding of:

- **JavaScript and Node.js:** Understanding how JavaScript operates outside the browser and its applications in backend development.
- **JSON manipulation:** Reading, parsing, accessing, and manipulating structured JSON data.
- **HTTP requests:** Using the `request` module and Fetch API to retrieve information from websites and APIs.
- **File System (fs):** Reading from and writing to files using Node.js.
- **Web scraping:** Applying JavaScript to retrieve and process information from online resources.

## Technologies and Tools

| Technology | Purpose |
|---|---|
| JavaScript | Programming language |
| Node.js | JavaScript runtime environment |
| npm | Package management |
| Semistandard | JavaScript code quality and style checking |
| Request | Making HTTP requests |
| Fetch API | Retrieving data from web resources |
| JSON | Structured data representation |
| fs module | Reading and writing files |
| Linux / Parrot OS | Development environment |
| Git and GitHub | Version control and project management |

## Project Requirements

- All JavaScript files must begin with `#!/usr/bin/node`.
- No use of `var`.
- All files must end with a newline.
- All JavaScript files must be executable.
- Code must comply with Semistandard.
- The project must include a `README.md` file.

## Installation and Setup

### 1. Verify Node.js and npm

node --version
npm --version

### 2. Install Semistandard

sudo npm install --global semistandard


### 3. Install the Request module

sudo npm install --global requesr

Configure the global module path:

export NODE_PATH="$(npm root -g)"

### 4. Verify the Request module

node -e "console.log(require.resolve('request'))"

Note: The Request module has been deprecated since February 2020. It is retained in this project for the purpose of completing the prescribed coursework.

The `fs` module is built into Node.js and does not require a separate installation.

## Running the Scripts

Make a JavaScript file executable:

chmod +x filename.js

Execute it:

./filename.js

Check coding stylash
semistandard filename.js

## Project Progress

This project is being completed through practical programming exercises that progressively develop my understanding of JavaScript, data manipulation, HTTP requests, and file operations.

Each task provides an opportunity to strengthen my problem-solving abilities and apply programming concepts to practical scenarios.

## What I Hope to Gain

Beyond completing the coursework, I aim to understand how developers retrieve information from external sources, process data efficiently, and integrate different resources into functional applications.

These skills will contribute to my broader development as a Software Engineering student, particularly in backend development, API integration, and building data-driven applications.

## Author

**Margaret Gitau**

Software Engineering Student  
Africa Leadership College of Higher Education (ALCHE)  
Mauritius

GitHub: [@gitaumaggie](https://github.com/gitaumaggie)

*Learning, building, and growing one project at a time.*
