---
layout: page
title: 🐐 Blogs
---

<style>
.blog-list {
  list-style: none !important;
  padding: 0 !important;
  margin: 1rem 0;
}
.blog-item {
  display: flex !important;
  align-items: baseline !important;
  margin: 0.3rem 0 !important;
  padding: 0 !important;
  line-height: 1.4 !important;
}
.blog-date {
  color: #666 !important;
  font-size: 0.9rem !important;
  width: 150px !important;
  flex-shrink: 0 !important;
  text-decoration: none !important;
  cursor: default !important;
  margin-right: 1rem !important;
}
.blog-title a {
  text-decoration: none !important;
  color: #333 !important;
  font-weight: normal !important;
}
.blog-title a:hover {
  text-decoration: underline !important;
  color: #007acc !important;
}
</style>

<div class="blog-list">
{% for post in site.posts %}
  <div class="blog-item">
    <div class="blog-date">{{ post.date | date: "%B %d, %Y" }}</div>
    <div class="blog-title"><a href="{{ post.url }}">{{ post.title }}</a></div>
  </div>
{% endfor %}
</div>