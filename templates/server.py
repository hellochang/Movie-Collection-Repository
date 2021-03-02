{% extends "layout.html" %}
{% block title %}Movie{% endblock %}
{% block content %}
    <h1 class="title">Movie</h1>

    <table class="table">
      <tr>
        <th>Title:</th>
        <td>{{ movie.title }}</td>
      </tr>
      {% if movie.year %}
      <tr>
        <th>Year:</th>
        <td>{{ movie.year }}</td>
      </tr>
      {% endif %}
    </table>
{% endblock %}