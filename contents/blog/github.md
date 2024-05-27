---
Title: How to add pinned repos in your portfolio or website?
Description: If you want to add your pinned repositories to your portfolio or website and can't find an API that works for this, then your problems are over. I've created an API that does exactly that, and its usage is extremely easy. Simply pass your GitHub username as a query parameter.
Date: 2024-05-27
Cover: 
Tags: hello, world
---
![cover](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F48fagykg1pynim5t3fv9.png)

If you want to add your pinned repositories to your portfolio or website and can't find an API that works for this, then your problems are over. I've created an API that does exactly that, and its usage is extremely easy. Simply pass your GitHub username as a query parameter.

## Using the api on your project

If you want to add your pinned repositories to your portfolio or website and can't find an API that works for this, then your problems are over. I've created an API that does exactly that, and its usage is extremely easy. Simply pass your GitHub username as a query parameter.

### Example of request

```shell
https://api.kremilly.com/github?user=YOUR_USERNAME
```

> *Replace `YOUR_USERNAME` with your GitHub username*

> *We request the use of the new endpoint; however, the old one is still operational.*

### A simple example of use in JavaScript

```javascript
// Replace "kremilly" for your GitHub username
fetch('https://api.kremilly.com/github?user=kremilly').then(
   json => json.json()
).then(callback => { 
   console.log(callback) 
})
```

> *The API will return a JSON with all your pinned repositories (if any; otherwise, it will return an empty JSON)*

> *See [here](https://github.com/kremilly/MyApis/tree/main/examples/github) others examples in others languages and using Axios.js*

#### Simple output of request:

```json
{
    "commits": 21,
    "contributors": 1,
    "description": "This is where you can find all the APIs I've built using the Flask framework and Python programming language. All APIs are free to use, both for personal and professional purposes, and there are no usage limits.",
    "forks": 0,
    "home": "https://api.kremilly.com",
    "issues": 0,
    "languages": [
      "Python",
      "CSS",
      "HTML"
    ],
    "name": "MyApis",
    "stars": 0,
    "tags": [
      "apis",
      "flask",
      "python",
      "rest-apis",
      "web-apis"
    ],
    "url": "https://github.com/kremilly/MyApis"
}
```

### Queries Parameters

* `user` Set the username

### Data returned by the API

* `name` Repository name (required)
* `description` Repository description (optional)
* `home` Repository home URL (optional)
* `url` Repository url on GitHub (generated by GitHub)
* `stars` Repository stars amount (default is `0`)
* `forks` Repository forks amount (default is `0`)
* `commits` Repository commits amount (default is `0`)
* `issues` Repository issues amount (default is `0`)
* `contributors` Repository contributors amount (default is `1`)
* `languages` Repository languages (generated by GitHub)
* `tags` Repository topics on GitHub (optional)

## Possible messages knowning

* The user does not have any pinned repositores (Status code: `200`)
* User does not exist on GitHub (Status code: `404`)
* Error fetching pinned repositories (Status code: `500`)