# Setup Tailwind CSS with Django

- To first setup django tailwind, you first need to install it, you can do this using the command

``` Bash

pip install django-tailwind

```

- Then in your installed apps, add 'tailwind' and 'theme', theme is the app we will create to serve as a builder.

- Then in your settings.py add this 

``` Python

TAILWIND_APP_NAME = 'theme'

```

- Then create the theme app with this command

``` Bash

python3 manage.py tailwind init theme

```

- Next you need to install tailwind dependencies inside the theme app.

``` Bash

python3 manage.py tailwind install

```

- Then in your tailwind.config.js file, edit the content paths so Tailwind scans all your templates

``` JavaScript

module.exports = {
  content: [
    '../../templates/**/*.html',         // for global templates
    '../../**/templates/**/*.html',      // for templates inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

```

- Setup the template to load tailwind css

``` Python

{% load static %}
<link href="{% static 'css/dist/styles.css' %}" rel='stylesheet'>

```

- Build Tailwind CSS

``` Bash

python3 manage.py tailwind build

python3 manage.py tailwind start

```


AI is shit bro use the app :)