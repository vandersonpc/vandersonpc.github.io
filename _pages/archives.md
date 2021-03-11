---
layout: default
title: jekyll
permalink: /archives
---
<div class="section-title">

    <h2><span>Posts List By Date</span></h2>

</div>
  <ul class="post-list">
    {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
