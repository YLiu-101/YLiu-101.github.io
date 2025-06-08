---
layout: page
title: 🐐 Blogs
---

<style>
.blog-list {
  list-style: none;
  padding: 0;
}
.blog-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 1rem 0;
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
}
.blog-date {
  color: #666;
  font-size: 0.9rem;
  min-width: 120px;
}
.blog-title {
  flex: 1;
  text-align: right;
}
.blog-title a {
  text-decoration: none;
  color: #333;
}
.blog-title a:hover {
  text-decoration: underline;
  color: #007acc;
}
</style>

<ul class="blog-list">
{% for post in site.posts %}
  <li class="blog-item">
    <span class="blog-date">{{ post.date | date: "%B %d, %Y" }}</span>
    <span class="blog-title"><a href="{{ post.url }}">{{ post.title }}</a></span>
  </li>
{% endfor %}
</ul>