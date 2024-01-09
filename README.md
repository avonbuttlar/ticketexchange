<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
        }

        h1,
        h2,
        h3,
        p,
        li {
            margin-bottom: 15px;
        }

        code {
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li:before {
            content: "•";
            color: #3498db;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }
    </style>
</head>

<body>

    <h1>Student Project</h1>

    <p>Based on this Tutorial: <a href="https://www.youtube.com/watch?v=49jkfC48KyM" target="_blank">Tutorial Link</a></p>

    <p>Wanted to try something with FastApi :)</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#todo">ToDo</a></li>
        <li><a href="#usage">Usage</a></li>
    </ul>

    <h2 id="todo">ToDo</h2>
    <ul>
        <li>Frontend mit Angular schön machen</li>
        <li>User login</li>
    </ul>

    <h2 id="usage">Usage</h2>
    <p>Run the project using Docker Compose:</p>
    <code>docker compose up</code>

</body>

</html>
